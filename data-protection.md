---
url: 'https://handbook.syslifters.com/data-protection.md'
description: >-
  How we handle customer data and protect evidence, notes, and reports during
  pentests.
---

# Data protection and security

We manage our notes and reports in our self-developed pentest reporting solution SysReptor (which we distribute internationally to pentesting teams; source-available on [GitHub](https://github.com/syslifters/sysreptor/)). The assignment of permissions to projects always follows the need-to-know principle. Stored data such as images, evidence, and database entries are encrypted on the server side (Encrypted Data at Rest; see also the [SysReptor documentation](https://docs.sysreptor.com/setup/configuration/#data-encryption-at-rest)), and transmission (Data in Transit) is likewise encrypted (via TLS/HTTPS).

Three months after a (re-)test has been completed, the reports, notes, and evidence are encrypted and can only be restored using hardware tokens and a four-eyes principle (encryption utilizing Shamir's Secret Sharing algorithm; further information: <https://docs.sysreptor.com/insights/archiving/>), until they are automatically deleted upon expiration of our retention periods.

Communication between components of our internal networks is end-to-end encrypted (utilizing a Tailscale VPN; sometimes with multiple encryption layers).

We provide each pentester with a smartphone featuring a dedicated business number as well as a computer. Private use is prohibited for security and data protection reasons. Members of project teams communicate via Signal Messenger using disappearing messages. We protect company computers with IKARUS / HarfangLab (endpoint protection, detection, and vulnerability management).

All web pentest activities are logged via the pentesters' local proxy servers ([PortSwigger Burp](https://portswigger.net/burp)) and deleted three months after completion of the pentests or re-tests.

In addition, we have non-disclosure agreements in place with our employees.
