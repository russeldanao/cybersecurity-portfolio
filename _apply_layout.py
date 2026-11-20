#!/usr/bin/env python3
"""One-shot layout move. Longest prefix wins. Does not edit attack-lab notes."""
import os
import posixpath
import re
import subprocess
from urllib.parse import quote, unquote

GIT = "git"
ROOT = os.path.dirname(os.path.abspath(__file__))
PRESERVE_UNPARSED = {
    "communications-os-and-data-management/drafts/~$README.md",
}

# Longest prefixes are matched first.
MOVES = [
    ("computer-networks/labs/pcap-protocol-counter", "05-ai-and-automation-security/pcap-protocol-counter"),
    ("communications-os-and-data-management/labs/endpoint-logging-and-detection", "03-detection-and-incident-response/endpoint-logging-and-detection"),
    ("communications-os-and-data-management/labs/sysmon-wazuh-detection", "03-detection-and-incident-response/sysmon-wazuh-detection"),
    ("communications-os-and-data-management/case-studies", "03-detection-and-incident-response/case-studies"),
    ("communications-os-and-data-management/notes/incident-response-and-cyber-kill-chain.md", "03-detection-and-incident-response/notes/incident-response-and-cyber-kill-chain.md"),
    ("communications-os-and-data-management/references/canadian-cyber-law-and-international-frameworks.md", "04-grc-and-risk-management/references/canadian-cyber-law-and-international-frameworks.md"),
    ("communications-os-and-data-management/notes/python-for-cybersecurity.md", "05-ai-and-automation-security/notes/python-for-cybersecurity.md"),
    ("network-security/labs/malware-detection-host-triage", "03-detection-and-incident-response/malware-detection-host-triage"),
    ("network-security/labs/llmnr-poisoning-responder.md", "03-detection-and-incident-response/labs/llmnr-poisoning-responder.md"),
    ("network-security/case-studies", "03-detection-and-incident-response/network-case-studies"),
    ("network-security/notes", "06-study-guides-and-notes/network-security-notes"),
    ("network-security/docs/sanitization-policy.md", "docs/sanitization-policy.md"),
    ("windows-server-adds", "01-identity-and-cloud-iam/windows-server-ad-ds"),
    ("cloud-computing", "01-identity-and-cloud-iam/cloud-fundamentals"),
    ("network-security", "02-network-and-host-hardening/network-security"),
    ("computer-networks", "02-network-and-host-hardening/computer-networks"),
    ("penetration-testing", "03-detection-and-incident-response/penetration-testing"),
    ("cryptography", "06-study-guides-and-notes/cryptography"),
    ("programming-fundamentals", "06-study-guides-and-notes/programming-fundamentals"),
    ("communications-os-and-data-management", "06-study-guides-and-notes/communications-os-and-data-management"),
    ("docs/coursework-review.md", "06-study-guides-and-notes/coursework-review.md"),
]

# Attack notes stay byte-for-byte. Only their path changes.
SKIP_EDIT = {
    "network-security/labs/llmnr-poisoning-responder.md",
    "penetration-testing/labs/bloodhound-ad-mapping.md",
}

MD_LINK = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
HTML_ATTR = re.compile(r"((?:src|href)=\")([^\"]+)(\")")
ABS = re.compile(
    r"^(https://(?:github\.com/(?:razdanao|russeldanao)/cybersecurity-portfolio/(?:blob|tree|raw)/main"
    r"|raw\.githubusercontent\.com/(?:razdanao|russeldanao)/cybersecurity-portfolio/main))/([^#?]*)([#?].*)?$"
)
SKIP_SCHEME = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#)", re.I)


def sh(*args):
    subprocess.run(args, cwd=ROOT, check=True)


def map_path(path):
    path = path.replace("\\", "/").lstrip("./")
    best = None
    for old, _new in MOVES:
        if path == old or path.startswith(old + "/"):
            if best is None or len(old) > len(best):
                best = old
    if best is None:
        return path
    new = dict(MOVES)[best]
    return new + path[len(best):]


def fix_abs(url):
    match = ABS.match(url)
    if not match:
        return url
    base, path, tail = match.groups()
    base = base.replace("/razdanao/", "/russeldanao/")
    mapped = map_path(unquote(path).rstrip("/"))
    slash = "/" if path.endswith("/") else ""
    return f"{base}/{quote(mapped, safe='/._-~')}{slash}{tail or ''}"


def fix_target(target, old_file, new_file):
    if target.startswith("/"):
        match = re.match(r"([^#?]*)([#?].*)?$", target[1:])
        path, tail = match.group(1), match.group(2) or ""
        mapped = map_path(unquote(path))
        if mapped == unquote(path):
            return target
        return "/" + quote(mapped, safe="/._-~") + tail
    if SKIP_SCHEME.match(target):
        return fix_abs(target) if target.startswith("http") else target
    match = re.match(r"([^#?]*)([#?].*)?$", target)
    path, tail = match.group(1), match.group(2) or ""
    if not path:
        return target
    old_target = posixpath.normpath(posixpath.join(posixpath.dirname(old_file), unquote(path)))
    if old_target.startswith(".."):
        return target
    mapped = map_path(old_target)
    rel = posixpath.relpath(mapped, posixpath.dirname(new_file) or ".")
    if path.endswith("/"):
        rel += "/"
    if rel == unquote(path) and mapped == old_target:
        return target
    return quote(rel, safe="/._-~") + tail


def process(text, old_file, new_file):
    text = text.replace(
        "github.com/razdanao/cybersecurity-portfolio",
        "github.com/russeldanao/cybersecurity-portfolio",
    )
    text = MD_LINK.sub(
        lambda m: m.group(1) + fix_target(m.group(2), old_file, new_file) + m.group(3),
        text,
    )
    text = HTML_ATTR.sub(
        lambda m: m.group(1) + fix_target(m.group(2), old_file, new_file) + m.group(3),
        text,
    )
    return text


def main():
    os.chdir(ROOT)
    lock = "communications-os-and-data-management/drafts/~$README.md"
    if os.path.exists(lock):
        print(f"Preserving {lock}; it will be moved with its parent folder without text rewriting.")

    files = subprocess.run(
        [GIT, "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.splitlines()
    updated = {}
    for rel in files:
        rel = rel.replace("\\", "/")
        if rel in PRESERVE_UNPARSED:
            continue
        if not rel.lower().endswith(".md"):
            continue
        if rel in SKIP_EDIT:
            continue
        new_rel = map_path(rel)
        with open(rel, encoding="utf-8", newline="") as fh:
            old = fh.read()
        new = process(old, rel, new_rel)
        if new != old:
            updated[new_rel] = new

    for old, new in sorted(MOVES, key=lambda item: len(item[0]), reverse=True):
        if not os.path.exists(old):
            print(f"skip missing {old}")
            continue
        os.makedirs(os.path.dirname(new) or ".", exist_ok=True)
        print(f"mv {old} -> {new}")
        sh(GIT, "mv", "--", old, new)

    for path, text in updated.items():
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        print(f"relink {path}")


if __name__ == "__main__":
    main()
