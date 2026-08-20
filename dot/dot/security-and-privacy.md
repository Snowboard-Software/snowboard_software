# Security & Privacy

Ensuring high standards to protect customer data is critical to operate successfully given rising IT security threats and increased privacy concerns.

We are continuously auditing our technical and organizational measures by monitoring our infrastructure and processes with [Probo](https://www.probo.com/).

We've successfully completed the AICPA Service Organization Control (SOC) 2 Type II audit. The audit confirms that Snowboard Software GmbH’s information security practices, policies, procedures, and operations meet the SOC 2 standards. Our current report is issued by [MJD Advisors](https://mjd.cpa/) and covers the Security, Availability and Confidentiality trust services criteria for the Dot Platform.

Our SOC 2 Type II report, our most recent penetration test summary, and a bridge letter covering the period since the last report are available under NDA. We also sign a Data Processing Agreement (DPA) with customers who need one.

For these documents, a completed security questionnaire, or any other question, contact us at [hi@getdot.ai](mailto:hi@getdot.ai).

<figure><img src="../.gitbook/assets/image (5) (1).png" alt="" width="203"><figcaption></figcaption></figure>

## Organizational Security

**Information Security Program**

We have an Information Security Program in place that is communicated throughout the organization. Our Information Security Program follows the criteria set forth by the SOC 2 Framework. SOC 2 is a widely known information security auditing procedure created by the American Institute of Certified Public Accountants.

**Third-Party Audits**

Our organization undergoes independent third-party assessments to test our security and compliance controls.

**Third-Party Penetration Testing**

We perform an independent third-party penetration test at least annually to ensure that the security posture of our services is uncompromised.

**Roles and Responsibilities**

Roles and responsibilities related to our Information Security Program and the protection of our customer’s data are well defined and documented. Our team members are required to review and accept all of the security policies.

**Security Awareness Training**

Our team members are required to go through employee security awareness training covering industry standard practices and information security topics such as phishing and password management.

**Confidentiality**

All team members are required to sign and adhere to an industry standard confidentiality agreement prior to their first day of work.

**Background Checks**

We perform background checks on all new team members in accordance with local laws.

## Cloud Security

**Cloud Infrastructure Security**

All of our services are hosted on [Hetzner Cloud](https://www.hetzner.com/), in Falkenstein, Germany (EU) and Hillsboro, Oregon (US). Hetzner operates its own data centres and publishes its security and compliance measures at [Hetzner Legal & Compliance](https://www.hetzner.com/legal/).

**Data Hosting Security**

Each customer is served from a single region — the EU or the US — and their data stays in that region. Every organization gets its own separate database.

Dot queries your data warehouse in place. We store the schema and documentation Dot needs as context, plus the results that are returned into a chat — we do not copy or replicate your warehouse.

**Encryption at Rest**

Backups are encrypted before they leave the server (see below).

**Encryption in Transit**

Our applications encrypt in transit with TLS/SSL only.

**Backups**

All data is backed up hourly with [restic](https://restic.net/) — encrypted and deduplicated on the server, before it leaves it — to off-site object storage in a different cloud than the servers themselves. Each server keeps its own independent repository. Snapshots age out on a rolling schedule and the oldest is never more than a year old. Restores are tested.

**Vulnerability Scanning**

We perform vulnerability scanning and actively monitor for threats.

**Logging and Monitoring**

We actively monitor and log various cloud services.

**Business Continuity and Disaster Recovery**

Encrypted off-site backups in a separate cloud from the servers themselves allow us to restore an individual organization's database or a complete host. We utilize monitoring services to alert the team in the event of any failures affecting users.

**Incident Response**

We have a process for handling information security events which includes escalation procedures, rapid mitigation and communication.

## Access Security

**Administrative Access**

Our servers have no publicly reachable SSH or administrative interfaces. All administrative access runs over a private mesh VPN and is limited to authorized employees.

**Permissions and Authentication**

Access to cloud infrastructure and other sensitive tools are limited to authorized employees who require it for their role.

Where available we have Single Sign-on (SSO), 2-factor authentication (2FA) and strong password policies to ensure access to cloud services are protected.

**Least Privilege Access Control**

We follow the principle of least privilege with respect to identity and access management.

**Quarterly Access Reviews**

We perform quarterly access reviews of all team members with access to sensitive systems.

**Password Requirements**

All team members are required to adhere to a minimum set of password requirements and complexity for access.

**Password Managers**

All company issued laptops utilize a password manager for team members to manage passwords and maintain password complexity.

## Your Controls

The sections above describe how we secure our own systems. These are the controls you operate yourself.

**Single Sign-On**

Dot supports SAML and OpenID Connect, with dedicated setup for Microsoft Entra ID, Okta and Google, and a generic OIDC option for any other identity provider. Group membership from your IdP can drive a user's role and access scope on every login. See [Single Sign On](integrations/sso/README.md).

**Roles and Permissions**

Access inside Dot is governed by three roles — Admin, Modeler and User — plus groups and workspaces that scope which data and chats a person can reach. Dot queries your warehouse as the database user you connect it with, so it can never read data that user is not granted. See [Permissions](whats-dot/permissions.md).

**Audit Logging**

Security-relevant events are recorded per organization and can be pulled through the API for forwarding to your own log management system.

## Data Retention and Deletion

Your data stays in Dot for as long as you are a customer. On request, or when an organization is deleted, we remove its database and associated files from our live systems. Backup snapshots containing that data age out on the rolling schedule described above.

## AI Security

**Secure AI Model Usage**

[Dot](https://getdot.ai/) is powered by leading frontier models from Anthropic, Google and OpenAI. Organizations that require it can instead be served through Azure OpenAI. These models provide state-of-the-art AI capabilities while maintaining strong security and privacy measures.

**No Training on Customer Data**

We use every model provider under zero data retention terms: your prompts and results are not stored by them and are never used for training. For more details, refer to:

* [Anthropic’s Privacy Policy](https://privacy.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training#h_1a7d240480)
* [Google’s Gemini API Terms](https://ai.google.dev/gemini-api/terms)
* [OpenAI’s API Data Usage Policies](https://openai.com/policies/api-data-usage-policies)

As an organization, we are committed to safeguarding customer data and will never use it to train our AI models.

**AI Data Protection Measures**

* Encryption: All data exchanged with AI models is encrypted in transit using TLS/SSL to prevent unauthorized interception.
* Access Control: Only authorized systems and users can interact with AI processing services, ensuring strict data governance.
* Logging & Monitoring: AI interactions are logged and monitored for anomalies to detect and prevent misuse.

**Compliance & Risk Management**

* Third-Party Security Audits: AI security practices are included in our periodic security assessments and SOC 2 audits.
* Regulatory Alignment: AI data handling complies with GDPR, CCPA, and other applicable data protection regulations.
* Incident Response: If an AI-related security incident occurs, we have an established protocol for rapid investigation and resolution.

## Sub-processors

We keep the number of parties that touch customer data small. These are the ones that do:

| Sub-processor | Purpose | Location |
| --- | --- | --- |
| Hetzner Online GmbH | Hosting and compute | Germany (EU customers) / United States (US customers) |
| Cloudflare, Inc. | Encrypted off-site backup storage | Global |
| Anthropic, Google, OpenAI | Model inference, under zero data retention terms | United States |
| Microsoft | Notification email delivery | European Union |
| PostHog, Inc. | Product analytics and error reporting | European Union |

Our own observability stack is self-hosted, so prompts and query results are not sent to a third-party monitoring vendor.

We notify customers of changes to this list. Organizations that require it can be served through Azure OpenAI instead of the model providers above.

## Vendor and Risk Management

**Annual Risk Assessments**

We undergo at least annual risk assessments to identify any potential threats, including considerations for fraud.

**Vendor Risk Management**

Vendor risk is determined, and the appropriate vendor reviews are performed prior to authorizing a new vendor.

## Responsible Disclosure

At Dot, we consider the security of our systems a top priority. But no matter how much effort we put into system security, there can still be vulnerabilities present.

If you discover a vulnerability, we would like to know about it so we can take steps to address it as quickly as possible. We would like to ask you to help us better protect our clients and our systems.

Please do the following:

* E-mail your findings to security@sled.so,
* Do not take advantage of the vulnerability or problem you have discovered, for example by downloading more data than necessary to demonstrate the vulnerability or deleting or modifying other people's data,
* Use test.getdot.ai for security testing and not one of our production services,
* Do not reveal the problem to others until it has been resolved,
* Do not use attacks on physical security, social engineering, distributed denial of service, spam, automated probing that strains our servers, or applications of third parties, and
* Do provide sufficient information to reproduce the problem, so we will be able to resolve it as quickly as possible. Usually, the IP address or the URL of the affected system and a description of the vulnerability will be sufficient, but complex vulnerabilities may require further explanation.

What we promise:

* We will respond to your report within 3 business days with our evaluation of the report and an expected resolution date,
* If you have followed the instructions above, we will not take any legal action against you in regard to the report,
* We will handle your report with strict confidentiality, and not pass on your personal details to third parties without your permission,
* We will keep you informed of the progress towards resolving the problem,
* In the public information concerning the problem reported, we will give your name as the discoverer of the problem (unless you desire otherwise), and
* As a token of our gratitude for your assistance, we offer a reward for every report of a security problem that was not yet known to us. The amount of the reward will be determined based on the severity of the leak and the quality of the report. The minimum reward will be a 50 USD gift certificate.

We strive to resolve all problems as quickly as possible, and we would like to play an active role in the ultimate publication on the problem after it is resolved.<br>
