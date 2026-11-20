# Sanitization Policy

Nothing is published as lab evidence until it passes this list. Lab reports remain drafts until rerun and verified; old notes and screenshots are not proof by default.

## Must be removed or replaced
| Item | Replace with |
|---|---|
| Real name / student ID on screenshots or headers | Remove entirely |
| Device name, Windows username (e.g., in `C:\Users\<name>`) | `LAB-WS01`, `C:\Users\labuser` |
| Device ID, Product ID, serial numbers | Black-box redaction (not blur) |
| Wi-Fi SSID, MAC addresses | `SSID-REDACTED`, `AA:BB:CC:00:00:01` | <!-- sanitize: ignore -->
| Home gateway/DNS and public IP | Documentation ranges: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` |
| Email addresses, tokens, cookies, hostnames from real networks | Remove |
| Third-party or institution-owned material (slides, handouts, papers) | Do not publish; link to it and write in your own words |

## Method
1. Redact by **solid black rectangles**, export as a new image, and inspect it at full size. Blur is reversible.
2. Strip image metadata with an available metadata tool, for example `exiftool -all= image.png`, then verify the exported file.
3. Do not publish raw PCAPs. If a capture is necessary for a local lab, keep it private and use only sanitized, minimal derived output.
4. Search text files for personal names, account identifiers, emails, addresses, tokens, private keys, and real network details. Review every match manually; examples and documentation ranges need context.
5. Link or embed an image only after its content and metadata have been reviewed.

## Final gate
- [ ] No private IPs from a real network
- [ ] No identifiers in image alt text or filenames
- [ ] Git history clean (use a fresh repo; do not commit then delete)

## Tooling
The repository does not currently contain the sanitization scripts or automated workflow previously described here. Until such tooling is added and verified, use the manual checks above and do not claim that an automated sanitizer has run. Visual image review remains required even if a text scanner is added.

## Git identity (often forgotten)
Commits embed your author email. Before the first commit:
```bash
git config user.name  "<GitHub display name>"
git config user.email "<your-id>+<username>@users.noreply.github.com"   # GitHub Settings > Emails
```
and enable **Keep my email addresses private** and **Block command line pushes that expose my email** in GitHub settings.
