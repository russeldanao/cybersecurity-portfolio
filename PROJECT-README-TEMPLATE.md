# <Project Title>

> **One-line summary:** <what you did, on what system, and the result a recruiter should remember>

| | |
|---|---|
| **Domain** | <Identity & Cloud IAM / Host & Network Hardening / Detection & IR / GRC / AI & Automation> |
| **Environment** | <e.g., VMware Workstation, Windows 11 lab VM, host-only network> |
| **Tools** | <free tools only, with versions if known> |
| **Frameworks** | <CIS Benchmark / NIST CSF 2.0 / MITRE ATT&CK / OWASP LLM Top 10> |
| **Status** | <Complete / Partial evidence / Draft> |
| **Date** | <YYYY-MM> |

## 1. Objective & Scope

- **Goal:** <the control, detection, or decision this project proves>
- **In scope:** <hosts, protocols, identities, or documents you actually tested>
- **Out of scope:** <what you did not test, and why>
- **Success criteria:** <the before/after or artifact that counts as done>
- **Assumptions:** isolated lab or free-tier tenant, dummy accounts, no production systems

## 2. Setup & Tooling

- **Environment:** <hypervisor, guest OS/build, network mode, tenant type>
- **Tools and versions:** <Wireshark, PowerShell, Python, browser, and so on>
- **Safety controls:** snapshot before changes; host-only or lab network; throwaway account; no public exposure of vulnerable services
- **Sanitization:** hostnames, IPs, usernames, and identifiers in this write-up are lab or dummy values

## 3. Execution & Findings

1. <what you changed or observed>
2. <how you captured evidence>
3. <what the evidence showed>

| # | Finding | Evidence | Severity | Recommendation |
|---|---------|----------|----------|----------------|
| 1 | <what was true before or after the change> | `evidence/<file>` | <Info / Low / Medium / High> | <what to keep or fix next> |

## 4. Verification

- **How I confirmed it:** <same trigger, same filter, or same check run before and after>
- **Before vs. after:** <one sentence each>
- **What is still open:** <missing screenshot, untested control, or draft step>
- **Limitations:** <single VM, one capture window, free-tier constraint, or tool limit>

## 5. Key Takeaways

- <what this demonstrates for a security role>
- <the control or detection you would repeat in a real environment>
- <the next check you would run>

## References

- <vendor doc, benchmark, or standard. Link the public source. Do not paste copyrighted lab manuals.>

## Sanitization note

No credentials, tokens, session cookies, raw packet captures, production hostnames, or real personal data are included. Screenshots are redacted and metadata is stripped before publication.
