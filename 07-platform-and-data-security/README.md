# Platform and Data Security

This domain covers foundational platform administration and data-security practice that does not fit cleanly under identity, network defense, detection, GRC, or AI security. The tracks group related exercises so they can be completed in one local setup.

## Environment tracks

| Environment | Combine these exercises | Where to start |
|---|---|---|
| Windows Server domain and services | AD DS, users/groups, DHCP, DNS, IIS/FTP/RDP, forest/DFS, WDS, Hyper-V, and defensive BloodHound review | [Windows Server AD DS](../01-identity-and-cloud-iam/windows-server-ad-ds/README.md) and [network services](../02-network-and-host-hardening/computer-networks/labs/network-services-and-host-access/README.md) |
| Windows endpoint and network analysis | Windows host/network baselines, Wireshark setup and protocol checks, PCAP counter | [Network diagnostics and packet analysis](../02-network-and-host-hardening/computer-networks/labs/network-diagnostics-and-packet-analysis/README.md) |
| Packet Tracer simulator | Static routing, OSPF, and switch-port security in one simulated topology | [Routing and switching](../02-network-and-host-hardening/computer-networks/labs/routing-and-switching/README.md) |
| Defensive monitoring range | Windows Sysmon endpoint, Wazuh manager, and separate isolated sensor/test VMs | [Detection & Incident Response](../03-detection-and-incident-response/README.md) |
| Own wireless network | inSSIDer observations and home-router configuration review; use only your own network | [Wireless assessment](../02-network-and-host-hardening/network-security/labs/wireless-assessment/README.md) |
| Local MySQL workstation | Sakila queries, local accounts, least privilege, backups/restores, and synthetic database design | [Database management](database-management/README.md) |
| Kali/Linux workstation | Filesystem, shell, system information, plus OpenSSL hashing, encryption, and signing with disposable files | [Linux basics](linux-basics/README.md) and [cryptography practice](../02-network-and-host-hardening/network-security/labs/cryptography-and-integrity/README.md) |

## Safe sequencing

1. Choose one environment track and record versions, topology, and reset/snapshot point.
2. Keep the exercise on local, isolated, or explicitly authorized systems.
3. Use dummy accounts and synthetic data; keep raw captures, secrets, and sensitive output private.
4. Treat all existing lab pages as drafts until rerun and verified; record actual results and sanitized evidence.

Tracks are groupings for planning, not claims that the exercises have been completed or validated together.
