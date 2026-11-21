# Security Assessment and Defensive Study Notes

This overview points to defensive assessment and security-concept materials. Lab guides remain in their technical domains: Active Directory path review is under Identity & Cloud IAM, while IDS and honeypot exercises are under Detection & Incident Response. All exercises are drafts for authorized, isolated labs; full exploitation walkthroughs are out of scope.

- [Snort IDS](../../03-detection-and-incident-response/labs/snort-ids.md) — install, run, and capture alerts for nmap/ping/hping3 traffic. **Draft, evidence pending.**
- [Pentbox Honeypot](../../03-detection-and-incident-response/labs/pentbox-honeypot.md) — stand up a honeypot and review its connection logs. **Draft, evidence pending.**
- [BloodHound AD Mapping](../../01-identity-and-cloud-iam/windows-server-ad-ds/labs/bloodhound-ad-mapping.md) — collect and graph attack paths in a lab AD domain. **Draft, evidence pending.**
- [DDoS / EternalBlue / SMBGhost — Vulnerability Notes](../../03-detection-and-incident-response/notes/ddos-eternalblue-smbghost-vulnerabilities.md) — what each vulnerability is, how to detect it, how to patch/mitigate it. **Final** (attack-execution steps intentionally omitted).
- **Planned defensive notes:** DHCP starvation and rogue DHCP detection and switch-level mitigations; no attack-execution procedures.
- **Planned defensive notes:** credential-dumping and lateral-movement detection and mitigation; no credential-theft procedures.
- [Concept Notes: DHCP Starvation, Malware Types, LLMNR, BloodHound, Metasploit](../../02-network-and-host-hardening/network-security/notes/network-attack-concepts.md) — conceptual write-up, no lab evidence required. **Final.**
- **Planned tool notes:** defensive context for network-analysis and password-auditing tools.

**Scope note:** phishing-kit and credential-harvesting-page tooling, and keylogger/persistence tooling, are deliberately excluded from this project — that category isn't something this portfolio builds or documents setup for.

All labs here assume an isolated, disposable VM lab you own — see the root [README](../../README.md#use-and-safety) for the standing safety note that applies across this repo.
