# Name Resolution and Discovery Protocols — Lab Study Guide

> **Draft: baseline observations plus one hardening change.** Microsoft Defender PUA protection was changed from Audit to Enabled, and the configuration was verified. PUA blocking behavior was not tested. No other settings were changed during this lab. [Lab study template](../../../../LAB-STUDY-TEMPLATE.md).

## Key Results

- Reviewed Windows Firewall, Microsoft Defender, NetBIOS, LLMNR, SSDP/UPnP, DHCP, DNS, and short Wireshark capture windows in an isolated VMware Host-only lab.
- The baseline showed NetBIOS disabled, LLMNR disabled by policy, SSDP/UPnP services stopped and disabled, and Windows Firewall profiles enabled with inbound traffic blocked by default.
- Changed Microsoft Defender Potentially Unwanted Application (PUA) protection from Audit to Enabled. A follow-up read-back confirmed **Enabled**.
- A DNS lookup for `example.com` timed out. The cause was not established.
- The screenshots below are sanitized evidence excerpts, not a complete record of every lab observation. Raw packet captures are not included.

## Sanitize First

- Use an isolated, owned lab and synthetic test names.
- Review screenshots before sharing. Do not publish raw packet captures, private network identifiers, credentials, internal hostnames, or personal data.
- The name-resolution test used `LAB-NO-SUCH-HOST`; the DNS lookup used `example.com`.

## Objective

Assess Windows host name-resolution and service-discovery configuration, observe related traffic in short Wireshark capture windows, and document one endpoint-protection setting change with configuration verification.

## Environment

- **Virtualization:** VMware Workstation; the connected adapter was configured as Host-only and set to connect at power on. No bridged adapter was shown.
- **Guest operating system:** Windows 11 Pro, version 26H2, build 26300.9974.
- **Packet analyzer:** Wireshark 4.6.9 (64-bit).
- **Network profile:** Public. PowerShell reported `NoTraffic` for both IPv4 and IPv6. `NlaSvc` was stopped when checked; this is a co-occurring observation, not an established cause.
- **Safety:** A pre-hardening VMware snapshot was created. Testing was performed in the isolated VM.

## Findings / Baseline

| Area | Observation |
|---|---|
| Windows Firewall | Domain, Private, and Public profiles were enabled. Effective default inbound action was `Block`; outbound action was `Allow`. |
| Microsoft Defender | Antivirus, real-time protection, and antimalware service were enabled. |
| NetBIOS over TCP/IP | `TcpipNetbiosOptions` was `2` (disabled) on the active virtual adapter. Read-only endpoint checks returned no output for UDP 137/138 or TCP 139. |
| LLMNR | Group Policy **Turn off multicast name resolution** displayed **Enabled**, meaning LLMNR was disabled by policy. A registry query produced no output; no registry value is claimed. |
| SSDP / UPnP | `SSDPSRV` and `upnphost` were both `Stopped`, with startup type `Disabled`. Read-only UDP endpoint checks returned no output for ports 1900 and 5355. |
| Short Wireshark observations | The `llmnr` and `nbns` display filters each showed 0 matches in a 41-packet capture window. The `ssdp` filter showed 0 matches in a separate 15-packet window. These results apply only to those windows. |
| Protocol hierarchy | The 15-packet SSDP-test capture was classified as UDP → DNS. This is a protocol breakdown of that capture, not evidence that DNS resolution succeeded. |
| DHCP | The capture showed a DHCP Request and ACK. A separate read-only configuration summary reported a 30-minute lease; that duration is not inferred from the packets. |
| DNS and network configuration | A DNS server was configured, and no default gateway was present. A lookup for `example.com` timed out with `ERROR_TIMEOUT`. |
| DNS connectivity checks | `Test-NetConnection` reported `PingSucceeded: False` and `TcpTestSucceeded: False` for the configured DNS server. These results do not establish whether DNS over UDP is reachable. |
| PUA protection | The PUA protection preference was in Audit mode before the hardening change. |

## Action / Hardening

The baseline finding was that Microsoft Defender PUA protection was in Audit mode. As the selected hardening action, PUA protection was changed to Enabled in the isolated VM.

No other settings were changed during this lab. In particular, no NetBIOS, LLMNR, SSDP/UPnP, firewall, network-profile, or DNS settings were changed.

## Verification

A follow-up read-back of the PUA protection preference confirmed **Enabled**. This verifies the configured preference only; no PUA sample was run, so detection and blocking behavior were not tested.

The DHCP Request/ACK, 30-minute lease, DNS lookup timeout, and DNS-configured/no-gateway summary are text-reported observations; they are not shown in the screenshots below.

### Sanitized Evidence

#### Windows 11 baseline settings

![Windows 11 baseline settings](evidence/windows11-baseline-settings-evidence.png)

*Look for: the documented firewall, Defender, name-resolution policy, service, and network-profile settings.*

#### Wireshark protocol filters and hierarchy

![Wireshark protocol filters and hierarchy](evidence/wireshark-protocol-evidence.png)

*Look for: the displayed filter results and the protocol breakdown for the short test capture.*

#### Network profile and connectivity

![Sanitized network profile and connectivity](evidence/network-profile-sanitized.png)

*Look for: the Public profile and `NoTraffic` connectivity values.*

#### Network Location Awareness service status

![Network Location Awareness service status](evidence/nlasvc-status.png)

*Look for: the observed stopped service status.*

#### DNS server connectivity checks

![Sanitized DNS server connectivity checks](evidence/dns-port-test-results.png)

*Look for: the failed ping and TCP connectivity checks; these do not test DNS over UDP.*

#### PUA protection hardening and verification

![PUA protection change and verification excerpt](evidence/pua-protection-enabled.png)

*Look for: the change and follow-up read-back. This is a cropped verification excerpt, not complete lab evidence.*

## Limitations and Lessons Learned

- Zero matching packets in a short capture means only that none matched during that observation window; it does not prove a protocol can never be used.
- A configured DNS server does not establish that it is reachable. Failed ping and TCP/53 checks do not determine whether DNS over UDP works.
- The cause of the DNS timeout was not established.
- The Public profile, `NoTraffic` connectivity values, and stopped `NlaSvc` status were observed together; no causal relationship was established.
- DHCP Request/ACK packets alone do not establish lease duration.
- The PUA preference was verified by configuration read-back. PUA blocking behavior was not tested.
- Packet captures were discarded and are not included as evidence. An earlier accidental capture screenshot exposed private network identifiers and was not reused.

## Next Steps

- Test whether DNS over UDP works in the isolated lab without assuming the result from the ping or TCP/53 checks.
- Investigate the Public profile using read-only checks; treat the stopped `NlaSvc` status as an observation, not a confirmed cause.
- If repeating protocol observations, use longer, controlled capture windows and record the trigger and filter for each one.

## Study Notes

- Distinguish configuration state from observed network behavior.
- NBNS and LLMNR are local name-resolution mechanisms; SSDP supports service discovery; DHCP provides network configuration; DNS resolves domain names.
- LLMNR and NBNS are commonly disabled in hardening guidance because local name-resolution traffic can be susceptible to spoofing.
- Record limitations alongside packet counts and configuration checks.

## References

- [Lab study template](../../../../LAB-STUDY-TEMPLATE.md)
- [Privacy and sanitization notes](windows-network-hardening/docs/privacy-and-sanitization.md)
- [Troubleshooting notes](windows-network-hardening/docs/troubleshooting.md)
- [Microsoft Defender PUA protection](https://learn.microsoft.com/defender-endpoint/detect-block-potentially-unwanted-apps-microsoft-defender-antivirus)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)