# -*- coding: utf-8 -*-
"""Large FAQ bank for JB Software Solutions (indexed topic pages + FAQPage schema)."""

BRAND = "JB Software Solutions"
EMAIL = "info@jbsoftwaresolutions.com"


def _topics():
    """Return list of {slug, title, desc, qs: [(q,a), ...]} with 180+ Q&As."""
    topics = []

    def add(slug, title, desc, pairs):
        topics.append({"slug": slug, "title": title, "desc": desc, "qs": pairs})

    # --- Website / web app ---
    add(
        "website-development-cost-india",
        "Website development cost in India",
        "What business website development costs in India, what is included, and what changes the quote.",
        [
            ("How much does website development cost in India?", f"At {BRAND}, business website development often starts from ₹50,000 for a focused multi-page site. Custom web apps and e-commerce cost more."),
            ("What is included in a website development package?", "Page structure, mobile-friendly layout, contact form, basic SEO setup, speed checks and a launch checklist."),
            ("How long does a business website take?", "Many 5 to 12 page sites finish in 2 to 6 weeks once content and approvals are ready."),
            ("Do you build SEO-friendly websites?", "Yes. Clean URLs, sitemap, schema where useful, and pages written for buyer questions, not just decoration."),
            ("Can you redesign my existing website?", "Yes. We audit speed, clarity and enquiry flow, then rebuild or improve without throwing away what already works."),
            ("Is WordPress okay for a business website?", "Sometimes. We recommend WordPress when your team needs frequent editorial updates. For product-heavy sites we often prefer a modern web stack."),
            ("Do you write website content?", "We can guide structure and headlines. Final business claims and legal copy stay with you unless content is scoped in."),
            ("What pages should a service business website include?", "Home, services, about, proof or process, FAQ, pricing guidance if you can share it, and contact."),
            ("Will my website work on phones?", "Yes. Mobile layout is part of every website development project."),
            ("Do you provide hosting?", "We can recommend and set up hosting. You keep ownership of the domain and accounts."),
            ("What is the difference between a website and a landing page?", "A website covers multiple offers and trust pages. A landing page focuses on one campaign or offer."),
            ("Can a website generate leads?", "Yes, if offers are clear, forms are easy, and pages answer buyer questions. That is how we scope lead-generation websites."),
        ],
    )
    add(
        "web-app-development-india",
        "Web app development in India",
        "When you need a web application instead of a brochure site, and how {BRAND} scopes first versions.".format(BRAND=BRAND),
        [
            ("What is web app development?", "Building a browser product people log into: dashboards, portals, workflows and SaaS tools."),
            ("How much does web app development cost in India?", f"Focused first versions at {BRAND} often start from ₹3,00,000. Multi-role products and integrations raise the quote."),
            ("How long does a web app MVP take?", "Many focused first versions land in 2 to 6 weeks when the main user journey is clear."),
            ("Website vs web app: which do I need?", "Choose a website for marketing and enquiries. Choose a web app when users must work inside the product daily."),
            ("Do you build SaaS products?", "Yes. We ship the first usable slice of a SaaS product with login, core workflow and admin basics."),
            ("Will I own the web app code?", "Yes. Client projects include IP handover for the work we create for you."),
            ("Can you connect my web app to WhatsApp or payments?", "Yes, when those integrations are in scope. We list them in the written quote."),
            ("Do you provide ongoing web app maintenance?", "Yes, via a retainer or phased updates after launch."),
            ("What stack do you use for web apps?", "Modern web stacks suited to speed and SEO when the product is public-facing. Exact tools are chosen after discovery."),
            ("Can staff use the web app on phones?", "Responsive layout is standard. If the journey is phone-first, we may recommend a mobile app instead or as well."),
        ],
    )
    add(
        "mobile-app-development-cost-india",
        "Mobile app development cost in India",
        "Android and iPhone app pricing, timelines and first-version planning for Indian startups and businesses.",
        [
            ("How much does mobile app development cost in India?", f"At {BRAND}, a focused first app often starts from ₹5,00,000. Payments, maps, chat and multi-role features increase cost."),
            ("How long does mobile app development take?", "A focused first version often takes about 8 to 12 weeks."),
            ("Android first or iPhone first?", "Many India launches start on Android. We plan one or both stores during discovery."),
            ("Do you publish to Google Play and the App Store?", "Yes. Store listing support can be included in the project scope."),
            ("What is included in a first mobile app?", "One main user journey done well, basic accounts if needed, analytics, and a plan for the next release."),
            ("Can you rebuild my app?", "Yes, if the brief is clear. We start with what to keep, what to cut, and a realistic timeline."),
            ("Do you build apps for internal staff only?", "Yes. Internal mobile tools for field teams are a common brief."),
            ("Will push notifications be included?", "When scoped. Notifications, payments and maps are priced as features, not surprises."),
            ("What happens after app launch?", "We recommend a support window or retainer for fixes and small improvements from real users."),
            ("Can one app serve customers and admins?", "Yes, with different roles. Multi-role apps take longer than single-role first versions."),
            ("Do you sign NDAs?", "Yes, when needed before detailed product discussions."),
            ("How do I hire a mobile app development company in India?", "Share goals, must-have features, timeline and budget. Ask for written scope, weekly demos and IP ownership."),
        ],
    )
    add(
        "custom-software-development-company-india",
        "Custom software development company India",
        "How custom software works, what it costs, and how to hire a custom software development company in India.",
        [
            ("What does a custom software development company in India do?", f"{BRAND} designs and builds software around your workflows: CRMs, dashboards, portals and internal tools."),
            ("How much does custom software development cost in India?", "Internal tools often start from ₹4,00,000. Price follows roles, workflows, integrations and reporting."),
            ("Custom software vs ready-made SaaS?", "Buy SaaS when it fits 80% of your process. Build custom when off-the-shelf tools force painful workarounds."),
            ("Who owns custom software IP?", "You should. Our contracts include handover of the work created for you."),
            ("How long does custom software take?", "Focused tools can ship in weeks. Multi-department systems take months and are phased."),
            ("Can you replace Excel and WhatsApp chaos?", "Yes. That is a common custom software brief: one system staff actually open."),
            ("Do you build ERP software?", "We build focused ERP-style modules when a full mega-suite is too heavy or too expensive."),
            ("Do you build CRM software?", "Yes, custom CRM-style tools when sales and follow-ups do not fit a generic CRM."),
            ("Fixed price or dedicated team?", "Fixed or phased quotes for clear scope. Dedicated pods for ongoing product work."),
            ("How do I choose a software development company in India?", "Check process, weekly demos, written scope, IP ownership, and whether they explain trade-offs in plain language."),
            ("Will you train my team?", "Handover includes walkthroughs and docs. Deeper training can be scoped."),
            ("Can custom software integrate with my current tools?", "Yes, when APIs or exports exist. Integrations are listed in the quote."),
        ],
    )
    add(
        "seo-company-india-aeo-geo",
        "SEO company India, AEO and GEO",
        "SEO, answer engine optimization and generative engine optimization for Indian businesses that want to get found.",
        [
            ("What does an SEO company in India do?", f"{BRAND} improves your site so people find you on Google, then keeps content and technical health moving."),
            ("How much is an SEO retainer in India?", "Our SEO and visibility retainers often start from ₹25,000 per month."),
            ("What is AEO?", "Answer engine optimization: structuring content so search systems can use it as a short answer."),
            ("What is GEO?", "Generative engine optimization: making your brand easy for AI assistants to cite."),
            ("Do you offer technical SEO?", "Yes: speed, indexation, sitemap, schema and crawl issues."),
            ("Is SEO only for big brands?", "No. Clear service pages and steady content help small India businesses too."),
            ("How long until SEO results?", "Technical fixes can help sooner. Content and authority usually take months of consistent work."),
            ("Do you do local SEO?", "Yes, including alignment with Google Business Profile where relevant."),
            ("Can SEO help ChatGPT mention my business?", "GEO-style pages, FAQs and proof help AI systems find accurate facts about you."),
            ("Do you write SEO content?", "We can plan clusters and write service or FAQ pages as part of retainers or projects."),
            ("Should SEO start before website launch?", "Yes when possible. Building discoverability into the site beats bolting SEO on later."),
            ("What is LLM SEO?", "Content and structure aimed at large language model answers, closely related to GEO."),
        ],
    )
    add(
        "workflow-automation-india",
        "Business workflow automation India",
        "Automating leads, follow-ups, approvals and ops without building experimental AI labs.",
        [
            ("What is workflow automation?", "Connecting tools so repetitive steps happen without copy-paste between forms, chat and sheets."),
            ("How much does workflow automation cost?", f"Projects at {BRAND} often start from ₹75,000 depending on systems and rules."),
            ("What can be automated first?", "Lead capture, follow-ups, reminders, approvals and CRM updates."),
            ("Will automation replace my team?", "No. It removes repetitive work so people focus on decisions and customers."),
            ("Do you build custom AI chatbots?", "We focus on business process automation. Light AI assist inside a workflow is fine. We do not sell custom RAG platforms."),
            ("Can you automate WhatsApp follow-ups?", "Often yes, as part of a wider ops flow when tools and permissions allow."),
            ("How long does an automation project take?", "Simple flows can ship in days or a few weeks. Multi-system setups take longer."),
            ("Do I need new software to automate?", "Not always. We often connect tools you already pay for."),
            ("What is CRM automation?", "Rules that move leads and tasks through your CRM without manual status chasing."),
            ("Can automation break if an API changes?", "Integrations need monitoring. We document owners and failure paths."),
        ],
    )
    add(
        "desktop-app-development-india",
        "Desktop app development India",
        "When you need installable computer software instead of a website-only product.",
        [
            ("When do I need a desktop app?", "Offline work, special devices, heavy local files, or locked-down office browsers."),
            ("How much does desktop app development cost?", "Quotes follow scope. Desktop work is priced after discovery like other custom software."),
            ("Windows and Mac?", "We commonly target Windows first. Mac can be included when scoped."),
            ("Can you turn my web app into a desktop app?", "Often yes, packing it as installable software with updates."),
            ("Do desktop apps work offline?", "They can. Offline-first design is a common reason to choose desktop."),
            ("Do you provide installers and updates?", "Yes, installers and update channels can be part of the delivery."),
            ("Is desktop better than mobile for field staff?", "Depends on the job. Phones win for on-the-go tasks. Desktops win for heavy local work."),
            ("Who owns the desktop software?", "You own the work created for you under contract."),
        ],
    )
    add(
        "hire-software-development-company-india",
        "Hire a software development company in India",
        "Checklist for hiring developers and agencies in India without vague quotes or lock-in.",
        [
            ("How do I hire a software development company in India?", "Write goals, must-haves, timeline and budget. Ask for process, demos, IP ownership and a written SOW."),
            ("What should be in a software development quote?", "Scope, milestones, exclusions, timeline, price model, support window and ownership terms."),
            ("Fixed price vs time and materials?", "Fixed or phased for clear scope. Time and materials or a pod when requirements will evolve."),
            ("What are red flags when hiring?", "No discovery, vague estimates, no weekly demos, and refusal to put IP in your name."),
            ("Should code live in my repository?", "Yes. Prefer your accounts from early in the project."),
            ("How fast should an agency reply?", f"{BRAND} aims to reply within 24 hours on business days for serious briefs."),
            ("Do I need a detailed spec before contacting you?", "No. A rough brief is enough to start. Discovery turns it into a clear plan."),
            ("Can you work with my existing developer?", "Yes. We can collaborate or take ownership of a defined module."),
            ("Do you work with US, UK or GCC clients?", "Yes. Remote delivery from India with overlap hours agreed up front."),
            ("What is a dedicated development team?", "A pod focused on your product for ongoing sprints, useful after the first release."),
            ("How do payments usually work?", "Milestones tied to acceptance. Exact schedule is in the proposal."),
            ("Will you sign an NDA?", "Yes when needed."),
        ],
    )
    add(
        "saas-mvp-development-india",
        "SaaS MVP development India",
        "Building the first version of a SaaS product in India with clear scope and ownership.",
        [
            ("What is a SaaS MVP?", "The smallest online product that real users can pay for or meaningfully try."),
            ("How much does a SaaS MVP cost in India?", "Focused slices often start in the low-to-mid lakhs INR depending on roles and billing needs."),
            ("How long does a SaaS MVP take?", "Many focused first versions take weeks to a few months, not a year of theatre."),
            ("What should an MVP include?", "One core journey, accounts, basic admin, and tracking. Cut nice-to-haves."),
            ("Do you handle subscriptions and payments?", "When scoped. Billing features are priced explicitly."),
            ("Multi-tenant SaaS from day one?", "Only if needed. Many MVPs start simpler and harden tenancy later."),
            ("Who owns the SaaS codebase?", "You do for client-funded builds."),
            ("Can you help after MVP launch?", "Yes, with retainers for features, SEO and reliability."),
        ],
    )
    add(
        "erp-crm-custom-software",
        "ERP and CRM custom software",
        "Custom CRM and ERP-style tools when off-the-shelf systems do not fit your process.",
        [
            ("Do you build custom CRM software?", "Yes, when sales stages and follow-ups need a tailored system."),
            ("Do you build custom ERP modules?", "Yes, focused modules for inventory, orders or ops when full ERP is overkill."),
            ("CRM vs spreadsheet?", "A CRM tracks owners, stages and reminders. Spreadsheets hide follow-ups."),
            ("Can you migrate data from Excel?", "Often yes. Migration is scoped after we see the sheets."),
            ("How long does a CRM build take?", "A focused sales CRM can land in weeks. Deep ERP-style systems are phased."),
            ("Will staff actually use it?", "We design around real roles and demos so the tool matches daily work."),
            ("Can CRM connect to email and WhatsApp?", "When integrations are available and in scope."),
            ("What about reporting?", "Dashboards and exports are common deliverables."),
        ],
    )
    add(
        "software-development-timeline-india",
        "Software development timeline India",
        "Realistic timelines for websites, web apps, mobile apps and custom software in India.",
        [
            ("How long does software development take in India?", "Websites: weeks. Web apps: weeks to a few months. Mobile apps: often 8 to 12 weeks for a first version. Larger systems are phased."),
            ("What slows projects down?", "Slow approvals, missing content, unclear owners and mid-project scope changes."),
            ("Do you work in sprints?", "Yes. Weekly demos keep progress visible."),
            ("What is a milestone?", "A paid checkpoint with clear acceptance criteria."),
            ("Can you rush a launch?", "Sometimes. Rush fees and cut scope are discussed honestly."),
            ("How do you handle delays?", "We surface risks early and replan milestones in writing."),
            ("Is discovery part of the timeline?", "Yes. Short discovery prevents expensive rebuilds."),
            ("When does QA happen?", "Throughout builds, not only on the last day."),
        ],
    )
    add(
        "ip-ownership-source-code",
        "Software IP ownership and source code",
        "Who owns the code, designs and accounts after a software project.",
        [
            ("Who owns the source code?", "For client projects, you own the work we create for you under contract."),
            ("When do I get repository access?", "Prefer your accounts early. Final handover is always documented."),
            ("What is included in handover?", "Source, key assets, environments notes and how to run the product."),
            ("Do you keep a license over my product?", "No hostage licensing for client-funded work."),
            ("What about third-party libraries?", "Open-source and vendor licenses are respected and noted."),
            ("Can another vendor take over later?", "Yes, if handover docs and access are complete. That is intentional."),
            ("Who owns the UI designs?", "Designs created for you are included in handover unless stated otherwise."),
            ("What about domain and hosting accounts?", "They should stay in your name."),
        ],
    )
    add(
        "startup-software-partner-india",
        "Startup software partner India",
        "How startups should pick a first product and an India build partner.",
        [
            ("What should a startup build first?", "The smallest product that proves value: website for demand, web app for workflows, or mobile if the journey is phone-first."),
            ("How do startups budget software in India?", "Share a range early. We map must-haves to a phased plan."),
            ("Do you work with early-stage founders?", "Yes, when the brief is serious and scope can be kept honest."),
            ("Can you help with investor demos?", "We can prioritize a demo-ready journey when that is the goal."),
            ("Should startups buy templates?", "Templates can help marketing sites. Products usually need custom work."),
            ("Do you offer equity partnerships?", "We are a services studio. Commercial terms are cash-based unless separately agreed."),
            ("How involved must the founder be?", "Weekly decisions matter. We do not disappear for months."),
            ("Can you scale the team later?", "Pods can grow after the first release if the product needs it."),
        ],
    )
    add(
        "ecommerce-website-development-india",
        "E-commerce and catalogue website development",
        "Online catalogues, stores and enquiry-led product sites for India businesses.",
        [
            ("Do you build e-commerce websites?", "Yes, when catalogue, cart or enquiry flows are in scope."),
            ("Shopify vs custom store?", "Shopify suits many stores. Custom fits unusual workflows or deep integrations."),
            ("How much does an e-commerce site cost in India?", "Ranges vary widely. We quote after seeing catalogue size and payment needs."),
            ("Can you connect UPI and Indian gateways?", "Yes when those gateways are part of the brief."),
            ("Do you handle product uploads?", "Bulk upload support can be scoped. Content ownership stays with you."),
            ("Is SEO important for e-commerce?", "Yes. Product and category pages need clear structure to get found."),
            ("Mobile shopping experience?", "Phone layout is mandatory for modern stores."),
            ("Inventory and orders admin?", "Admin tools are common deliverables for custom stores."),
        ],
    )
    add(
        "maintenance-support-retainer",
        "Software maintenance and support retainers",
        "What happens after launch: fixes, small features, SEO retainers and support windows.",
        [
            ("Do you offer post-launch support?", "Yes. Support windows and monthly retainers are available."),
            ("What is a software maintenance retainer?", "A monthly engagement for fixes, small improvements and monitoring."),
            ("SEO retainer vs product retainer?", "SEO focuses on visibility. Product retainers focus on features and reliability. Many clients run both."),
            ("How fast are bug fixes?", "Priority depends on severity and the support plan you choose."),
            ("Can you take over someone else's codebase?", "Sometimes, after an audit. Legacy takeovers are quoted separately."),
            ("Do retainers include new features?", "Small improvements yes. Large features are scoped as projects."),
            ("What if we pause the retainer?", "We document handover so you are not stuck."),
            ("Is hosting monitoring included?", "It can be. Monitoring is listed in the retainer scope."),
        ],
    )
    add(
        "security-privacy-software-projects",
        "Security and privacy in software projects",
        "Practical security expectations for SMB and mid-market software builds in India.",
        [
            ("How do you handle security?", "Role-based access, least privilege, secure hosting practices and careful handling of secrets."),
            ("Do you store passwords safely?", "Modern hashing practices are standard for apps with accounts."),
            ("Are you GDPR ready?", "We can design consent and data flows for the markets you serve. Legal advice stays with your counsel."),
            ("Do you do penetration testing?", "We can coordinate or leave room in the plan for third-party tests."),
            ("Who accesses production?", "Access is limited and documented."),
            ("Backups?", "Backup strategy is part of launch planning for serious products."),
            ("Data residency?", "We can target regions you require when cloud choices allow."),
            ("What about security for internal tools?", "Internal does not mean careless. Roles and audit trails still matter."),
        ],
    )
    add(
        "communication-process-demos",
        "Project communication and weekly demos",
        "How {BRAND} runs communication, demos and approvals during a build.".format(BRAND=BRAND),
        [
            ("How often do we meet?", "Weekly demos are the default. More calls when a milestone needs decisions."),
            ("What is a weekly demo?", "A working build walkthrough, not a slide deck."),
            ("Which tools do you use for updates?", "Email plus a shared task board. Chat tools can be added if you prefer."),
            ("Who is my point of contact?", "A build-side contact, not a ticket black hole."),
            ("How are change requests handled?", "In writing: impact on scope, time and cost before work starts."),
            ("What language do you work in?", "English for project communication. Simple language, not jargon soup."),
            ("Time zone overlap?", "Agreed during kickoff for India and international clients."),
            ("What do you need from us each week?", "Decisions, content and timely feedback."),
        ],
    )
    add(
        "pricing-quotes-india-software",
        "Software development pricing and quotes India",
        "How quotes work, what floors mean, and how to compare India software proposals.",
        [
            ("Why show starting prices?", "Floors help buyers plan. Exact quotes still need scope."),
            ("Are your prices fixed forever?", "No. Starting prices guide budgeting. Final numbers follow discovery."),
            ("What increases software cost?", "Extra roles, integrations, compliance, bilingual content and unclear requirements."),
            ("Do you charge for discovery?", "Light fit checks are free. Deep discovery may be a paid sprint for large jobs."),
            ("GST on invoices?", "Invoices follow applicable tax rules for your engagement."),
            ("Can I get a ballpark on a call?", "Yes, after we hear goals and constraints."),
            ("Cheapest quote vs best quote?", "Compare inclusions, ownership and demos, not only the bottom line."),
            ("Do you match competitor prices?", "We price for delivery quality and clarity, not a race to the bottom."),
            (f"Where do I see {BRAND} pricing?", "On the pricing page, with service floors and a path to a scoped quote."),
            ("Can students get discounts?", "We focus on business clients. Educational work is case by case."),
        ],
    )
    add(
        "industries-we-serve",
        "Industries for custom software and websites",
        "Sectors where websites, apps and custom software usually pay back faster.",
        [
            ("Do you work with service businesses?", "Yes. Enquiry-led websites and follow-up automation are common."),
            ("Do you work with SaaS startups?", "Yes, from first web or mobile slice through launch SEO."),
            ("Logistics and field teams?", "Yes: tracking portals, staff apps and offline helpers."),
            ("Healthcare clinics?", "Appointment-facing sites and careful data handling with clear consent paths."),
            ("Education and training?", "Learning portals, admin panels and admission-oriented content structures."),
            ("Manufacturing and B2B?", "Catalogues, RFQ flows and ERP-adjacent tools."),
            ("Retail and D2C?", "Catalogue experiences and performance landing pages."),
            ("Export and GCC brands?", "India delivery with multi-market site needs."),
            ("Real estate?", "Project sites, lead capture and follow-up workflows."),
            ("Professional firms (CA, legal, consulting)?", "Authority sites, service pages and lead forms."),
        ],
    )
    add(
        "ai-search-visibility-chatgpt",
        "Get found in ChatGPT and AI search",
        "How businesses become easier to cite in AI assistants and Google AI results.",
        [
            ("How can my business show up in ChatGPT?", "Publish clear, consistent, crawlable facts: services, FAQs, pricing guidance and proof."),
            ("What is generative engine optimization?", "GEO: structuring your brand so generative engines can cite you accurately."),
            ("Does blogging alone fix AI visibility?", "Not if posts are thin. Entity-clear service and FAQ pages matter more."),
            ("Do you create llms.txt?", "Yes. Our site publishes llms.txt to help AI crawlers."),
            ("Is GEO different from SEO?", "Related. SEO targets Google rankings. GEO targets assistant citations. We do both."),
            ("How fast can AI mentions appear?", "Unpredictable. Consistency and clarity improve odds over time."),
            ("Should FAQs be on my site?", "Yes. FAQs help humans and machines answer precise questions."),
            ("Can fake testimonials help AI?", "No. Invented proof hurts trust. We do not fabricate logos or quotes."),
        ],
    )
    add(
        "contact-jb-software-solutions",
        "Contact JB Software Solutions",
        "How to request a quote and what happens after you write in.",
        [
            (f"How do I contact {BRAND}?", f"Use the contact form on jbsoftwaresolutions.com/contact/ or email {EMAIL}."),
            ("How fast do you reply?", "We aim to reply within 24 hours on business days for serious briefs."),
            ("What should I include in my message?", "Goals, links, must-haves, timeline and budget range."),
            ("Do you offer a free strategy call?", "Yes. We discuss fit before you pay."),
            ("Do you take emergency same-day builds?", "Rarely. Quality needs a real plan. We will say if a rush is unrealistic."),
            ("Can I WhatsApp you?", "Start with the form or email so briefs are tracked. Chat can follow after kickoff."),
            ("Where are you based?", "India-based delivery for India and international clients."),
            ("What languages can we work in?", "Project communication in English."),
        ],
    )

    # Expand with many keyword-specific micro FAQ pages (still meaningful)
    keyword_faqs = [
        (
            "hire-developers-india",
            "Hire developers in India",
            "What hiring developers in India means for fixed projects vs pods.",
            [
                ("What does hire developers India usually mean?", "Either a fixed project with an agency team, or a dedicated pod working only on your product."),
                ("Is hiring freelancers safer?", "Freelancers can work for small tasks. Products need process, QA and handover."),
                (f"Does {BRAND} provide dedicated developers?", "We provide accountable pods, not anonymous body shopping."),
                ("Senior vs junior developers?", "We staff for the problem. Critical paths get experienced eyes."),
                ("Can I interview the builders?", "Yes for serious engagements."),
                ("Full-time equivalent meaning?", "A measure of capacity. Ask what percent of each person's week is yours."),
            ],
        ),
        (
            "android-ios-app-development",
            "Android and iOS app development",
            "Building for Google Play and the Apple App Store without jargon overload.",
            [
                ("Do you build for both Android and iOS?", "Yes. Many projects share one codebase approach to save time and budget."),
                ("Native vs cross-platform?", "Cross-platform is the default for most business apps. Native is for special device needs."),
                ("Play Store rejection risks?", "We follow store policies and prepare listings carefully. Review timelines still belong to the stores."),
                ("App Store developer account?", "You should own the account. We guide setup."),
                ("Tablet support?", "When scoped. Phones are the usual first target."),
                ("Offline mobile apps?", "Possible for field use cases when designed that way."),
            ],
        ),
        (
            "business-website-design-india",
            "Business website design India",
            "Design that supports enquiries, trust and search visibility.",
            [
                ("Do you do UI design only?", "Design is part of build. Pure design-only work is rare; we prefer design that ships."),
                ("Can you follow my brand kit?", "Yes. Share logos, colours and fonts."),
                ("Do you use templates?", "We may start from solid patterns, then customize. Cookie-cutter brochure clones are not the goal."),
                ("Accessibility?", "We aim for clear contrast, readable type and usable forms."),
                ("Animations on websites?", "Motion with purpose. We avoid heavy effects that hurt speed."),
                ("Stock photos?", "Prefer real product or workplace imagery when you have it."),
            ],
        ),
        (
            "lead-generation-website-faq",
            "Lead generation website FAQ",
            "Turning website visitors into qualified enquiries.",
            [
                ("What is a lead generation website?", "A site built to convert visitors into form fills, calls or chats."),
                ("What improves conversion rate?", "Clear offers, proof, fast pages and simple forms."),
                ("How many form fields?", "As few as needed. Extra fields kill completions."),
                ("Should pricing be public?", "Floors help serious buyers. Exact quotes still need scope."),
                ("Chat widgets?", "Optional. Forms plus fast human reply often convert better."),
                ("Thank-you pages?", "Yes, for tracking and next-step clarity."),
            ],
        ),
        (
            "api-integration-automation",
            "API integration and automation",
            "Connecting payments, CRM, forms and internal systems.",
            [
                ("What is API integration?", "Connecting two systems so data moves without manual export."),
                ("Which APIs can you integrate?", "Common payment, CRM, form and messaging APIs when documented."),
                ("What if there is no API?", "We look for exports, email parsers or staged processes. Honest limits apply."),
                ("How are API keys stored?", "In secure environment config, not in public code."),
                ("Who monitors integrations?", "Ownership is defined at handover. Retainers can include checks."),
                ("Rate limits?", "We design for vendor limits and retries where needed."),
            ],
        ),
        (
            "agile-software-development-process",
            "Agile software development process",
            "How sprints, demos and acceptance criteria work on JB projects.",
            [
                ("Do you use agile?", "Yes: short cycles, demos and a backlog you can see."),
                ("What is a sprint?", "A time box of work ending in a reviewable build."),
                ("Do I need Jira?", "Any shared board works. Tool choice is flexible."),
                ("Definition of done?", "Agreed acceptance checks before a milestone is marked complete."),
                ("Can scope change mid-sprint?", "Small swaps yes. Larger changes go through a written request."),
                ("Documentation?", "Enough to run and extend the product. Not a novel nobody reads."),
            ],
        ),
        (
            "offshore-software-development-india",
            "Offshore software development India",
            "Working with an India team from abroad: overlap, quality and ownership.",
            [
                ("Is offshore software development safe?", "It is when process, ownership and communication are clear."),
                ("How do you handle time zones?", "Overlap hours are agreed at kickoff."),
                ("Will English be clear?", "Yes. Plain English updates are standard."),
                ("Quality vs cost?", "India delivery can be cost-effective without meaning disposable quality."),
                ("Data security offshore?", "Access controls and NDAs apply the same as domestic work."),
                ("Can you join our standups?", "Yes when the cadence fits both sides."),
            ],
        ),
        (
            "website-maintenance-india",
            "Website maintenance India",
            "Updates, security patches, content edits and uptime care after launch.",
            [
                ("Do you maintain websites after launch?", "Yes, through support plans or retainers."),
                ("What does website maintenance include?", "Updates, small content edits, uptime checks and minor fixes as scoped."),
                ("How often should a site be updated?", "Whenever offers change. Technical updates follow a schedule."),
                ("Broken forms?", "Priority fixes under support agreements."),
                ("SSL and domain renewals?", "You own renewals. We can remind and guide."),
                ("Content updates pricing?", "Small edits may sit in a retainer. Large rewrites are quoted."),
            ],
        ),
        (
            "progressive-web-app-pwa",
            "Progressive web apps (PWA)",
            "When a installable web experience is enough versus a store app.",
            [
                ("What is a PWA?", "A website that can behave more like an app, sometimes installable on a phone."),
                ("PWA vs mobile app?", "PWAs avoid stores. Native or store apps win for deeper device features."),
                ("Do you build PWAs?", "When the brief fits. We recommend honestly if a store app is better."),
                ("Offline PWAs?", "Limited offline is possible. True offline-first often needs a stronger approach."),
                ("Push on PWA?", "Browser support varies. We explain limits up front."),
                ("SEO for PWAs?", "Public content can still be crawlable when built correctly."),
            ],
        ),
        (
            "admin-panel-dashboard-development",
            "Admin panel and dashboard development",
            "Internal dashboards for ops, sales and support teams.",
            [
                ("Do you build admin panels?", "Yes. Most products need an admin side."),
                ("What belongs in a dashboard?", "The metrics and actions your team uses weekly, not every chart imaginable."),
                ("Role-based admin access?", "Yes. Different staff see different data."),
                ("Export to Excel?", "Common request. We include exports when scoped."),
                ("Real-time dashboards?", "Possible. Real-time costs more than daily snapshots."),
                ("Mobile admin?", "Responsive admin is standard. Dedicated admin apps are optional."),
            ],
        ),
        (
            "payment-gateway-integration-india",
            "Payment gateway integration India",
            "UPI and card payments inside websites and apps.",
            [
                ("Can you integrate Indian payment gateways?", "Yes when the gateway and compliance needs are in scope."),
                ("UPI support?", "Available through supported gateways."),
                ("Who creates the merchant account?", "You. We integrate once credentials exist."),
                ("Subscriptions and recurring billing?", "Possible for SaaS when scoped."),
                ("Refunds and webhooks?", "Part of a proper payments integration plan."),
                ("PCI concerns?", "We use gateway-hosted flows so card data stays with the provider."),
            ],
        ),
        (
            "cloud-hosting-deployment",
            "Cloud hosting and deployment",
            "Where apps run, who owns accounts, and how releases ship.",
            [
                ("Which cloud do you use?", "AWS, GCP or Azure based on your needs and budget."),
                ("Who owns the cloud account?", "You should."),
                ("CI/CD meaning?", "Automated checks and deploy pipelines so releases are repeatable."),
                ("Staging environment?", "Yes for serious products. Staging mirrors production safely."),
                ("Downtime during deploys?", "We aim for low-drama releases. Plans depend on architecture."),
                ("Cost optimization?", "We avoid over-provisioning on day one."),
            ],
        ),
        (
            "ui-ux-for-software-products",
            "UI and UX for software products",
            "Practical UX that helps users finish tasks without expensive redesign theatre.",
            [
                ("Do you provide UX research?", "Lightweight research for SMB budgets: interviews, task flows and prototypes as needed."),
                ("Wireframes first?", "Yes for non-trivial products."),
                ("Design systems?", "Simple component consistency matters more than a 200-page brand book."),
                ("User testing?", "We recommend testing critical flows before big launches."),
                ("Dark mode?", "Optional. Not required for every product."),
                ("Copywriting in UX?", "Button and empty-state copy is part of building usable software."),
            ],
        ),
        (
            "qa-testing-software-india",
            "QA and testing for software projects",
            "How quality checks run before you pay for a milestone.",
            [
                ("Do you test on real devices?", "Yes for mobile and responsive checks."),
                ("Automated tests?", "Added where they protect critical paths without slowing delivery."),
                ("Who writes test cases?", "We cover critical acceptance paths. You confirm business rules."),
                ("Browser support?", "Modern evergreen browsers unless you need legacy."),
                ("Performance testing?", "For public sites and busy apps, speed checks are part of launch."),
                ("Bug warranty?", "Support windows cover defects from our work as defined in the agreement."),
            ],
        ),
        (
            "migration-legacy-software",
            "Legacy software migration",
            "Moving off old tools, Access databases, or abandoned codebases.",
            [
                ("Can you migrate legacy software?", "Often, after an audit of data and must-keep workflows."),
                ("Big bang vs phased migration?", "Phased is usually safer."),
                ("What about old data quality?", "Cleanup is part of the plan. Garbage in stays garbage unless cleaned."),
                ("Can users keep working during migration?", "Parallel run strategies reduce risk."),
                ("Rewrite vs extend?", "We recommend based on cost and risk, not ideology."),
                ("Documentation for legacy systems?", "We reverse-engineer enough to ship safely."),
            ],
        ),
    ]

    for slug, title, desc, qs in keyword_faqs:
        add(slug, title, desc, qs)

    # Cost-alias topics for common search URLs
    add(
        "custom-software-cost-india",
        "Custom software cost in India",
        "What drives custom software pricing in India and how JB Software Solutions quotes fixed or phased work.",
        [
            ("How much does custom software cost in India?", f"Focused internal tools at {BRAND} often start from ₹4,00,000. Price follows roles, workflows, integrations and reporting."),
            ("Fixed price or monthly?", "We prefer written fixed or phased quotes for clear builds. Retainers fit ongoing SEO or product updates."),
            ("Who owns the software?", "You do. Contracts include handover of the work we create for you."),
            ("What makes custom software expensive?", "Multiple user roles, complex approvals, third-party integrations, reporting and data migration."),
            ("Can you phase custom software delivery?", "Yes. Ship the highest-ROI workflow first, then expand."),
            ("Do you quote after a free discovery call?", "Yes. Serious briefs get a fit check and a path to a written quote."),
        ],
    )
    add(
        "seo-aeo-geo-explained",
        "What are SEO, AEO and GEO?",
        "Simple definitions of SEO, AEO and GEO for Indian businesses that want to get found online and in AI answers.",
        [
            ("What is SEO?", "SEO helps people find you on Google through better pages, speed and content."),
            ("What is AEO?", "AEO helps your content show up as a short answer when search systems display direct answers."),
            ("What is GEO?", "GEO helps AI assistants like ChatGPT mention your brand when buyers ask questions."),
            (f"Does {BRAND} offer all three?", "Yes. We treat SEO, AEO and GEO as one visibility practice tied to the product you ship."),
            ("Is GEO the same as LLM SEO?", "Closely related. Both focus on making your brand easy for AI systems to cite accurately."),
            ("Where should I start?", "Fix technical basics, publish clear service pages and FAQs, then expand content clusters."),
        ],
    )

    # Programmatic expansions for volume with unique, useful Q&As
    services = [
        ("website development", "website development company India", "₹50,000"),
        ("web app development", "web application development", "₹3,00,000"),
        ("mobile app development", "mobile app development company India", "₹5,00,000"),
        ("custom software", "custom software development company India", "₹4,00,000"),
        ("SEO services", "SEO company India", "₹25,000/mo"),
        ("workflow automation", "business workflow automation", "₹75,000"),
        ("desktop apps", "desktop app development", "scoped quote"),
    ]
    extra = []
    for svc, kw, floor in services:
        slug = ("about-" + kw.replace(" ", "-").replace("/", "-")[:48]).lower().strip("-")
        qs = [
            (f"Why hire {BRAND} for {svc}?", f"You get written scope, weekly demos, plain-language updates and ownership of the work we create for you."),
            (f"What is a starting price for {kw}?", f"Starting points begin around {floor}. Final quotes follow discovery."),
            (f"Do you offer {svc} for startups?", f"Yes, when the brief is focused and decisions can be made weekly."),
            (f"Do you offer {svc} for established companies?", f"Yes. We work with growing businesses that need reliable delivery, not just a pitch deck."),
            (f"Is {kw} available remotely?", f"Yes. {BRAND} delivers remotely across India and to international clients."),
            (f"How do I start a {svc} project?", f"Send goals, links and budget via the contact form. We reply with fit and next steps."),
        ]
        extra.append(
            {
                "slug": slug,
                "title": f"{svc.title()} with {BRAND}",
                "desc": f"Common questions about {kw} and how {BRAND} delivers.",
                "qs": qs,
            }
        )
    topics.extend(extra)

    return topics


def all_faq_topics():
    return _topics()


def count_faqs():
    return sum(len(t["qs"]) for t in _topics())
