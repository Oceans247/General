# Accord Insurance Brokers: Master Remediation Tracker

Read-only audit baseline, 2 Oct 2026. Creating this tracker authorises no website change. Statuses use only the approved list.

| Priority | Count |
|---|---|
| Critical | 3 |
| High | 12 |
| Medium | 38 |
| Low | 48 |
| Enhancement | 8 |

## 1. Immediate concerns

### ACC-001: Contact form notifications are routed to the agency mailbox, not a client mailbox

- **Category:** Forms / conversion
- **Affected URL / template / setting:** /contact-us/ (page 387), Elementor form widget 59a67030 'Get in Touch Form'
- **Exact supporting evidence:** Stored settings: email_to, email_to_2 and email_reply_to_2 all use an address on the orbitagency.co.uk domain; email_from = email@accordib.com. No webhook, CRM or redirect configured. Reported independently by two agents. Form was NOT submitted.
- **Priority:** Critical
- **Status:** Awaiting client information
- **Impact:** Visitor, conversion: genuine enquiries may not reach the client; compliance: enquiries held by a third party
- **Confirmed or needs verification:** Confirmed (stored settings); intent unverified
- **Approval required:** Client (recipients) and you
- **Recommended action:** Confirm intended recipient list with the client, then update recipients, From and Reply-To. Keep the agency copy only if the client agrees (BCC).
- **Change risk:** Low (settings change) but affects live lead flow
- **Dependencies:** ACC-002, ACC-140, ACC-141
- **Verification test after remediation:** Client-approved test submission: confirm delivery to the named mailbox(es), inbox not spam, reply-to works, SPF/DKIM pass for sender domain.
- **Notes:** Possibly deliberate during build; must be decided before further marketing. The agency address is deliberately not reproduced in full here.

### ACC-002: Placeholder demo phone number and a US tel: link on the live Book a Call page

- **Category:** Content / contact details
- **Affected URL / template / setting:** /book-a-call/ (page 2792)
- **Exact supporting evidence:** Visible text '020 10 200 300' wrapped in <a href="tel:+11228008808"> (a +1 US number from a dynamic contact tag). Contact page shows '020 3764 9691' / tel:+442037649691. Page also shows only 'London / United Kingdom' as location. Reported by two agents.
- **Priority:** Critical
- **Status:** Awaiting client information
- **Impact:** Visitor: a click-to-call goes to the wrong country/number; brand and compliance risk
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client (correct number) and you
- **Recommended action:** Replace with the client-confirmed number (or remove the block) and align the tel: link with the visible text.
- **Change risk:** Low
- **Dependencies:** ACC-032, ACC-053
- **Verification test after remediation:** View page on desktop and mobile; tap the number and confirm the dialler shows the confirmed number; text matches href.
- **Notes:** Vamtam demo debris. Do not guess the number: confirm which of the three numbers found on the site is current.

### ACC-003: Complaints page states it is interim and awaits legal/compliance review

- **Category:** Legal / compliance wording
- **Affected URL / template / setting:** /complaints/ (page 1642)
- **Exact supporting evidence:** Published text: 'Important Note: This page contains interim general complaints information only. It should be reviewed and approved by our legal and compliance advisers before being relied upon as the final complaints policy.' Page is indexable and in the page sitemap.
- **Priority:** Critical
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance, visitor trust; regulated firm publishing self-declared provisional complaints text
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Legal/compliance and client
- **Recommended action:** Obtain approved complaints wording, replace the page text and remove the interim note. Until then consider temporarily setting the page to noindex only if compliance agrees.
- **Change risk:** Medium (regulatory wording)
- **Dependencies:** ACC-030, ACC-031, ACC-038
- **Verification test after remediation:** Re-read the page against the approved text; confirm no 'interim' wording remains; check timescales match the Terms of Business.
- **Notes:** Do not rewrite or paraphrase: wording must come from the client's compliance adviser.

### ACC-004: Four dummy posts are published, indexable, in the Yoast sitemap, in the RSS feed and linked from Insights, search and archives

- **Category:** Indexing / content exposure
- **Affected URL / template / setting:** /protecting-businesses-against-operational-disruption/ (post 218) and -2 (1302), -3 (1305), -4 (2192)
- **Exact supporting evidence:** All status 'publish'. robots meta 'index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1', no X-Robots-Tag, canonical self. All four listed in post-sitemap.xml (lastmod 2026-08-18T15:07:13+00:00). Identical post title and Article headline 'Protecting Businesses Against Operational Disruption', identical 241-word body, same author and category 'Accord'. Distinct per-post Yoast titles (Commercial Risk Insurance, Operational Disruption Insurance, Business Interruption Insurance, Business Continuity Insurance). Full text in /feed/. Linked from the Insights loop grid (template 119), /category/accord/, the author archive, search results and each post's 'More Insights' loop. Not in header or footer menus.
- **Priority:** High
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO (duplicate/thin content, keyword cannibalisation), visitor (placeholder-grade articles publicly reachable), compliance
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client (publish/hold decision) and you
- **Recommended action:** Decide the intended state, then either set all four to noindex and remove from the sitemap, or unpublish/draft three and keep one genuine article. Do not delete until the client confirms.
- **Change risk:** Low to Medium (reversible if set to noindex first)
- **Dependencies:** ACC-070, ACC-071, ACC-013
- **Verification test after remediation:** Fetch each post URL: expect noindex or 404/redirect as decided; post-sitemap.xml no longer lists them; /feed/ and Insights no longer show them; Search Console URL inspection after crawl.
- **Notes:** Known and expected placeholders, but public exposure is actionable. The article body reads as real insurance prose, not lorem ipsum: the client should confirm whether it is approved copy.

### ACC-005: Complianz client credentials were printed into an audit agent transcript

- **Category:** Security / process
- **Affected URL / template / setting:** Option values under cmplz_* (Complianz account connection)
- **Exact supporting evidence:** Config agent reported that a 'wp option list --search=cmplz_*' output contained a WSC client secret and an access token. Values are not reproduced here. The local scratchpad file holding the dump was deleted. Elementor licence data was also in that dump.
- **Priority:** High
- **Status:** Awaiting client information
- **Impact:** Security: credentials exposed to this session's logs
- **Confirmed or needs verification:** Confirmed (agent report)
- **Approval required:** You and client
- **Recommended action:** Decide whether to rotate the Complianz connection credentials (disconnect and reconnect the licence in Complianz) and review Elementor licence handling.
- **Change risk:** Low to Medium (reconnecting Complianz account)
- **Dependencies:** ACC-006
- **Verification test after remediation:** After rotation confirm Complianz still shows as connected and the banner renders.
- **Notes:** Exposure was to this session only, not public. Rotation is precautionary.

### ACC-006: Audit side effects: 11 server-side database checkpoints were created by wp_cli calls

- **Category:** Process / maintenance
- **Affected URL / template / setting:** Cowboy MCP checkpoints 1-11; change journal
- **Exact supporting evidence:** wp_list_checkpoints shows ids up to 11, created 2026-10-02 14:22:50 to 14:24:36 UTC, labelled 'Before wp_cli: ...' (trigger auto_wp_cli, about 0.6 MB each). 29 wp_cli entries in the journal; none after 14:24:53. wp_http_request GET/HEAD calls and one wp_batch_execute wrapper (20 HEADs) are journaled as 'not_undoable' audit entries. No posts, pages, templates, options or plugins were changed.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Maintenance: extra dump files on the server (contain site database copies)
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Decide whether to keep the checkpoints (harmless backups, but contain database copies including option values) or delete them in a controlled batch. Do not delete without approval.
- **Change risk:** Low
- **Dependencies:** ACC-005
- **Verification test after remediation:** wp_list_checkpoints after any clean-up; confirm no checkpoint remains if deletion approved.
- **Notes:** These breached the strict read-only brief and are disclosed as such. GET/HEAD journal entries are audit records, not site changes.

## 2. Content and development leftovers

### ACC-010: Pasted ChatGPT interface markup inside the Insights page text widget

- **Category:** Content / development artefact
- **Affected URL / template / setting:** /insights/ (page 324), text-editor widget 5446eed
- **Exact supporting evidence:** Widget HTML contains qMYqUG_convSearchResultHighlightRoot, data-turn-id, data-testid="conversation-turn-50", data-message-model-slug="gpt-5-5-thinking" and Tailwind-like classes wrapping the intro paragraph. Reported by two agents.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO and maintenance: junk attributes in crawlable HTML; possible visual or accessibility side effects
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Replace the widget content with the plain paragraph text (keep wording unchanged), using the Elementor editor on staging first.
- **Change risk:** Low
- **Dependencies:** ACC-070
- **Verification test after remediation:** View source of /insights/: no 'conversation-turn', 'data-message-model-slug' or similar; text renders identically.

### ACC-011: Commodities & Trade Finance hero/CTA link is empty or malformed

- **Category:** Broken link
- **Affected URL / template / setting:** /sectors/commodities-trade-finance/ (page 2084)
- **Exact supporting evidence:** Body agent A saw the hero 'Contact us' button rendering href="" . Config agent saw a stored CTA href 'Ωhttps://accordib.com/contact-us/#touch' (stray leading character). The two may be different buttons or the same button in rendered vs stored form.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Visitor: dead or broken primary CTA
- **Confirmed or needs verification:** Needs verification (agents disagree on which button)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Inspect both buttons in Elementor, fix the stray character, and point the empty button to /contact-us/#touch.
- **Change risk:** Low
- **Dependencies:** ACC-012
- **Verification test after remediation:** Click every CTA on the page on desktop and mobile; each lands on /contact-us/#touch.

### ACC-012: Claims page: both 'Get in touch' buttons have no destination

- **Category:** Broken link
- **Affected URL / template / setting:** /claims/ (page 2027), widgets ede4610 and 4b19451
- **Exact supporting evidence:** Rendered href="#" on both; config agent found no link set. Reported by two agents.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Visitor: dead CTAs on a claims page
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client (confirm destination) and you
- **Recommended action:** Link both buttons to /contact-us/#touch (or the client's claims contact route).
- **Change risk:** Low
- **Dependencies:** ACC-011
- **Verification test after remediation:** Click each button; correct destination loads.
- **Notes:** Claims route may need a specific contact: confirm with client.

### ACC-013: Footer 'Insights' entry is plain text, not a link

- **Category:** Navigation / unfinished content
- **Affected URL / template / setting:** Footer template 108, text-editor widget f85de31
- **Exact supporting evidence:** Widget outputs <p>Insights</p> with no anchor. /insights/ is live (HTTP 200), absent from the header menu (menu 47) and listed in the page sitemap. Reported by three agents.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** Visitor: unlinked item looks broken; consistency with a hidden/unfinished News area
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client (decide whether Insights should be public) and you
- **Recommended action:** Decide Insights visibility first. If public later, link it; if not, remove the footer entry.
- **Change risk:** Low
- **Dependencies:** ACC-004, ACC-070
- **Verification test after remediation:** Footer renders without an unlinked text item, or the link resolves 200 and matches header navigation.

### ACC-014: Footer LinkedIn icon has no URL

- **Category:** Navigation / unfinished content
- **Affected URL / template / setting:** Footer template 108, social-icons widget 72646685
- **Exact supporting evidence:** Single LinkedIn icon with no link configured (reported by two agents).
- **Priority:** Low
- **Status:** Awaiting client information
- **Impact:** Visitor, brand: dead icon
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client (profile URL)
- **Recommended action:** Add the confirmed LinkedIn company URL or remove the icon.
- **Change risk:** Low
- **Dependencies:** ACC-056
- **Verification test after remediation:** Icon opens the correct profile in a new tab with rel=noopener.

### ACC-015: Footer sub-footer nav-menu widget points at an empty menu with no theme location

- **Category:** Navigation / architecture
- **Affected URL / template / setting:** Footer template 108 nav-menu widget 77c20636; menu 'Footer - Main' (id 28); theme location menu-2
- **Exact supporting evidence:** Menu 28 has 0 items and no location; menu-2 is unassigned. The visible footer link columns are text-editor widgets, not a WordPress menu. The nav-menu widget therefore renders nothing.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance only; no visible defect
- **Confirmed or needs verification:** Confirmed (empty widget); defect not confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Not defective by itself because the footer navigation is built inside the Elementor template. Verify the rendered footer, then either remove the empty widget or populate menu 28 and drive the footer links from it.
- **Change risk:** Low
- **Dependencies:** ACC-016
- **Verification test after remediation:** Rendered footer has no empty nav element; links unchanged.
- **Notes:** Per your caution, the empty location alone is not treated as a bug.

### ACC-016: Unassigned menus: 'Sectors Menu' (id 46, 4 items) and 'Footer - Main' (id 28)

- **Category:** Maintenance
- **Affected URL / template / setting:** Appearance > Menus
- **Exact supporting evidence:** wp_list_menus: Sectors Menu has 4 items and no locations; Footer - Main has 0 items and no location. Menu 46 duplicates the sector links already in the header.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance clutter
- **Confirmed or needs verification:** Needs verification (check no widget uses menu 46)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Search Elementor data for menu slug 'sectors-menu' before any removal; keep if used.
- **Change risk:** Low
- **Dependencies:** ACC-015
- **Verification test after remediation:** No widget or location references the removed menu; header and footer unchanged.

### ACC-017: Finance and Investment template-kit leftovers (loop/archive/search templates and slugs)

- **Category:** Development artefact
- **Affected URL / template / setting:** Elementor templates 64, 68, 78, 93, 101, 117, 119, 121, 123, 133; Header (slug header-finance-investment) and Footer (slug footer-finance-investment)
- **Exact supporting evidence:** Created 2026-05-23, all published. Config agent: no display conditions on the loop items and archive 64, and elementor_library URLs redirect to home. Body agent B: template 119 'Blog Post Loop - Classic' is the loop used by the Insights page and each post's 'More Insights' block, so at least one is in use. Search Results 70 references a loop template.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance: dead templates and demo slugs
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Do not delete yet. For each template confirm: no display conditions, not referenced by another template or page loop widget, and not needed for rollback. Remove only unreferenced ones after a backup. Template 119 must stay while the Insights loop exists.
- **Change risk:** Medium (Elementor references are not always visible)
- **Dependencies:** ACC-018, ACC-190
- **Verification test after remediation:** After each removal, load home, Insights, a post, search results, 404 and a legal page and compare to baseline.
- **Notes:** Your caution applied: nothing is marked deletable.

### ACC-018: Active Elementor kit is titled 'test' and carries Vamtam theme globals

- **Category:** Maintenance / design system
- **Affected URL / template / setting:** Elementor kit post 10 (title 'test'); Default Kit post 6 (unused)
- **Exact supporting evidence:** Config agent: kit 10 is the live global-settings kit (elementor_active_kit), previous_kit=6. It still holds vamtam_accent_1..8, vamtam_h1..h6 and 'Sticky Header Bg Color' ids; many widgets reference globals/colors?id=vamtam_*.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Maintenance: risk that 'test' is mistaken for junk and deleted, breaking global styles
- **Confirmed or needs verification:** Confirmed (the template named 'test' is the live kit)
- **Approval required:** None beyond normal change approval
- **Recommended action:** NEVER delete post 10. Optionally rename the kit title after approval. Migrate Vamtam global references to Accord globals only on staging.
- **Change risk:** High if mishandled
- **Dependencies:** ACC-081, ACC-190
- **Verification test after remediation:** Site renders identically after any rename; kit settings unchanged.
- **Notes:** Resolves the earlier suspicion that the 'test' template was a demo leftover.

### ACC-019: Demo debris in settings and templates (hidden video URLs, demo image, demo slug, placeholder headings)

- **Category:** Development artefact
- **Affected URL / template / setting:** Home hero video widgets; container 3b962d8b; loop template 119; post 218 old slug; Search Results template 70
- **Exact supporting evidence:** Hidden settings keep demo YouTube, Vimeo (vimeo.com/236906999), Dailymotion and VideoPress URLs. Template 119 fallback image: finovate.demo.vamtam.com/.../dummy-post-horisontal-thegem-blog-default-large.jpg (third-party dependency, used only without a featured image). Post 218 RSS guid uses slug from-local-to-leader-scaling-strategies-for-ambitious-regional-banks. Search Results 70 contains two 'Add Your Heading Text Here' placeholders.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance; small chance of visible placeholder on edge states
- **Confirmed or needs verification:** Confirmed (stored data); visibility unverified
- **Approval required:** None beyond normal change approval
- **Recommended action:** Clean on staging: remove unused URLs, replace the third-party fallback image with a local one, replace placeholder headings.
- **Change risk:** Low
- **Dependencies:** ACC-190
- **Verification test after remediation:** Search with and without results; post without featured image; no requests to vamtam.com in network log.

### ACC-020: Unused global container templates and saved sections

- **Category:** Maintenance
- **Affected URL / template / setting:** Templates 1830, 1753, 2373, 1836, 1727 (slug global-our-values)
- **Exact supporting evidence:** No usage seen by the config agent; usage scan was incomplete (template widgets on pages 256, 2084, 2125, 2140, 2171, 324, 426 did not expose ids; legal pages 1273, 1278, 1640, 1642 and templates 80, 82 not scanned).
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Complete a usage scan across all pages/templates before any decision. Keep as reusable sections if the client wants them.
- **Change risk:** Low
- **Dependencies:** ACC-190
- **Verification test after remediation:** Usage report shows zero references before removal.

### ACC-021: Draft, private, pending, future and trash content

- **Category:** Inventory
- **Affected URL / template / setting:** All post types
- **Exact supporting evidence:** Config agent: no draft, pending, private, future or trash items. Only auto-draft 3154. 19 pages, 4 posts, 33 elementor_library, 100 attachments, 14 nav items. 0 revisions.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None
- **Recommended action:** No action. Re-check after remediation.
- **Change risk:** None
- **Notes:** Recorded for baseline. The 'unpublished News/Insights area' is in fact published (see ACC-070).

### ACC-022: Elementor library templates and Coming Soon page publicly reachable

- **Category:** Indexing
- **Affected URL / template / setting:** /?elementor_library=test, =header-finance-investment, =elementor-single-page-1239, =coming-soon
- **Exact supporting evidence:** Config agent GET on all four: HTTP 200 after 1 redirect, serving the home page with canonical https://accordib.com/ and robots index,follow. Maintenance mode is off.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None
- **Recommended action:** No action.
- **Change risk:** None
- **Notes:** Template URLs are not exposed as separate pages.

### ACC-023: Unresolved '{title}' style template variables in crawlable markup

- **Category:** Content / SEO
- **Affected URL / template / setting:** All inspected heads and visible bodies
- **Exact supporting evidence:** No '{title}', '%%title%%' or similar token was found in any Yoast head, in get-post-seo-data for 23 URLs, or in the visible HTML read. Only legitimate '{search_term_string}' in WebSite schema. Limitation: full HTML was truncated at about 51,200 characters per page.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** SEO
- **Confirmed or needs verification:** Needs verification (not found, not fully excluded)
- **Approval required:** None
- **Recommended action:** Run a full-DOM crawl (browser or full-fetch) and search for '{title}', '%%' and unrendered shortcodes.
- **Change risk:** None
- **Dependencies:** ACC-190
- **Verification test after remediation:** Crawl output contains zero matches.
- **Notes:** Seed item not confirmed by any agent.

## 3. Legal, regulatory and company-information consistency

### ACC-030: Two different company names used across legal pages and settings

- **Category:** Company information
- **Affected URL / template / setting:** Footer; /regulatory-status/; /terms-of-business/; /website-terms-of-use/; /privacy-policy/; Complianz organisation setting; Yoast schema; /sectors/ hero alt
- **Exact supporting evidence:** 'Accord Risk Limited' (footer, regulatory status, Terms of Business, Terms of Use). 'Accord Insurance Brokers Ltd' (Privacy Policy data controller; Complianz organisation name). 'Accord Insurance Brokers' (site name, schema, title tags, home). 'Accord insurance limited' (hero alt/title on /sectors/).
- **Priority:** High
- **Status:** Awaiting client information
- **Impact:** Compliance, trust, legal identity of the data controller
- **Confirmed or needs verification:** Confirmed (variants exist); correct form unknown
- **Approval required:** Client and legal/compliance
- **Recommended action:** Client to confirm legal entity name and any trading name, then standardise legal pages, Complianz settings and schema. Do not edit until confirmed.
- **Change risk:** Medium
- **Dependencies:** ACC-031, ACC-003
- **Verification test after remediation:** Search the site for each name variant; only approved forms remain; privacy controller matches ToB.
- **Notes:** Footer states an appointed-representative relationship with Bennett Gould and Partners Limited, which appears elsewhere on the same account.

### ACC-031: Two different registered office addresses

- **Category:** Company information
- **Affected URL / template / setting:** Footer, /regulatory-status/, /terms-of-business/ vs /website-terms-of-use/, /privacy-policy/; /contact-us/
- **Exact supporting evidence:** Footer, regulatory status, ToB: '2 Manor Farm Court Old Wolverton Road, Old Wolverton, Milton Keynes, Buckinghamshire, England, MK12 5NN', company number 16261233. Terms of Use: 'Registered Office: 9 New Street, London EC2M 4TP'. Privacy: '9 New Street, London, EC2M 4TP'. Contact page: Milton Keynes address. Book a Call: 'London / United Kingdom'.
- **Priority:** High
- **Status:** Awaiting client information
- **Impact:** Compliance, legal validity of terms
- **Confirmed or needs verification:** Confirmed (conflict); correct address unknown
- **Approval required:** Client and legal/compliance
- **Recommended action:** Confirm registered office and any trading/office address, then align every page and Complianz.
- **Change risk:** Medium
- **Dependencies:** ACC-030
- **Verification test after remediation:** Single approved address set appears consistently; Companies House record matches (client to check).
- **Notes:** Do not infer which address is correct.

### ACC-032: Three different telephone numbers, one mismatching its link

- **Category:** Contact details
- **Affected URL / template / setting:** /contact-us/, /book-a-call/, /website-terms-of-use/, /privacy-policy/, Complianz setting
- **Exact supporting evidence:** Contact: 020 3764 9691 (tel:+442037649691). Terms of Use and Privacy: +44 (0)78 7148 6392. Book a Call: 020 10 200 300 with tel:+11228008808 (demo). Complianz phone: 020 3764 9691.
- **Priority:** High
- **Status:** Awaiting client information
- **Impact:** Visitor, compliance
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Client to confirm the published number(s); apply across pages, Complianz and schema where appropriate.
- **Change risk:** Low
- **Dependencies:** ACC-002
- **Verification test after remediation:** Every phone mention and tel: link matches the approved list.

### ACC-033: Several email addresses, mixed case, and a named individual's mailbox for complaints

- **Category:** Contact details
- **Affected URL / template / setting:** Contact, Complaints, Terms of Use, Privacy, form sender
- **Exact supporting evidence:** hello@accordib.com (Contact, Book a Call, Complianz), matthew@accordib.com (Complaints, Privacy, ToB), Info@accordib.com and info@accordib.com (Terms of Use), email@accordib.com (form From). Complaints page gives only matthew@accordib.com.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** Compliance (complaints route), continuity
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client and legal/compliance
- **Recommended action:** Client to confirm which addresses are intended, whether complaints should use a role mailbox, and the exact case.
- **Change risk:** Low
- **Dependencies:** ACC-030
- **Verification test after remediation:** All addresses valid and monitored; mail test per address.

### ACC-034: Typo in the regulatory statement: 'is a an appointed representative'

- **Category:** Legal wording / typo
- **Affected URL / template / setting:** Footer template 108 (all pages)
- **Exact supporting evidence:** 'Accord Risk Limited is a an appointed representative of Bennett Gould and Partners Limited, which is authorised and regulated by the Financial Conduct Authority (firm reference number 306850).' Reported by three agents.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance, credibility
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Legal/compliance (regulatory text) and client
- **Recommended action:** Obtain approval to correct 'a an' to the approved wording; apply in the footer template only.
- **Change risk:** Low
- **Dependencies:** ACC-030
- **Verification test after remediation:** Footer on every page shows the approved sentence; no other legal text changed.
- **Notes:** Likely a one-word fix but it sits inside a regulatory disclosure, so approval is required.

### ACC-035: 'Independent insurance broker' claim alongside appointed-representative status

- **Category:** Regulatory claim
- **Affected URL / template / setting:** Home and About (template 1716 and page text); footer
- **Exact supporting evidence:** Home: 'Accord is an independent insurance broker focused on delivering the right cover...'. About: 'Accord is an independent insurance broker focused on arranging cover shaped around each client's needs.' Footer: appointed representative of Bennett Gould and Partners Limited.
- **Priority:** High
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance (possible misleading status description)
- **Confirmed or needs verification:** Needs verification (legal judgement)
- **Approval required:** Legal/compliance
- **Recommended action:** Ask compliance whether 'independent' is permissible for an appointed representative.
- **Change risk:** Medium
- **Dependencies:** ACC-030
- **Verification test after remediation:** Approved wording in place or claim retained with written sign-off.
- **Notes:** No judgement made here.

### ACC-036: Terms of Business states FSCS membership

- **Category:** Legal wording
- **Affected URL / template / setting:** /terms-of-business/ (page 1640)
- **Exact supporting evidence:** 'We are a member of the Financial Services Compensation Scheme (FSCS)'. Page also describes Accord as a trading name and an appointed representative.
- **Priority:** High
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to confirm the statement and who the FSCS member is.
- **Change risk:** Medium
- **Dependencies:** ACC-035
- **Verification test after remediation:** Approved wording published.

### ACC-037: Typos and wording errors in the Terms of Business

- **Category:** Legal wording / typo
- **Affected URL / template / setting:** /terms-of-business/ (page 1640)
- **Exact supporting evidence:** 'commisison' and 'commisson'; 'settle your complain'; 'The Financial Ombudsman Exchange Tower' (word 'Service' missing); 'will be handed in accordance with the Data Protection regulations'; 'Cheques should be payable to directly to'; 'If we may employ the services of other intermediaries'.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance, credibility
- **Confirmed or needs verification:** Confirmed (quotes)
- **Approval required:** Legal/compliance
- **Recommended action:** Provide the list to compliance; apply only their approved corrections.
- **Change risk:** Low
- **Dependencies:** ACC-003
- **Verification test after remediation:** Re-read the page; each quoted error resolved with approved text.

### ACC-038: Inconsistent complaint timescales between Complaints page and Terms of Business

- **Category:** Legal wording
- **Affected URL / template / setting:** /complaints/ vs /terms-of-business/
- **Exact supporting evidence:** Complaints: acknowledgement within '5 business days'. ToB: 'resolved by close of business on the 3rd working day'; complex-case acknowledgement has no day count. Both state a final response within 8 weeks.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to reconcile timescales.
- **Change risk:** Medium
- **Dependencies:** ACC-003
- **Verification test after remediation:** Both pages carry the same approved timescales.

### ACC-039: Website Terms of Use: dated and future-tense regulatory wording, terminology mismatch

- **Category:** Legal wording
- **Affected URL / template / setting:** /website-terms-of-use/ (page 1278)
- **Exact supporting evidence:** Opens 'Last Updated: June 2026'. 'Where applicable, details of our regulatory status will be displayed on this website and in our client documentation.' Refers to 'our Privacy Notice and Cookie Policy' (pages are titled Privacy Policy and Cookie Policy).
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance
- **Confirmed or needs verification:** Confirmed (quotes)
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to confirm date, status wording and document names.
- **Change risk:** Low
- **Dependencies:** ACC-030
- **Verification test after remediation:** Approved text and consistent document names.

### ACC-040: Privacy Policy lacks a last-updated date and regulatory identity

- **Category:** Legal wording
- **Affected URL / template / setting:** /privacy-policy/ (page 1245)
- **Exact supporting evidence:** No 'last updated' date seen; controller 'Accord Insurance Brokers Ltd'; no FCA/appointed-representative mention; ICO address listed.
- **Priority:** Low
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to confirm required content.
- **Change risk:** Low
- **Dependencies:** ACC-030
- **Verification test after remediation:** Policy reviewed and approved.

### ACC-041: Third-party regulator/ombudsman links and details to verify

- **Category:** Legal wording
- **Affected URL / template / setting:** /complaints/, /terms-of-business/, /privacy-policy/
- **Exact supporting evidence:** FOS link uses http://www.financial-ombudsman.org.uk; FOS phone 0800 023 4567 and Exchange Tower address; BGP Corinium House Gloucester address and 03330 146 156; ICO Wycliffe House address.
- **Priority:** Low
- **Status:** Awaiting client information
- **Impact:** Compliance, link integrity
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Client/compliance
- **Recommended action:** Verify current details; use https links.
- **Change risk:** Low
- **Dependencies:** ACC-003
- **Verification test after remediation:** All external links 200 over https; details match source organisations.
- **Notes:** External links were not fetched (accordib.com only).

### ACC-042: Strong product and market claims needing compliance review

- **Category:** Regulatory claim
- **Affected URL / template / setting:** /insurance-for-bridging-lenders/, /sectors/bridging-lenders/, Home, Sectors
- **Exact supporting evidence:** 'The policy is designed to cover valuation fraud.'; 'Accord has developed specialist fraud insurance wording designed specifically for bridging lenders...'; 'Fraud within the short-term mortgage lending sector remains a material and ongoing risk.'; 'Market-leading insurers' (h4); 'access to Lloyd's, London market and international insurance capacity'.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance (financial promotion / product claims)
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to review claims; do not alter copy before sign-off.
- **Change risk:** Medium
- **Dependencies:** ACC-035
- **Verification test after remediation:** Approved or amended text recorded.
- **Notes:** No insurance-product facts were invented.

## 4. SEO and Yoast

### ACC-050: No H1 on most pages

- **Category:** Heading structure
- **Affected URL / template / setting:** Home, /sectors/ and 4 children, /solutions/, /about-us/, /claims/, /insurance-for-bridging-lenders/, /insights/, the four posts, six legal pages, cookie policy
- **Exact supporting evidence:** First heading on each page is an H2 from an Elementor heading widget (home widget a3d8ef7: <h2 class="elementor-heading-title">Specialist insurance broking for complex commercial, financial and credit risks.</h2>). Header (125) and footer (108) contain no H1. Posts: title renders as H2 via template 82. Legal pages: H2 title then H4 sections. Page-title selector in kit is h1.entry-title. Rendered tails were truncated at about 51,200 characters, so an H1 late in the page is unlikely but not excluded.
- **Priority:** High
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO, accessibility (page has no primary heading)
- **Confirmed or needs verification:** Confirmed in Elementor and rendered HTML (partly truncated)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Set the hero heading widget on each page to H1 (one per page); keep typography consistent via widget style because kit H1 is 52px vs H2 48px.
- **Change risk:** Medium (visual size changes)
- **Dependencies:** ACC-052, ACC-190
- **Verification test after remediation:** DOM check: exactly one H1 per URL matching the page topic; visual diff on desktop/tablet/mobile.
- **Notes:** Seed item 'most sampled pages may lack an H1' is confirmed on 10 body pages plus posts and legal pages.

### ACC-051: Contact and Book a Call use the wrong H1

- **Category:** Heading structure
- **Affected URL / template / setting:** /contact-us/ (widget 3d0c99e) and /book-a-call/
- **Exact supporting evidence:** Outline: H2 'Contact Us', H2 'Let's Connect', H2 'Send a Message', H2 'Book a Call', then H1 'General Enquiries' (last). Book a Call: H2 'Book a Call' then H1 'General Enquiries'.
- **Priority:** High
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO, accessibility
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Make the hero title the H1 and demote 'General Enquiries' to a lower heading.
- **Change risk:** Low
- **Dependencies:** ACC-050
- **Verification test after remediation:** One H1 matching page topic, in first position.

### ACC-052: Inconsistent heading hierarchy in shared templates, legal, search and 404 pages

- **Category:** Heading structure
- **Affected URL / template / setting:** Template 1709 (Our sectors); sector pages; legal pages; search results; 404
- **Exact supporting evidence:** Template 1709: three cards H3, 'Bridging Lenders' H2 (widget 4650a43). 'Why Choose' blocks jump H2 to H4. Sector card titles and coverage items are <p>. Cookie page H2 to H3 to H4 to H5; Complaints H2 'Complaints' then H4 'Complaints' and footer H2 'Talk to our experts today'. Search: H2 then H1 both 'Search Results for: ...'. 404: H1 '404' then H3.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Accessibility, SEO
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Normalise levels in the shared template first (one change fixes many pages), then per page.
- **Change risk:** Medium (shared template)
- **Dependencies:** ACC-050
- **Verification test after remediation:** Heading outline export per URL has no skipped levels.

### ACC-053: /book-a-call/ duplicates the Contact page metadata and is indexable

- **Category:** Metadata / indexing
- **Affected URL / template / setting:** /book-a-call/ (page 2792) vs /contact-us/
- **Exact supporting evidence:** SEO title, meta description, og:title, og:description, twitter fields and og:image identical to Contact; indexable; in page sitemap; schema plain WebPage.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** SEO: duplicate metadata, thin page
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Give it unique metadata or set noindex/canonical to Contact if it is only a booking utility.
- **Change risk:** Low
- **Dependencies:** ACC-002
- **Verification test after remediation:** Unique title/description or noindex as decided.

### ACC-054: Cookie Policy has no meta description and default title format

- **Category:** Metadata
- **Affected URL / template / setting:** /cookie-policy-uk/ (page 2862)
- **Exact supporting evidence:** Title 'Cookie Policy - Accord Insurance Brokers' (40 chars, ' - ' separator vs ' | ' elsewhere); no description, og:description or twitter fields; no focus keyphrase.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Add a factual, non-legal meta description and align the title pattern. Draft wording for your approval.
- **Change risk:** Low
- **Verification test after remediation:** View source shows one description (70-160 chars) and matching OG tags.
- **Notes:** Seed item confirmed.

### ACC-055: Overlapping bridging-lender pages and keyphrase cannibalisation

- **Category:** SEO structure
- **Affected URL / template / setting:** /insurance-for-bridging-lenders/ (2916) vs /sectors/bridging-lenders/ (256)
- **Exact supporting evidence:** Both cover bridging-lender fraud, PI and D&O. 256 links to 2916 ('Find out more'); 2916 is not in the main menu. Focus keyphrase on 2916 'specialist insurance brokers' equals the homepage's. 2916 og:title and twitter:title repeat the full SEO title with brand suffix. 2916 'Review Policy' button points to /sectors/.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** SEO: competing pages
- **Confirmed or needs verification:** Confirmed (overlap); intent unknown
- **Approval required:** Client
- **Recommended action:** Client to decide the role of each page, then differentiate keyphrases or consolidate.
- **Change risk:** Medium
- **Dependencies:** ACC-143
- **Verification test after remediation:** Distinct intent, titles and keyphrases; no cannibalising queries in Search Console.

### ACC-056: Organization schema is minimal

- **Category:** Structured data
- **Affected URL / template / setting:** Sitewide Yoast schema graph
- **Exact supporting evidence:** Organization has name, url and SVG logo 333x73 only: no address, telephone, sameAs, contactPoint, legalName or regulator reference. Type is generic Organization. Yoast global settings could not be read.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** SEO enhancement, entity clarity
- **Confirmed or needs verification:** Confirmed (rendered)
- **Approval required:** Client and legal/compliance (any regulatory property)
- **Recommended action:** After company details are settled, complete Yoast organisation data (address, phone, profiles, logo). Do not add details until verified.
- **Change risk:** Low
- **Dependencies:** ACC-030, ACC-031, ACC-032, ACC-014
- **Verification test after remediation:** Rich Results / schema validator shows complete Organization without errors.

### ACC-057: Open Graph images lack width, height and type on several URLs

- **Category:** Metadata
- **Affected URL / template / setting:** /, /sectors/, /solutions/, /insurance-for-bridging-lenders/, author archive
- **Exact supporting evidence:** get_head json shows og_image with empty width/height/type (Elementor thumbs or missing image metadata). Yoast og_default_image appears empty (media agent), unverified.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** SEO, social sharing
- **Confirmed or needs verification:** Confirmed (rendered); default setting needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Set explicit social images with metadata in Yoast, plus a default social image.
- **Change risk:** Low
- **Dependencies:** ACC-060
- **Verification test after remediation:** Facebook/LinkedIn debugger shows correct image and size.

### ACC-058: Schema and breadcrumb text defects

- **Category:** Structured data
- **Affected URL / template / setting:** Home, Commodities page, author archive
- **Exact supporting evidence:** Home breadcrumb second item 'Accord Insurance Brokers' (not a page label); Commodities title stored with '&amp;' and double-encoded in JSON-LD breadcrumb; author sameAs 'http://accordib.com'.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Correct entity encoding and breadcrumb labels.
- **Change risk:** Low
- **Verification test after remediation:** Schema validator and rendered breadcrumbs correct.

### ACC-059: Possible second meta description tag on Contact

- **Category:** Metadata
- **Affected URL / template / setting:** /contact-us/
- **Exact supporting evidence:** Body agent B saw two <meta name="description"> tags (one from Yoast, one plain). Not seen by the SEO agent.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** SEO
- **Confirmed or needs verification:** Needs verification (single source)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Confirm in full source; find and remove the non-Yoast tag.
- **Change risk:** Low
- **Verification test after remediation:** Exactly one description tag.

### ACC-060: Yoast global settings not inspected

- **Category:** Inspection gap
- **Affected URL / template / setting:** wpseo, wpseo_titles, wpseo_social options
- **Exact supporting evidence:** No safe read-only reader exists in the allowed toolset (only wp_cli, which creates checkpoints). Settings inferred from rendering: author and category archives indexable, attachments redirect to file, search and 404 noindex, breadcrumbs on, llms.txt off, Google verification present.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** SEO
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (access)
- **Recommended action:** Export Yoast settings from wp-admin (SEO > Tools) or share screenshots, or approve a one-off read via wp_cli on staging.
- **Change risk:** None
- **Verification test after remediation:** Settings compared with rendered output.

### ACC-061: Yoast traffic-light scores on some pages

- **Category:** SEO optimisation
- **Affected URL / template / setting:** Bridging Lenders, Commercial Insurance, Commodities, Solutions, Regulatory Status (seo 'bad'); Financial Institutions, Terms of Use, Terms of Business (readability 'bad')
- **Exact supporting evidence:** yoast-seo get-post-seo-data: seo 'bad' on 256, 2140, 2084, 2125, 1273; readability 'bad' on 2171, 1278, 1640.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** SEO (indicator only)
- **Confirmed or needs verification:** Confirmed (scores)
- **Approval required:** You
- **Recommended action:** Do not chase green indicators. Review only where scores point to real content issues.
- **Change risk:** None
- **Notes:** Per your instruction.

### ACC-062: llms.txt not generated

- **Category:** SEO enhancement
- **Affected URL / template / setting:** /llms.txt
- **Exact supporting evidence:** GET returned the theme 404 page.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Optional discoverability
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Optional. Decide later.
- **Change risk:** Low
- **Dependencies:** ACC-060

### ACC-063: Yoast get_head endpoint returned 404 for /claims/

- **Category:** Tool artefact
- **Affected URL / template / setting:** /claims/
- **Exact supporting evidence:** REST get_head returned a 404 head twice; direct GET returned 200 with title 'Insurance Claims Support | Accord Insurance Brokers', canonical self, index.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None for visitors
- **Confirmed or needs verification:** Confirmed (artefact)
- **Approval required:** None
- **Recommended action:** No action. Use direct page fetch for this slug in future tests.
- **Change risk:** None

## 5. Sitemap, indexing and archives

### ACC-070: Insights page is live, indexable, in the sitemap and not in navigation

- **Category:** Indexing / unfinished area
- **Affected URL / template / setting:** /insights/ (page 324)
- **Exact supporting evidence:** HTTP 200, robots index, in page-sitemap (lastmod 2026-06-08T14:34:36+00:00). Not in header menu 47. Loop grid (template 119, 9 per page) shows all four dummy posts. Contains pasted ChatGPT markup (ACC-010). Hero image Accord-Insurance-Insughts.jpg (typo in filename) with alt 'Accord Insurance Insughts'.
- **Priority:** High
- **Status:** Awaiting client information
- **Impact:** SEO, visitor: unfinished area publicly discoverable via sitemap and search
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Client to decide: hold back (noindex, remove from sitemap) until content is supplied, or publish with real content.
- **Change risk:** Low to Medium
- **Dependencies:** ACC-004, ACC-010, ACC-013
- **Verification test after remediation:** Sitemap and robots meta reflect the decision; page reachable only as intended.
- **Notes:** The unfinished area was expected; the public exposure is the actionable part.

### ACC-071: Author and category archives are indexable and in the sitemap

- **Category:** Indexing
- **Affected URL / template / setting:** /author/matthewaccordib-com/, /category/accord/
- **Exact supporting evidence:** author-sitemap and category-sitemap both listed in sitemap_index.xml. Both robots 'index, follow', no description, thin listing of the dummy posts. Author slug is email-derived. /author/ itself returns 404.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO: thin duplicate archives; privacy: email-derived username
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client and you
- **Recommended action:** Set author and category archives to noindex and exclude from sitemap (Yoast settings), or disable the author archive. Settings change reversible.
- **Change risk:** Low
- **Dependencies:** ACC-060, ACC-161
- **Verification test after remediation:** sitemap_index.xml lists only intended sitemaps; archive URLs noindex or redirect.

### ACC-072: Legal and utility pages are all indexable

- **Category:** Indexing
- **Affected URL / template / setting:** Privacy, Cookie, Regulatory Status, Terms of Use, Terms of Business, Complaints, Book a Call, Claims
- **Exact supporting evidence:** All 'index, follow' and in page-sitemap. Legal pages share hero contact-hero.jpeg as og:image.
- **Priority:** Low
- **Status:** Awaiting client information
- **Impact:** SEO (low value pages competing)
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Decide which should be indexed (regulatory status and complaints may be wanted).
- **Change risk:** Low
- **Dependencies:** ACC-053
- **Verification test after remediation:** Indexing matches decision.

### ACC-073: Sitemap composition matches published pages; redirects and special URLs behave

- **Category:** Indexing
- **Affected URL / template / setting:** sitemap_index.xml, page-sitemap.xml, wp-sitemap.xml, sitemap.xml, robots.txt, search, 404, attachments
- **Exact supporting evidence:** page-sitemap lists exactly the 19 published pages; wp-sitemap.xml and sitemap.xml redirect once to sitemap_index.xml; robots.txt allows all and points to sitemap_index.xml; search and 404 are noindex,follow; attachment pages redirect to the file; ?p=448 and ?page_id=426 redirect once to canonical URLs; http and www redirect once to the https apex.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None
- **Recommended action:** No action.
- **Change risk:** None
- **Notes:** X-Robots-Tag noindex on robots.txt and sitemap XML is normal Yoast behaviour.

## 6. Elementor templates and design consistency

### ACC-080: Hero colour differs per page from one shared hero template

- **Category:** Design consistency
- **Affected URL / template / setting:** Template 1787 'Global - Hero Option 1 (Variable Colour)'
- **Exact supporting evidence:** Per-page overrides: #2E2E2E (Financial Institutions), #042705 (About), #153130 (Claims); home uses #0B203B (Accord Dark Blue). Kit holds Accord Dark Blue #0B203B and Accord Dark Green #042705; #2E2E2E and #153130 are not Accord globals.
- **Priority:** Low
- **Status:** Awaiting client information
- **Impact:** Design consistency
- **Confirmed or needs verification:** Needs verification (template name suggests variable colour is intended)
- **Approval required:** Client
- **Recommended action:** Confirm intended colour per page; map to global brand colours.
- **Change risk:** Low
- **Dependencies:** ACC-081
- **Verification test after remediation:** Hero colours match the approved scheme.

### ACC-081: Global palette mixes Vamtam demo colours with the Accord brand; hard-coded colours on pages

- **Category:** Design system
- **Affected URL / template / setting:** Elementor kit 10
- **Exact supporting evidence:** System colours #2E2E2E, #FFFBE7, #F6F5F2, #92C200 (link hover), #7E7E7E from Vamtam; custom Accord Dark Blue #0B203B, Accord Dark Green #042705. Hard-coded #B4E717 and #415B76 appear on pages. Typography is Work Sans plus Poppins for 'Body Link' only.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Design consistency, maintainability
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Client (brand)
- **Recommended action:** Document the approved brand palette; replace Vamtam system colours on staging and re-map widget references.
- **Change risk:** Medium
- **Dependencies:** ACC-018
- **Verification test after remediation:** Visual regression across all templates shows no unintended colour change.

### ACC-082: Legal Pages template condition lists a page that does not exist

- **Category:** Theme Builder
- **Affected URL / template / setting:** Template 1239 'Accord Legal Pages'
- **Exact supporting evidence:** Display conditions include page IDs 1245, 1249, 1273, 2862, 1642, 1640, 1278. Page 1249 does not exist. Complianz option for the custom cookie page also points to 1249 (real cookie page is 2862).
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Maintenance
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Remove the stale ID on staging.
- **Change risk:** Low
- **Dependencies:** ACC-183
- **Verification test after remediation:** All six legal pages still use the template.

### ACC-083: Book a Call is implemented two ways

- **Category:** Conversion consistency
- **Affected URL / template / setting:** Header 125; popup 2804 'Book a Call'; /book-a-call/ (2792)
- **Exact supporting evidence:** Desktop header and in-page buttons open popup 2804. Tablet/mobile header button links to /book-a-call/. Popup has no stored display conditions or trigger settings found; display settings not read. Popup holds a HubSpot Meetings embed with unquoted attributes.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Conversion consistency
- **Confirmed or needs verification:** Confirmed (behaviour); intent unknown
- **Approval required:** Client
- **Recommended action:** Choose one pattern for all devices.
- **Change risk:** Low
- **Dependencies:** ACC-002, ACC-180
- **Verification test after remediation:** Same behaviour on desktop and mobile.

### ACC-084: Search Results template carries placeholder headings

- **Category:** Template content
- **Affected URL / template / setting:** Template 70 'Search Results'
- **Exact supporting evidence:** Two 'Add Your Heading Text Here' placeholders; search pages are noindex,follow.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Visitor on empty or edge searches
- **Confirmed or needs verification:** Needs verification (when shown)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Replace placeholders on staging.
- **Change risk:** Low
- **Dependencies:** ACC-019
- **Verification test after remediation:** Search for a nonsense term and a valid term; no placeholder text.

### ACC-085: Atomic (V4) editor experiments are active with mixed widget generations

- **Category:** Platform / maintenance
- **Affected URL / template / setting:** Elementor experiments
- **Exact supporting evidence:** e_atomic_elements, e_classes, e_components, e_opt_in_v4, e_variables, container, mega-menu, nested-elements all 'active'; e-image widgets on home and 2916; global classes empty; Elementor usage tracking on.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance risk during Elementor updates
- **Confirmed or needs verification:** Confirmed (settings)
- **Approval required:** You
- **Recommended action:** Note for regression testing; no action.
- **Change risk:** Low
- **Dependencies:** ACC-160

### ACC-086: Child theme is effectively empty

- **Category:** Maintenance
- **Affected URL / template / setting:** Theme accord-insurance 1.0.0
- **Exact supporting evidence:** Files: README.txt, functions.php (592 B, enqueues style.css), style.css (692 B header only), accord-insurance.min.css (0 bytes), screenshot.png (650 KB). Kit has no custom CSS.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Maintenance
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Decide where site-specific CSS should live. No action now.
- **Change risk:** None

## 7. Responsive layout

### ACC-100: Responsive rendering was not inspected visually

- **Category:** Inspection gap
- **Affected URL / template / setting:** All pages, tablet and mobile
- **Exact supporting evidence:** No browser or screenshot access in this phase. Breakpoints: tablet 1025, mobile 768; no widescreen. Header uses separate desktop and tablet/mobile containers. Lazy images omit width/height.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Visitor
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (access to a browser capture)
- **Recommended action:** Run a visual QA at 1440, 1025, 768 and 390px on staging for all 19 pages and the popup.
- **Change risk:** None
- **Verification test after remediation:** Screenshot set reviewed.

### ACC-101: Footer legal text is set at 11px

- **Category:** Responsive / readability
- **Affected URL / template / setting:** Footer template 108
- **Exact supporting evidence:** Copyright and regulatory block font size 11px (config agent).
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Readability, accessibility
- **Confirmed or needs verification:** Needs verification (contrast and mobile size not measured)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Check legibility and contrast on mobile; increase if needed.
- **Change risk:** Low
- **Dependencies:** ACC-100
- **Verification test after remediation:** Passes contrast and minimum size review.

## 8. Images and media

### ACC-110: Most media have empty alt text; informative images must be classified before any change

- **Category:** Alt text
- **Affected URL / template / setting:** Media library (95 of 96 images with empty alt); Elementor widgets
- **Exact supporting evidence:** Only the logo SVG (701) has alt. Media agent identified 16 informative-looking images with empty alt on 5 pages (home 2417; sectors 2614, 2556, 2561, 2603, 2602; commercial 2533; solutions 2755, 2743, 2742, 2741, 2744, 2745, 2750; bridging 2513, 2510). Body agent A judged many card/body images decorative. Team headshots 2255, 2256, 2257, 2368 empty in library; widget alt unverified.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Accessibility, SEO
- **Confirmed or needs verification:** Needs verification (purpose classification required)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Classify each image (informative vs decorative) with the client where needed. Leave decorative images blank. Write specific alt only for informative ones, especially team photos.
- **Change risk:** Low
- **Dependencies:** ACC-121
- **Verification test after remediation:** Alt audit table matches classification; decorative remain alt="".
- **Notes:** Empty alt is valid for decorative images; not assumed wrong.

### ACC-111: Weak or placeholder-grade alt text on specific images

- **Category:** Alt text
- **Affected URL / template / setting:** Commodities hero; legal page heroes; dummy post featured images; Insights hero; Sectors hero
- **Exact supporting evidence:** Commodities hero alt and title '1'; five legal heroes alt 'contact hero'; post featured alts 'contact hero', 'hero2', '3'; Insights alt 'Accord Insurance Insughts' (typo); Sectors hero alt/title 'Accord insurance limited'; Bridging hero 'Bridging Lenders accord'.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Accessibility, SEO
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Replace with descriptive alt if informative, or blank if decorative (hero backgrounds are likely decorative).
- **Change risk:** Low
- **Dependencies:** ACC-110
- **Verification test after remediation:** Alt values reviewed by classification.

### ACC-112: Non-descriptive filenames and typos in filenames

- **Category:** Media hygiene
- **Affected URL / template / setting:** 1.jpg, 2.jpg, 3.jpg, 9-1.jpg, 1-1.jpg, hero-scaled.jpg, hero2-scaled.jpg, London.jpg, 47f24040-...-scaled.jpg, Accor-insurance-commercial-insurance.jpg, Accord-Insurance-Insughts.jpg
- **Exact supporting evidence:** Examples from the media agent and sitemap image lists; typos 'Accor' and 'Insughts'.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** SEO (minor), maintainability
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Do not rename live files (breaks URLs). Improve titles/alt now; use clean names for new uploads.
- **Change risk:** High if renamed
- **Verification test after remediation:** No broken image URLs after any change.

### ACC-113: Site icon is a 584 KB JPEG at 514x512

- **Category:** Image optimisation
- **Affected URL / template / setting:** Attachment 705 Accord-favicon.jpg; option site_icon
- **Exact supporting evidence:** JPEG, 514x512, 584,126 bytes.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Performance, correctness
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Supply a square PNG/ICO at 512px optimised; set as site icon.
- **Change risk:** Low
- **Verification test after remediation:** Favicon appears in tab and search result; file under 50 KB.

### ACC-114: Oversize images and videos

- **Category:** Performance / media
- **Affected URL / template / setting:** Images 956, 1590, 2554, 1585; videos 2233, 2969, 3066
- **Exact supporting evidence:** 956 47f24040-...-scaled.jpg 554,422 B 2560x1440; 1590 hero-scaled.jpg 299,615 B; 2554 295,760 B; 1585 283,161 B. Videos: 2233 32.9 MB (likely unused), 2969 8.2 MB (likely unused), 3066 8.3 MB (home hero in use). All raster images JPEG/PNG, no WebP/AVIF seen.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Performance
- **Confirmed or needs verification:** Needs verification (usage incomplete)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Confirm usage, then compress or replace; consider WebP; trim unused videos only after confirming zero references.
- **Change risk:** Medium
- **Dependencies:** ACC-121
- **Verification test after remediation:** Page weights and LCP improve; no missing media.

### ACC-115: Duplicate or orphan media candidates

- **Category:** Media hygiene
- **Affected URL / template / setting:** 3094, 3070, 2987, 2956, 2859, 2858, 2805, 2413, 2381, 2357, 2265, 741, 459, 458, 2677, 740, 2746
- **Exact supporting evidence:** Candidates only (usage mapped for 5 pages). Examples: 2413 duplicates 2417 name; 2746 and 2750 same size 28,842 B; 2677 and 740 are Elementor screenshot artefacts; 2987 BIBA-logo.png is 1920x1080 for a logo; 2381 placeholder.png.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Do not delete until a full usage scan is complete and the client agrees.
- **Change risk:** Medium
- **Dependencies:** ACC-121
- **Verification test after remediation:** Zero references before any removal.

### ACC-116: One stock hero image reused across legal pages and as social image

- **Category:** Media reuse
- **Affected URL / template / setting:** contact-hero.jpeg (784)
- **Exact supporting evidence:** Hero on privacy, regulatory status, Terms of Use, Terms of Business and complaints; og:image on those pages and post 1302; fallback featured image in template 82. 2048x1366, 223,390 B.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Design, SEO
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Optional: give legal pages their own or no hero.
- **Change risk:** Low

### ACC-117: Footer logo Asset-2.svg has empty alt

- **Category:** Alt text
- **Affected URL / template / setting:** Footer template 108, attachment 741
- **Exact supporting evidence:** Logo image alt="" next to text; a second near-identical SVG 701 is the header logo with alt 'Accord Insurance Brokers logo'.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Accessibility
- **Confirmed or needs verification:** Needs verification (informative or decorative?)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Decide: decorative duplicate (leave blank) or informative (alt = company name).
- **Change risk:** Low
- **Dependencies:** ACC-110

### ACC-118: Image-to-page usage mapping is incomplete

- **Category:** Inspection gap
- **Affected URL / template / setting:** Pages 2084, 2171, 412, 387, 2027, 2916, 324, 2792, six legal pages; templates 125, 108, 2804, 1679, 1689, 1700, 1709, 1716, 1727, 1776, 1787, 1830, 2373, 82, 66, 70, 80, 1239, 2649
- **Exact supporting evidence:** Media agent read full Elementor data for 5 pages only. Body agents recorded images for the others. The consolidated 100-row CSV marks upload-parent usage as inferred.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Completeness of the image inventory
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (access to full-fetch tooling)
- **Recommended action:** Run a one-page-at-a-time Elementor JSON scan and regex image ids.
- **Change risk:** None
- **Verification test after remediation:** Inventory CSV with verified usage for all rows.
- **Notes:** CSV: scratchpad media/image_inventory.csv (library metadata complete).

### ACC-119: Yoast default social image not set

- **Category:** Metadata
- **Affected URL / template / setting:** wpseo_social
- **Exact supporting evidence:** Media agent reported og_default_image, og_default_image_id and og_frontpage_image empty. Not independently verified.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Social sharing
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Verify in Yoast settings; set a default.
- **Change risk:** Low
- **Dependencies:** ACC-060

## 9. Accessibility

### ACC-130: Header desktop and mobile duplicates both present in HTML

- **Category:** Hidden duplicate content
- **Affected URL / template / setting:** Header template 125, containers 4d1f8e33 (desktop) and 52fea39 (tablet/mobile)
- **Exact supporting evidence:** Each holds the logo (alt 'Accord Insurance Brokers logo'), nav menu and Book a Call button; nav list markup appears four times in the header. Hidden by Elementor responsive classes (elementor-hidden-*). Only spacers elsewhere carry hidden classes; no duplicated body text found.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Accessibility, crawlers
- **Confirmed or needs verification:** Needs verification (computed display:none not tested)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Confirm with a browser accessibility tree that hidden copies are excluded; if not, restructure to a single responsive header.
- **Change risk:** Medium (header is global)
- **Dependencies:** ACC-100
- **Verification test after remediation:** Accessibility tree contains one navigation per viewport.

### ACC-131: Autoplay hero video without pause control, captions or accessible name; two 8.3 MB references

- **Category:** Accessibility / performance
- **Affected URL / template / setting:** Home hero, video widgets 25b7e71 (hidden mobile) and a0db8c6 (hidden desktop/tablet)
- **Exact supporting evidence:** Accord-Insurance-Brokers.mp4, 8,330,239 bytes; autoplay muted playsinline; lazyload data-src; no caption track; no accessible name. Both widgets in markup, one hidden per breakpoint.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Accessibility (moving content), performance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Add pause control and accessible label; confirm only one file downloads per device.
- **Change risk:** Medium
- **Dependencies:** ACC-114
- **Verification test after remediation:** Network log shows one video request; keyboard can pause.

### ACC-132: Repeated and weak link text

- **Category:** Accessibility
- **Affected URL / template / setting:** /sectors/ (four 'Read more'), 'Get in touch' buttons, 'Speak to a broker' buttons
- **Exact supporting evidence:** Four identical 'Read more' buttons; SVG <style> rules appear inside link text on buttons with icons.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Accessibility
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Add distinct accessible names (aria-label or visible text) per card.
- **Change risk:** Low
- **Verification test after remediation:** Link list in screen reader shows distinct names.

### ACC-133: Duplicate HTML ids

- **Category:** Accessibility / validity
- **Affected URL / template / setting:** /sectors/financial-institutions/ (id Layer_1 x14); /insurance-for-bridging-lenders/ (hero image id 2956 / data-id 589d177 reused); home hero img id 2417 on lazy and noscript copies
- **Exact supporting evidence:** As reported by body agent A.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Validity
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Make SVG ids unique.
- **Change risk:** Low
- **Verification test after remediation:** HTML validator reports no duplicate ids.

### ACC-134: Colour contrast, focus order and form accessibility not tested

- **Category:** Inspection gap
- **Affected URL / template / setting:** Sitewide
- **Exact supporting evidence:** No browser-based audit performed. Skip link present and lang='en-GB' (positive).
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Accessibility
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (access)
- **Recommended action:** Run axe/Lighthouse and keyboard tests on staging.
- **Change risk:** None
- **Dependencies:** ACC-100
- **Verification test after remediation:** Report with zero critical issues.

### ACC-135: Form field labelling oddities

- **Category:** Accessibility / forms
- **Affected URL / template / setting:** /contact-us/ form 59a67030
- **Exact supporting evidence:** 'Company name' field has custom id email_get_in_touch; Name and Company fields have no field type set.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Accessibility, data quality
- **Confirmed or needs verification:** Needs verification
- **Approval required:** None beyond normal change approval
- **Recommended action:** Correct ids and types on staging.
- **Change risk:** Low
- **Dependencies:** ACC-001
- **Verification test after remediation:** Fields announce correct labels and types.

## 10. Forms and conversion paths

### ACC-140: Contact form has no consent or privacy notice, no spam control, default success message

- **Category:** Forms
- **Affected URL / template / setting:** /contact-us/ form 59a67030
- **Exact supporting evidence:** Fields Name, Company name, Email, Phone, Your message (all required). No consent checkbox or privacy link, no honeypot or reCAPTCHA/hCaptcha/Turnstile, no redirect or webhook, Elementor default success text. Submissions DB storage not confirmed.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Compliance, spam, data handling
- **Confirmed or needs verification:** Confirmed (settings)
- **Approval required:** Legal/compliance and client
- **Recommended action:** Add an approved privacy notice or consent line and spam protection; confirm submission storage.
- **Change risk:** Medium
- **Dependencies:** ACC-001, ACC-183
- **Verification test after remediation:** Test submission (approved) passes validation, shows notice, reaches the mailbox.

### ACC-141: Contact form subject and sender name contain a typo

- **Category:** Forms / typo
- **Affected URL / template / setting:** /contact-us/ form 59a67030
- **Exact supporting evidence:** Subject and from-name: 'New message from "Accord Insurance Borkers"'.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Brand, deliverability
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Correct 'Borkers' to 'Brokers'.
- **Change risk:** Low
- **Dependencies:** ACC-001
- **Verification test after remediation:** Received test email shows the corrected text.

### ACC-143: 'Review Policy' button on the bridging lenders page points to /sectors/

- **Category:** Broken or misleading link
- **Affected URL / template / setting:** /insurance-for-bridging-lenders/
- **Exact supporting evidence:** Button label 'Review Policy' links to https://accordib.com/sectors/.
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** Conversion
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Client
- **Recommended action:** Client to confirm intended destination; relabel or relink.
- **Change risk:** Low
- **Dependencies:** ACC-055
- **Verification test after remediation:** Button label and destination agree.

### ACC-144: Sector links omit the trailing slash and cause a redirect

- **Category:** Links
- **Affected URL / template / setting:** Template 1709 buttons and /sectors/ 'Read more' buttons
- **Exact supporting evidence:** /sectors/commercial-insurance and /sectors/commodities-trade-finance return 200 after 1 redirect.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Performance (minor), crawl
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Update link targets to canonical trailing-slash URLs.
- **Change risk:** Low
- **Verification test after remediation:** Links return 200 with 0 redirects.

### ACC-145: Joinchat WhatsApp widget configuration

- **Category:** Conversion / privacy
- **Affected URL / template / setting:** Joinchat settings
- **Exact supporting evidence:** Number ends 392, right position, button delay 3, message_delay 10, message_text empty, optin_check no, tracking yes, visible on all pages.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Conversion, privacy
- **Confirmed or needs verification:** Confirmed (settings)
- **Approval required:** Client (number, message)
- **Recommended action:** Confirm the number is the intended business line and decide on the opt-in.
- **Change risk:** Low
- **Dependencies:** ACC-185
- **Verification test after remediation:** Chat opens the intended number with the agreed message.

## 11. Performance and technical health

### ACC-150: Performance not measured; console errors and network failures not captured

- **Category:** Inspection gap
- **Affected URL / template / setting:** Sitewide
- **Exact supporting evidence:** No browser or Lighthouse in this phase. Static checks: HEAD on sampled uploads all 200; no http:// mixed content except the FOS link text; combined CSS via SG Optimizer; fonts from fonts.googleapis.com.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Performance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (access)
- **Recommended action:** Capture Lighthouse/CWV and console logs for key pages on staging.
- **Change risk:** None
- **Dependencies:** ACC-100
- **Verification test after remediation:** Baseline report stored for comparison.

### ACC-151: Lazy images omit width and height; high fetch priority on a below-fold card

- **Category:** Performance
- **Affected URL / template / setting:** Most pages (lazysizes markup); /sectors/ card image 2556
- **Exact supporting evidence:** Lazy <img> has a 1x1 GIF src, no width/height; noscript copy has them. fetchpriority=high on a below-fold card.
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Layout shift, LCP
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None beyond normal change approval
- **Recommended action:** Set intrinsic dimensions and prioritise only the LCP image.
- **Change risk:** Low
- **Dependencies:** ACC-150
- **Verification test after remediation:** CLS and LCP improve in Lighthouse.

### ACC-152: PHP error log shows cron save failures and old fatal errors

- **Category:** Technical health
- **Affected URL / template / setting:** php_errorlog
- **Exact supporting evidence:** 'cron event list could not be saved' for action_scheduler_run_queue, cmplz_every_five_minutes_hook and delete_expired_transients (29 Jun, 17 Aug, 7-15 Sep); Elementor cloud-library 403 fatal on 10 Jun; sg_ai_studio invalid_schedule 21 Jun; repeated SG auto-login lines. No overdue cron events.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Reliability
- **Confirmed or needs verification:** Needs verification (history, may be resolved)
- **Approval required:** None beyond normal change approval
- **Recommended action:** Review with hosting after Elementor update; confirm cron health.
- **Change risk:** Low
- **Dependencies:** ACC-160
- **Verification test after remediation:** No new entries over 7 days.

### ACC-153: Cache drop-ins and detection mismatch

- **Category:** Technical health
- **Affected URL / template / setting:** wp-content
- **Exact supporting evidence:** advanced-cache.php, object-cache.php (12,532 B), sgo-config.php, stray object-cache-socket-missing.php (same size), upgrade-temp-backup/; wp_cache_get_provider returns 'none' although SG caching headers are present.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Maintenance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Hosting
- **Recommended action:** Ask hosting whether the stray file and upgrade backup can be cleaned.
- **Change risk:** Low

### ACC-154: Redirect behaviour is clean on core URLs

- **Category:** Redirects
- **Affected URL / template / setting:** http, www, sitemaps, ?p= and ?page_id= URLs
- **Exact supporting evidence:** Each redirects once to the canonical URL; no loops.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None
- **Recommended action:** No action.
- **Change risk:** None

## 12. WordPress maintenance and security

### ACC-160: Elementor Pro 4.3.0 has an update available (4.3.1)

- **Category:** Maintenance
- **Affected URL / template / setting:** Plugin elementor-pro/elementor-pro.php
- **Exact supporting evidence:** wp_list_plugins: version 4.3.0, update_available true, new_version 4.3.1; Site Health flags it as recommended. Elementor 4.3.3 and all other plugins current; WP 7.1.2, PHP 8.2.34.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Maintenance, security
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You and client (maintenance window)
- **Recommended action:** Do not update live. Take full backup, test on staging, run regression tests, then update in a window.
- **Change risk:** Medium to High (page builder)
- **Dependencies:** ACC-190, ACC-191
- **Verification test after remediation:** Staging regression passes; live post-update crawl matches baseline.
- **Notes:** Per your instruction recorded as a controlled maintenance task.

### ACC-161: Public REST API exposes user accounts

- **Category:** Security / privacy
- **Affected URL / template / setting:** /wp-json/wp/v2/users
- **Exact supporting evidence:** HTTP 200, X-WP-Total 3. Two administrators have a full email address as display name and an email-derived slug; user 4 slug 'matthewaccordib-com'. Gravatar hashes exposed. Reported by three agents.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Security: username and email disclosure
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Restrict the endpoint for logged-out users and set safe display names/nicenames. Use the security plugin if it supports it.
- **Change risk:** Low to Medium
- **Dependencies:** ACC-071
- **Verification test after remediation:** Logged-out GET returns 401/403 or no users; author URLs not email-derived.
- **Notes:** Emails are not reproduced here.

### ACC-162: Cowboy MCP plugin with write, file and SQL tools is active in production; 4 administrators including a personal account

- **Category:** Security / access
- **Affected URL / template / setting:** Plugin cowboy-mcp 1.6.9; users
- **Exact supporting evidence:** Plugin exposes tools including wp_write_file, wp_cli, raw SQL; safe mode on. 4 users, all administrators (2 agency, 1 personal gmail-domain, 1 client).
- **Priority:** Medium
- **Status:** Awaiting client information
- **Impact:** Security
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You and client
- **Recommended action:** Keep only for the remediation window; review admin accounts and remove unneeded access.
- **Change risk:** Low
- **Dependencies:** ACC-005
- **Verification test after remediation:** Plugin deactivated after remediation; admin list reviewed.

### ACC-163: Security headers missing on front-end pages

- **Category:** Security
- **Affected URL / template / setting:** Front-end responses
- **Exact supporting evidence:** Home/robots responses show only x-content-type-options and x-xss-protection. No HSTS, CSP, X-Frame-Options, Referrer-Policy or Permissions-Policy (present on wp-login only).
- **Priority:** Low
- **Status:** Confirmed — awaiting approval
- **Impact:** Security hardening
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Hosting/you
- **Recommended action:** Add headers via hosting; start with HSTS, Referrer-Policy, Permissions-Policy; test CSP carefully (Elementor, HubSpot).
- **Change risk:** Medium
- **Verification test after remediation:** securityheaders scan; site still functions.

### ACC-164: No post revisions; remediation needs an external backup

- **Category:** Safety
- **Affected URL / template / setting:** Database
- **Exact supporting evidence:** Revisions 0; auto-draft 1. No content history to roll back to.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Change safety
- **Confirmed or needs verification:** Confirmed
- **Approval required:** You
- **Recommended action:** Take full backup and use staging before any edits.
- **Change risk:** None
- **Dependencies:** ACC-190
- **Verification test after remediation:** Backup restore tested.
- **Notes:** Cowboy checkpoints are not a substitute.

### ACC-165: SVG upload settings

- **Category:** Security
- **Affected URL / template / setting:** Safe SVG 2.5.1; Elementor unfiltered_files_upload=1
- **Exact supporting evidence:** Both active.
- **Priority:** Low
- **Status:** Needs verification
- **Impact:** Security
- **Confirmed or needs verification:** Confirmed (settings)
- **Approval required:** You
- **Recommended action:** Review whether unfiltered uploads are still needed alongside Safe SVG.
- **Change risk:** Low

### ACC-166: Activity logging and security plugins present

- **Category:** Security
- **Affected URL / template / setting:** Stream 4.4.0, SG Security 1.6.8
- **Exact supporting evidence:** Active. xmlrpc.php returns 403.
- **Priority:** Low
- **Status:** Not an issue
- **Impact:** None
- **Confirmed or needs verification:** Confirmed
- **Approval required:** None
- **Recommended action:** No action.
- **Change risk:** None

## 13. Privacy and cookies

### ACC-180: HubSpot Meetings embed loads without consent gating

- **Category:** Privacy / cookies
- **Affected URL / template / setting:** /contact-us/, /book-a-call/, popup 2804
- **Exact supporting evidence:** HTML widget: data-src=https://meetings-eu1.hubspot.com/mwaterson?embed=true and script static.hsappstatic.net/MeetingsEmbed/ex/MeetingsEmbedCode.js (unquoted attributes). Complianz block_hubspot_service='no'. Banner behaviour not observed.
- **Priority:** Medium
- **Status:** Awaiting legal/compliance approval
- **Impact:** Privacy compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Compliance to decide; then gate the embed behind consent or add to Complianz blocking.
- **Change risk:** Medium
- **Dependencies:** ACC-182
- **Verification test after remediation:** Network log before consent shows no HubSpot requests.
- **Notes:** No legal judgement made.

### ACC-181: Google Fonts load from Google servers despite a self-host setting

- **Category:** Privacy / performance
- **Affected URL / template / setting:** Head on all pages; Complianz setting
- **Exact supporting evidence:** Work Sans and Poppins from fonts.googleapis.com; Complianz self_host_google_fonts='self-host'.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Privacy, performance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance
- **Recommended action:** Self-host fonts or confirm the consent treatment.
- **Change risk:** Low
- **Dependencies:** ACC-182
- **Verification test after remediation:** No requests to fonts.googleapis.com or fonts.gstatic.com.

### ACC-182: Complianz configuration incomplete or inconsistent

- **Category:** Privacy / cookies
- **Affected URL / template / setting:** Complianz settings
- **Exact supporting evidence:** Region uk only; cookie blocker 'not-set'; consent type not set; consent mode no; statistics 'google-analytics' declared but ua/gtm/aw codes empty; cookie scan 2026-10-02 detected google-analytics and google-fonts; services declared: google-fonts, vimeo, google-maps, google-recaptcha (blocking no).
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Privacy compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** Legal/compliance and client
- **Recommended action:** Reconcile with what the site actually loads; no analytics ID is configured in Complianz or visible HTML.
- **Change risk:** Medium
- **Dependencies:** ACC-180, ACC-181
- **Verification test after remediation:** Consent test across browsers; declarations match actual cookies.

### ACC-183: Cookie statement points to a non-existent page

- **Category:** Privacy / cookies
- **Affected URL / template / setting:** Complianz cmplz_cookie-statement_custom_page; /cookie-policy-uk/ (2862)
- **Exact supporting evidence:** Setting points to page 1249 (does not exist); the live cookie page 2862 uses [cmplz-document type="cookie-statement" region="uk"]. Privacy statement is custom (page 1245).
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Privacy compliance, link integrity
- **Confirmed or needs verification:** Confirmed
- **Approval required:** Legal/compliance
- **Recommended action:** Point the setting at page 2862 or regenerate; keep one cookie policy page.
- **Change risk:** Low
- **Dependencies:** ACC-082
- **Verification test after remediation:** Banner 'Cookie Policy' link opens /cookie-policy-uk/.

### ACC-184: Cookie Policy text includes irrelevant boilerplate and services not evidently used

- **Category:** Privacy wording
- **Affected URL / template / setting:** /cookie-policy-uk/
- **Exact supporting evidence:** Mentions 'items remain in your shopping cart until you have paid' and embedded content from WhatsApp, LinkedIn, X, Facebook and Instagram; only a link-less LinkedIn icon and the Joinchat plugin were seen.
- **Priority:** Low
- **Status:** Awaiting legal/compliance approval
- **Impact:** Privacy wording
- **Confirmed or needs verification:** Confirmed (quotes)
- **Approval required:** Legal/compliance
- **Recommended action:** Revisit Complianz wizard answers so generated text matches the site.
- **Change risk:** Low
- **Dependencies:** ACC-182
- **Verification test after remediation:** Policy matches actual services.

### ACC-185: Joinchat has no consent opt-in and tracking enabled

- **Category:** Privacy
- **Affected URL / template / setting:** Joinchat settings
- **Exact supporting evidence:** optin_check no; tracking yes.
- **Priority:** Low
- **Status:** Awaiting legal/compliance approval
- **Impact:** Privacy
- **Confirmed or needs verification:** Confirmed (settings)
- **Approval required:** Legal/compliance
- **Recommended action:** Decide on opt-in and tracking.
- **Change risk:** Low
- **Dependencies:** ACC-145

### ACC-186: Cookie banner markup and pre-consent scripts not observed

- **Category:** Inspection gap
- **Affected URL / template / setting:** All pages
- **Exact supporting evidence:** Full HTML was truncated at about 51,200 characters, so wp_footer output and the banner were not seen.
- **Priority:** Medium
- **Status:** Needs verification
- **Impact:** Privacy compliance
- **Confirmed or needs verification:** Needs verification
- **Approval required:** You (browser access)
- **Recommended action:** Capture with a browser: first-visit requests before consent.
- **Change risk:** None
- **Dependencies:** ACC-180
- **Verification test after remediation:** Documented request log.

## 14. Final regression testing

### ACC-190: Pre-remediation baseline and staging

- **Category:** Regression
- **Affected URL / template / setting:** Whole site
- **Exact supporting evidence:** Revisions 0; live site; Elementor Pro update pending.
- **Priority:** High
- **Status:** Confirmed — awaiting approval
- **Impact:** Change safety
- **Confirmed or needs verification:** Task
- **Approval required:** You
- **Recommended action:** Full backup (database and uploads), staging clone, baseline crawl: status, titles, descriptions, canonicals, robots, H1, images, forms.
- **Change risk:** None
- **Verification test after remediation:** Baseline file stored.

### ACC-191: Post-batch regression checklist

- **Category:** Regression
- **Affected URL / template / setting:** All 19 pages, 4 posts, archives, popup, 404, search
- **Priority:** High
- **Status:** Confirmed — awaiting approval
- **Impact:** Change safety
- **Confirmed or needs verification:** Task
- **Approval required:** You
- **Recommended action:** After each batch: crawl for 200/301/404, one H1, meta and canonical, sitemap diff, link check, image check, console check, form test (approved), cookie banner test, desktop/tablet/mobile visual review, schema validation.
- **Change risk:** None
- **Dependencies:** ACC-190
- **Verification test after remediation:** Checklist signed off per batch.

### ACC-192: Search Console and indexing follow-up

- **Category:** Regression
- **Affected URL / template / setting:** Google Search Console
- **Exact supporting evidence:** Google site verification tag present on home.
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** SEO
- **Confirmed or needs verification:** Task
- **Approval required:** Client
- **Recommended action:** After indexing changes, resubmit sitemap and inspect key URLs.
- **Change risk:** None
- **Dependencies:** ACC-004, ACC-071
- **Verification test after remediation:** Index coverage matches intent.

### ACC-193: Repeat this audit against the baseline

- **Category:** Regression
- **Affected URL / template / setting:** Whole site
- **Priority:** Medium
- **Status:** Confirmed — awaiting approval
- **Impact:** Assurance
- **Confirmed or needs verification:** Task
- **Approval required:** You
- **Recommended action:** Re-run the inventory after the last batch and compare to the original findings.
- **Change risk:** None
- **Dependencies:** ACC-191
- **Verification test after remediation:** All findings Verified complete or Intentionally retained.

## 15. Client-facing improvements summary

### ACC-200: Client summary: enquiries and contact details

- **Category:** Summary
- **Affected URL / template / setting:** ACC-001, ACC-002, ACC-032, ACC-033, ACC-140, ACC-141
- **Exact supporting evidence:** Roll-up of contact and form fixes.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Visitor conversion
- **Confirmed or needs verification:** Roll-up
- **Approval required:** Client
- **Recommended action:** Write the client-facing statement once these are fixed.
- **Change risk:** None
- **Dependencies:** ACC-001

### ACC-201: Client summary: legal and regulatory accuracy

- **Category:** Summary
- **Affected URL / template / setting:** ACC-003, ACC-030 to ACC-042
- **Exact supporting evidence:** Roll-up of legal and company consistency.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Compliance
- **Confirmed or needs verification:** Roll-up
- **Approval required:** Client
- **Recommended action:** Write once approved wording is live.
- **Change risk:** None
- **Dependencies:** ACC-003

### ACC-202: Client summary: search visibility and clean indexing

- **Category:** Summary
- **Affected URL / template / setting:** ACC-004, ACC-050 to ACC-058, ACC-070 to ACC-072
- **Exact supporting evidence:** Roll-up of SEO fixes.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** SEO
- **Confirmed or needs verification:** Roll-up
- **Approval required:** Client
- **Recommended action:** Write once done.
- **Change risk:** None
- **Dependencies:** ACC-050

### ACC-203: Client summary: accessibility, images and speed

- **Category:** Summary
- **Affected URL / template / setting:** ACC-110 to ACC-119, ACC-130 to ACC-135, ACC-150, ACC-151
- **Exact supporting evidence:** Roll-up.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Accessibility, performance
- **Confirmed or needs verification:** Roll-up
- **Approval required:** Client
- **Recommended action:** Write once done.
- **Change risk:** None
- **Dependencies:** ACC-110

### ACC-204: Client summary: privacy, security and upkeep

- **Category:** Summary
- **Affected URL / template / setting:** ACC-160 to ACC-164, ACC-180 to ACC-185
- **Exact supporting evidence:** Roll-up.
- **Priority:** Enhancement
- **Status:** Deferred
- **Impact:** Security, compliance
- **Confirmed or needs verification:** Roll-up
- **Approval required:** Client
- **Recommended action:** Write once done.
- **Change risk:** None
- **Dependencies:** ACC-160
