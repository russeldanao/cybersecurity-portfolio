# Repository Structure

The portfolio is organized by the six domains in the root [README](../README.md). Historical lab notes are retained as draft study guides; they are not verified reports of completed work. Use the root [lab study template](../LAB-STUDY-TEMPLATE.md) and sanitize evidence before publication.

```text
cybersecurity-portfolio/
├── 01-identity-and-cloud-iam/
│   ├── cloud-fundamentals/
│   ├── notes/
│   └── windows-server-ad-ds/
├── 02-network-and-host-hardening/
│   ├── computer-networks/
│   └── network-security/
│       ├── labs/
│       ├── notes/
│       └── study-guides/
├── 03-detection-and-incident-response/
│   ├── case-studies/
│   ├── endpoint-logging-and-detection/
│   ├── labs/
│   ├── malware-detection-host-triage/
│   ├── network-case-studies/
│   ├── notes/
│   ├── penetration-testing/
│   └── sysmon-wazuh-detection/
├── 04-grc-and-risk-management/
│   └── references/
├── 05-ai-and-automation-security/
│   └── notes/
├── 06-platform-and-data-security/
│   ├── career-and-reference/
│   ├── coursework/
│   ├── cryptography/
│   ├── database-management/
│   ├── linux-basics/
│   └── programming/
├── docs/
├── LAB-STUDY-TEMPLATE.md
├── PROJECT-README-TEMPLATE.md
├── LICENSE
└── CONTENT-LICENSE.md
```

## Lab lifecycle

1. Sanitize notes and evidence before using them in a public write-up.
2. Keep the report marked as a draft while historical results are unverified or evidence is missing.
3. Rerun the exercise in an owned, isolated lab using dummy data.
4. Record the objective, environment, findings/baseline, action/hardening, and verification.
5. Publish only fresh evidence that has been reviewed and sanitized.

Study guides and notes are filed with the domain they support. Identity, network, detection, and GRC references live alongside their relevant materials; general programming, Linux, database, and cryptography foundations live under `06-platform-and-data-security/`. Related exercises are grouped by shared setup.
