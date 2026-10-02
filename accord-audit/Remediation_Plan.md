# Accord remediation plan (proposal only, nothing here is approved)

No change below may be made until you approve it. All work should happen on staging first, after a full external backup (revisions are 0 and the Cowboy checkpoints are not a substitute: ACC-164, ACC-190).

## A. Recommended first batch (low risk, high confidence, no legal or client facts needed)

| ID | Change | Why it is safe |
|---|---|---|
| ACC-141 | Correct "Borkers" to "Brokers" in the contact form subject and from-name | One word, notification text only |
| ACC-010 | Remove pasted ChatGPT markup from the Insights text widget, keeping the paragraph wording | Junk attributes only; text unchanged |
| ACC-144 | Add trailing slashes to the two sector links in template 1709 and the /sectors/ buttons | Removes a redirect; same destination |
| ACC-133 | Make duplicate SVG ids unique on /sectors/financial-institutions/ | Invisible markup fix |
| ACC-082 | Remove the non-existent page 1249 from the Legal Pages template condition (staging first) | Stale reference; all six real legal pages stay assigned |
| ACC-054 | Add a plain factual meta description to the Cookie Policy (draft wording for your approval first) | SEO field only, not legal text |

Held back deliberately: anything touching legal wording, company details, phone numbers, recipients, indexing decisions, template deletion, the Elementor Pro update and alt text (needs classification).

## B. Items needing your decision or client / compliance confirmation

**Client information**
- ACC-001 who receives contact form enquiries (and whether the agency keeps a BCC)
- ACC-002 / ACC-032 the correct public phone number(s)
- ACC-033 valid email addresses and a role mailbox for complaints
- ACC-030 / ACC-031 legal entity name, trading name, registered office, company number
- ACC-004 / ACC-070 / ACC-013 whether the four posts and Insights should be public now
- ACC-014 LinkedIn URL; ACC-145 WhatsApp number
- ACC-011 / ACC-012 / ACC-143 destinations for dead or mislabelled buttons
- ACC-053 / ACC-055 role of /book-a-call/ and /insurance-for-bridging-lenders/
- ACC-072 which legal/utility pages should be indexed
- ACC-080 / ACC-081 brand palette and hero colours; ACC-116 legal page hero image
- ACC-056 organisation details for schema (after legal facts are settled)

**Legal / compliance approval**
- ACC-003 approved complaints wording (and ACC-038 timescales)
- ACC-034 footer sentence correction ("a an")
- ACC-035 "independent broker" claim; ACC-036 FSCS statement; ACC-042 product and market claims
- ACC-037 Terms of Business typos; ACC-039 / ACC-040 other legal pages
- ACC-140 form consent wording; ACC-180 / ACC-181 / ACC-182 / ACC-183 / ACC-184 / ACC-185 cookie and consent treatment

**Your decision**
- ACC-006 keep or delete the 11 audit checkpoints
- ACC-005 whether to rotate the exposed Complianz credentials
- ACC-160 Elementor Pro update window (staging first, never live-first)
- ACC-162 how long Cowboy MCP stays active; admin account review
- ACC-060 how to supply Yoast settings (export or screenshots)
- ACC-100 / ACC-134 / ACC-150 / ACC-186 provide browser or staging access for the visual, accessibility, performance and cookie-banner checks

## C. Proposed sequence of controlled batches

| Batch | Contents | Gate |
|---|---|---|
| 0 Preparation | Full external backup, staging clone, baseline crawl (ACC-190); decisions in section B; decide ACC-005 and ACC-006 | All decisions logged |
| 1 Low-risk corrections | Section A items | You approve; staging regression (ACC-191) |
| 2 Critical facts-dependent fixes | ACC-001 recipients, ACC-002 phone, ACC-003 complaints text, company/address/phone alignment (ACC-030 to ACC-033), ACC-034, ACC-011 / 012 / 143 | Client facts and compliance sign-off in writing |
| 3 Indexing and sitemap | ACC-004, ACC-070, ACC-071, ACC-053, ACC-072 (noindex first, reversible; delete nothing) | Client decisions; Search Console follow-up (ACC-192) |
| 4 Headings | ACC-050 to ACC-052 (shared templates first, then pages) | Visual regression at 4 widths |
| 5 Images and media | ACC-110 to ACC-119 after classification and a full usage scan; ACC-113 site icon | Usage scan complete |
| 6 Privacy and cookies | ACC-180 to ACC-186, ACC-140 | Compliance sign-off; browser consent test |
| 7 Security and maintenance | ACC-161, ACC-163, ACC-162; ACC-160 Elementor Pro 4.3.1 on staging then live in a window | Backup, staging pass |
| 8 Template clean-up | ACC-016, ACC-017, ACC-018, ACC-019, ACC-020, ACC-084 (only items proven unused, unconditioned, unreferenced and not needed for rollback; never delete kit 10 or template 119 while the Insights loop exists) | Verification evidence per template |
| 9 Final regression | ACC-191 to ACC-193 | All items Verified complete or Intentionally retained |
