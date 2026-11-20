# Home Router Security Review — Lab Study Guide
> **Draft study guide - prior results and evidence are unavailable or have not been reverified. Treat existing details as study notes; rerun and sanitize before reporting findings.** [Use the lab template](../../../LAB-STUDY-TEMPLATE.md).



## Sanitize First

- Do not publish a real SSID, home address, public IP, MAC address, account name, password, serial number, or ISP/customer identifier.
- Review every screenshot at full size; black-box sensitive fields, remove metadata, export a sanitized copy, and inspect it again.
- Historical screenshots in the repository are not linked here and should not be treated as proof until reviewed again.

## Objective

Practice reviewing a router's customer-accessible security settings, identify controls that can and cannot be changed, and document safe recommendations without exposing home-network details.

## Environment

- **Device:** Router/ONT owned by the lab operator; record a generic model or omit it if it could identify the home network.
- **Connection:** Local administration interface only; do not expose the management page to the internet.
- **Tools:** Web browser and a written checklist; record firmware and tool versions only if safe to publish.
- **Safety:** Use a device you own or are explicitly authorized to assess. Avoid changes that could disrupt household connectivity unless it is an isolated lab device.

## Findings / Baseline

- **Historical notes:** The prior write-up recorded the following observations and actions. They are unverified study notes, not current findings; confirm each item during a fresh rerun.

| Area | Historical note to validate |
|---|---|
| Administrator access | The earlier notes reported a factory-default password warning and a password change. No password is retained here. |
| Wi-Fi encryption | The notes reported WPA/WPA2-PSK with AES on both bands and no WPA3 option in the available firmware. |
| SSID privacy | The notes reported that the former SSID exposed location information; the actual SSID and address remain intentionally omitted. |
| WPS | The notes reported WPS enabled on both bands, followed by disabling it. |
| Guest/client isolation | The notes reported no customer-accessible guest or client-isolation feature. |
| MAC filtering | The notes reported MAC filtering disabled with no rules and left disabled because it does not provide network segmentation. |
| Remote administration | The notes reported that WAN management was not customer-configurable. |
| Firmware | The notes reported no customer-facing firmware-update option. |

- **Baseline to collect:** Record each setting as observed, unsupported, or not assessed. Do not write a real SSID, address, account name, password, or ISP identifier into the report.
- **Evidence status:** The old screenshots remain as historical artifacts, but this draft does not rely on them as proof. They were visually reviewed for obvious visible identifiers and their image metadata was stripped; review them again before linking or publishing.

## Action / Hardening

In the authorized lab device's local management interface:

1. Check whether the administrative password is a unique, strong, non-default value; never record it.
2. Record the available Wi-Fi authentication and encryption options without recording the SSID or pre-shared key.
3. Check whether WPS is available and enabled.
4. Determine whether guest networking or client isolation is supported; do not assume a second SSID is isolated.
5. Review MAC filtering and explain its limitations; do not treat it as a substitute for encryption or segmentation.
6. Determine whether remote administration and firmware updates are customer-configurable; record unsupported controls as limitations.
7. Make only changes you understand and are authorized to make; record rollback steps before applying changes.

## Verification

- **Status:** Not verified — rerun required.
- Revisit each setting after any change and record the result without sensitive values.
- Confirm administrative access remains available and normal connectivity still works.
- **Evidence:** None claimed. Add only freshly captured, fully redacted, metadata-stripped images.
- **Limitations:** ISP-managed firmware or access restrictions can prevent independent verification of remote management and patch status.

Historical, redacted screenshots retained in `../images/`:

- [Account-management screen](../images/01-account-management.png)
- [2.4 GHz settings](../images/02-24g-encryption.png)
- [5 GHz settings](../images/03-5g-encryption.png)
- [WPS after-state, 2.4 GHz](../images/05-24g-wps-after.png)
- [WPS after-state, 5 GHz](../images/06-5g-wps-after.png)
- [Device access control](../images/07-device-access-control.png)

## Study Notes

- Explain the difference between authentication, encryption, WPS, guest isolation, and MAC filtering.
- Separate observed settings from features that are unavailable or outside the operator's control.
- Recommend a safe next step for any unsupported control without exposing the home network.

## References

- Add the router manufacturer's public documentation and applicable Wi-Fi security guidance used during the rerun.
