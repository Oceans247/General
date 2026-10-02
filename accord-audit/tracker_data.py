# Master remediation tracker data for accordib.com (read-only audit, 2 Oct 2026).
# Status values are restricted to the approved list.

SECTIONS = {
    1: "Immediate concerns",
    2: "Content and development leftovers",
    3: "Legal, regulatory and company-information consistency",
    4: "SEO and Yoast",
    5: "Sitemap, indexing and archives",
    6: "Elementor templates and design consistency",
    7: "Responsive layout",
    8: "Images and media",
    9: "Accessibility",
    10: "Forms and conversion paths",
    11: "Performance and technical health",
    12: "WordPress maintenance and security",
    13: "Privacy and cookies",
    14: "Final regression testing",
    15: "Client-facing improvements summary",
}

STATUSES = [
    "Confirmed — awaiting approval", "Needs verification", "Awaiting client information",
    "Awaiting legal/compliance approval", "Approved", "In progress", "Fixed — awaiting QA",
    "Verified complete", "Deferred", "Intentionally retained", "Not an issue",
]

CA = "Confirmed — awaiting approval"
NV = "Needs verification"
CI = "Awaiting client information"
LC = "Awaiting legal/compliance approval"
DF = "Deferred"
NI = "Not an issue"

COLS = ["ID", "Section", "Finding / task", "Category", "Affected URL / template / setting", "Exact supporting evidence",
        "Priority", "Status", "Impact", "Confirmed or needs verification", "Approval required", "Recommended action",
        "Change risk", "Dependencies", "Verification test after remediation", "Notes"]

R = []
def F(id, sec, finding, cat, affected, evidence, pri, status, impact, conf, appr, action, risk, deps, test, notes=""):
    assert status in STATUSES, status
    assert pri in ("Critical", "High", "Medium", "Low", "Enhancement"), pri
    R.append(dict(zip(COLS, [id, SECTIONS[sec], finding, cat, affected, evidence, pri, status, impact, conf, appr, action, risk, deps, test, notes])))

# ---------------- 1. Immediate concerns ----------------
F("ACC-001", 1, "Contact form notifications are routed to the agency mailbox, not a client mailbox", "Forms / conversion",
  "/contact-us/ (page 387), Elementor form widget 59a67030 'Get in Touch Form'",
  "Stored settings: email_to, email_to_2 and email_reply_to_2 all use an address on the orbitagency.co.uk domain; email_from = email@accordib.com. No webhook, CRM or redirect configured. Reported independently by two agents. Form was NOT submitted.",
  "Critical", CI, "Visitor, conversion: genuine enquiries may not reach the client; compliance: enquiries held by a third party",
  "Confirmed (stored settings); intent unverified", "Client (recipients) and you",
  "Confirm intended recipient list with the client, then update recipients, From and Reply-To. Keep the agency copy only if the client agrees (BCC).",
  "Low (settings change) but affects live lead flow", "ACC-002, ACC-140, ACC-141",
  "Client-approved test submission: confirm delivery to the named mailbox(es), inbox not spam, reply-to works, SPF/DKIM pass for sender domain.",
  "Possibly deliberate during build; must be decided before further marketing. The agency address is deliberately not reproduced in full here.")
F("ACC-002", 1, "Placeholder demo phone number and a US tel: link on the live Book a Call page", "Content / contact details",
  "/book-a-call/ (page 2792)",
  "Visible text '020 10 200 300' wrapped in <a href=\"tel:+11228008808\"> (a +1 US number from a dynamic contact tag). Contact page shows '020 3764 9691' / tel:+442037649691. Page also shows only 'London / United Kingdom' as location. Reported by two agents.",
  "Critical", CI, "Visitor: a click-to-call goes to the wrong country/number; brand and compliance risk",
  "Confirmed", "Client (correct number) and you",
  "Replace with the client-confirmed number (or remove the block) and align the tel: link with the visible text.",
  "Low", "ACC-032, ACC-053",
  "View page on desktop and mobile; tap the number and confirm the dialler shows the confirmed number; text matches href.",
  "Vamtam demo debris. Do not guess the number: confirm which of the three numbers found on the site is current.")
F("ACC-003", 1, "Complaints page states it is interim and awaits legal/compliance review", "Legal / compliance wording",
  "/complaints/ (page 1642)",
  "Published text: 'Important Note: This page contains interim general complaints information only. It should be reviewed and approved by our legal and compliance advisers before being relied upon as the final complaints policy.' Page is indexable and in the page sitemap.",
  "Critical", LC, "Compliance, visitor trust; regulated firm publishing self-declared provisional complaints text",
  "Confirmed", "Legal/compliance and client",
  "Obtain approved complaints wording, replace the page text and remove the interim note. Until then consider temporarily setting the page to noindex only if compliance agrees.",
  "Medium (regulatory wording)", "ACC-030, ACC-031, ACC-038",
  "Re-read the page against the approved text; confirm no 'interim' wording remains; check timescales match the Terms of Business.",
  "Do not rewrite or paraphrase: wording must come from the client's compliance adviser.")
F("ACC-004", 1, "Four dummy posts are published, indexable, in the Yoast sitemap, in the RSS feed and linked from Insights, search and archives", "Indexing / content exposure",
  "/protecting-businesses-against-operational-disruption/ (post 218) and -2 (1302), -3 (1305), -4 (2192)",
  "All status 'publish'. robots meta 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1', no X-Robots-Tag, canonical self. All four listed in post-sitemap.xml (lastmod 2026-08-18T15:07:13+00:00). Identical post title and Article headline 'Protecting Businesses Against Operational Disruption', identical 241-word body, same author and category 'Accord'. Distinct per-post Yoast titles (Commercial Risk Insurance, Operational Disruption Insurance, Business Interruption Insurance, Business Continuity Insurance). Full text in /feed/. Linked from the Insights loop grid (template 119), /category/accord/, the author archive, search results and each post's 'More Insights' loop. Not in header or footer menus.",
  "High", CA, "SEO (duplicate/thin content, keyword cannibalisation), visitor (placeholder-grade articles publicly reachable), compliance",
  "Confirmed", "Client (publish/hold decision) and you",
  "Decide the intended state, then either set all four to noindex and remove from the sitemap, or unpublish/draft three and keep one genuine article. Do not delete until the client confirms.",
  "Low to Medium (reversible if set to noindex first)", "ACC-070, ACC-071, ACC-013",
  "Fetch each post URL: expect noindex or 404/redirect as decided; post-sitemap.xml no longer lists them; /feed/ and Insights no longer show them; Search Console URL inspection after crawl.",
  "Known and expected placeholders, but public exposure is actionable. The article body reads as real insurance prose, not lorem ipsum: the client should confirm whether it is approved copy.")
F("ACC-005", 1, "Complianz client credentials were printed into an audit agent transcript", "Security / process",
  "Option values under cmplz_* (Complianz account connection)",
  "Config agent reported that a 'wp option list --search=cmplz_*' output contained a WSC client secret and an access token. Values are not reproduced here. The local scratchpad file holding the dump was deleted. Elementor licence data was also in that dump.",
  "High", CI, "Security: credentials exposed to this session's logs",
  "Confirmed (agent report)", "You and client",
  "Decide whether to rotate the Complianz connection credentials (disconnect and reconnect the licence in Complianz) and review Elementor licence handling.",
  "Low to Medium (reconnecting Complianz account)", "ACC-006",
  "After rotation confirm Complianz still shows as connected and the banner renders.",
  "Exposure was to this session only, not public. Rotation is precautionary.")
F("ACC-006", 1, "Audit side effects: 11 server-side database checkpoints were created by wp_cli calls", "Process / maintenance",
  "Cowboy MCP checkpoints 1-11; change journal",
  "wp_list_checkpoints shows ids up to 11, created 2026-10-02 14:22:50 to 14:24:36 UTC, labelled 'Before wp_cli: ...' (trigger auto_wp_cli, about 0.6 MB each). 29 wp_cli entries in the journal; none after 14:24:53. wp_http_request GET/HEAD calls and one wp_batch_execute wrapper (20 HEADs) are journaled as 'not_undoable' audit entries. No posts, pages, templates, options or plugins were changed.",
  "Low", CA, "Maintenance: extra dump files on the server (contain site database copies)",
  "Confirmed", "You",
  "Decide whether to keep the checkpoints (harmless backups, but contain database copies including option values) or delete them in a controlled batch. Do not delete without approval.",
  "Low", "ACC-005",
  "wp_list_checkpoints after any clean-up; confirm no checkpoint remains if deletion approved.",
  "These breached the strict read-only brief and are disclosed as such. GET/HEAD journal entries are audit records, not site changes.")

# ---------------- 2. Content and development leftovers ----------------
F("ACC-010", 2, "Pasted ChatGPT interface markup inside the Insights page text widget", "Content / development artefact",
  "/insights/ (page 324), text-editor widget 5446eed",
  "Widget HTML contains qMYqUG_convSearchResultHighlightRoot, data-turn-id, data-testid=\"conversation-turn-50\", data-message-model-slug=\"gpt-5-5-thinking\" and Tailwind-like classes wrapping the intro paragraph. Reported by two agents.",
  "Medium", CA, "SEO and maintenance: junk attributes in crawlable HTML; possible visual or accessibility side effects",
  "Confirmed", "None beyond normal change approval",
  "Replace the widget content with the plain paragraph text (keep wording unchanged), using the Elementor editor on staging first.",
  "Low", "ACC-070",
  "View source of /insights/: no 'conversation-turn', 'data-message-model-slug' or similar; text renders identically.", "")
F("ACC-011", 2, "Commodities & Trade Finance hero/CTA link is empty or malformed", "Broken link",
  "/sectors/commodities-trade-finance/ (page 2084)",
  "Body agent A saw the hero 'Contact us' button rendering href=\"\" . Config agent saw a stored CTA href 'Ωhttps://accordib.com/contact-us/#touch' (stray leading character). The two may be different buttons or the same button in rendered vs stored form.",
  "Medium", NV, "Visitor: dead or broken primary CTA",
  "Needs verification (agents disagree on which button)", "None beyond normal change approval",
  "Inspect both buttons in Elementor, fix the stray character, and point the empty button to /contact-us/#touch.",
  "Low", "ACC-012",
  "Click every CTA on the page on desktop and mobile; each lands on /contact-us/#touch.", "")
F("ACC-012", 2, "Claims page: both 'Get in touch' buttons have no destination", "Broken link",
  "/claims/ (page 2027), widgets ede4610 and 4b19451",
  "Rendered href=\"#\" on both; config agent found no link set. Reported by two agents.",
  "Medium", CA, "Visitor: dead CTAs on a claims page",
  "Confirmed", "Client (confirm destination) and you",
  "Link both buttons to /contact-us/#touch (or the client's claims contact route).",
  "Low", "ACC-011", "Click each button; correct destination loads.", "Claims route may need a specific contact: confirm with client.")
F("ACC-013", 2, "Footer 'Insights' entry is plain text, not a link", "Navigation / unfinished content",
  "Footer template 108, text-editor widget f85de31",
  "Widget outputs <p>Insights</p> with no anchor. /insights/ is live (HTTP 200), absent from the header menu (menu 47) and listed in the page sitemap. Reported by three agents.",
  "Medium", CI, "Visitor: unlinked item looks broken; consistency with a hidden/unfinished News area",
  "Confirmed", "Client (decide whether Insights should be public) and you",
  "Decide Insights visibility first. If public later, link it; if not, remove the footer entry.",
  "Low", "ACC-004, ACC-070",
  "Footer renders without an unlinked text item, or the link resolves 200 and matches header navigation.", "")
F("ACC-014", 2, "Footer LinkedIn icon has no URL", "Navigation / unfinished content",
  "Footer template 108, social-icons widget 72646685",
  "Single LinkedIn icon with no link configured (reported by two agents).",
  "Low", CI, "Visitor, brand: dead icon", "Confirmed", "Client (profile URL)",
  "Add the confirmed LinkedIn company URL or remove the icon.", "Low", "ACC-056", "Icon opens the correct profile in a new tab with rel=noopener.", "")
F("ACC-015", 2, "Footer sub-footer nav-menu widget points at an empty menu with no theme location", "Navigation / architecture",
  "Footer template 108 nav-menu widget 77c20636; menu 'Footer - Main' (id 28); theme location menu-2",
  "Menu 28 has 0 items and no location; menu-2 is unassigned. The visible footer link columns are text-editor widgets, not a WordPress menu. The nav-menu widget therefore renders nothing.",
  "Low", NV, "Maintenance only; no visible defect",
  "Confirmed (empty widget); defect not confirmed", "None beyond normal change approval",
  "Not defective by itself because the footer navigation is built inside the Elementor template. Verify the rendered footer, then either remove the empty widget or populate menu 28 and drive the footer links from it.",
  "Low", "ACC-016", "Rendered footer has no empty nav element; links unchanged.",
  "Per your caution, the empty location alone is not treated as a bug.")
F("ACC-016", 2, "Unassigned menus: 'Sectors Menu' (id 46, 4 items) and 'Footer - Main' (id 28)", "Maintenance",
  "Appearance > Menus",
  "wp_list_menus: Sectors Menu has 4 items and no locations; Footer - Main has 0 items and no location. Menu 46 duplicates the sector links already in the header.",
  "Low", NV, "Maintenance clutter", "Needs verification (check no widget uses menu 46)", "None beyond normal change approval",
  "Search Elementor data for menu slug 'sectors-menu' before any removal; keep if used.", "Low", "ACC-015", "No widget or location references the removed menu; header and footer unchanged.", "")
F("ACC-017", 2, "Finance and Investment template-kit leftovers (loop/archive/search templates and slugs)", "Development artefact",
  "Elementor templates 64, 68, 78, 93, 101, 117, 119, 121, 123, 133; Header (slug header-finance-investment) and Footer (slug footer-finance-investment)",
  "Created 2026-05-23, all published. Config agent: no display conditions on the loop items and archive 64, and elementor_library URLs redirect to home. Body agent B: template 119 'Blog Post Loop - Classic' is the loop used by the Insights page and each post's 'More Insights' block, so at least one is in use. Search Results 70 references a loop template.",
  "Low", NV, "Maintenance: dead templates and demo slugs",
  "Needs verification", "None beyond normal change approval",
  "Do not delete yet. For each template confirm: no display conditions, not referenced by another template or page loop widget, and not needed for rollback. Remove only unreferenced ones after a backup. Template 119 must stay while the Insights loop exists.",
  "Medium (Elementor references are not always visible)", "ACC-018, ACC-190",
  "After each removal, load home, Insights, a post, search results, 404 and a legal page and compare to baseline.",
  "Your caution applied: nothing is marked deletable.")
F("ACC-018", 2, "Active Elementor kit is titled 'test' and carries Vamtam theme globals", "Maintenance / design system",
  "Elementor kit post 10 (title 'test'); Default Kit post 6 (unused)",
  "Config agent: kit 10 is the live global-settings kit (elementor_active_kit), previous_kit=6. It still holds vamtam_accent_1..8, vamtam_h1..h6 and 'Sticky Header Bg Color' ids; many widgets reference globals/colors?id=vamtam_*.",
  "Medium", NV, "Maintenance: risk that 'test' is mistaken for junk and deleted, breaking global styles",
  "Confirmed (the template named 'test' is the live kit)", "None beyond normal change approval",
  "NEVER delete post 10. Optionally rename the kit title after approval. Migrate Vamtam global references to Accord globals only on staging.",
  "High if mishandled", "ACC-081, ACC-190", "Site renders identically after any rename; kit settings unchanged.",
  "Resolves the earlier suspicion that the 'test' template was a demo leftover.")
F("ACC-019", 2, "Demo debris in settings and templates (hidden video URLs, demo image, demo slug, placeholder headings)", "Development artefact",
  "Home hero video widgets; container 3b962d8b; loop template 119; post 218 old slug; Search Results template 70",
  "Hidden settings keep demo YouTube, Vimeo (vimeo.com/236906999), Dailymotion and VideoPress URLs. Template 119 fallback image: finovate.demo.vamtam.com/.../dummy-post-horisontal-thegem-blog-default-large.jpg (third-party dependency, used only without a featured image). Post 218 RSS guid uses slug from-local-to-leader-scaling-strategies-for-ambitious-regional-banks. Search Results 70 contains two 'Add Your Heading Text Here' placeholders.",
  "Low", NV, "Maintenance; small chance of visible placeholder on edge states",
  "Confirmed (stored data); visibility unverified", "None beyond normal change approval",
  "Clean on staging: remove unused URLs, replace the third-party fallback image with a local one, replace placeholder headings.",
  "Low", "ACC-190", "Search with and without results; post without featured image; no requests to vamtam.com in network log.", "")
F("ACC-020", 2, "Unused global container templates and saved sections", "Maintenance",
  "Templates 1830, 1753, 2373, 1836, 1727 (slug global-our-values)",
  "No usage seen by the config agent; usage scan was incomplete (template widgets on pages 256, 2084, 2125, 2140, 2171, 324, 426 did not expose ids; legal pages 1273, 1278, 1640, 1642 and templates 80, 82 not scanned).",
  "Low", NV, "Maintenance", "Needs verification", "None beyond normal change approval",
  "Complete a usage scan across all pages/templates before any decision. Keep as reusable sections if the client wants them.", "Low", "ACC-190",
  "Usage report shows zero references before removal.", "")
F("ACC-021", 2, "Draft, private, pending, future and trash content", "Inventory",
  "All post types",
  "Config agent: no draft, pending, private, future or trash items. Only auto-draft 3154. 19 pages, 4 posts, 33 elementor_library, 100 attachments, 14 nav items. 0 revisions.",
  "Low", NI, "None", "Confirmed", "None", "No action. Re-check after remediation.", "None", "", "", "Recorded for baseline. The 'unpublished News/Insights area' is in fact published (see ACC-070).")
F("ACC-022", 2, "Elementor library templates and Coming Soon page publicly reachable", "Indexing",
  "/?elementor_library=test, =header-finance-investment, =elementor-single-page-1239, =coming-soon",
  "Config agent GET on all four: HTTP 200 after 1 redirect, serving the home page with canonical https://accordib.com/ and robots index,follow. Maintenance mode is off.",
  "Low", NI, "None", "Confirmed", "None", "No action.", "None", "", "", "Template URLs are not exposed as separate pages.")
F("ACC-023", 2, "Unresolved '{title}' style template variables in crawlable markup", "Content / SEO",
  "All inspected heads and visible bodies",
  "No '{title}', '%%title%%' or similar token was found in any Yoast head, in get-post-seo-data for 23 URLs, or in the visible HTML read. Only legitimate '{search_term_string}' in WebSite schema. Limitation: full HTML was truncated at about 51,200 characters per page.",
  "Low", NV, "SEO", "Needs verification (not found, not fully excluded)", "None",
  "Run a full-DOM crawl (browser or full-fetch) and search for '{title}', '%%' and unrendered shortcodes.", "None", "ACC-190",
  "Crawl output contains zero matches.", "Seed item not confirmed by any agent.")

# ---------------- 3. Legal, regulatory and company information ----------------
F("ACC-030", 3, "Two different company names used across legal pages and settings", "Company information",
  "Footer; /regulatory-status/; /terms-of-business/; /website-terms-of-use/; /privacy-policy/; Complianz organisation setting; Yoast schema; /sectors/ hero alt",
  "'Accord Risk Limited' (footer, regulatory status, Terms of Business, Terms of Use). 'Accord Insurance Brokers Ltd' (Privacy Policy data controller; Complianz organisation name). 'Accord Insurance Brokers' (site name, schema, title tags, home). 'Accord insurance limited' (hero alt/title on /sectors/).",
  "High", CI, "Compliance, trust, legal identity of the data controller", "Confirmed (variants exist); correct form unknown", "Client and legal/compliance",
  "Client to confirm legal entity name and any trading name, then standardise legal pages, Complianz settings and schema. Do not edit until confirmed.",
  "Medium", "ACC-031, ACC-003", "Search the site for each name variant; only approved forms remain; privacy controller matches ToB.",
  "Footer states an appointed-representative relationship with Bennett Gould and Partners Limited, which appears elsewhere on the same account.")
F("ACC-031", 3, "Two different registered office addresses", "Company information",
  "Footer, /regulatory-status/, /terms-of-business/ vs /website-terms-of-use/, /privacy-policy/; /contact-us/",
  "Footer, regulatory status, ToB: '2 Manor Farm Court Old Wolverton Road, Old Wolverton, Milton Keynes, Buckinghamshire, England, MK12 5NN', company number 16261233. Terms of Use: 'Registered Office: 9 New Street, London EC2M 4TP'. Privacy: '9 New Street, London, EC2M 4TP'. Contact page: Milton Keynes address. Book a Call: 'London / United Kingdom'.",
  "High", CI, "Compliance, legal validity of terms", "Confirmed (conflict); correct address unknown", "Client and legal/compliance",
  "Confirm registered office and any trading/office address, then align every page and Complianz.", "Medium", "ACC-030",
  "Single approved address set appears consistently; Companies House record matches (client to check).", "Do not infer which address is correct.")
F("ACC-032", 3, "Three different telephone numbers, one mismatching its link", "Contact details",
  "/contact-us/, /book-a-call/, /website-terms-of-use/, /privacy-policy/, Complianz setting",
  "Contact: 020 3764 9691 (tel:+442037649691). Terms of Use and Privacy: +44 (0)78 7148 6392. Book a Call: 020 10 200 300 with tel:+11228008808 (demo). Complianz phone: 020 3764 9691.",
  "High", CI, "Visitor, compliance", "Confirmed", "Client",
  "Client to confirm the published number(s); apply across pages, Complianz and schema where appropriate.", "Low", "ACC-002",
  "Every phone mention and tel: link matches the approved list.", "")
F("ACC-033", 3, "Several email addresses, mixed case, and a named individual's mailbox for complaints", "Contact details",
  "Contact, Complaints, Terms of Use, Privacy, form sender",
  "hello@accordib.com (Contact, Book a Call, Complianz), matthew@accordib.com (Complaints, Privacy, ToB), Info@accordib.com and info@accordib.com (Terms of Use), email@accordib.com (form From). Complaints page gives only matthew@accordib.com.",
  "Medium", CI, "Compliance (complaints route), continuity", "Confirmed", "Client and legal/compliance",
  "Client to confirm which addresses are intended, whether complaints should use a role mailbox, and the exact case.", "Low", "ACC-030", "All addresses valid and monitored; mail test per address.", "")
F("ACC-034", 3, "Typo in the regulatory statement: 'is a an appointed representative'", "Legal wording / typo",
  "Footer template 108 (all pages)",
  "'Accord Risk Limited is a an appointed representative of Bennett Gould and Partners Limited, which is authorised and regulated by the Financial Conduct Authority (firm reference number 306850).' Reported by three agents.",
  "Medium", LC, "Compliance, credibility", "Confirmed", "Legal/compliance (regulatory text) and client",
  "Obtain approval to correct 'a an' to the approved wording; apply in the footer template only.", "Low", "ACC-030",
  "Footer on every page shows the approved sentence; no other legal text changed.", "Likely a one-word fix but it sits inside a regulatory disclosure, so approval is required.")
F("ACC-035", 3, "'Independent insurance broker' claim alongside appointed-representative status", "Regulatory claim",
  "Home and About (template 1716 and page text); footer",
  "Home: 'Accord is an independent insurance broker focused on delivering the right cover...'. About: 'Accord is an independent insurance broker focused on arranging cover shaped around each client's needs.' Footer: appointed representative of Bennett Gould and Partners Limited.",
  "High", LC, "Compliance (possible misleading status description)", "Needs verification (legal judgement)", "Legal/compliance",
  "Ask compliance whether 'independent' is permissible for an appointed representative.", "Medium", "ACC-030", "Approved wording in place or claim retained with written sign-off.", "No judgement made here.")
F("ACC-036", 3, "Terms of Business states FSCS membership", "Legal wording",
  "/terms-of-business/ (page 1640)",
  "'We are a member of the Financial Services Compensation Scheme (FSCS)'. Page also describes Accord as a trading name and an appointed representative.",
  "High", LC, "Compliance", "Needs verification", "Legal/compliance", "Compliance to confirm the statement and who the FSCS member is.", "Medium", "ACC-035", "Approved wording published.", "")
F("ACC-037", 3, "Typos and wording errors in the Terms of Business", "Legal wording / typo",
  "/terms-of-business/ (page 1640)",
  "'commisison' and 'commisson'; 'settle your complain'; 'The Financial Ombudsman Exchange Tower' (word 'Service' missing); 'will be handed in accordance with the Data Protection regulations'; 'Cheques should be payable to directly to'; 'If we may employ the services of other intermediaries'.",
  "Medium", LC, "Compliance, credibility", "Confirmed (quotes)", "Legal/compliance", "Provide the list to compliance; apply only their approved corrections.", "Low", "ACC-003",
  "Re-read the page; each quoted error resolved with approved text.", "")
F("ACC-038", 3, "Inconsistent complaint timescales between Complaints page and Terms of Business", "Legal wording",
  "/complaints/ vs /terms-of-business/",
  "Complaints: acknowledgement within '5 business days'. ToB: 'resolved by close of business on the 3rd working day'; complex-case acknowledgement has no day count. Both state a final response within 8 weeks.",
  "Medium", LC, "Compliance", "Needs verification", "Legal/compliance", "Compliance to reconcile timescales.", "Medium", "ACC-003", "Both pages carry the same approved timescales.", "")
F("ACC-039", 3, "Website Terms of Use: dated and future-tense regulatory wording, terminology mismatch", "Legal wording",
  "/website-terms-of-use/ (page 1278)",
  "Opens 'Last Updated: June 2026'. 'Where applicable, details of our regulatory status will be displayed on this website and in our client documentation.' Refers to 'our Privacy Notice and Cookie Policy' (pages are titled Privacy Policy and Cookie Policy).",
  "Medium", LC, "Compliance", "Confirmed (quotes)", "Legal/compliance", "Compliance to confirm date, status wording and document names.", "Low", "ACC-030", "Approved text and consistent document names.", "")
F("ACC-040", 3, "Privacy Policy lacks a last-updated date and regulatory identity", "Legal wording",
  "/privacy-policy/ (page 1245)",
  "No 'last updated' date seen; controller 'Accord Insurance Brokers Ltd'; no FCA/appointed-representative mention; ICO address listed.",
  "Low", LC, "Compliance", "Needs verification", "Legal/compliance", "Compliance to confirm required content.", "Low", "ACC-030", "Policy reviewed and approved.", "")
F("ACC-041", 3, "Third-party regulator/ombudsman links and details to verify", "Legal wording",
  "/complaints/, /terms-of-business/, /privacy-policy/",
  "FOS link uses http://www.financial-ombudsman.org.uk; FOS phone 0800 023 4567 and Exchange Tower address; BGP Corinium House Gloucester address and 03330 146 156; ICO Wycliffe House address.",
  "Low", CI, "Compliance, link integrity", "Needs verification", "Client/compliance", "Verify current details; use https links.", "Low", "ACC-003", "All external links 200 over https; details match source organisations.", "External links were not fetched (accordib.com only).")
F("ACC-042", 3, "Strong product and market claims needing compliance review", "Regulatory claim",
  "/insurance-for-bridging-lenders/, /sectors/bridging-lenders/, Home, Sectors",
  "'The policy is designed to cover valuation fraud.'; 'Accord has developed specialist fraud insurance wording designed specifically for bridging lenders...'; 'Fraud within the short-term mortgage lending sector remains a material and ongoing risk.'; 'Market-leading insurers' (h4); 'access to Lloyd's, London market and international insurance capacity'.",
  "Medium", LC, "Compliance (financial promotion / product claims)", "Needs verification", "Legal/compliance", "Compliance to review claims; do not alter copy before sign-off.", "Medium", "ACC-035", "Approved or amended text recorded.", "No insurance-product facts were invented.")

# ---------------- 4. SEO and Yoast ----------------
F("ACC-050", 4, "No H1 on most pages", "Heading structure",
  "Home, /sectors/ and 4 children, /solutions/, /about-us/, /claims/, /insurance-for-bridging-lenders/, /insights/, the four posts, six legal pages, cookie policy",
  "First heading on each page is an H2 from an Elementor heading widget (home widget a3d8ef7: <h2 class=\"elementor-heading-title\">Specialist insurance broking for complex commercial, financial and credit risks.</h2>). Header (125) and footer (108) contain no H1. Posts: title renders as H2 via template 82. Legal pages: H2 title then H4 sections. Page-title selector in kit is h1.entry-title. Rendered tails were truncated at about 51,200 characters, so an H1 late in the page is unlikely but not excluded.",
  "High", CA, "SEO, accessibility (page has no primary heading)", "Confirmed in Elementor and rendered HTML (partly truncated)", "None beyond normal change approval",
  "Set the hero heading widget on each page to H1 (one per page); keep typography consistent via widget style because kit H1 is 52px vs H2 48px.",
  "Medium (visual size changes)", "ACC-052, ACC-190", "DOM check: exactly one H1 per URL matching the page topic; visual diff on desktop/tablet/mobile.",
  "Seed item 'most sampled pages may lack an H1' is confirmed on 10 body pages plus posts and legal pages.")
F("ACC-051", 4, "Contact and Book a Call use the wrong H1", "Heading structure",
  "/contact-us/ (widget 3d0c99e) and /book-a-call/",
  "Outline: H2 'Contact Us', H2 'Let's Connect', H2 'Send a Message', H2 'Book a Call', then H1 'General Enquiries' (last). Book a Call: H2 'Book a Call' then H1 'General Enquiries'.",
  "High", CA, "SEO, accessibility", "Confirmed", "None beyond normal change approval",
  "Make the hero title the H1 and demote 'General Enquiries' to a lower heading.", "Low", "ACC-050", "One H1 matching page topic, in first position.", "")
F("ACC-052", 4, "Inconsistent heading hierarchy in shared templates, legal, search and 404 pages", "Heading structure",
  "Template 1709 (Our sectors); sector pages; legal pages; search results; 404",
  "Template 1709: three cards H3, 'Bridging Lenders' H2 (widget 4650a43). 'Why Choose' blocks jump H2 to H4. Sector card titles and coverage items are <p>. Cookie page H2 to H3 to H4 to H5; Complaints H2 'Complaints' then H4 'Complaints' and footer H2 'Talk to our experts today'. Search: H2 then H1 both 'Search Results for: ...'. 404: H1 '404' then H3.",
  "Medium", CA, "Accessibility, SEO", "Confirmed", "None beyond normal change approval",
  "Normalise levels in the shared template first (one change fixes many pages), then per page.", "Medium (shared template)", "ACC-050", "Heading outline export per URL has no skipped levels.", "")
F("ACC-053", 4, "/book-a-call/ duplicates the Contact page metadata and is indexable", "Metadata / indexing",
  "/book-a-call/ (page 2792) vs /contact-us/",
  "SEO title, meta description, og:title, og:description, twitter fields and og:image identical to Contact; indexable; in page sitemap; schema plain WebPage.",
  "Medium", CI, "SEO: duplicate metadata, thin page", "Confirmed", "Client",
  "Give it unique metadata or set noindex/canonical to Contact if it is only a booking utility.", "Low", "ACC-002", "Unique title/description or noindex as decided.", "")
F("ACC-054", 4, "Cookie Policy has no meta description and default title format", "Metadata",
  "/cookie-policy-uk/ (page 2862)",
  "Title 'Cookie Policy - Accord Insurance Brokers' (40 chars, ' - ' separator vs ' | ' elsewhere); no description, og:description or twitter fields; no focus keyphrase.",
  "Low", CA, "SEO", "Confirmed", "None beyond normal change approval",
  "Add a factual, non-legal meta description and align the title pattern. Draft wording for your approval.", "Low", "", "View source shows one description (70-160 chars) and matching OG tags.", "Seed item confirmed.")
F("ACC-055", 4, "Overlapping bridging-lender pages and keyphrase cannibalisation", "SEO structure",
  "/insurance-for-bridging-lenders/ (2916) vs /sectors/bridging-lenders/ (256)",
  "Both cover bridging-lender fraud, PI and D&O. 256 links to 2916 ('Find out more'); 2916 is not in the main menu. Focus keyphrase on 2916 'specialist insurance brokers' equals the homepage's. 2916 og:title and twitter:title repeat the full SEO title with brand suffix. 2916 'Review Policy' button points to /sectors/.",
  "Medium", CI, "SEO: competing pages", "Confirmed (overlap); intent unknown", "Client",
  "Client to decide the role of each page, then differentiate keyphrases or consolidate.", "Medium", "ACC-143", "Distinct intent, titles and keyphrases; no cannibalising queries in Search Console.", "")
F("ACC-056", 4, "Organization schema is minimal", "Structured data",
  "Sitewide Yoast schema graph",
  "Organization has name, url and SVG logo 333x73 only: no address, telephone, sameAs, contactPoint, legalName or regulator reference. Type is generic Organization. Yoast global settings could not be read.",
  "Medium", CI, "SEO enhancement, entity clarity", "Confirmed (rendered)", "Client and legal/compliance (any regulatory property)",
  "After company details are settled, complete Yoast organisation data (address, phone, profiles, logo). Do not add details until verified.", "Low", "ACC-030, ACC-031, ACC-032, ACC-014",
  "Rich Results / schema validator shows complete Organization without errors.", "")
F("ACC-057", 4, "Open Graph images lack width, height and type on several URLs", "Metadata",
  "/, /sectors/, /solutions/, /insurance-for-bridging-lenders/, author archive",
  "get_head json shows og_image with empty width/height/type (Elementor thumbs or missing image metadata). Yoast og_default_image appears empty (media agent), unverified.",
  "Low", NV, "SEO, social sharing", "Confirmed (rendered); default setting needs verification", "None beyond normal change approval",
  "Set explicit social images with metadata in Yoast, plus a default social image.", "Low", "ACC-060", "Facebook/LinkedIn debugger shows correct image and size.", "")
F("ACC-058", 4, "Schema and breadcrumb text defects", "Structured data",
  "Home, Commodities page, author archive",
  "Home breadcrumb second item 'Accord Insurance Brokers' (not a page label); Commodities title stored with '&amp;' and double-encoded in JSON-LD breadcrumb; author sameAs 'http://accordib.com'.",
  "Low", CA, "SEO", "Confirmed", "None beyond normal change approval", "Correct entity encoding and breadcrumb labels.", "Low", "", "Schema validator and rendered breadcrumbs correct.", "")
F("ACC-059", 4, "Possible second meta description tag on Contact", "Metadata",
  "/contact-us/",
  "Body agent B saw two <meta name=\"description\"> tags (one from Yoast, one plain). Not seen by the SEO agent.",
  "Low", NV, "SEO", "Needs verification (single source)", "None beyond normal change approval", "Confirm in full source; find and remove the non-Yoast tag.", "Low", "", "Exactly one description tag.", "")
F("ACC-060", 4, "Yoast global settings not inspected", "Inspection gap",
  "wpseo, wpseo_titles, wpseo_social options",
  "No safe read-only reader exists in the allowed toolset (only wp_cli, which creates checkpoints). Settings inferred from rendering: author and category archives indexable, attachments redirect to file, search and 404 noindex, breadcrumbs on, llms.txt off, Google verification present.",
  "Medium", NV, "SEO", "Needs verification", "You (access)",
  "Export Yoast settings from wp-admin (SEO > Tools) or share screenshots, or approve a one-off read via wp_cli on staging.", "None", "", "Settings compared with rendered output.", "")
F("ACC-061", 4, "Yoast traffic-light scores on some pages", "SEO optimisation",
  "Bridging Lenders, Commercial Insurance, Commodities, Solutions, Regulatory Status (seo 'bad'); Financial Institutions, Terms of Use, Terms of Business (readability 'bad')",
  "yoast-seo get-post-seo-data: seo 'bad' on 256, 2140, 2084, 2125, 1273; readability 'bad' on 2171, 1278, 1640.",
  "Enhancement", DF, "SEO (indicator only)", "Confirmed (scores)", "You",
  "Do not chase green indicators. Review only where scores point to real content issues.", "None", "", "", "Per your instruction.")
F("ACC-062", 4, "llms.txt not generated", "SEO enhancement",
  "/llms.txt", "GET returned the theme 404 page.", "Enhancement", DF, "Optional discoverability", "Confirmed", "You", "Optional. Decide later.", "Low", "ACC-060", "", "")
F("ACC-063", 4, "Yoast get_head endpoint returned 404 for /claims/", "Tool artefact",
  "/claims/", "REST get_head returned a 404 head twice; direct GET returned 200 with title 'Insurance Claims Support | Accord Insurance Brokers', canonical self, index.",
  "Low", NI, "None for visitors", "Confirmed (artefact)", "None", "No action. Use direct page fetch for this slug in future tests.", "None", "", "", "")

# ---------------- 5. Sitemap, indexing and archives ----------------
F("ACC-070", 5, "Insights page is live, indexable, in the sitemap and not in navigation", "Indexing / unfinished area",
  "/insights/ (page 324)",
  "HTTP 200, robots index, in page-sitemap (lastmod 2026-06-08T14:34:36+00:00). Not in header menu 47. Loop grid (template 119, 9 per page) shows all four dummy posts. Contains pasted ChatGPT markup (ACC-010). Hero image Accord-Insurance-Insughts.jpg (typo in filename) with alt 'Accord Insurance Insughts'.",
  "High", CI, "SEO, visitor: unfinished area publicly discoverable via sitemap and search", "Confirmed", "Client",
  "Client to decide: hold back (noindex, remove from sitemap) until content is supplied, or publish with real content.", "Low to Medium", "ACC-004, ACC-010, ACC-013",
  "Sitemap and robots meta reflect the decision; page reachable only as intended.", "The unfinished area was expected; the public exposure is the actionable part.")
F("ACC-071", 5, "Author and category archives are indexable and in the sitemap", "Indexing",
  "/author/matthewaccordib-com/, /category/accord/",
  "author-sitemap and category-sitemap both listed in sitemap_index.xml. Both robots 'index, follow', no description, thin listing of the dummy posts. Author slug is email-derived. /author/ itself returns 404.",
  "Medium", CA, "SEO: thin duplicate archives; privacy: email-derived username", "Confirmed", "Client and you",
  "Set author and category archives to noindex and exclude from sitemap (Yoast settings), or disable the author archive. Settings change reversible.", "Low", "ACC-060, ACC-161",
  "sitemap_index.xml lists only intended sitemaps; archive URLs noindex or redirect.", "")
F("ACC-072", 5, "Legal and utility pages are all indexable", "Indexing",
  "Privacy, Cookie, Regulatory Status, Terms of Use, Terms of Business, Complaints, Book a Call, Claims",
  "All 'index, follow' and in page-sitemap. Legal pages share hero contact-hero.jpeg as og:image.",
  "Low", CI, "SEO (low value pages competing)", "Confirmed", "Client",
  "Decide which should be indexed (regulatory status and complaints may be wanted).", "Low", "ACC-053", "Indexing matches decision.", "")
F("ACC-073", 5, "Sitemap composition matches published pages; redirects and special URLs behave", "Indexing",
  "sitemap_index.xml, page-sitemap.xml, wp-sitemap.xml, sitemap.xml, robots.txt, search, 404, attachments",
  "page-sitemap lists exactly the 19 published pages; wp-sitemap.xml and sitemap.xml redirect once to sitemap_index.xml; robots.txt allows all and points to sitemap_index.xml; search and 404 are noindex,follow; attachment pages redirect to the file; ?p=448 and ?page_id=426 redirect once to canonical URLs; http and www redirect once to the https apex.",
  "Low", NI, "None", "Confirmed", "None", "No action.", "None", "", "", "X-Robots-Tag noindex on robots.txt and sitemap XML is normal Yoast behaviour.")

# ---------------- 6. Elementor templates and design consistency ----------------
F("ACC-080", 6, "Hero colour differs per page from one shared hero template", "Design consistency",
  "Template 1787 'Global - Hero Option 1 (Variable Colour)'",
  "Per-page overrides: #2E2E2E (Financial Institutions), #042705 (About), #153130 (Claims); home uses #0B203B (Accord Dark Blue). Kit holds Accord Dark Blue #0B203B and Accord Dark Green #042705; #2E2E2E and #153130 are not Accord globals.",
  "Low", CI, "Design consistency", "Needs verification (template name suggests variable colour is intended)", "Client",
  "Confirm intended colour per page; map to global brand colours.", "Low", "ACC-081", "Hero colours match the approved scheme.", "")
F("ACC-081", 6, "Global palette mixes Vamtam demo colours with the Accord brand; hard-coded colours on pages", "Design system",
  "Elementor kit 10",
  "System colours #2E2E2E, #FFFBE7, #F6F5F2, #92C200 (link hover), #7E7E7E from Vamtam; custom Accord Dark Blue #0B203B, Accord Dark Green #042705. Hard-coded #B4E717 and #415B76 appear on pages. Typography is Work Sans plus Poppins for 'Body Link' only.",
  "Low", NV, "Design consistency, maintainability", "Needs verification", "Client (brand)",
  "Document the approved brand palette; replace Vamtam system colours on staging and re-map widget references.", "Medium", "ACC-018", "Visual regression across all templates shows no unintended colour change.", "")
F("ACC-082", 6, "Legal Pages template condition lists a page that does not exist", "Theme Builder",
  "Template 1239 'Accord Legal Pages'",
  "Display conditions include page IDs 1245, 1249, 1273, 2862, 1642, 1640, 1278. Page 1249 does not exist. Complianz option for the custom cookie page also points to 1249 (real cookie page is 2862).",
  "Low", CA, "Maintenance", "Confirmed", "None beyond normal change approval", "Remove the stale ID on staging.", "Low", "ACC-183", "All six legal pages still use the template.", "")
F("ACC-083", 6, "Book a Call is implemented two ways", "Conversion consistency",
  "Header 125; popup 2804 'Book a Call'; /book-a-call/ (2792)",
  "Desktop header and in-page buttons open popup 2804. Tablet/mobile header button links to /book-a-call/. Popup has no stored display conditions or trigger settings found; display settings not read. Popup holds a HubSpot Meetings embed with unquoted attributes.",
  "Low", NV, "Conversion consistency", "Confirmed (behaviour); intent unknown", "Client",
  "Choose one pattern for all devices.", "Low", "ACC-002, ACC-180", "Same behaviour on desktop and mobile.", "")
F("ACC-084", 6, "Search Results template carries placeholder headings", "Template content",
  "Template 70 'Search Results'", "Two 'Add Your Heading Text Here' placeholders; search pages are noindex,follow.", "Low", NV, "Visitor on empty or edge searches", "Needs verification (when shown)", "None beyond normal change approval",
  "Replace placeholders on staging.", "Low", "ACC-019", "Search for a nonsense term and a valid term; no placeholder text.", "")
F("ACC-085", 6, "Atomic (V4) editor experiments are active with mixed widget generations", "Platform / maintenance",
  "Elementor experiments", "e_atomic_elements, e_classes, e_components, e_opt_in_v4, e_variables, container, mega-menu, nested-elements all 'active'; e-image widgets on home and 2916; global classes empty; Elementor usage tracking on.",
  "Low", NV, "Maintenance risk during Elementor updates", "Confirmed (settings)", "You",
  "Note for regression testing; no action.", "Low", "ACC-160", "", "")
F("ACC-086", 6, "Child theme is effectively empty", "Maintenance",
  "Theme accord-insurance 1.0.0",
  "Files: README.txt, functions.php (592 B, enqueues style.css), style.css (692 B header only), accord-insurance.min.css (0 bytes), screenshot.png (650 KB). Kit has no custom CSS.",
  "Enhancement", DF, "Maintenance", "Confirmed", "You", "Decide where site-specific CSS should live. No action now.", "None", "", "", "")

# ---------------- 7. Responsive layout ----------------
F("ACC-100", 7, "Responsive rendering was not inspected visually", "Inspection gap",
  "All pages, tablet and mobile",
  "No browser or screenshot access in this phase. Breakpoints: tablet 1025, mobile 768; no widescreen. Header uses separate desktop and tablet/mobile containers. Lazy images omit width/height.",
  "Medium", NV, "Visitor", "Needs verification", "You (access to a browser capture)",
  "Run a visual QA at 1440, 1025, 768 and 390px on staging for all 19 pages and the popup.", "None", "", "Screenshot set reviewed.", "")
F("ACC-101", 7, "Footer legal text is set at 11px", "Responsive / readability",
  "Footer template 108", "Copyright and regulatory block font size 11px (config agent).", "Low", NV, "Readability, accessibility", "Needs verification (contrast and mobile size not measured)", "None beyond normal change approval",
  "Check legibility and contrast on mobile; increase if needed.", "Low", "ACC-100", "Passes contrast and minimum size review.", "")

# ---------------- 8. Images and media ----------------
F("ACC-110", 8, "Most media have empty alt text; informative images must be classified before any change", "Alt text",
  "Media library (95 of 96 images with empty alt); Elementor widgets",
  "Only the logo SVG (701) has alt. Media agent identified 16 informative-looking images with empty alt on 5 pages (home 2417; sectors 2614, 2556, 2561, 2603, 2602; commercial 2533; solutions 2755, 2743, 2742, 2741, 2744, 2745, 2750; bridging 2513, 2510). Body agent A judged many card/body images decorative. Team headshots 2255, 2256, 2257, 2368 empty in library; widget alt unverified.",
  "Medium", NV, "Accessibility, SEO", "Needs verification (purpose classification required)", "None beyond normal change approval",
  "Classify each image (informative vs decorative) with the client where needed. Leave decorative images blank. Write specific alt only for informative ones, especially team photos.", "Low",
  "ACC-121", "Alt audit table matches classification; decorative remain alt=\"\".", "Empty alt is valid for decorative images; not assumed wrong.")
F("ACC-111", 8, "Weak or placeholder-grade alt text on specific images", "Alt text",
  "Commodities hero; legal page heroes; dummy post featured images; Insights hero; Sectors hero",
  "Commodities hero alt and title '1'; five legal heroes alt 'contact hero'; post featured alts 'contact hero', 'hero2', '3'; Insights alt 'Accord Insurance Insughts' (typo); Sectors hero alt/title 'Accord insurance limited'; Bridging hero 'Bridging Lenders accord'.",
  "Medium", CA, "Accessibility, SEO", "Confirmed", "None beyond normal change approval",
  "Replace with descriptive alt if informative, or blank if decorative (hero backgrounds are likely decorative).", "Low", "ACC-110", "Alt values reviewed by classification.", "")
F("ACC-112", 8, "Non-descriptive filenames and typos in filenames", "Media hygiene",
  "1.jpg, 2.jpg, 3.jpg, 9-1.jpg, 1-1.jpg, hero-scaled.jpg, hero2-scaled.jpg, London.jpg, 47f24040-...-scaled.jpg, Accor-insurance-commercial-insurance.jpg, Accord-Insurance-Insughts.jpg",
  "Examples from the media agent and sitemap image lists; typos 'Accor' and 'Insughts'.",
  "Low", NV, "SEO (minor), maintainability", "Confirmed", "None beyond normal change approval",
  "Do not rename live files (breaks URLs). Improve titles/alt now; use clean names for new uploads.", "High if renamed", "", "No broken image URLs after any change.", "")
F("ACC-113", 8, "Site icon is a 584 KB JPEG at 514x512", "Image optimisation",
  "Attachment 705 Accord-favicon.jpg; option site_icon", "JPEG, 514x512, 584,126 bytes.", "Low", CA, "Performance, correctness", "Confirmed", "You",
  "Supply a square PNG/ICO at 512px optimised; set as site icon.", "Low", "", "Favicon appears in tab and search result; file under 50 KB.", "")
F("ACC-114", 8, "Oversize images and videos", "Performance / media",
  "Images 956, 1590, 2554, 1585; videos 2233, 2969, 3066",
  "956 47f24040-...-scaled.jpg 554,422 B 2560x1440; 1590 hero-scaled.jpg 299,615 B; 2554 295,760 B; 1585 283,161 B. Videos: 2233 32.9 MB (likely unused), 2969 8.2 MB (likely unused), 3066 8.3 MB (home hero in use). All raster images JPEG/PNG, no WebP/AVIF seen.",
  "Medium", NV, "Performance", "Needs verification (usage incomplete)", "None beyond normal change approval",
  "Confirm usage, then compress or replace; consider WebP; trim unused videos only after confirming zero references.", "Medium", "ACC-121", "Page weights and LCP improve; no missing media.", "")
F("ACC-115", 8, "Duplicate or orphan media candidates", "Media hygiene",
  "3094, 3070, 2987, 2956, 2859, 2858, 2805, 2413, 2381, 2357, 2265, 741, 459, 458, 2677, 740, 2746",
  "Candidates only (usage mapped for 5 pages). Examples: 2413 duplicates 2417 name; 2746 and 2750 same size 28,842 B; 2677 and 740 are Elementor screenshot artefacts; 2987 BIBA-logo.png is 1920x1080 for a logo; 2381 placeholder.png.",
  "Low", NV, "Maintenance", "Needs verification", "None beyond normal change approval", "Do not delete until a full usage scan is complete and the client agrees.", "Medium", "ACC-121", "Zero references before any removal.", "")
F("ACC-116", 8, "One stock hero image reused across legal pages and as social image", "Media reuse",
  "contact-hero.jpeg (784)", "Hero on privacy, regulatory status, Terms of Use, Terms of Business and complaints; og:image on those pages and post 1302; fallback featured image in template 82. 2048x1366, 223,390 B.",
  "Low", CA, "Design, SEO", "Confirmed", "Client", "Optional: give legal pages their own or no hero.", "Low", "", "", "")
F("ACC-117", 8, "Footer logo Asset-2.svg has empty alt", "Alt text",
  "Footer template 108, attachment 741", "Logo image alt=\"\" next to text; a second near-identical SVG 701 is the header logo with alt 'Accord Insurance Brokers logo'.", "Low", NV, "Accessibility", "Needs verification (informative or decorative?)", "None beyond normal change approval",
  "Decide: decorative duplicate (leave blank) or informative (alt = company name).", "Low", "ACC-110", "", "")
F("ACC-118", 8, "Image-to-page usage mapping is incomplete", "Inspection gap",
  "Pages 2084, 2171, 412, 387, 2027, 2916, 324, 2792, six legal pages; templates 125, 108, 2804, 1679, 1689, 1700, 1709, 1716, 1727, 1776, 1787, 1830, 2373, 82, 66, 70, 80, 1239, 2649",
  "Media agent read full Elementor data for 5 pages only. Body agents recorded images for the others. The consolidated 100-row CSV marks upload-parent usage as inferred.",
  "Medium", NV, "Completeness of the image inventory", "Needs verification", "You (access to full-fetch tooling)",
  "Run a one-page-at-a-time Elementor JSON scan and regex image ids.", "None", "", "Inventory CSV with verified usage for all rows.", "CSV: scratchpad media/image_inventory.csv (library metadata complete).")
F("ACC-119", 8, "Yoast default social image not set", "Metadata",
  "wpseo_social", "Media agent reported og_default_image, og_default_image_id and og_frontpage_image empty. Not independently verified.", "Low", NV, "Social sharing", "Needs verification", "None beyond normal change approval",
  "Verify in Yoast settings; set a default.", "Low", "ACC-060", "", "")

# ---------------- 9. Accessibility ----------------
F("ACC-130", 9, "Header desktop and mobile duplicates both present in HTML", "Hidden duplicate content",
  "Header template 125, containers 4d1f8e33 (desktop) and 52fea39 (tablet/mobile)",
  "Each holds the logo (alt 'Accord Insurance Brokers logo'), nav menu and Book a Call button; nav list markup appears four times in the header. Hidden by Elementor responsive classes (elementor-hidden-*). Only spacers elsewhere carry hidden classes; no duplicated body text found.",
  "Low", NV, "Accessibility, crawlers", "Needs verification (computed display:none not tested)", "None beyond normal change approval",
  "Confirm with a browser accessibility tree that hidden copies are excluded; if not, restructure to a single responsive header.", "Medium (header is global)", "ACC-100", "Accessibility tree contains one navigation per viewport.", "")
F("ACC-131", 9, "Autoplay hero video without pause control, captions or accessible name; two 8.3 MB references", "Accessibility / performance",
  "Home hero, video widgets 25b7e71 (hidden mobile) and a0db8c6 (hidden desktop/tablet)",
  "Accord-Insurance-Brokers.mp4, 8,330,239 bytes; autoplay muted playsinline; lazyload data-src; no caption track; no accessible name. Both widgets in markup, one hidden per breakpoint.",
  "Medium", NV, "Accessibility (moving content), performance", "Needs verification", "None beyond normal change approval",
  "Add pause control and accessible label; confirm only one file downloads per device.", "Medium", "ACC-114", "Network log shows one video request; keyboard can pause.", "")
F("ACC-132", 9, "Repeated and weak link text", "Accessibility",
  "/sectors/ (four 'Read more'), 'Get in touch' buttons, 'Speak to a broker' buttons",
  "Four identical 'Read more' buttons; SVG <style> rules appear inside link text on buttons with icons.",
  "Low", CA, "Accessibility", "Confirmed", "None beyond normal change approval", "Add distinct accessible names (aria-label or visible text) per card.", "Low", "", "Link list in screen reader shows distinct names.", "")
F("ACC-133", 9, "Duplicate HTML ids", "Accessibility / validity",
  "/sectors/financial-institutions/ (id Layer_1 x14); /insurance-for-bridging-lenders/ (hero image id 2956 / data-id 589d177 reused); home hero img id 2417 on lazy and noscript copies",
  "As reported by body agent A.", "Low", CA, "Validity", "Confirmed", "None beyond normal change approval", "Make SVG ids unique.", "Low", "", "HTML validator reports no duplicate ids.", "")
F("ACC-134", 9, "Colour contrast, focus order and form accessibility not tested", "Inspection gap",
  "Sitewide", "No browser-based audit performed. Skip link present and lang='en-GB' (positive).", "Medium", NV, "Accessibility", "Needs verification", "You (access)", "Run axe/Lighthouse and keyboard tests on staging.", "None", "ACC-100", "Report with zero critical issues.", "")
F("ACC-135", 9, "Form field labelling oddities", "Accessibility / forms",
  "/contact-us/ form 59a67030", "'Company name' field has custom id email_get_in_touch; Name and Company fields have no field type set.", "Low", NV, "Accessibility, data quality", "Needs verification", "None beyond normal change approval",
  "Correct ids and types on staging.", "Low", "ACC-001", "Fields announce correct labels and types.", "")

# ---------------- 10. Forms and conversion paths ----------------
F("ACC-140", 10, "Contact form has no consent or privacy notice, no spam control, default success message", "Forms",
  "/contact-us/ form 59a67030",
  "Fields Name, Company name, Email, Phone, Your message (all required). No consent checkbox or privacy link, no honeypot or reCAPTCHA/hCaptcha/Turnstile, no redirect or webhook, Elementor default success text. Submissions DB storage not confirmed.",
  "Medium", LC, "Compliance, spam, data handling", "Confirmed (settings)", "Legal/compliance and client",
  "Add an approved privacy notice or consent line and spam protection; confirm submission storage.", "Medium", "ACC-001, ACC-183", "Test submission (approved) passes validation, shows notice, reaches the mailbox.", "")
F("ACC-141", 10, "Contact form subject and sender name contain a typo", "Forms / typo",
  "/contact-us/ form 59a67030", "Subject and from-name: 'New message from \"Accord Insurance Borkers\"'.", "Low", CA, "Brand, deliverability", "Confirmed", "None beyond normal change approval",
  "Correct 'Borkers' to 'Brokers'.", "Low", "ACC-001", "Received test email shows the corrected text.", "")
F("ACC-143", 10, "'Review Policy' button on the bridging lenders page points to /sectors/", "Broken or misleading link",
  "/insurance-for-bridging-lenders/", "Button label 'Review Policy' links to https://accordib.com/sectors/.", "Medium", CI, "Conversion", "Confirmed", "Client",
  "Client to confirm intended destination; relabel or relink.", "Low", "ACC-055", "Button label and destination agree.", "")
F("ACC-144", 10, "Sector links omit the trailing slash and cause a redirect", "Links",
  "Template 1709 buttons and /sectors/ 'Read more' buttons", "/sectors/commercial-insurance and /sectors/commodities-trade-finance return 200 after 1 redirect.", "Low", CA, "Performance (minor), crawl", "Confirmed", "None beyond normal change approval",
  "Update link targets to canonical trailing-slash URLs.", "Low", "", "Links return 200 with 0 redirects.", "")
F("ACC-145", 10, "Joinchat WhatsApp widget configuration", "Conversion / privacy",
  "Joinchat settings", "Number ends 392, right position, button delay 3, message_delay 10, message_text empty, optin_check no, tracking yes, visible on all pages.", "Low", NV, "Conversion, privacy", "Confirmed (settings)", "Client (number, message)", "Confirm the number is the intended business line and decide on the opt-in.", "Low", "ACC-185", "Chat opens the intended number with the agreed message.", "")

# ---------------- 11. Performance and technical health ----------------
F("ACC-150", 11, "Performance not measured; console errors and network failures not captured", "Inspection gap",
  "Sitewide", "No browser or Lighthouse in this phase. Static checks: HEAD on sampled uploads all 200; no http:// mixed content except the FOS link text; combined CSS via SG Optimizer; fonts from fonts.googleapis.com.", "Medium", NV, "Performance", "Needs verification", "You (access)",
  "Capture Lighthouse/CWV and console logs for key pages on staging.", "None", "ACC-100", "Baseline report stored for comparison.", "")
F("ACC-151", 11, "Lazy images omit width and height; high fetch priority on a below-fold card", "Performance",
  "Most pages (lazysizes markup); /sectors/ card image 2556", "Lazy <img> has a 1x1 GIF src, no width/height; noscript copy has them. fetchpriority=high on a below-fold card.", "Low", CA, "Layout shift, LCP", "Confirmed", "None beyond normal change approval",
  "Set intrinsic dimensions and prioritise only the LCP image.", "Low", "ACC-150", "CLS and LCP improve in Lighthouse.", "")
F("ACC-152", 11, "PHP error log shows cron save failures and old fatal errors", "Technical health",
  "php_errorlog", "'cron event list could not be saved' for action_scheduler_run_queue, cmplz_every_five_minutes_hook and delete_expired_transients (29 Jun, 17 Aug, 7-15 Sep); Elementor cloud-library 403 fatal on 10 Jun; sg_ai_studio invalid_schedule 21 Jun; repeated SG auto-login lines. No overdue cron events.", "Low", NV, "Reliability", "Needs verification (history, may be resolved)", "None beyond normal change approval",
  "Review with hosting after Elementor update; confirm cron health.", "Low", "ACC-160", "No new entries over 7 days.", "")
F("ACC-153", 11, "Cache drop-ins and detection mismatch", "Technical health",
  "wp-content", "advanced-cache.php, object-cache.php (12,532 B), sgo-config.php, stray object-cache-socket-missing.php (same size), upgrade-temp-backup/; wp_cache_get_provider returns 'none' although SG caching headers are present.", "Low", NV, "Maintenance", "Needs verification", "Hosting",
  "Ask hosting whether the stray file and upgrade backup can be cleaned.", "Low", "", "", "")
F("ACC-154", 11, "Redirect behaviour is clean on core URLs", "Redirects",
  "http, www, sitemaps, ?p= and ?page_id= URLs", "Each redirects once to the canonical URL; no loops.", "Low", NI, "None", "Confirmed", "None", "No action.", "None", "", "", "")

# ---------------- 12. WordPress maintenance and security ----------------
F("ACC-160", 12, "Elementor Pro 4.3.0 has an update available (4.3.1)", "Maintenance",
  "Plugin elementor-pro/elementor-pro.php", "wp_list_plugins: version 4.3.0, update_available true, new_version 4.3.1; Site Health flags it as recommended. Elementor 4.3.3 and all other plugins current; WP 7.1.2, PHP 8.2.34.", "Medium", CA, "Maintenance, security", "Confirmed", "You and client (maintenance window)",
  "Do not update live. Take full backup, test on staging, run regression tests, then update in a window.", "Medium to High (page builder)", "ACC-190, ACC-191", "Staging regression passes; live post-update crawl matches baseline.", "Per your instruction recorded as a controlled maintenance task.")
F("ACC-161", 12, "Public REST API exposes user accounts", "Security / privacy",
  "/wp-json/wp/v2/users", "HTTP 200, X-WP-Total 3. Two administrators have a full email address as display name and an email-derived slug; user 4 slug 'matthewaccordib-com'. Gravatar hashes exposed. Reported by three agents.", "Medium", CA, "Security: username and email disclosure", "Confirmed", "You",
  "Restrict the endpoint for logged-out users and set safe display names/nicenames. Use the security plugin if it supports it.", "Low to Medium", "ACC-071", "Logged-out GET returns 401/403 or no users; author URLs not email-derived.", "Emails are not reproduced here.")
F("ACC-162", 12, "Cowboy MCP plugin with write, file and SQL tools is active in production; 4 administrators including a personal account", "Security / access",
  "Plugin cowboy-mcp 1.6.9; users", "Plugin exposes tools including wp_write_file, wp_cli, raw SQL; safe mode on. 4 users, all administrators (2 agency, 1 personal gmail-domain, 1 client).", "Medium", CI, "Security", "Confirmed", "You and client",
  "Keep only for the remediation window; review admin accounts and remove unneeded access.", "Low", "ACC-005", "Plugin deactivated after remediation; admin list reviewed.", "")
F("ACC-163", 12, "Security headers missing on front-end pages", "Security",
  "Front-end responses", "Home/robots responses show only x-content-type-options and x-xss-protection. No HSTS, CSP, X-Frame-Options, Referrer-Policy or Permissions-Policy (present on wp-login only).", "Low", CA, "Security hardening", "Confirmed", "Hosting/you",
  "Add headers via hosting; start with HSTS, Referrer-Policy, Permissions-Policy; test CSP carefully (Elementor, HubSpot).", "Medium", "", "securityheaders scan; site still functions.", "")
F("ACC-164", 12, "No post revisions; remediation needs an external backup", "Safety",
  "Database", "Revisions 0; auto-draft 1. No content history to roll back to.", "Medium", CA, "Change safety", "Confirmed", "You", "Take full backup and use staging before any edits.", "None", "ACC-190", "Backup restore tested.", "Cowboy checkpoints are not a substitute.")
F("ACC-165", 12, "SVG upload settings", "Security",
  "Safe SVG 2.5.1; Elementor unfiltered_files_upload=1", "Both active.", "Low", NV, "Security", "Confirmed (settings)", "You", "Review whether unfiltered uploads are still needed alongside Safe SVG.", "Low", "", "", "")
F("ACC-166", 12, "Activity logging and security plugins present", "Security",
  "Stream 4.4.0, SG Security 1.6.8", "Active. xmlrpc.php returns 403.", "Low", NI, "None", "Confirmed", "None", "No action.", "None", "", "", "")

# ---------------- 13. Privacy and cookies ----------------
F("ACC-180", 13, "HubSpot Meetings embed loads without consent gating", "Privacy / cookies",
  "/contact-us/, /book-a-call/, popup 2804", "HTML widget: data-src=https://meetings-eu1.hubspot.com/mwaterson?embed=true and script static.hsappstatic.net/MeetingsEmbed/ex/MeetingsEmbedCode.js (unquoted attributes). Complianz block_hubspot_service='no'. Banner behaviour not observed.", "Medium", LC, "Privacy compliance", "Needs verification", "Legal/compliance",
  "Compliance to decide; then gate the embed behind consent or add to Complianz blocking.", "Medium", "ACC-182", "Network log before consent shows no HubSpot requests.", "No legal judgement made.")
F("ACC-181", 13, "Google Fonts load from Google servers despite a self-host setting", "Privacy / performance",
  "Head on all pages; Complianz setting", "Work Sans and Poppins from fonts.googleapis.com; Complianz self_host_google_fonts='self-host'.", "Medium", NV, "Privacy, performance", "Needs verification", "Legal/compliance",
  "Self-host fonts or confirm the consent treatment.", "Low", "ACC-182", "No requests to fonts.googleapis.com or fonts.gstatic.com.", "")
F("ACC-182", 13, "Complianz configuration incomplete or inconsistent", "Privacy / cookies",
  "Complianz settings", "Region uk only; cookie blocker 'not-set'; consent type not set; consent mode no; statistics 'google-analytics' declared but ua/gtm/aw codes empty; cookie scan 2026-10-02 detected google-analytics and google-fonts; services declared: google-fonts, vimeo, google-maps, google-recaptcha (blocking no).", "Medium", NV, "Privacy compliance", "Needs verification", "Legal/compliance and client",
  "Reconcile with what the site actually loads; no analytics ID is configured in Complianz or visible HTML.", "Medium", "ACC-180, ACC-181", "Consent test across browsers; declarations match actual cookies.", "")
F("ACC-183", 13, "Cookie statement points to a non-existent page", "Privacy / cookies",
  "Complianz cmplz_cookie-statement_custom_page; /cookie-policy-uk/ (2862)", "Setting points to page 1249 (does not exist); the live cookie page 2862 uses [cmplz-document type=\"cookie-statement\" region=\"uk\"]. Privacy statement is custom (page 1245).", "Medium", CA, "Privacy compliance, link integrity", "Confirmed", "Legal/compliance", "Point the setting at page 2862 or regenerate; keep one cookie policy page.", "Low", "ACC-082", "Banner 'Cookie Policy' link opens /cookie-policy-uk/.", "")
F("ACC-184", 13, "Cookie Policy text includes irrelevant boilerplate and services not evidently used", "Privacy wording",
  "/cookie-policy-uk/", "Mentions 'items remain in your shopping cart until you have paid' and embedded content from WhatsApp, LinkedIn, X, Facebook and Instagram; only a link-less LinkedIn icon and the Joinchat plugin were seen.", "Low", LC, "Privacy wording", "Confirmed (quotes)", "Legal/compliance", "Revisit Complianz wizard answers so generated text matches the site.", "Low", "ACC-182", "Policy matches actual services.", "")
F("ACC-185", 13, "Joinchat has no consent opt-in and tracking enabled", "Privacy",
  "Joinchat settings", "optin_check no; tracking yes.", "Low", LC, "Privacy", "Confirmed (settings)", "Legal/compliance", "Decide on opt-in and tracking.", "Low", "ACC-145", "", "")
F("ACC-186", 13, "Cookie banner markup and pre-consent scripts not observed", "Inspection gap",
  "All pages", "Full HTML was truncated at about 51,200 characters, so wp_footer output and the banner were not seen.", "Medium", NV, "Privacy compliance", "Needs verification", "You (browser access)", "Capture with a browser: first-visit requests before consent.", "None", "ACC-180", "Documented request log.", "")

# ---------------- 14. Final regression testing ----------------
F("ACC-190", 14, "Pre-remediation baseline and staging", "Regression",
  "Whole site", "Revisions 0; live site; Elementor Pro update pending.", "High", CA, "Change safety", "Task", "You",
  "Full backup (database and uploads), staging clone, baseline crawl: status, titles, descriptions, canonicals, robots, H1, images, forms.", "None", "", "Baseline file stored.", "")
F("ACC-191", 14, "Post-batch regression checklist", "Regression",
  "All 19 pages, 4 posts, archives, popup, 404, search", "", "High", CA, "Change safety", "Task", "You",
  "After each batch: crawl for 200/301/404, one H1, meta and canonical, sitemap diff, link check, image check, console check, form test (approved), cookie banner test, desktop/tablet/mobile visual review, schema validation.", "None", "ACC-190", "Checklist signed off per batch.", "")
F("ACC-192", 14, "Search Console and indexing follow-up", "Regression",
  "Google Search Console", "Google site verification tag present on home.", "Medium", CA, "SEO", "Task", "Client",
  "After indexing changes, resubmit sitemap and inspect key URLs.", "None", "ACC-004, ACC-071", "Index coverage matches intent.", "")
F("ACC-193", 14, "Repeat this audit against the baseline", "Regression",
  "Whole site", "", "Medium", CA, "Assurance", "Task", "You", "Re-run the inventory after the last batch and compare to the original findings.", "None", "ACC-191", "All findings Verified complete or Intentionally retained.", "")

# ---------------- 15. Client-facing improvements summary ----------------
F("ACC-200", 15, "Client summary: enquiries and contact details", "Summary",
  "ACC-001, ACC-002, ACC-032, ACC-033, ACC-140, ACC-141", "Roll-up of contact and form fixes.", "Enhancement", DF, "Visitor conversion", "Roll-up", "Client", "Write the client-facing statement once these are fixed.", "None", "ACC-001", "", "")
F("ACC-201", 15, "Client summary: legal and regulatory accuracy", "Summary",
  "ACC-003, ACC-030 to ACC-042", "Roll-up of legal and company consistency.", "Enhancement", DF, "Compliance", "Roll-up", "Client", "Write once approved wording is live.", "None", "ACC-003", "", "")
F("ACC-202", 15, "Client summary: search visibility and clean indexing", "Summary",
  "ACC-004, ACC-050 to ACC-058, ACC-070 to ACC-072", "Roll-up of SEO fixes.", "Enhancement", DF, "SEO", "Roll-up", "Client", "Write once done.", "None", "ACC-050", "", "")
F("ACC-203", 15, "Client summary: accessibility, images and speed", "Summary",
  "ACC-110 to ACC-119, ACC-130 to ACC-135, ACC-150, ACC-151", "Roll-up.", "Enhancement", DF, "Accessibility, performance", "Roll-up", "Client", "Write once done.", "None", "ACC-110", "", "")
F("ACC-204", 15, "Client summary: privacy, security and upkeep", "Summary",
  "ACC-160 to ACC-164, ACC-180 to ACC-185", "Roll-up.", "Enhancement", DF, "Security, compliance", "Roll-up", "Client", "Write once done.", "None", "ACC-160", "", "")
