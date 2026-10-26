import{d as e,l as t,p as n,r,t as i}from"./jsx-runtime-CdRB5hBm.js";import{c as a,f as o,g as s,i as c,l,n as u,r as d,s as f}from"./index-BUnjjIUL.js";var p=n(e(),1),m=i(),h=`https://easypeeze-tools-j6dbitzprq-el.a.run.app/contact`,g=`6Lf-LsEtAAAAAKGPRWhI5GDDjIYNOa_hWohbAJ9c`,_=`jbsoftwaresolutions.com/contact`;async function v(e,t){try{let n=await fetch(e,{method:`POST`,headers:{"Content-Type":`application/json`,Accept:`application/json`},body:JSON.stringify(t)}),r=await n.json().catch(()=>null);return{httpOk:n.ok,json:r}}catch{return{httpOk:!1,json:null}}}function y(){return window.grecaptcha?.render?Promise.resolve():(window.__jbRecaptchaLoading||(window.__jbRecaptchaLoading=new Promise((e,t)=>{window.__jbRecaptchaReady=()=>e();let n=document.createElement(`script`);n.src=`https://www.google.com/recaptcha/api.js?onload=__jbRecaptchaReady&render=explicit`,n.async=!0,n.defer=!0,n.onerror=t,document.head.appendChild(n)})),window.__jbRecaptchaLoading)}function b(){let e=(0,p.useRef)(null),t=(0,p.useRef)(null),n=(0,p.useRef)(null),[i,a]=(0,p.useState)(!1),[s,c]=(0,p.useState)(!1),[l,u]=(0,p.useState)(null),[d,f]=(0,p.useState)(!1),b=()=>f(!0);(0,p.useEffect)(()=>{if(!d)return;let e=!1;return y().then(()=>{!e&&t.current&&n.current===null&&(n.current=window.grecaptcha.render(t.current,{sitekey:g,theme:`dark`,callback:()=>a(!0),"expired-callback":()=>a(!1),"error-callback":()=>a(!1)}))}).catch(()=>u({error:!0,text:`Could not load the spam check. Email ${o} instead.`})),()=>{e=!0}},[d]),(0,p.useEffect)(()=>{let e=setInterval(()=>{if(n.current===null||!window.grecaptcha?.getResponse)return;let e=!!window.grecaptcha.getResponse(n.current);a(t=>t===e?t:e)},400);return()=>clearInterval(e)},[]);let x=()=>{a(!1);try{n.current!==null&&window.grecaptcha.reset(n.current)}catch{}};return(0,m.jsxs)(`form`,{className:`form`,ref:e,onSubmit:async t=>{if(t.preventDefault(),s)return;let r=new FormData(e.current),a=String(r.get(`name`)||``).trim(),o=String(r.get(`email`)||``).trim(),l=String(r.get(`message`)||``).trim();if(!a)return u({error:!0,text:`Please enter your name.`});if(!o.includes(`@`))return u({error:!0,text:`Please enter a valid email.`});if(!l)return u({error:!0,text:`Please add some project details.`});let d=``;if(d=window.grecaptcha?.getResponse(n.current)||``,!d||!i)return x(),u({error:!0,text:`Please complete the reCAPTCHA before sending.`});c(!0),u({error:!1,text:`Sending...`});try{let t=await v(h,{name:a,email:o,company:String(r.get(`company`)||``).trim(),service:r.get(`service`),budget:r.get(`budget`),project_details:l,source:_,"g-recaptcha-response":d});if(!(t.httpOk&&t.json?.ok===!0&&t.json?.emailQueued===!0))throw Error(t.json?.error||`Could not send. Email info@jbsoftwaresolutions.com instead.`);e.current.reset(),u({error:!1,text:`Thanks - your brief was sent. We reply within 24 hours on business days.`})}catch(e){u({error:!0,text:e?.message||`Could not send. Email info@jbsoftwaresolutions.com instead.`})}finally{c(!1),x()}},onFocus:b,onPointerDown:b,onKeyDown:b,noValidate:!0,children:[(0,m.jsxs)(`label`,{children:[`Name`,(0,m.jsx)(`input`,{name:`name`,required:!0,maxLength:80,autoComplete:`name`,placeholder:`Your name`})]}),(0,m.jsxs)(`label`,{children:[`Email`,(0,m.jsx)(`input`,{type:`email`,name:`email`,required:!0,maxLength:120,autoComplete:`email`,placeholder:`you@company.com`})]}),(0,m.jsxs)(`label`,{children:[`Company / project name`,(0,m.jsx)(`input`,{name:`company`,maxLength:120,placeholder:`Optional`})]}),(0,m.jsxs)(`label`,{children:[`Service`,(0,m.jsxs)(`select`,{name:`service`,children:[(0,m.jsx)(`option`,{children:`Web development`}),(0,m.jsx)(`option`,{children:`Mobile app`}),(0,m.jsx)(`option`,{children:`Custom software`}),(0,m.jsx)(`option`,{children:`SEO / AEO / GEO`}),(0,m.jsx)(`option`,{children:`Workflow / business automation`}),(0,m.jsx)(`option`,{children:`Desktop app`}),(0,m.jsx)(`option`,{children:`Not sure yet`})]})]}),(0,m.jsxs)(`label`,{children:[`Budget range`,(0,m.jsxs)(`select`,{name:`budget`,children:[(0,m.jsx)(`option`,{children:`Under ₹1 lakh`}),(0,m.jsx)(`option`,{children:`₹1-5 lakh`}),(0,m.jsx)(`option`,{children:`₹5-15 lakh`}),(0,m.jsx)(`option`,{children:`₹15 lakh+`}),(0,m.jsx)(`option`,{children:`Not sure yet`})]})]}),(0,m.jsxs)(`label`,{children:[`Project details`,(0,m.jsx)(`textarea`,{name:`message`,required:!0,maxLength:4e3,placeholder:`Goals, timeline, links, must-haves`})]}),(0,m.jsx)(`div`,{ref:t,className:`form-captcha`}),!i&&!s&&(0,m.jsx)(`p`,{className:`form-hint`,children:`Tick "I'm not a robot" to enable the button.`}),(0,m.jsxs)(`p`,{className:`form-legal`,children:[`By sending this form you agree to our `,(0,m.jsx)(r,{to:`/privacy`,children:`privacy policy`}),` and`,` `,(0,m.jsx)(r,{to:`/terms`,children:`terms`}),`.`]}),l&&(0,m.jsx)(`p`,{className:`form-status${l.error?` is-error`:` is-ok`}`,role:`status`,"aria-live":`polite`,children:l.text}),(0,m.jsx)(`button`,{className:`btn btn-primary`,type:`submit`,disabled:s||!i,"aria-busy":s,children:s?`Sending...`:`Get my quote`})]})}var x=`<section class="page-hero"><div class="container">
    <div class="section-kicker">Legal</div>
    <h1>Privacy policy</h1>
    <p>Last updated: 15 October 2026. This notice explains what personal information JB Software Solutions collects through jbsoftwaresolutions.com and related project work, why we use it, and the choices you have.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose prose-wide">
    <h2>1. Who we are</h2>
    <p>JB Software Solutions ("we", "us", "our") provides website development, mobile app development, custom software, desktop apps, SEO, AEO, GEO and workflow automation services. Our public website is <a href="https://jbsoftwaresolutions.com/">https://jbsoftwaresolutions.com/</a>. For privacy questions, email <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a> or use the <a href="/contact/" data-to="/contact">contact form</a>.</p>
    <p>This policy covers visitors and enquirers on our marketing site, people who email us, and (at a high level) how we handle personal data shared with us during a client engagement. A signed statement of work, master services agreement or non-disclosure agreement may add stricter rules for a specific project. Where those documents conflict with this page on project data, the signed document controls for that project.</p>

    <h2>2. Scope</h2>
    <p>This policy applies to:</p>
    <ul>
      <li>jbsoftwaresolutions.com and pages we publish under that domain</li>
      <li>Our contact form and email conversations about enquiries</li>
      <li>Analytics and technical logs created when you browse the site</li>
      <li>Personal data you share so we can quote, contract, invoice or deliver services</li>
    </ul>
    <p>It does not govern third-party sites we link to, app stores, payment gateways you use with your own customers, or products we build for you once those products are live under your accounts. Those systems have their own operators and policies.</p>

    <h2>3. Information we collect</h2>
    <h3>3.1 Information you give us</h3>
    <ul>
      <li><strong>Contact and enquiry data:</strong> name, email address, company or project name, service interest, budget range, message text, and any files or links you choose to share</li>
      <li><strong>Communication records:</strong> emails, call notes and meeting notes related to your enquiry or project</li>
      <li><strong>Business and billing data for clients:</strong> billing name, address, GSTIN where needed, bank or UPI details for receiving or sending invoices, and payment references. We do not store full card numbers on our website. Card payments, if used, are handled by the payment partner named in your invoice or agreement</li>
      <li><strong>Project materials:</strong> credentials, content, customer lists, designs, source access and other materials you provide so we can deliver the work. We treat these as confidential under our engagement terms</li>
    </ul>
    <h3>3.2 Information collected automatically</h3>
    <ul>
      <li><strong>Device and browser data:</strong> IP address, browser type, device type, operating system, language and approximate location derived from IP</li>
      <li><strong>Usage data:</strong> pages viewed, referrer, time on page, clicks and similar interaction events</li>
      <li><strong>Cookies and similar technologies:</strong> see section 6</li>
    </ul>
    <h3>3.3 Sensitive personal data</h3>
    <p>We do not ask website visitors for sensitive personal data (for example health, biometrics, caste, religion or political opinions). If a project requires handling such data for your users, we will agree purpose, security and processing roles in writing before that work starts.</p>

    <h2>4. How we use personal information</h2>
    <ul>
      <li>To respond to enquiries, assess fit and prepare quotes</li>
      <li>To enter into and perform contracts, deliver services, support you and provide handover</li>
      <li>To invoice, collect payment, maintain accounting and meet tax or statutory duties in India</li>
      <li>To improve the website, measure traffic and fix technical issues</li>
      <li>To send project updates and, only where appropriate, limited service announcements. You can ask us to stop marketing messages at any time</li>
      <li>To detect abuse, spam, fraud or security incidents</li>
      <li>To establish, exercise or defend legal claims</li>
    </ul>
    <p>We do not sell your personal information. We do not rent enquiry lists to advertisers.</p>

    <h2>5. Legal bases and Indian law</h2>
    <p>We process personal data in line with applicable Indian law, including the Information Technology Act, 2000 and the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, and we are preparing practices for the Digital Personal Data Protection Act, 2023 (DPDP Act) and its rules as they apply to our business.</p>
    <p>Depending on the context, processing rests on your consent (for example submitting the contact form), performance of a contract or steps prior to a contract, our legitimate interests in running and securing an agency website, and legal obligations such as tax retention.</p>

    <h2>6. Cookies, analytics and similar tools</h2>
    <p>Our site uses:</p>
    <ul>
      <li><strong>Essential technical storage</strong> needed for the site to load and function</li>
      <li><strong>Google Analytics 4</strong> (measurement ID G-RMGPE314SF) to understand aggregate traffic and page performance. Google may process data according to its own terms and privacy policy</li>
      <li><strong>Fonts and CDN assets</strong> loaded from Google Fonts / Google hosts when you visit pages that request them</li>
    </ul>
    <p>You can block or delete cookies in your browser. Blocking some cookies may affect analytics accuracy but should not block the core marketing pages. We do not currently run advertising pixels for retargeting on this site. If that changes, we will update this policy.</p>

    <h2>7. Who we share data with</h2>
    <p>We share personal data only when needed to operate the business or when the law requires it:</p>
    <ul>
      <li><strong>Google Cloud and Gmail</strong> carry contact-form submissions: our form service on Google Cloud receives them and emails them to info@jbsoftwaresolutions.com. Messages are not stored in a database</li>
      <li><strong>Email providers</strong> that deliver and store business email</li>
      <li><strong>Google Analytics / Google</strong> for site analytics as described above</li>
      <li><strong>Hosting and infrastructure</strong> such as GitHub Pages (or a successor host) that serves this static website</li>
      <li><strong>Professional advisers</strong> (for example accountants or lawyers) under confidentiality where needed</li>
      <li><strong>Authorities</strong> when required by Indian law, court order or a lawful request</li>
      <li><strong>Subcontractors or specialists</strong> we engage for a project, only as needed, under confidentiality and instructions that match the engagement</li>
    </ul>
    <p>If we use additional tools (project boards, cloud repos, design tools), access is limited to people working on your project.</p>

    <h2>8. International transfers</h2>
    <p>Our team primarily works from India. Some processors (for example form delivery, analytics or hosting) may store or process data on servers outside India. By using the site or submitting an enquiry, you understand that your information may be processed in other countries with different data-protection rules. We take reasonable steps to work with reputable providers and to limit what we send them to what is needed.</p>

    <h2>9. Retention</h2>
    <ul>
      <li><strong>Website enquiries:</strong> typically up to 24 months from last meaningful contact, unless a project starts or you ask us to delete sooner where we can</li>
      <li><strong>Client and project records:</strong> for the life of the engagement and a reasonable period after, often 3 years or longer where needed for support, IP proof or disputes</li>
      <li><strong>Financial and tax records:</strong> as required under Indian tax and company law (often 8 years or more for certain records)</li>
      <li><strong>Analytics data:</strong> according to Google Analytics retention settings (commonly up to 26 months unless changed)</li>
    </ul>
    <p>When retention ends, we delete or anonymise data where practical, except where the law requires us to keep it.</p>

    <h2>10. Security</h2>
    <p>We use reasonable technical and organisational measures appropriate to a small software agency: HTTPS on the public site, access limited to people who need it, careful handling of credentials, and private repositories for client code where we control the repo. No method of transmission or storage is perfectly secure. Please do not send passwords or production secrets over public forms or unencrypted chat unless we agree a safer channel.</p>
    <p>If we become aware of a personal data breach that is likely to cause significant harm, we will take steps required by applicable law, which may include notifying affected people and relevant authorities where mandatory.</p>

    <h2>11. Your choices and rights</h2>
    <p>Subject to Indian law and reasonable verification, you may ask us to:</p>
    <ul>
      <li>Confirm whether we hold personal data about you and receive a copy</li>
      <li>Correct inaccurate or incomplete data</li>
      <li>Withdraw consent where processing is based on consent</li>
      <li>Request deletion where the law allows and retention is no longer required</li>
      <li>Object to or restrict certain processing where applicable</li>
      <li>Nominate another person to exercise rights in limited circumstances under the DPDP Act once those provisions apply to us in practice</li>
    </ul>
    <p>Email <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a> with the subject "Privacy request". We aim to respond within 15 working days. We may keep limited records of the request itself. If you are unhappy with our response, you may escalate under the grievance process below and, where available, to the Data Protection Board of India or other competent authority.</p>

    <h2>12. Children</h2>
    <p>Our services and website are aimed at businesses and adults 18 years or older. We do not knowingly collect personal data from children. If you believe a minor has submitted information, contact us and we will delete it where appropriate.</p>

    <h2>13. Client products and end-user data</h2>
    <p>When we build software for you, you are typically the controller (or equivalent) of your end users' data. You must have a lawful basis and your own privacy notices for that product. We process such data only as needed to deliver the project, under your instructions and our confidentiality terms, unless a separate data processing agreement says otherwise.</p>

    <h2>14. Third-party links</h2>
    <p>Our site may link to GitHub, Google and other services. Their privacy practices are their own. Read their policies before sharing data with them.</p>

    <h2>15. Changes to this policy</h2>
    <p>We may update this page when our practices, tools or the law change. The "Last updated" date at the top will change. Continued use of the site after an update means you have read the revised notice. For material changes that affect existing clients, we may also notify the primary contact by email where practical.</p>

    <h2>16. Grievance officer / contact</h2>
    <p>For privacy or data-protection complaints related to this website or our services:</p>
    <ul>
      <li><strong>Email:</strong> <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a></li>
      <li><strong>Contact form:</strong> <a href="/contact/" data-to="/contact">https://jbsoftwaresolutions.com/contact/</a></li>
    </ul>
    <p>We aim to acknowledge and resolve grievances within 15 working days where reasonably possible. See also our <a href="/terms/" data-to="/terms">terms and conditions</a>.</p>
  </div></section>`,S=`<section class="page-hero"><div class="container">
    <div class="section-kicker">Legal</div>
    <h1>Terms and conditions</h1>
    <p>Last updated: 15 October 2026. These terms cover use of jbsoftwaresolutions.com and the general rules for hiring JB Software Solutions. Paid work is always confirmed in a written quote, statement of work or agreement.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="container prose prose-wide">
    <h2>1. Agreement to these terms</h2>
    <p>By browsing this website, submitting the contact form, emailing us, or engaging JB Software Solutions for services, you agree to these terms and our <a href="/privacy/" data-to="/privacy">privacy policy</a>. If you do not agree, do not use the site or request services.</p>
    <p>If you act for a company, you confirm you are authorised to bind that company. "You" means the individual or the organisation you represent.</p>

    <h2>2. Who we are</h2>
    <p>JB Software Solutions provides software and digital services including website development, web applications, mobile apps, desktop apps, custom business software, SEO, AEO, GEO and workflow automation. Contact: <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a> · <a href="https://jbsoftwaresolutions.com/contact/">https://jbsoftwaresolutions.com/contact/</a>.</p>

    <h2>3. Website use</h2>
    <ul>
      <li>The site is for information about our services and to receive business enquiries</li>
      <li>Content is provided for general guidance. It is not legal, tax, accounting or investment advice</li>
      <li>We may change, pause or remove pages, prices shown as starting ranges, or features without notice</li>
      <li>You may not scrape the site in a way that harms availability, attempt unauthorised access, upload malware, or use the site for unlawful, harassing or fraudulent activity</li>
      <li>You may not copy substantial site content for commercial reuse without our written permission, except fair dealing or other rights Indian law allows</li>
    </ul>

    <h2>4. Enquiries, quotes and when a contract starts</h2>
    <p>Sending a form, chat or email is a request for information, not a binding order. Ballpark prices on the <a href="/pricing/" data-to="/pricing">pricing page</a> and elsewhere are illustrative starting ranges, not fixed offers.</p>
    <p>A paid engagement starts only when we issue a written quote or statement of work (SOW) and you accept it in writing (email is enough) and, where required, pay the agreed advance. The SOW, invoice terms and any master agreement sit above these website terms for that project. If documents conflict, the order of control is: signed MSA (if any), then SOW / accepted quote, then these website terms, then marketing pages.</p>

    <h2>5. Scope of services</h2>
    <p>Services may include discovery, design, development, testing, deployment support, SEO / AEO / GEO work, automation setup, documentation and support windows as written in the SOW. Unless the SOW says otherwise:</p>
    <ul>
      <li>Work outside the written scope needs a change request and may change price and timeline</li>
      <li>Third-party fees (hosting, domains, app store accounts, SMS, paid APIs, stock assets, ads) are yours unless we clearly include them</li>
      <li>App store approval, Google ranking, AI citation, lead volume and revenue outcomes depend on many factors outside our sole control. We commit to professional effort against the agreed scope, not to guaranteed rankings, traffic numbers or sales figures unless a written guarantee says so</li>
    </ul>

    <h2>6. Client responsibilities</h2>
    <p>You agree to:</p>
    <ul>
      <li>Provide timely access, content, feedback and decisions so we can meet the schedule</li>
      <li>Ensure you have rights to materials you supply (logos, copy, data, credentials)</li>
      <li>Keep login secrets safe and rotate anything shared after handover when appropriate</li>
      <li>Use deliverables lawfully and in line with app-store, payment and platform rules that apply to your product</li>
      <li>Pay invoices on the dates in the SOW or invoice</li>
    </ul>
    <p>Delays on your side may push timelines. We are not responsible for losses caused by late feedback, missing assets or third-party outages.</p>

    <h2>7. Fees, taxes, advances and refunds</h2>
    <ul>
      <li>Fees are usually in Indian rupees unless we agree another currency in writing</li>
      <li>GST and other taxes apply as required by law and will appear on invoices where applicable</li>
      <li>Many projects need an advance before build starts. Remaining amounts follow milestones in the SOW</li>
      <li>Late payment may pause work and may attract reasonable recovery costs</li>
      <li>Advances for work already started are generally non-refundable, except where Indian law requires a refund, where we cancel for our convenience without delivering agreed work, or where a signed SOW expressly allows a refund</li>
      <li>Retainers are billed as stated in the retainer agreement and may renew until either side cancels on the notice period written there</li>
    </ul>

    <h2>8. Intellectual property</h2>
    <p>Unless the SOW says otherwise:</p>
    <ul>
      <li><strong>Your materials</strong> remain yours</li>
      <li><strong>Custom work we create for you</strong> under a paid SOW (code, designs and content made specifically for your project) is assigned to you after full payment of all amounts due for that scope, subject to the licence carve-outs below</li>
      <li><strong>Our pre-existing tools, templates, libraries, know-how and internal frameworks</strong> stay ours. We grant you a non-exclusive licence to use them as embedded in the deliverables for your business</li>
      <li><strong>Open-source and third-party components</strong> keep their own licences. You must follow those licences</li>
      <li>Until invoices for a scope are paid in full, we may withhold final source handover or production credentials for that unpaid scope</li>
    </ul>
    <p>We may showcase non-confidential project names, screenshots or case summaries in our portfolio and proposals unless you ask us in writing to keep a project private. We will not publish secrets, private credentials or confidential business data.</p>

    <h2>9. Confidentiality</h2>
    <p>Each party must protect the other's non-public business information and use it only for the engagement, except information that is public, independently developed, or required to be disclosed by law. This duty continues for a reasonable period after the project ends (at least 3 years unless a signed NDA sets another period).</p>

    <h2>10. Acceptable use of deliverables</h2>
    <p>You must not use our work to break the law, infringe others' rights, distribute malware, process data unlawfully, or misrepresent affiliation with JB Software Solutions. We may suspend work if we reasonably believe continued delivery would cause us to violate law or platform rules.</p>

    <h2>11. Warranties and disclaimers</h2>
    <p>We warrant that we will perform services with reasonable skill and care consistent with a professional software services firm in India. Except for that and any express written warranty in an SOW, the website and services are provided on an "as available" basis.</p>
    <p>To the fullest extent Indian law allows, we disclaim implied warranties of merchantability, fitness for a particular purpose and non-infringement for marketing-site content and for outcomes that depend on third parties (hosting, stores, search engines, payment networks, client-supplied data quality).</p>
    <p>Browser and device differences, third-party API changes and platform policy changes can affect software after delivery. Support after the warranty or support window in the SOW is chargeable unless included.</p>

    <h2>12. Limitation of liability</h2>
    <p>To the fullest extent permitted by Indian law:</p>
    <ul>
      <li>We are not liable for indirect, incidental, special, consequential, punitive or exemplary damages, or for lost profits, lost revenue, lost data, business interruption or reputational harm, even if advised of the possibility</li>
      <li>Our total aggregate liability arising out of or related to a project is limited to the fees you actually paid us for that project's scope in the 12 months before the claim</li>
      <li>For website visitors who have not paid us, our aggregate liability related to site use is limited to INR 1,000</li>
    </ul>
    <p>Nothing in these terms excludes liability that Indian law does not allow us to exclude, including liability for fraud or for death or personal injury caused by negligence where such exclusion is prohibited.</p>

    <h2>13. Indemnity</h2>
    <p>You agree to indemnify and hold JB Software Solutions and its team harmless from claims, losses and reasonable costs arising from: materials you supply; your product's compliance with law and platform rules; your end users' data and content; and your misuse of deliverables, except to the extent caused by our wilful misconduct.</p>

    <h2>14. Termination</h2>
    <p>Either party may end an engagement as the SOW describes. We may suspend or end work for non-payment, illegal instructions, abusive conduct, or material breach not cured within a reasonable time after notice. On termination you pay for work performed and approved expenses. Sections on IP, confidentiality, liability, indemnity and governing law survive termination.</p>

    <h2>15. Non-solicitation</h2>
    <p>During an engagement and for 12 months after, you agree not to solicit our employees or exclusive contractors who worked on your project to leave us for a competing role, except with our written consent or via a general public job ad not aimed at them. Reasonable recruitment fees may be due if this clause is breached, as a genuine pre-estimate of disruption.</p>

    <h2>16. Force majeure</h2>
    <p>Neither party is liable for delay or failure caused by events beyond reasonable control, including natural disasters, war, epidemics, major infrastructure failure, or changes in law. Obligations resume when the event ends. Either party may end a long-blocked engagement if the event continues beyond 60 days.</p>

    <h2>17. Third-party services</h2>
    <p>The site uses Google Cloud and Gmail for form delivery, Google Analytics for traffic measurement, Google Fonts for typography, and GitHub Pages (or successor hosting) for hosting. Your use of those services is also subject to their terms. We are not responsible for outages or policy changes by those providers.</p>

    <h2>18. Electronic communications</h2>
    <p>You agree that quotes, acceptances, notices and invoices may be sent by email or other electronic means and that such records can form a binding record of agreement under Indian law.</p>

    <h2>19. Governing law and disputes</h2>
    <p>These terms and any dispute arising from the website or our services are governed by the laws of India, without regard to conflict-of-law rules. Courts in India shall have exclusive jurisdiction, subject to the city or forum named in a signed SOW or MSA if different.</p>
    <p>Before filing a claim, email <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a> and allow 15 working days for good-faith resolution. Nothing prevents either party from seeking urgent injunctive relief for IP or confidentiality breaches.</p>

    <h2>20. Grievance contact</h2>
    <p>For complaints about the website or our services: <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a> or the <a href="/contact/" data-to="/contact">contact form</a>. We aim to respond within 15 working days.</p>

    <h2>21. Changes</h2>
    <p>We may update these website terms by posting a new version with a new "Last updated" date. Changes do not retroactively rewrite a signed SOW unless both parties agree. For ongoing retainers, material term changes will be communicated to the billing contact where practical.</p>

    <h2>22. Severability and entire agreement (website)</h2>
    <p>If a clause is held unenforceable, the rest remains in force. These website terms plus the privacy policy are the entire agreement for site use. They do not cancel a signed project agreement, which controls for that engagement.</p>

    <h2>23. Contact</h2>
    <p>JB Software Solutions<br />Email: <a href="mailto:info@jbsoftwaresolutions.com">info@jbsoftwaresolutions.com</a><br />Web: <a href="https://jbsoftwaresolutions.com/contact/">https://jbsoftwaresolutions.com/contact/</a></p>
    <p>Related: <a href="/privacy/" data-to="/privacy">Privacy policy</a> · <a href="/faq/" data-to="/faq">FAQs</a></p>
  </div></section>`,C=[{title:`Website development`,from:`From ₹50,000`,items:[`Business website, about 5 to 12 pages`,`Works well on phones`,`Contact form and basic SEO setup`]},{title:`Web app development`,from:`From ₹3,00,000`,featured:!0,items:[`First version of your product in the browser`,`Login, dashboard or simple workflows`,`Clear milestones and handover docs`]},{title:`Mobile app development`,from:`From ₹5,00,000`,items:[`First app for Android and/or iPhone`,`Typical timeline around 8 to 12 weeks`,`Help publishing to the app stores`]},{title:`Custom software`,from:`From ₹4,00,000`,items:[`Internal tools for your team`,`Connect to the apps you already use`,`You own the finished work`]},{title:`SEO and visibility`,from:`From ₹25,000/mo`,items:[`Help people find you on Google`,`Useful content for buyer questions`,`Checks for AI search mentions`]},{title:`Workflow automation`,from:`From ₹75,000`,items:[`Lead and follow-up flows`,`Connect forms, chat and CRM`,`Approvals and reminders`]}];function w({html:e}){let n=t();return(0,p.useEffect)(()=>{let e=document.getElementById(`legal-html-root`);if(!e)return;let t=e=>{let t=e.target.closest(`[data-to]`);t&&(e.preventDefault(),n(t.getAttribute(`data-to`)))};return e.addEventListener(`click`,t),()=>e.removeEventListener(`click`,t)},[n,e]),(0,m.jsx)(`div`,{id:`legal-html-root`,dangerouslySetInnerHTML:{__html:e}})}function T(){return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(c,{children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(d,{className:`section-kicker`,children:`About`}),(0,m.jsx)(d,{as:`h1`,children:`A small agency that fights for your outcome`}),(0,m.jsx)(d,{as:`p`,children:`We are not a factory floor of tickets. We are a tight team that works hard, stays close to the people who hire us, and actually loves seeing customers win.`}),(0,m.jsxs)(`div`,{className:`hero-cta`,style:{marginTop:`1.75rem`},children:[(0,m.jsx)(u,{to:`/contact`,className:`btn btn-primary`,children:`Work with us`}),(0,m.jsx)(u,{to:`/pricing`,className:`btn btn-ghost`,children:`See pricing`})]})]})}),(0,m.jsx)(`section`,{className:`section`,style:{paddingTop:0},children:(0,m.jsxs)(`div`,{className:`container prose`,children:[(0,m.jsx)(d,{as:`h2`,children:`We are small on purpose`}),(0,m.jsx)(d,{as:`p`,children:`JB Software Solutions is a small agency by choice. That means you are not lost behind layers of account managers. When you message us, the people building your product are in the loop. We sweat the details, we answer fast, and we stay supportive long after the launch party ends.`}),(0,m.jsx)(d,{as:`p`,children:`We really love our customers. Not as a slogan on a wall. As a working rule: clear communication, honest scope, patient hand-holding when something is new, and zero ego when feedback arrives. Your success is the only scoreboard that matters to us.`}),(0,m.jsx)(d,{as:`h2`,children:`Who we are`}),(0,m.jsx)(d,{as:`p`,children:`We help founders and operators ship digital products: websites, mobile apps, custom software, desktop tools, and the SEO / AEO / GEO layer that makes those products easier to find on Google and in answer-style results.`}),(0,m.jsx)(d,{as:`h2`,children:`How we work`}),(0,m.jsxs)(`ul`,{children:[(0,m.jsx)(`li`,{children:`Ship systems, not slide decks`}),(0,m.jsx)(`li`,{children:`Measure outcomes: leads, retention, citations, not vanity screenshots`}),(0,m.jsx)(`li`,{children:`Keep IP with the client`}),(0,m.jsx)(`li`,{children:`Use AI for velocity. Keep humans on taste, care and accountability`}),(0,m.jsx)(`li`,{children:`Treat every customer like the reason we get to do this work`})]}),(0,m.jsx)(d,{as:`h2`,children:`Where we work`}),(0,m.jsx)(d,{as:`p`,children:`India-first delivery with remote collaboration for clients across India, the Middle East, the UK, the US and beyond.`}),(0,m.jsx)(`p`,{children:(0,m.jsx)(u,{to:`/contact`,className:`btn btn-primary`,children:`Work with us`})})]})})]})}function E(){return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(c,{children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(d,{className:`section-kicker`,children:`Pricing`}),(0,m.jsx)(d,{as:`h1`,children:`Starting prices, not mystery quotes`}),(0,m.jsx)(d,{as:`p`,children:`Buyers compare India agencies on clarity. These floors help you budget. Final quotes are fixed or phased after discovery.`}),(0,m.jsxs)(`div`,{className:`hero-cta`,style:{marginTop:`1.75rem`},children:[(0,m.jsx)(u,{to:`/contact`,className:`btn btn-primary`,children:`Get a scoped quote`}),(0,m.jsx)(u,{to:`/services/web-development`,className:`btn btn-ghost`,children:`Browse services`})]})]})}),(0,m.jsx)(`section`,{className:`section`,style:{paddingTop:0},children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(`h2`,{className:`sr-only`,children:`Starting prices by service`}),(0,m.jsx)(s.div,{className:`price-grid`,variants:l(.08),initial:`hidden`,whileInView:`show`,viewport:{once:!0},children:C.map(e=>(0,m.jsxs)(s.article,{className:`price-card${e.featured?` is-featured`:``}`,variants:a,whileHover:{y:-10,scale:1.02},children:[(0,m.jsx)(`h3`,{children:e.title}),(0,m.jsx)(`div`,{className:`from`,children:e.from}),(0,m.jsx)(`ul`,{children:e.items.map(e=>(0,m.jsx)(`li`,{children:e},e))}),(0,m.jsx)(u,{to:`/contact`,className:`btn ${e.featured?`btn-primary`:`btn-ghost`}`,children:`Request quote`})]},e.title))}),(0,m.jsxs)(`div`,{className:`prose`,style:{marginTop:`2.5rem`},children:[(0,m.jsx)(d,{as:`h2`,children:`What changes the number`}),(0,m.jsx)(d,{as:`p`,children:`Integrations, compliance, bilingual content, offline/desktop needs, and how finished your requirements already are. We would rather quote honestly than win a fake low bid.`}),(0,m.jsx)(`p`,{children:(0,m.jsx)(u,{to:`/contact`,className:`btn btn-primary`,children:`Get a fixed or phased quote`})})]})]})})]})}function D(){return(0,m.jsxs)(m.Fragment,{children:[(0,m.jsx)(c,{children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(d,{className:`section-kicker`,children:`Contact`}),(0,m.jsx)(d,{as:`h1`,children:`Get a scoped quote`}),(0,m.jsx)(d,{as:`p`,children:`Send a short brief. We reply within 24 hours on business days with fit, rough timeline and next steps. No phone tag. No spam.`})]})}),(0,m.jsx)(`section`,{className:`section`,style:{paddingTop:0},children:(0,m.jsxs)(`div`,{className:`container contact-grid`,children:[(0,m.jsx)(d,{variants:f,children:(0,m.jsx)(b,{})}),(0,m.jsxs)(`div`,{className:`prose`,children:[(0,m.jsx)(d,{as:`h2`,children:`How we reply`}),(0,m.jsxs)(d,{as:`p`,children:[`This form emails the JB team directly and confirms on this page once it is sent. Prefer email? Write `,(0,m.jsx)(`a`,{href:`mailto:${o}`,children:o}),` with your brief.`]}),(0,m.jsx)(d,{as:`h2`,children:`What happens next`}),(0,m.jsxs)(`ul`,{children:[(0,m.jsx)(`li`,{children:`We confirm fit within 24 hours on business days`}),(0,m.jsx)(`li`,{children:`You get a written scope outline`}),(0,m.jsx)(`li`,{children:`We agree fixed or phased pricing before build starts`})]}),(0,m.jsxs)(`p`,{children:[(0,m.jsx)(r,{to:`/pricing`,children:`See starting prices`}),` if you want ballpark numbers first.`]}),(0,m.jsxs)(`p`,{className:`section-note`,children:[`By submitting, you agree we may contact you about your enquiry. See our`,` `,(0,m.jsx)(r,{to:`/privacy`,children:`privacy policy`}),` and `,(0,m.jsx)(r,{to:`/terms`,children:`terms`}),`.`]})]})]})})]})}function O(){return(0,m.jsx)(c,{children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(d,{className:`section-kicker`,children:`Resources`}),(0,m.jsx)(d,{as:`h1`,children:`Blog`}),(0,m.jsx)(d,{as:`p`,children:`Guides on software, apps and getting found online.`}),(0,m.jsx)(u,{to:`/`,className:`btn btn-primary`,style:{marginTop:`1rem`},children:`Back home`})]})})}function k(){return(0,m.jsx)(w,{html:x})}function A(){return(0,m.jsx)(w,{html:S})}function j(){return(0,m.jsx)(c,{children:(0,m.jsxs)(`div`,{className:`container`,children:[(0,m.jsx)(d,{className:`section-kicker`,children:`Error`}),(0,m.jsx)(d,{as:`h1`,children:`Page not found`}),(0,m.jsx)(u,{to:`/`,className:`btn btn-primary`,children:`Go home`})]})})}export{T as About,O as BlogHub,D as Contact,j as NotFound,E as Pricing,k as Privacy,A as Terms};