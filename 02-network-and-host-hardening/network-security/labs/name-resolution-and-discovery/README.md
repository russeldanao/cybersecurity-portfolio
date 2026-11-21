# Name Resolution and Discovery Protocols — Lab Study Guide
> **Draft — baseline observations plus one hardening change.** Microsoft Defender PUA protection was changed from Audit to Enabled and the preference was verified. Functional blocking behavior was not tested. No other settings were changed during this rerun. [Use the lab template](../../../../LAB-STUDY-TEMPLATE.md).

## Sanitize First

- Use an isolated, owned lab and dummy hostnames and accounts.
- Review every screenshot before sharing. Publish only sanitized configuration/results screenshots; never publish raw packet captures, private addresses, MAC addresses, credentials, internal hostnames, or personal data.
- Use synthetic hostnames. The DNS lookup of `example.com` is a public-domain connectivity check, not an internal identifier.
- Evidence exported during the rerun is available in the conversation; it has not yet been added to this repository.

## Objective

Assess Windows name-resolution and service-discovery configuration, observe NBNS, LLMNR, SSDP, DHCP, and DNS behavior in a short isolated lab capture, and apply one reversible endpoint-protection setting change with configuration verification.

## Environment

- **Virtualization:** VMware Workstation; connected network adapter configured as Host-only and set to connect at power on. No bridged adapter was shown.
- **Guest:** Windows 11 Pro, version 26H2, OS build 26300.9974.
- **Packet analyzer:** Wireshark 4.6.9 (64-bit).
- **Network profile:** Public; PowerShell reported `NoTraffic` for IPv4 and IPv6. `NlaSvc` was `Stopped` when checked. These are co-occurring observations; the cause of the profile was not established.
- **Safety:** A pre-hardening VMware snapshot was created. Checks were performed in the isolated VM.

## Findings / Baseline

| Area | Observed baseline |
|---|---|
| Windows Firewall | Domain, Private, and Public profiles enabled; effective inbound default `Block` and outbound default `Allow`. |
| Microsoft Defender | Antivirus, real-time protection, and antimalware service reported enabled. |
| NetBIOS over TCP/IP | `TcpipNetbiosOptions = 2` (disabled) on the active virtual adapter. Read-only endpoint checks returned no output for UDP 137/138 or TCP 139. |
| LLMNR | Group Policy **Turn off multicast name resolution** displayed **Enabled** (LLMNR disabled by policy). Registry query produced no output; no registry value is claimed. |
| SSDP / UPnP | `SSDPSRV` and `upnphost` both `Stopped`, startup type `Disabled`. UDP endpoint checks returned no output for ports 1900 and 5355. |
| Short Wireshark observations | Display filters showed 0 matches for `llmnr` and `nbns` in a 41-packet capture window, and 0 matches for `ssdp` in a separate 15-packet window. These results apply only to those windows and triggers. |
| Protocol hierarchy | The 15-packet SSDP-test capture was classified as UDP → DNS. This is a breakdown of that capture, not proof of successful DNS resolution. |
| DHCP | Capture showed a DHCP Request and ACK. A separate read-only configuration summary reported a 30-minute lease; this duration is not inferred from the packets. |
| DNS / network configuration | A DNS server was configured; no default gateway was present. `Resolve-DnsName example.com` timed out (`ERROR_TIMEOUT`). The configured server address is intentionally omitted. |
| DNS connectivity checks | `Test-NetConnection` reported `PingSucceeded: False` and `TcpTestSucceeded: False` for the configured DNS server. These results do not establish UDP DNS reachability or explain the lookup timeout. |
| PUA protection | `(Get-MpPreference).PUAProtection` returned `2` before the change (Audit mode). |

## Action / Hardening

Changed Microsoft Defender Potentially Unwanted Application (PUA) protection from Audit mode to Enabled in the isolated VM:

```powershell
Set-MpPreference -PUAProtection Enabled
```

No NetBIOS, LLMNR, SSDP/UPnP, firewall, network-profile, or DNS settings were changed during this rerun. Do not change those controls solely to generate traffic. Investigate the DNS timeout separately before considering network changes.

## Verification

- Re-ran `(Get-MpPreference).PUAProtection`; it returned `1` after the change (Enabled).
- The verification screenshot shows the prior value (`2`), change command, and resulting value (`1`). A sanitized copy was exported in the conversation; upload it to this folder before adding an image link.
- No PUA sample was run. This verifies the configured preference only, not detection or blocking behavior.
- No post-change protocol capture was required because the PUA preference does not change the NBNS, LLMNR, SSDP, DHCP, or DNS settings documented above.

## Limitations and Lessons Learned

- Zero matching packets in a short capture only means none matched in that observation window; it does not prove a protocol can never be used.
- A DNS server being configured does not prove it is reachable. Failed ICMP and TCP/53 checks do not determine whether DNS over UDP is reachable. The cause of the DNS timeout remains unknown.
- The Public profile, `NoTraffic` connectivity values, and stopped `NlaSvc` status were observed; no causal relationship was established.
- DHCP Request/ACK packets alone do not establish lease duration.
- Packet captures were discarded. One accidental screenshot exposed private network identifiers and must not be reused. Only sanitized evidence should be published.
- PUA protection was verified by reading its configuration value; no benign test file or unwanted-app sample was used.

## Study Notes

- Distinguish configuration state from observed network behavior.
- NBNS and LLMNR support local name resolution; SSDP supports service discovery; DHCP assigns network configuration; DNS resolves domain names.
- Record the trigger, display filter, observation window, configuration state, and evidence source for each test.
- Preserve the VM snapshot until the lab write-up and evidence have been reviewed.

## References

- [Microsoft Defender Antivirus PowerShell cmdlets](https://learn.microsoft.com/powershell/module/defender/)
- [Microsoft Defender PUA protection](https://learn.microsoft.com/defender-endpoint/detect-block-potentially-unwanted-apps-microsoft-defender-antivirus)
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)
- See the Windows hardening notes in `windows-network-hardening/docs/`.