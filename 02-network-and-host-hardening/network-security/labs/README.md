# Network Security Labs

This collection documents practical network and host-security work. The Windows name-resolution lab is the featured case study: it combines controlled baselines, configuration changes, packet-level verification, a repeat run, and explicit limits. Smaller related exercises are grouped into broader assessment labs below, while their detailed procedures remain available as modules.

## Featured case study

### Windows 11 name-resolution and discovery hardening

[Open the full case study](name-resolution-and-discovery/README.md) for the environment, commands, evidence, and limitations.

In an isolated Windows 11 VM, I disabled NetBIOS over TCP/IP and LLMNR, then checked the configuration and repeated the same name-lookup triggers in packet captures. In the first pass, the VM's three NBNS queries and eight test-name LLMNR queries were no longer observed after hardening. A second pass reproduced those before/after results. SSDP/UPnP services were disabled, but the VM emitted no SSDP traffic either before or after, so that change has configuration evidence only—not a measured traffic reduction.

This demonstrates Windows hardening, PowerShell configuration read-back, Wireshark filtering and sender attribution, repeatable test design, rollback, and careful evidence handling. The report also states what was not tested: this is not a Windows Firewall/Defender assessment, a direct network-reachability test, or proof that the protocols can never appear.

## Supporting assessment labs

| Lab | Modules | Evidence status |
|---|---|---|
| **Home Network Security Assessment** | [Combined assessment overview](home-network-security-assessment/README.md), with modules for [wireless surveying](wireless-assessment/wifi-assessment-with-inssider.md) and [router review](home-network-hardening.md) | Partial: the Wi-Fi module has two sanitized screenshots and initial scan observations; its walk test and remaining evidence are pending. Router notes are historical and unverified. Keep all identifiers redacted. |
| **Firewall and ARP Defense** | [Lab guide](firewall-and-arp-defense/README.md) | Planned exercises; no results are claimed. |
| **PCAP Protocol Counter** | [Lab guide](pcap-protocol-counter/README.md) · [Python helper](pcap-protocol-counter/count_protocols.py) | Code is present; execution, test cases, and comparison against Wireshark are pending. |
| **Cryptography and Data Integrity** | [Lab overview](cryptography-and-integrity/README.md), with focused procedures for [AES file encryption](cryptography-and-integrity/openssl-aes-file-encryption.md) and [RSA signing](cryptography-and-integrity/openssl-rsa-signing.md) | Draft procedures; no verified runs are claimed. |
| **Endpoint Encryption** | [BitLocker full-volume encryption](bitlocker-full-volume.md) | Incomplete: unlock method, cipher, and verification evidence still need to be recorded. |

These are portfolio groupings, not claims that every module is complete. A combined assessment should only be presented as a completed lab after its own planned checks have been run and its results documented.

## Evidence standard

Results are labeled as observed, configuration-only, historical, or not yet tested. A procedure and its expected output are not evidence of completion. Review each module's scope, authorization, sanitization guidance, and limitations before reusing its findings.
