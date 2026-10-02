# Accord Insurance Brokers: Read-Only Audit Report (accordib.com)

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

Counts by priority: Critical 3, High 12, Medium 38, Low 48, Enhancement 8.

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
- **ACC-001** (Awaiting client information): Contact form notifications are routed to the agency mailbox, not a client mailbox
- **ACC-002** (Awaiting client information): Placeholder demo phone number and a US tel: link on the live Book a Call page
- **ACC-003** (Awaiting legal/compliance approval): Complaints page states it is interim and awaits legal/compliance review

### High
- **ACC-004** (Confirmed — awaiting approval): Four dummy posts are published, indexable, in the Yoast sitemap, in the RSS feed and linked from Insights, search and archives
- **ACC-005** (Awaiting client information): Complianz client credentials were printed into an audit agent transcript
- **ACC-030** (Awaiting client information): Two different company names used across legal pages and settings
- **ACC-031** (Awaiting client information): Two different registered office addresses
- **ACC-032** (Awaiting client information): Three different telephone numbers, one mismatching its link
- **ACC-035** (Awaiting legal/compliance approval): 'Independent insurance broker' claim alongside appointed-representative status
- **ACC-036** (Awaiting legal/compliance approval): Terms of Business states FSCS membership
- **ACC-050** (Confirmed — awaiting approval): No H1 on most pages
- **ACC-051** (Confirmed — awaiting approval): Contact and Book a Call use the wrong H1
- **ACC-070** (Awaiting client information): Insights page is live, indexable, in the sitemap and not in navigation
- **ACC-190** (Confirmed — awaiting approval): Pre-remediation baseline and staging
- **ACC-191** (Confirmed — awaiting approval): Post-batch regression checklist

### Medium
- **ACC-010** (Confirmed — awaiting approval): Pasted ChatGPT interface markup inside the Insights page text widget
- **ACC-011** (Needs verification): Commodities & Trade Finance hero/CTA link is empty or malformed
- **ACC-012** (Confirmed — awaiting approval): Claims page: both 'Get in touch' buttons have no destination
- **ACC-013** (Awaiting client information): Footer 'Insights' entry is plain text, not a link
- **ACC-018** (Needs verification): Active Elementor kit is titled 'test' and carries Vamtam theme globals
- **ACC-033** (Awaiting client information): Several email addresses, mixed case, and a named individual's mailbox for complaints
- **ACC-034** (Awaiting legal/compliance approval): Typo in the regulatory statement: 'is a an appointed representative'
- **ACC-037** (Awaiting legal/compliance approval): Typos and wording errors in the Terms of Business
- **ACC-038** (Awaiting legal/compliance approval): Inconsistent complaint timescales between Complaints page and Terms of Business
- **ACC-039** (Awaiting legal/compliance approval): Website Terms of Use: dated and future-tense regulatory wording, terminology mismatch
- **ACC-042** (Awaiting legal/compliance approval): Strong product and market claims needing compliance review
- **ACC-052** (Confirmed — awaiting approval): Inconsistent heading hierarchy in shared templates, legal, search and 404 pages
- **ACC-053** (Awaiting client information): /book-a-call/ duplicates the Contact page metadata and is indexable
- **ACC-055** (Awaiting client information): Overlapping bridging-lender pages and keyphrase cannibalisation
- **ACC-056** (Awaiting client information): Organization schema is minimal
- **ACC-060** (Needs verification): Yoast global settings not inspected
- **ACC-071** (Confirmed — awaiting approval): Author and category archives are indexable and in the sitemap
- **ACC-100** (Needs verification): Responsive rendering was not inspected visually
- **ACC-110** (Needs verification): Most media have empty alt text; informative images must be classified before any change
- **ACC-111** (Confirmed — awaiting approval): Weak or placeholder-grade alt text on specific images
- **ACC-114** (Needs verification): Oversize images and videos
- **ACC-118** (Needs verification): Image-to-page usage mapping is incomplete
- **ACC-131** (Needs verification): Autoplay hero video without pause control, captions or accessible name; two 8.3 MB references
- **ACC-134** (Needs verification): Colour contrast, focus order and form accessibility not tested
- **ACC-140** (Awaiting legal/compliance approval): Contact form has no consent or privacy notice, no spam control, default success message
- **ACC-143** (Awaiting client information): 'Review Policy' button on the bridging lenders page points to /sectors/
- **ACC-150** (Needs verification): Performance not measured; console errors and network failures not captured
- **ACC-160** (Confirmed — awaiting approval): Elementor Pro 4.3.0 has an update available (4.3.1)
- **ACC-161** (Confirmed — awaiting approval): Public REST API exposes user accounts
- **ACC-162** (Awaiting client information): Cowboy MCP plugin with write, file and SQL tools is active in production; 4 administrators including a personal account
- **ACC-164** (Confirmed — awaiting approval): No post revisions; remediation needs an external backup
- **ACC-180** (Awaiting legal/compliance approval): HubSpot Meetings embed loads without consent gating
- **ACC-181** (Needs verification): Google Fonts load from Google servers despite a self-host setting
- **ACC-182** (Needs verification): Complianz configuration incomplete or inconsistent
- **ACC-183** (Confirmed — awaiting approval): Cookie statement points to a non-existent page
- **ACC-186** (Needs verification): Cookie banner markup and pre-consent scripts not observed
- **ACC-192** (Confirmed — awaiting approval): Search Console and indexing follow-up
- **ACC-193** (Confirmed — awaiting approval): Repeat this audit against the baseline

### Low
- **ACC-006** (Confirmed — awaiting approval): Audit side effects: 11 server-side database checkpoints were created by wp_cli calls
- **ACC-014** (Awaiting client information): Footer LinkedIn icon has no URL
- **ACC-015** (Needs verification): Footer sub-footer nav-menu widget points at an empty menu with no theme location
- **ACC-016** (Needs verification): Unassigned menus: 'Sectors Menu' (id 46, 4 items) and 'Footer - Main' (id 28)
- **ACC-017** (Needs verification): Finance and Investment template-kit leftovers (loop/archive/search templates and slugs)
- **ACC-019** (Needs verification): Demo debris in settings and templates (hidden video URLs, demo image, demo slug, placeholder headings)
- **ACC-020** (Needs verification): Unused global container templates and saved sections
- **ACC-021** (Not an issue): Draft, private, pending, future and trash content
- **ACC-022** (Not an issue): Elementor library templates and Coming Soon page publicly reachable
- **ACC-023** (Needs verification): Unresolved '{title}' style template variables in crawlable markup
- **ACC-040** (Awaiting legal/compliance approval): Privacy Policy lacks a last-updated date and regulatory identity
- **ACC-041** (Awaiting client information): Third-party regulator/ombudsman links and details to verify
- **ACC-054** (Confirmed — awaiting approval): Cookie Policy has no meta description and default title format
- **ACC-057** (Needs verification): Open Graph images lack width, height and type on several URLs
- **ACC-058** (Confirmed — awaiting approval): Schema and breadcrumb text defects
- **ACC-059** (Needs verification): Possible second meta description tag on Contact
- **ACC-063** (Not an issue): Yoast get_head endpoint returned 404 for /claims/
- **ACC-072** (Awaiting client information): Legal and utility pages are all indexable
- **ACC-073** (Not an issue): Sitemap composition matches published pages; redirects and special URLs behave
- **ACC-080** (Awaiting client information): Hero colour differs per page from one shared hero template
- **ACC-081** (Needs verification): Global palette mixes Vamtam demo colours with the Accord brand; hard-coded colours on pages
- **ACC-082** (Confirmed — awaiting approval): Legal Pages template condition lists a page that does not exist
- **ACC-083** (Needs verification): Book a Call is implemented two ways
- **ACC-084** (Needs verification): Search Results template carries placeholder headings
- **ACC-085** (Needs verification): Atomic (V4) editor experiments are active with mixed widget generations
- **ACC-101** (Needs verification): Footer legal text is set at 11px
- **ACC-112** (Needs verification): Non-descriptive filenames and typos in filenames
- **ACC-113** (Confirmed — awaiting approval): Site icon is a 584 KB JPEG at 514x512
- **ACC-115** (Needs verification): Duplicate or orphan media candidates
- **ACC-116** (Confirmed — awaiting approval): One stock hero image reused across legal pages and as social image
- **ACC-117** (Needs verification): Footer logo Asset-2.svg has empty alt
- **ACC-119** (Needs verification): Yoast default social image not set
- **ACC-130** (Needs verification): Header desktop and mobile duplicates both present in HTML
- **ACC-132** (Confirmed — awaiting approval): Repeated and weak link text
- **ACC-133** (Confirmed — awaiting approval): Duplicate HTML ids
- **ACC-135** (Needs verification): Form field labelling oddities
- **ACC-141** (Confirmed — awaiting approval): Contact form subject and sender name contain a typo
- **ACC-144** (Confirmed — awaiting approval): Sector links omit the trailing slash and cause a redirect
- **ACC-145** (Needs verification): Joinchat WhatsApp widget configuration
- **ACC-151** (Confirmed — awaiting approval): Lazy images omit width and height; high fetch priority on a below-fold card
- **ACC-152** (Needs verification): PHP error log shows cron save failures and old fatal errors
- **ACC-153** (Needs verification): Cache drop-ins and detection mismatch
- **ACC-154** (Not an issue): Redirect behaviour is clean on core URLs
- **ACC-163** (Confirmed — awaiting approval): Security headers missing on front-end pages
- **ACC-165** (Needs verification): SVG upload settings
- **ACC-166** (Not an issue): Activity logging and security plugins present
- **ACC-184** (Awaiting legal/compliance approval): Cookie Policy text includes irrelevant boilerplate and services not evidently used
- **ACC-185** (Awaiting legal/compliance approval): Joinchat has no consent opt-in and tracking enabled

### Enhancement
- **ACC-061** (Deferred): Yoast traffic-light scores on some pages
- **ACC-062** (Deferred): llms.txt not generated
- **ACC-086** (Deferred): Child theme is effectively empty
- **ACC-200** (Deferred): Client summary: enquiries and contact details
- **ACC-201** (Deferred): Client summary: legal and regulatory accuracy
- **ACC-202** (Deferred): Client summary: search visibility and clean indexing
- **ACC-203** (Deferred): Client summary: accessibility, images and speed
- **ACC-204** (Deferred): Client summary: privacy, security and upkeep

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
