# PCAP Protocol Counter — Lab Study Guide
> **Draft study guide ? prior results and evidence are unavailable or have not been reverified. Treat existing details as study notes; rerun and sanitize before reporting findings.** [Use the lab template](../../../../LAB-STUDY-TEMPLATE.md).



## Sanitize First

- Analyze only packet captures you own or are authorized to use.
- Keep original PCAP/PCAPNG files outside the repository.
- Never publish packet payloads, real source addresses, hostnames, credentials, or personal data.
- Review and pseudonymize command output before sharing; aggregate output still contains source IP addresses.

## Objective

Use a small Python helper to count UDP packets associated with NBNS, LLMNR, and SSDP by source address, then compare the counts with Wireshark. The exercise demonstrates triage automation, not protocol validation or a security verdict.

## Environment

- **System:** Record operating system, Python version, and capture provenance during the rerun.
- **Dependency:** Scapy; record the installed version.
- **Input:** An authorized local PCAP/PCAPNG kept outside the repository.
- **Script:** [`count_protocols.py`](count_protocols.py).

Create a virtual environment and install Scapy:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install scapy
```

## Findings / Baseline

- **Prior results:** None recorded. The starter parser has not been executed or validated.
- **Baseline to collect:** Record the authorized capture source, packet counts, Wireshark comparison, and any discrepancies.
- The parser classifies by UDP port: NBNS 137, LLMNR 5355, and SSDP 1900. It does not validate packet payloads.

## Action / Hardening

Run the helper against a private, authorized capture:

```powershell
.\.venv\Scripts\python.exe .\count_protocols.py "C:\path\to\private-capture.pcapng"
```

The designed output is CSV with `protocol`, `source_ip`, and `packet_count` columns. The script does not print payloads or write another capture, but its source addresses still require sanitization before publication.

## Verification

- **Status:** Not verified — rerun required.
- Record Python and Scapy versions, the exact command, capture authorization, actual output, and Wireshark filters/results.
- Test IPv4 and IPv6, source- and destination-port matches, empty captures, missing files, and corrupt or unsupported captures.
- Explain discrepancies and possible false positives caused by port-based classification.
- **Evidence:** None claimed. Add only fresh, reviewed, sanitized test output.
- **Limitations:** A matching port does not prove protocol semantics, malicious activity, or intent.

## Study Notes

- Explain how aggregate counts differ from payload inspection.
- Describe what the parser can and cannot conclude.
- Identify how IP pseudonymization affects comparison with Wireshark.

## References

- See the public [Scapy documentation](https://scapy.readthedocs.io/).
