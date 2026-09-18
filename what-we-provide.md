---
url: 'https://handbook.syslifters.com/what-we-provide.md'
description: >-
  Overview of Syslifters offensive security services, our efficient pentesting
  approach, and services we do not offer.
---

# What we provide

We provide offensive security services to customers in the DACH region and beyond. Our specialisations are internal enterprise networks (Active Directory, Entra ID and Azure cloud), external infrastructure and web security. With this clear focus we help you find and fix real risks.

We work efficiently (and keep your costs down) with a grey-to-white-box approach, a clear time box, and, where it makes sense, agreed leg-ups such as an assumed-breach starting point instead of lengthy and costly covert end-to-end campaigns.

## Services we offer

* [Assumed breach assessments](#assumed-breach-assessments)
* [Active Directory pentests](#active-directory-pentests)
* [Entra ID and Azure cloud assessments](#entra-id-and-azure-cloud-assessments)
* [External infrastructure pentests](#external-infrastructure-pentests)
* [Web application pentests](#web-application-pentests)
* [Attack detection & response tests](#attack-detection-response-tests)
* [Password analysis](#password-analysis)
* [Load tests](#load-tests)

### Assumed breach assessments

Tests from a starting point where an attacker might already be inside, for example a standard domain user, a compromised workstation, or an agreed internal foothold. The initial compromise phase is out of scope. From there we work towards the goals agreed for the scope, for example reaching domain admin, accessing a defined target system, or exfiltrating specific data. On request we can align techniques with known threat actor TTPs.

### Active Directory pentests

Pentests of on-prem and hybrid Active Directory environments. We look at the attack paths and misconfigurations that ransomware actors and attackers with an existing foothold (for example a compromised workstation or device) typically exploit. The outcome is a clear picture of how an attack would propagate from a single endpoint to your most sensitive systems.

### Entra ID and Azure cloud assessments

Identity and configuration review of Microsoft Entra ID and Azure, including hybrid scenarios where Entra ID and on-prem AD intersect. We assess identity risk, access policies and the attack paths between cloud and on-premises identities that real attackers use to move laterally and escalate privileges. The result shows how a compromised cloud account could affect your on-prem environment, and the other way around.

### External infrastructure pentests

Pentests of your external attack surface: exposed services, patching gaps, misconfigurations and paths into your environment. Often combined with Active Directory or Entra ID work for a full external-to-internal picture, so you see not only what is reachable from the internet but also where it leads inside.

### Web application pentests

Manual pentests of web applications and APIs, following common best practices such as the OWASP Testing Guide. We test at least grey-box with authenticated access and can extend to white-box with source code review when useful. Coverage focuses on findings that affect your specific risk model, including business logic, authentication and authorization, data handling and relevant integrations.

### Attack detection & response tests

Realistic attack techniques executed in your environment, so you can evaluate whether your SOC, SIEM and response processes detect and handle them. We coordinate closely with your blue team and report on which techniques were noticed, which were missed, and where detection rules could be tuned. The result is concrete, technique-level feedback for your detection engineering.

### Password analysis

Analysis of password hygiene, for example in Active Directory: weak passwords, common patterns, reuse and policy gaps. A focused, low-effort way to surface accounts and policies that need attention. Useful before or alongside a pentest, since weak credentials are still one of the most common starting points for real attacks.

### Load tests

Performance and stability tests of web applications under load, scoped separately from vulnerability testing and agreed in advance to avoid unintended impact. We help you understand how your application behaves under realistic and peak load, and where bottlenecks, errors or stability issues appear. A useful complement to security testing for applications that have to survive real user traffic.

## What we don't provide

We are experts in offensive security. Having the best knowledge in a domain makes focus mandatory.

This is why we don't provide:

* SOC/SIEM services
* Incident response
* ISMS consulting
* CISO as a service
* Awareness trainings

For services outside our scope we can recommend partners. We do not take referral fees.

## Further projects

Two products grew out of our daily pentest work and are run as separate services: SysReptor, our pentest reporting platform, and SysLeaks, our data leak monitoring service.
