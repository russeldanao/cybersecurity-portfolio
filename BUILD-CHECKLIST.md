# Portfolio Build Checklist

Use this list to turn the current portfolio into a reviewable public repository. Keep status statements aligned with evidence and use numbered steps when they help reproduce setup or command order.

## 1. Publication hygiene

- [ ] Use [LAB-STUDY-TEMPLATE.md](LAB-STUDY-TEMPLATE.md) for lab drafts, in this order: Objective, Environment, Findings / Baseline, Action / Hardening, Verification.
- [ ] Keep every lab marked as a draft until it has been safely rerun and its new evidence verified.
- [ ] Inspect every screenshot at full size; redact private addresses, MACs, IPv6 addresses, usernames, host/router names, capture filenames, device IDs, and the bytes pane where required.
- [ ] Confirm image metadata has been stripped.
- [ ] Keep PDFs, slide decks, handouts, course archives, credentials, raw unsanitized captures, and third-party materials out of Git.
- [ ] Cite public standards and documentation; paraphrase concepts in original wording.
- [ ] Manually scan text and inspect every image; the referenced automated sanitization checker is not present in this repository.
- [ ] Check local Markdown links and image paths before publishing.

## 2. Rerun labs and collect fresh evidence

### Name Resolution and Discovery
- [ ] Rerun the baseline and hardening checks in an isolated lab; treat historical counts as unverified.
- [ ] Collect fresh NetBIOS after-state checks (`nbtstat -n` and ports 137–139).
- [ ] Capture SSDP service state and UDP 1900 listener state; separately verify UPnP Host start type.
- [ ] Complete a DNS query/cache exercise and explain record types, TTLs, and caching.
- [ ] Compare before/after observations using the same filter, trigger, and capture window.

### Host Baselines and Virtualization
- [ ] Fill in the VirtualBox/Kali environment versions and VM resource allocation.
- [ ] Explain NAT, host-only, internal, and bridged modes in the context of this lab.
- [ ] Capture snapshot creation and restore.
- [ ] Document isolation evidence and the hardware virtualization troubleshooting steps.

## 3. Build the draft labs

### Network Diagnostics and Packet Analysis
- [ ] Explain ipconfig, ping, nslookup, tracert, and netstat outputs.
- [ ] Capture a TCP handshake and a DNS query/response.
- [ ] Compare cleartext HTTP with TLS in a controlled lab application.
- [ ] Complete the PCAP analysis report; publish only sanitized captures.

### Firewall and ARP Defense
- [ ] Record firewall profile defaults and the baseline.
- [ ] Create, test, and remove an inbound and outbound test rule.
- [ ] Capture a normal ARP exchange on an isolated owned network.
- [ ] Explain detection signals and mitigations, including their limitations.

### Network Design and Reconnaissance
- [ ] Complete subnetting practice and finish the subnet calculator functions.
- [ ] Build two subnets with a router; compare static and dynamic routes.
- [ ] Record convergence after a controlled link failure.
- [ ] Scan only an owned target on an isolated lab network and explain the observed packets.

### Cryptography and Data Integrity
- [ ] Demonstrate SHA-256 avalanche behavior, an OpenSSL signature, and a Merkle proof.
- [ ] Explain the security property and limitation of each demonstration.

### Windows Malware Triage
- [ ] Use a disposable VM snapshot and a benign listener.
- [ ] Compare process, port, Autoruns, and hash observations.
- [ ] Document cleanup and snapshot restoration; never submit an unknown file to a scanning service.

## 4. Final review

- [ ] Each combined lab links to its preserved source write-ups where useful.
- [ ] Every command has a purpose and expected result.
- [ ] Every result distinguishes fresh observations from historical or expected behavior.
- [ ] Draft or planned work is not described as completed.
- [ ] Run the sanitization checker, inspect its warnings, and review the repository as a first-time reader.