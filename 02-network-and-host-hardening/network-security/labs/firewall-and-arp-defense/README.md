# Firewall and ARP Defense
> **Draft study guide - prior results and evidence are unavailable or have not been reverified. Treat existing details as study notes; rerun and sanitize before reporting findings.** [Use the lab template](../../../../LAB-STUDY-TEMPLATE.md).



This lab combines host firewall controls with local-network address-resolution defenses. Perform all tests only on systems and networks you own or have explicit authorization to assess.

## Skills Demonstrated

- Design scoped firewall rules and verification steps.
- Explain ARP behavior and defensive monitoring.
- Plan safe testing on an isolated authorized network.

*Complete marked steps and record actual results before claiming hands-on completion.*

## Experiment tracks
- **Windows Defender Firewall:** review profile defaults; create, test, and remove inbound and outbound rules; reproduce a rule with netsh.
- **ARP security:** capture a normal request/reply, inspect cache behavior, detect suspicious replies, and document mitigations.

## Build next
1. Record the active firewall profile and baseline rules.
2. Add and verify an inbound and outbound test rule.
3. Repeat one rule with netsh and explain each parameter.
4. Remove the test rules and verify the original state.
5. On an isolated network with owned VMs, capture a normal ARP exchange.
6. Document indicators such as unsolicited replies and conflicting address-to-MAC mappings.
7. Explain static entries and Dynamic ARP Inspection, including their limits.

## Source notes

The earlier source-archive write-ups are not present in this publication copy. Keep any recovered originals separate until they have been reviewed and sanitized; use this document as the current draft study guide.

