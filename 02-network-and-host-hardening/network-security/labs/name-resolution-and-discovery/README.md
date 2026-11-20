# Name Resolution and Discovery Protocols — Lab Study Guide
> **Draft study guide - prior results and evidence are unavailable or have not been reverified. Treat existing details as study notes; rerun and sanitize before reporting findings.** [Use the lab template](../../../../LAB-STUDY-TEMPLATE.md).



## Sanitize First

- Use an isolated, owned lab and dummy hostnames and accounts.
- Review every screenshot before sharing. Existing images in this folder are historical artifacts and have not been revalidated as evidence for this draft.
- Do not publish raw packet captures, real host or network identifiers, credentials, or personal data.
- If an artifact cannot be confirmed safe, do not link or publish it.

## Objective

Practice observing name-resolution and service-discovery traffic and evaluating host configuration changes for NBNS, LLMNR, and SSDP. Separately inspect a DHCP lease option and learn how DNS lookups and caching can be documented.

## Environment

- **System:** Windows lab host; edition, build, and VM/network details must be recorded during the rerun.
- **Tools:** Wireshark and Windows configuration, service, and listener checks; record versions when rerun.
- **Isolation:** Owned lab only. Document the network mode and use synthetic hostnames.
- **Prior trigger notes:** `ping nonexistentuser` was used for name-resolution observations; opening File Explorer > Network and waiting was used for SSDP observations. Reconfirm safe, reproducible triggers in the lab.

## Findings / Baseline

The following are historical notes only. They are **not verified findings** because the prior evidence is unavailable or has not been revalidated:

| Area | Historical note to retest |
|---|---|
| NBNS | Notes describe NBNS as enabled and a packet count of 3 for a test trigger. |
| LLMNR | Notes describe 8 queries and a UDP 5355 listener at baseline. |
| SSDP | Notes describe SSDPSRV running, UDP 1900 activity, and 12 packets during discovery. |
| DHCP option 51 | Notes describe a DHCP ACK with a 3600-second lease value. This is a lease observation, not a hardening result. |
| DNS | A complete DNS lookup and cache analysis was not documented. |

Collect a fresh baseline with the exact trigger, Wireshark filter, capture window, service state, and listener state recorded. Do not copy the historical counts into a new results section as observed data.

## Action / Hardening

In an isolated, snapshot-backed Windows lab, review the relevant settings and test one change at a time:

1. Record NetBIOS over TCP/IP state. If appropriate for the lab, disable it through the adapter's IPv4 Advanced > WINS settings.
2. Record LLMNR policy and listener state. If appropriate for the lab, disable LLMNR through policy, apply the setting, and restart as required.
3. Record SSDPSRV and UPnP Host state. If appropriate for the lab, disable only the services in scope and note any discovery features affected.
4. Repeat the same test triggers after each change.
5. Treat DHCP option inspection as a separate lease-audit exercise.
6. Add DNS A/AAAA, MX, NS, and TXT lookup and cache inspection as a separate study exercise.

Use the Microsoft documentation for the exact OS version. Do not apply settings to a production or shared system.

## Verification

- **Status:** Not verified — prior evidence unavailable or not revalidated; rerun required.
- **For each protocol:** Compare fresh before/after observations using the same trigger, filter, and capture duration; record relevant configuration, service, and listener state.
- **Follow-up checks from old notes:** Record NetBIOS after-state checks (`nbtstat -n` and ports 137–139), UPnP Host start type, and DNS lookup/cache observations.
- **Evidence:** None claimed for this draft. Add only newly captured, reviewed, and sanitized evidence.
- **Limitations:** A zero packet count applies only to the tested trigger and observation window; it does not prove a protocol can never be used.

## Study Notes

- Distinguish configuration state from observed network behavior.
- Explain the difference between NBNS, LLMNR, SSDP, DHCP lease options, and DNS.
- Record false positives, unrelated multicast traffic, and test limitations.

## References

- See the Windows hardening notes in `windows-network-hardening/docs/`.
- Add links to relevant Microsoft and Wireshark documentation for the OS and tool versions used during the rerun.
