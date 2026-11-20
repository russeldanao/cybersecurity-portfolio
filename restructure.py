#!/usr/bin/env python3
"""
restructure.py - move the portfolio into the 01-06 domain layout and fix every link.

Usage (from the repo root):
    python restructure.py            # dry run: shows the plan, changes nothing
    python restructure.py --apply    # creates branch 'restructure', moves, rewrites, commits

What it does:
  * git mv each old folder into its new home (history preserved)
  * rewrites relative links AND image paths in every .md file (including ![](...) and <img src>)
  * rewrites absolute github.com/.../blob|tree|raw/main/... URLs and razdanao -> russeldanao
  * creates README stubs for the six top-level folders + PROJECT-README-TEMPLATE.md
  * reports any broken links and any plain-text mentions of old paths left to review
"""
import os
import posixpath
import re
import subprocess
import sys
from urllib.parse import quote, unquote

# Old path -> new path. Whole-folder moves keep internal links/screenshots intact.
# Add file-level moves here too (e.g. a single case study) and links follow automatically.
MOVES = {
    "network-security": "02-network-and-host-hardening/network-security",
    "penetration-testing": "03-detection-and-incident-response/penetration-testing",
    "cryptography": "06-study-guides-and-notes/cryptography",
    "windows-server-adds": "06-study-guides-and-notes/windows-server-adds",
    "cloud-computing": "06-study-guides-and-notes/cloud-computing",
    "programming-fundamentals": "06-study-guides-and-notes/programming-fundamentals",
    "computer-networks": "06-study-guides-and-notes/computer-networks",
    "communications-os-and-data-management": "06-study-guides-and-notes/communications-os-and-data-management",
}

TOP = {
    "01-identity-and-cloud-iam": ("Identity & Cloud IAM", "Microsoft Entra ID free-tier labs, Joiner/Mover/Leaver scenarios, cloud asset risk."),
    "02-network-and-host-hardening": ("Network & Host Hardening", "Windows 11 baselines, protocol hardening, Wireshark verification."),
    "03-detection-and-incident-response": ("Detection & Incident Response", "Blue-team triage, IOCs, timelines, containment, detection/mitigation notes."),
    "04-grc-and-risk-management": ("GRC & Risk Management", "NIST CSF 2.0 assessment, risk register, starter ISMS/policies."),
    "05-ai-and-automation-security": ("AI & Automation Security", "Agentic workflow risk testing and sanitized Python automation."),
    "06-study-guides-and-notes": ("Study Guides & Notes", "Sanitized coursework notes and reference material."),
}

TEMPLATE = """# <Project Title>

> **One-line summary:** <what you did and the result>

| | |
|---|---|
| **Domain** | <Identity / Hardening / IR / GRC / AI Security> |
| **Environment** | <e.g., VMware Workstation, Windows 11 VM, host-only network> |
| **Tools** | <all free tools> |
| **Frameworks** | <CIS / NIST CSF 2.0 / MITRE ATT&CK / OWASP LLM Top 10> |
| **Status** | <Complete / Draft> |
| **Date** | <YYYY-MM> |

## 1. Objective & Scope
- **Goal:**
- **In scope:**
- **Out of scope:**
- **Assumptions:** lab-only, isolated network, dummy data

## 2. Setup & Tooling
- **Environment:**
- **Tools & versions:**
- **Safety controls:**

## 3. Execution & Findings
1. <step>

| # | Finding | Evidence | Severity | Recommendation |
|---|---------|----------|----------|----------------|
| 1 | | `evidence/<file>` | | |

## 4. Verification
- **How I confirmed it:**
- **Before vs. after:**
- **Limitations:**

## 5. Key Takeaways
-

## References
-

## Sanitization note
All hostnames, IPs, usernames, and identifiers are lab/dummy values. No credentials or real data included.
"""

APPLY = "--apply" in sys.argv

MD_LINK = re.compile(r'(\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
PRESERVE_UNPARSED = {"communications-os-and-data-management/drafts/~$README.md"}
HTML_ATTR = re.compile(r'((?:src|href)=")([^"]+)(")')
ABS = re.compile(
    r'^(https://(?:github\.com/(?:razdanao|russeldanao)/cybersecurity-portfolio/(?:blob|tree|raw)/main'
    r'|raw\.githubusercontent\.com/(?:razdanao|russeldanao)/cybersecurity-portfolio/main))/([^#?]*)([#?].*)?$'
)
SKIP = re.compile(r'^(?:[a-z][a-z0-9+.-]*:|#|/)', re.I)


def sh(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def new_path(p):
    best = None
    for old in MOVES:
        if p == old or p.startswith(old + "/"):
            if best is None or len(old) > len(best):
                best = old
    return MOVES[best] + p[len(best):] if best else p


def fix_abs(t):
    m = ABS.match(t)
    if not m:
        return t
    base, path, tail = m.groups()
    base = base.replace("/razdanao/", "/russeldanao/")
    new = new_path(unquote(path).rstrip("/"))
    slash = "/" if path.endswith("/") else ""
    return f"{base}/{quote(new, safe='/._-~')}{slash}{tail or ''}"


def fix_target(t, old_file, new_file):
    if SKIP.match(t):
        return fix_abs(t) if t.startswith("http") else t
    m = re.match(r'([^#?]*)([#?].*)?$', t)
    path, tail = m.group(1), m.group(2) or ""
    if not path:
        return t
    old_t = posixpath.normpath(posixpath.join(posixpath.dirname(old_file), unquote(path)))
    if old_t.startswith(".."):
        return t
    rel = posixpath.relpath(new_path(old_t), posixpath.dirname(new_file) or ".")
    if path.endswith("/"):
        rel += "/"
    if rel == unquote(path):
        return t
    return quote(rel, safe="/._-~") + tail


def process(text, old_file, new_file):
    text = text.replace("github.com/razdanao/cybersecurity-portfolio", "github.com/russeldanao/cybersecurity-portfolio")
    text = MD_LINK.sub(lambda m: m.group(1) + fix_target(m.group(2), old_file, new_file) + m.group(3), text)
    text = HTML_ATTR.sub(lambda m: m.group(1) + fix_target(m.group(2), old_file, new_file) + m.group(3), text)
    return text


def read(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return fh.read()


def write(p, text):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def scaffold():
    for folder, (title, blurb) in TOP.items():
        os.makedirs(folder, exist_ok=True)
        readme = os.path.join(folder, "README.md")
        if os.path.exists(readme):
            continue
        subs = sorted(d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d)))
        body = f"# {title}\n\n{blurb}\n\n## Contents\n\n"
        if subs:
            for d in subs:
                target = f"{d}/README.md" if os.path.exists(os.path.join(folder, d, "README.md")) else f"{d}/"
                body += f"- [{d}]({target})\n"
        else:
            body += "_Planned - not started yet._\n"
        write(readme, body)
    if not os.path.exists("PROJECT-README-TEMPLATE.md"):
        write("PROJECT-README-TEMPLATE.md", TEMPLATE)


def broken_links():
    out = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if not fn.lower().endswith(".md"):
                continue
            p = os.path.join(root, fn)
            text = read(p)
            targets = [m.group(2) for m in MD_LINK.finditer(text)] + [m.group(2) for m in HTML_ATTR.finditer(text)]
            for t in targets:
                if SKIP.match(t):
                    continue
                path = unquote(re.split(r'[#?]', t)[0])
                if path and not os.path.exists(os.path.join(root, path)):
                    out.append(f"{os.path.normpath(p)} -> {t}")
    return out


def old_mentions():
    hits = []
    pat = re.compile("|".join(re.escape(o) + "/" for o in MOVES))
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.lower().endswith(".md"):
                p = os.path.join(root, fn)
                for i, line in enumerate(read(p).splitlines(), 1):
                    for m in pat.finditer(line):
                        before = line[: m.start()]
                        if not before.endswith(("](", "/")):
                            hits.append(f"{os.path.normpath(p)}:{i}: {line.strip()[:100]}")
                            break
    return hits


def main():
    if not os.path.isdir(".git"):
        sys.exit("Run this from the repo root (the folder containing .git).")
    if sh("git", "status", "--porcelain", "-uno").strip():
        sys.exit("Working tree not clean. Commit or stash first.")

    files = sh("git", "ls-files").splitlines()
    md = [f for f in files if f.lower().endswith(".md") and f not in PRESERVE_UNPARSED]
    updated = {}
    for f in md:
        nf = new_path(f)
        old = read(f)
        new = process(old, f, nf)
        if new != old or nf != f:
            updated[f] = (nf, new, new != old)

    moves = [(o, n) for o, n in MOVES.items() if os.path.exists(o)]
    print("Planned moves:")
    for o, n in moves:
        print(f"  {o}  ->  {n}")
    print(f"\nMarkdown files with rewritten links: {sum(1 for v in updated.values() if v[2])}")
    for f, (nf, _, changed) in updated.items():
        if changed:
            print(f"  {f}")
    if not APPLY:
        print("\nDry run only. Re-run with --apply to execute.")
        return

    sh("git", "checkout", "-b", "restructure")
    for o, n in moves:
        os.makedirs(os.path.dirname(n), exist_ok=True)
        sh("git", "mv", o, n)
    for f, (nf, text, changed) in updated.items():
        if changed:
            write(nf, text)
    scaffold()
    sh("git", "add", "-A")
    subprocess.run(["git", "reset", "-q", "--", os.path.basename(__file__)], capture_output=True)
    sh("git", "commit", "-m", "Restructure into six domain folders; fix links and account URLs")

    broken = broken_links()
    print("\nDone. Committed on branch 'restructure'.")
    print(f"Broken relative links: {len(broken)}")
    for b in broken:
        print("  " + b)
    mentions = old_mentions()
    if mentions:
        print("\nPlain-text mentions of old paths (review manually):")
        for h in mentions:
            print("  " + h)
    print("\nNext: review with 'git diff main --stat', then merge/push when happy.")


if __name__ == "__main__":
    main()
