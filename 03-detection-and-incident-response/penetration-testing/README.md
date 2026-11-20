# Penetration Testing

A self-directed lab set covering AD/network attack techniques from both sides — running assessment tooling (IDS, honeypot, AD attack-path mapping) and studying well-known attack classes (exploits, DHCP starvation, credential dumping) closely enough to document detection and mitigation for each. Full exploitation walkthroughs are intentionally out of scope — see the note in each vulnerability doc for the reasoning.

- [Snort IDS](labs/snort-ids.md) — install, run, and capture alerts for nmap/ping/hping3 traffic. **Draft, evidence pending.**
- [Pentbox Honeypot](labs/pentbox-honeypot.md) — stand up a honeypot and review its connection logs. **Draft, evidence pending.**
- [BloodHound AD Mapping](labs/bloodhound-ad-mapping.md) — collect and graph attack paths in a lab AD domain. **Draft, evidence pending.**
- [DDoS / EternalBlue / SMBGhost — Vulnerability Notes](notes/ddos-eternalblue-smbghost-vulnerabilities.md) — what each vulnerability is, how to detect it, how to patch/mitigate it. **Final** (attack-execution steps intentionally omitted).
- **Planned defensive notes:** DHCP starvation and rogue DHCP detection and switch-level mitigations; no attack-execution procedures.
- **Planned defensive notes:** credential-dumping and lateral-movement detection and mitigation; no credential-theft procedures.
- [Concept Notes: DHCP Starvation, Malware Types, LLMNR, BloodHound, Metasploit](theory/network-attack-concepts.md) — conceptual write-up, no lab evidence required. **Final.**
- **Planned tool notes:** defensive context for network-analysis and password-auditing tools.

**Scope note:** phishing-kit and credential-harvesting-page tooling, and keylogger/persistence tooling, are deliberately excluded from this project — that category isn't something this portfolio builds or documents setup for.

All labs here assume an isolated, disposable VM lab you own — see the root [README](../../README.md#use-and-safety) for the standing safety note that applies across this repo.
