from tracker_data import R, SECTIONS
def lst(p):
    return "\n".join(f"- **{r['ID']}** ({r['Status']}): {r['Finding / task']}" for r in R if r["Priority"]==p)
def sec(n): return SECTIONS[n]
approval = [r for r in R if r["Status"] in ("Awaiting client information","Awaiting legal/compliance approval")]
out = []
A = out.append
A("""# Accord Insurance Brokers: Read-Only Audit Report (accordib.com)

Audit date: 2 October 2026. Mode: strictly read-only. Companion file: `Accord_Master_Remediation_Tracker.xlsx` (and `.md`), 109 items with stable IDs ACC-001 onward.

## 1. Executive summary

The site is structurally sound (WordPress 7.1.2, PHP 8.2.34, Elementor 4.3.3 / Pro 4.3.0, Yoast 28.6, no critical Site Health issues, clean redirects, search and 404 pages set to noindex, attachment pages redirect to files, sitemap lists exactly the 19 published pages). It is not yet launch-clean. The main risks are:

1. **Lead and contact integrity.** The contact form emails an agency address, not a client mailbox (ACC-001). The Book a Call page shows a demo phone number with a US tel: link (ACC-002). Three different phone numbers and several email addresses appear across the site (ACC-032, ACC-033).
2. **Provisional and inconsistent legal and company information.** The Complaints page says it is interim and awaits legal review (ACC-003). Two company names (Accord Risk Limited / Accord Insurance Brokers Ltd) and two registered addresses (Milton Keynes / 9 New Street, London) are published (ACC-030, ACC-031). The footer regulatory sentence reads "is a an appointed representative" (ACC-034).
3. **Dummy content is publicly discoverable.** All four dummy posts and the Insights page are published, indexable, in the Yoast sitemap, in the RSS feed and linked from Insights, search and archives (ACC-004, ACC-070). The Insights page contains pasted ChatGPT markup (ACC-010).
4. **Heading structure.** No H1 on most pages; Contact and Book a Call use "General Enquiries" as a late H1 (ACC-050, ACC-051).
5. **Privacy/cookies.** HubSpot Meetings and Google Fonts are not consent-gated, and Complianz points to a non-existent cookie page (ACC-180 to ACC-183). Banner behaviour could not be observed.
6. **Security hygiene.** Public REST user enumeration exposing admin email-style names (ACC-161), Cowboy MCP plugin with write tools active on production (ACC-162), missing front-end security headers (ACC-163), Elementor Pro update pending (ACC-160), no post revisions so backups are essential (ACC-164).

Two earlier suspicions were corrected by evidence: the Elementor template named "test" is the **live global kit** (ID 10) and must not be deleted (ACC-018); the empty footer menu location is **not a defect by itself** because the footer links are built in the Elementor footer template (ACC-015). Elementor library template URLs are not publicly exposed (ACC-022).

Counts by priority: """ + ", ".join(f"{p} {sum(1 for r in R if r['Priority']==p)}" for p in ["Critical","High","Medium","Low","Enhancement"]) + """.

## 2. Complete URL and template inventory

### Published pages (19, all in page-sitemap, all robots "index, follow", canonical self)
| URL | ID | Notes |
|---|---|---|
| / | 448 | Home. og:image lacks dimensions |
| /sectors/ | 426 | Overview |
| /sectors/bridging-lenders/ | 256 | Overlaps 2916 |
| /sectors/commercial-insurance/ | 2140 | |
| /sectors/commodities-trade-finance/ | 2084 | Title stored with &amp;; CTA link defect |
| /sectors/financial-institutions/ | 2171 | |
| /solutions/ | 2125 | |
| /about-us/ | 412 | |
| /claims/ | 2027 | Two dead buttons |
| /insights/ | 324 | Unfinished area, indexable, in sitemap |
| /contact-us/ | 387 | Form to agency mailbox |
| /book-a-call/ | 2792 | Duplicate metadata, demo phone |
| /insurance-for-bridging-lenders/ | 2916 | Not in menu; overlaps 256 |
| /privacy-policy/ | 1245 | |
| /cookie-policy-uk/ | 2862 | No meta description |
| /regulatory-status/ | 1273 | |
| /website-terms-of-use/ | 1278 | |
| /terms-of-business/ | 1640 | |
| /complaints/ | 1642 | Interim wording |

### Posts (4, dummy, published, indexable, in post-sitemap)
/protecting-businesses-against-operational-disruption/ (218), -2/ (1302), -3/ (1305), -4/ (2192).

### Archives and special URLs
/category/accord/ (indexable, in sitemap); /author/matthewaccordib-com/ (indexable, in sitemap); /author/ (404); /blog/ (404); /feed/ (200, full content of the 4 posts); /?s=... (noindex,follow); 404 page (noindex,follow); /llms.txt (404); /robots.txt (allow all, sitemap_index.xml); sitemap_index.xml (post, page, category, author); /sitemap.xml and /wp-sitemap.xml redirect once; attachment pages redirect to file; /wp-json/wp/v2/users public (3 users); xmlrpc.php 403.

### Menus
Header (id 47, location menu-1): Home, Sectors (#) with Overview and four sector pages, Solutions, About, Contact. Footer - Main (id 28, 0 items, no location). Sectors Menu (id 46, 4 items, unassigned).

### Elementor Theme Builder and library (33 items)
- Header 125 (all), Footer 108 (all), Accord Legal Pages 1239 (single-page, pages 1245, 1249 [does not exist], 1273, 2862, 1642, 1640, 1278), Insights Template 82 (single post), Error 404 (66), Blog Posts Archive 80, Search Results 70.
- Popup: Book a Call 2804 (no stored conditions found; opened by header button on desktop).
- Page templates: Coming Soon 2649 (not served; maintenance mode off).
- Global containers: Hero Option 1 (1787), Why choose Accord 1 image (1689), 3 images (1776), Our 3 Step Process (1700), Our sectors (1709), Expertise (1716), Our Expertise (1727), Our Team (1679), Our team with Bios (2373), Template Container (1753), Sectors 4 images (1830), Button White BG (1836).
- Loop and archive templates (Finance and Investment kit leftovers): 64, 68, 78, 93, 101, 117, 119, 121, 123, 133 (119 is in use by the Insights loop).
- Kits: active kit 10 (titled "test"), Default Kit 6 (unused). No e-floating-buttons.
- Global colours: Accent 9 #000000CC, Accent 10 #FFFFFF33, Background Blur #FFFFFFCC, Accord Dark Blue #0B203B, Accord Dark Green #042705, Trans #FFFFFF00, No colour; system colours from the Vamtam demo (#2E2E2E, #FFFBE7, #F6F5F2, #92C200, #7E7E7E). Fonts: Work Sans (all), Poppins (Body Link). Container width 1280px, breakpoints mobile 768 and tablet 1025, no widescreen.

### Platform
Theme: accord-insurance 1.0.0 (child of Hello Elementor 3.5.1; effectively empty). 14 active plugins, none inactive: ACF 6.8.10, Complianz 7.5.5, Cowboy MCP 1.6.9, Joinchat 6.4.0, Yoast Duplicate Post 4.7, Elementor 4.3.3, Elementor Pro 4.3.0 (4.3.1 available), Orbit Yoast Data Dashboard 1.3.2, Safe SVG 2.5.1, SG Speed Optimizer 7.8.3, SG Security 1.6.8, Custom Content by Orbit 1.1.1, Stream 4.4.0, Yoast SEO 28.6. MySQL 8.4.6. No mu-plugins.

### Per-URL SEO head (rendered, from Yoast)
Titles are 40 to 59 characters, descriptions 127 to 152 characters, canonical self on all, og:type article on all but home. Exceptions: Cookie Policy (no description), Book a Call (duplicates Contact), og:image dimensions missing on home, sectors, solutions, 2916 and the author page. Full per-URL table: see the SEO agent notes in the scratchpad (`seo/`) and tracker items ACC-053 to ACC-059.

### Forms and integrations (not submitted)
One Elementor form (Contact, 5 required fields, no consent, no spam control, to agency mailbox). HubSpot Meetings embed on Contact, Book a Call and the popup. Joinchat WhatsApp widget. Complianz (UK). Google site verification tag. No analytics IDs found (GTM, GA4, Pixel).

### Images
100 attachments (96 images including 12 SVG, 4 MP4, 0 PDF); 95 of 96 images have empty library alt. Image CSV: `scratchpad/media/image_inventory.csv` (library metadata complete; page usage verified for only part of the site). See ACC-110 to ACC-119.

## 3. Findings by priority
### Critical
""" + lst("Critical") + """

### High
""" + lst("High") + """

### Medium
""" + lst("Medium") + """

### Low
""" + lst("Low") + """

### Enhancement
""" + lst("Enhancement") + """

Every finding has full evidence, severity, confidence, scope, recommended action and approval needs in the tracker.

## 4. Facts to verify with the client (not inferred)
- Legal entity name, trading name, registered office and company number; which address and phone number are current (ACC-030, 031, 032).
- Which email addresses are valid and monitored, and who should receive form enquiries and complaints (ACC-001, 033).
- Whether the Insights area and the four posts are meant to be public; whether the posts' text is approved copy (ACC-004, 070).
- Whether Accord may call itself an independent broker as an appointed representative; the FSCS statement; complaint timescales (ACC-035, 036, 038).
- Approved complaints, terms, privacy and cookie wording (ACC-003, 037 to 040, 184).
- LinkedIn company URL (ACC-014); WhatsApp number (ACC-145); intended destinations for dead CTAs (ACC-011, 012, 143).
- Preferred role of /book-a-call/ and /insurance-for-bridging-lenders/ (ACC-053, 055).
- Brand palette and hero colours (ACC-080, 081).
- Whether the HubSpot meeting link and calendar belong to a named individual or the firm (ACC-180).

## 5. Things that could not be inspected, and what is needed
- Full rendered HTML and the wp_footer output: the HTTP tool truncates bodies at about 51,200 characters, so cookie banner markup, late scripts, footer headings and page tails were not seen. Need: browser or full-fetch access.
- Console errors, network failures, Core Web Vitals, responsive rendering, colour contrast, keyboard behaviour. Need: browser with dev tools or staging access.
- Yoast global settings (wpseo, wpseo_titles, wpseo_social). Need: a settings export or screenshots.
- Complete image-to-page usage mapping; ACF field details; Elementor popup display settings; submission storage; Orbit plugin options; SG optimiser settings; comment/pingback defaults; show_on_front and similar core options. Need: staging read access or exports.
- External URLs (HubSpot, FOS, ICO, Vamtam demo): outside the permitted host.
- Form behaviour (not submitted by design).

## 6. Proposed remediation sequence (controlled batches)
Details of batch contents are in `Remediation_Plan.md`. In order: Batch 0 preparation and decisions; Batch 1 low-risk corrections; Batch 2 facts-dependent critical fixes (contact routing, phone, legal wording); Batch 3 indexing and sitemap controls; Batch 4 headings and H1; Batch 5 images and alt; Batch 6 privacy and cookies; Batch 7 security and maintenance including the Elementor Pro update on staging; Batch 8 template clean-up after verification; Batch 9 final regression.

## 7. Process disclosure and statement on changes
- **No website content, templates, settings, plugins, themes, users, forms or caches were changed.** No form was submitted; no update or install was run.
- Beyond the strict brief: audit agents ran `wp_cli` read commands with `confirm:true`, which made the Cowboy plugin create **11 server-side database checkpoints** (IDs 1 to 11, 14:22:50 to 14:24:36 UTC, none after). They are backup dumps, not changes to the site, and are recorded as ACC-006 for your decision. They were not deleted. One agent also used a `wp_batch_execute` wrapper around 20 HEAD requests.
- Every GET/HEAD through the plugin's HTTP tool is logged in the plugin's change journal as a "not_undoable" entry. These are audit records, not site changes.
- A Complianz client secret and access token were printed into an agent's working output (ACC-005). A local file containing them was deleted. They were not placed in this report.
- This report quotes publicly visible text. Admin emails and secrets are not reproduced.
""")
open("Accord_Audit_Report.md","w").write("\n".join(out))
