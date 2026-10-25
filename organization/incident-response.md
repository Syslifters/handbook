---
url: 'https://handbook.syslifters.com/organization/incident-response.md'
description: >-
  How Syslifters reports, contains, and notifies on security and privacy
  incidents, including CRA reporting for SysReptor and reptor.
---

# 🔥 Incident Response

## Purpose

This process covers how we report, contain, assess, and notify on suspected or confirmed security incidents, privacy incidents, and personal data breaches, including customer data we handle as a processor. It also covers Cyber Resilience Act (CRA) reporting for actively exploited vulnerabilities and severe incidents in [SysReptor](https://docs.sysreptor.com/) and [reptor](https://docs.sysreptor.com/cli/getting-started/).

## Scope

This process applies to all employees, contractors, and third parties who access or manage our information systems, networks, or data, whether stored digitally or physically. CRA manufacturer duties in this process apply to SysReptor and reptor as products with digital elements.

## How to report

Report immediately to a director or Data Protection Officer (DPO) via Signal. Do not wait for a complete picture. Report even if you are unsure.

If Signal is unavailable, or the person you would report to is involved in the incident, send S/MIME email to <team@syslifters.com> ([cer](/assets/team.cer){target="\_blank" rel="noreferrer"} / [pem](/assets/team.pem){target="\_blank" rel="noreferrer"}).

Include what you know: date and time, what happened, systems or data involved, and people involved. Incomplete reports are expected.

Examples:

* Lost or stolen company laptop or phone
* Customer data on a personal device, in a personal cloud, or in a cloud AI tool
* Unexpected access to SysReptor, SysLeaks, GitHub, or mail
* Signal or email sent to the wrong person
* A vulnerability report that looks like it is being exploited
* A severe security incident in SysReptor or reptor, including compromise of the product, the update pipeline, or a user system via the product

**Do not:**

* Wipe logs, reimage, or quietly fix before reporting
* Discuss the incident in customer channels, public tickets, or unencrypted mail unless a director or the DPO says to
* Contact affected people or the DSB on your own

## Roles

Directors own intake, containment, customer communication, and CRA reporting for SysReptor and reptor (SRP submissions and product-user notification). The DPO, or a director not involved in the incident, decides on DSB and individual notification. If a named person is involved, report to someone else.

## Containment and assessment

Directors start containment using existing controls: lock or wipe via IKARUS/HarfangLab, revoke access, and rotate credentials. Preserve evidence (logs, Burp states, device state, access logs).

Classify in plain language:

* Security incident with no personal data
* Personal data incident
* Customer-data incident (we are the processor)
* Notifiable breach
* Actively exploited vulnerability in SysReptor or reptor (CRA)
* Severe incident affecting the security of SysReptor or reptor (CRA)

Record what is known now. Do not wait for a finished root cause.

## Notification

* **Customers / controllers** first when their data or systems may be affected (processor duty under GDPR Art. 33(2), plus the contract). Do not wait for a full write-up.
* The Austrian [DSB](https://www.dsb.gv.at/) and individuals when Syslifters is the controller and GDPR thresholds are met. The 72-hour clock in Art. 33 runs from awareness. Notifying individuals under Art. 34 is a higher bar. A late DSB notification needs a reason.
* **SysReptor and reptor users** when CRA reporting is triggered. See [CRA reporting](#cra-reporting-sysreptor-and-reptor). The 24-hour CRA clock is independent of the GDPR 72-hour clock. If both apply, run both.

Notifications describe the nature of the incident, data involved, likely consequences, what we did, what we ask them to do, and a named contact.

## CRA reporting (SysReptor and reptor)

As manufacturer of SysReptor and reptor, we notify the designated CSIRT and ENISA of actively exploited vulnerabilities and severe incidents that affect the security of those products. Submit through the [single reporting platform (SRP)](https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp). Use one notification record and update it as more is known.

The 24-hour clock starts when we become aware, not when we have a complete picture. Directors decide awareness and submit. Staff still report internally immediately.

### What to report

An **actively exploited vulnerability** is a vulnerability for which there is reliable evidence that a malicious actor has exploited it in a system without permission of the system owner (Art. 3(42)). Good-faith testing, bug-bounty reports, and pentest findings with no evidence of malicious exploitation are not mandatory CRA notifications. Zero-days are in scope only if there is reliable evidence of exploitation.

A **severe incident** having an impact on the security of the product is considered severe where (Art. 14(5)):

* it negatively affects or is capable of negatively affecting the ability of the product to protect the availability, authenticity, integrity or confidentiality of sensitive or important data or functions, or
* it has led or is capable of leading to the introduction or execution of malicious code in the product or in the network and information systems of a user of the product.

Examples that **count**:

* Unauthorized access to SysReptor management systems that can expose or alter other customers' projects, notes, evidence, or encryption keys
* Tampering with a SysReptor release, Docker image, or PyPI `reptor` package so users could install attacker-controlled code
* Compromise of the build, signing, or update pipeline in a way that could ship malicious code to users
* Malicious code reaching a user's instance or workstation through SysReptor or reptor (for example a backdoored dependency that executes when reptor runs)

Examples that **do not count** as a CRA severe incident (still report internally):

* A pentest, bug-bounty, or researcher finding with no incident and no evidence of malicious exploitation
* A crash, performance issue, or planned downtime that does not weaken confidentiality, integrity, authenticity, or access control
* A lost company laptop, mail sent to the wrong person, or a SysLeaks-only event, unless it also compromises SysReptor or reptor
* A third-party CVE that cannot be exploited in SysReptor or reptor
* Customer misconfiguration of a self-hosted instance, with no product security failure on our side

If an actively exploited vulnerability comes from a third-party component and can be exploited in SysReptor or reptor, we notify it. If it cannot be exploited in our product, Art. 14 is not mandatory. Still report it to the component maintainer.

### Inform users

After becoming aware of an actively exploited vulnerability or a severe incident, directors inform the impacted users or, where appropriate, all users of SysReptor or reptor in a timely manner about (Art. 14(8)):

* The vulnerability or incident
* Where necessary, any risk mitigation and corrective measures that users can deploy
* Where appropriate, the same information in a structured, machine-readable format that is easily automatically processable
  * GitHub provides a machine-readable format for published advisories (e.g., <https://api.github.com/repos/Syslifters/sysreptor/security-advisories/GHSA-x3m3-v8pv-442r>)

Do not wait for a full write-up if users can already mitigate. If we fail to inform users in a timely manner, the notified CSIRT may inform them.

Where necessary, the designated CSIRT may request an intermediate report on relevant status updates (Art. 14(6)). Provide it.

### Submit to the CSIRT and ENISA

Directors submit via the SRP. Select [CERT.at](https://www.cert.at/) as the CSIRT designated as coordinator for our main establishment in Austria. The submission is simultaneously available to ENISA.

Submitters need an [EU Login](https://ecas.ec.europa.eu/cas/login) and must register as Assigned Representatives on the SRP.

If the SRP is temporarily unavailable, wait until it is back and then submit. If immediate communication is necessary, contact CERT.at directly, then still submit through the SRP once it is available.

If dissemination would increase security risk, mark how sensitive we consider the notified information in the 72-hour notification. The receiving CSIRT can delay dissemination in particularly exceptional circumstances.

#### Actively exploited vulnerability

| Deadline | Submit |
| --- | --- |
| **24 hours** after awareness (Art. 14(2a)) | Early warning, indicating where applicable the Member States where the product has been made available |
| **72 hours** after awareness (Art. 14(2b)) | Vulnerability notification, unless already provided: general information about the affected product, general nature of the exploit and vulnerability, corrective or mitigating measures taken, measures users can take, and how sensitive we consider the notified information |
| **14 days after** a corrective or mitigating measure is available (Art. 14(2c)) | Final report, unless already provided: description of the vulnerability, severity and impact, available information about any malicious actor that has exploited or is exploiting it, and details of the security update or other corrective measures made available |

#### Severe incident

| Deadline | Submit |
| --- | --- |
| **24 hours** after awareness (Art. 14(4a)) | Early warning including at least whether the incident is suspected of being caused by unlawful or malicious acts, and where applicable the Member States where the product has been made available |
| **72 hours** after awareness (Art. 14(4b)) | Incident notification, unless already provided: general information about the nature of the incident, an initial assessment, corrective or mitigating measures taken, measures users can take, and how sensitive we consider the notified information |
| **One month after** the 72-hour incident notification (Art. 14(4c)) | Final report, unless already provided: detailed description including severity and impact, the type of threat or root cause that is likely to have triggered it, and applied and ongoing mitigation measures |

## Records, recovery, and review

Directors or the DPO create a new SysReptor project at [syslifters.sysre.pt](https://syslifters.sysre.pt/) for each incident and keep the timeline, decisions, and notifications there. Include GDPR notifications, CRA SRP submissions and identifiers, and product-user notices.

Restore systems only after access is re-checked. Fix the cause, not only the symptom. Add a short post-incident note to the project.

This process is reviewed annually, after a real incident, or after a legal change.

## Further reading

* [ENISA Single Reporting Platform](https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp)
* [ENISA CRA SRP Factsheet](https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA_CRA_SRP_Factsheet_v1.0_0.pdf)
* [ENISA CRA SRP FAQs](https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions)
* [European Commission FAQs on CRA implementation](https://ec.europa.eu/newsroom/dae/redirection/document/122331)

Last reviewed: 03/09/2026
