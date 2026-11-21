# Repository Structure

The portfolio is organized by the six domains in the root [README](../README.md). Historical lab notes are retained as draft study guides; they are not verified reports of completed work. Use the root [lab study template](../LAB-STUDY-TEMPLATE.md) and sanitize evidence before publication.

```text
cybersecurity-portfolio/
├── 01-identity-and-cloud-iam/
│   ├── cloud-fundamentals/
│   └── windows-server-ad-ds/
│       └── labs/
├── 02-network-and-host-hardening/
│   ├── computer-networks/
│   └── network-security/
│       └── labs/
├── 03-detection-and-incident-response/
│   ├── case-studies/
│   ├── endpoint-logging-and-detection/
│   ├── labs/
│   ├── malware-detection-host-triage/
│   ├── network-case-studies/
│   ├── notes/
│   └── sysmon-wazuh-detection/
├── 04-grc-and-risk-management/
│   └── references/
├── 05-ai-and-automation-security/
│   └── notes/
├── 06-study-guides-and-notes/
│   ├── communications-os-and-data-management/
│   ├── cryptography/
│   ├── network-security-notes/
│   └── programming-fundamentals/
├── 07-platform-and-data-security/
│   ├── database-management/
│   └── linux-basics/
├── docs/
├── BUILD-CHECKLIST.md
├── LAB-STUDY-TEMPLATE.md
├── PROJECT-README-TEMPLATE.md
├── LICENSE
├── CONTENT-LICENSE.md
├── _apply_layout.py
└── restructure.py
```

## Lab lifecycle

1. Sanitize notes and evidence before using them in a public write-up.
2. Keep the report marked as a draft while historical results are unverified or evidence is missing.
3. Rerun the exercise in an owned, isolated lab using dummy data.
4. Record the objective, environment, findings/baseline, action/hardening, and verification.
5. Publish only fresh evidence that has been reviewed and sanitized.

The `06-study-guides-and-notes/` area is for coursework summaries and reference notes, with no lab directories. Technical lab drafts stay in their domain folders; foundational Linux and database practice is grouped under `07-platform-and-data-security/`, organized by shared setup.
