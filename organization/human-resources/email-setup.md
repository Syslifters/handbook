---
url: /organization/human-resources/email-setup.md
description: >-
  Configure email encryption (S/MIME) and legally required signatures/footers
  for eM Client, Nextcloud Mail, and Thunderbird.
---

# Email setup

## Email encryption

Emails are encrypted using S/MIME at the email gateway. Outgoing emails are signed and encrypted if the public key of the recipient is present. You cannot control signing and encryption from your email client.

Test (e.g. with your colleagues) if email encryption and signing works. It should work out of the box if we have acquired a certificate for your user account.

## Email footers

Email footers are [legally required](https://www.wko.at/internetrecht/das-korrekte-e-mail-impressum).\
The first email or the first reply to an email should include your email footer. This makes your contact details available to the recipients.\
Follow-up emails don't have to include an email signature.

### eM Client

1. Go to "Settings"
2. Go to "Mail" Menu
3. Go to "Templates and Signatures"
4. Import Sample Signatures
   * Sample email footers: Syslifters.html
   * Sample email footers with SysReptor: SysReptor.html
   * Sample email footers with SysLeaks: SysLeaks.html
5. Update the email footer/signature with your data
   * Your job title could be something like... `Security Penetration Tester`, `Pentester`, etc.

### eM Client (mobile)

1. QR Export your email footer in eM Client desktop
2. Go to "Settings" in eM Client on your phone
3. Click "import/export"
4. Scan the QR Code

### NextCloud

You can update your email footer in the [NextCloud mail app](https://cloud.syslifters.com/apps/mail/) via "Account Settings"/"Signatures".\
Copy and paste the signature below and update the data and the links.

> **ARON MOLNAR**
> CO-FOUNDER
> +43 660 923 40 60
> aron@syslifters.com
> [More about me...](https://handbook.syslifters.com/about-us/aron)[www.syslifters.com](https://www.syslifters.com)

### Thunderbird

Import the sample signatures from [eM Client](#em-client).

## Setting Nextcloud Talk as online Meeting provider

This works in eM Client only.

1. Hamburger Menu on the top left: `Settings -> Online Meetings -> Add`
2. Select "Nextcloud Talk" and when prompted for the URL enter: `https://cloud.syslifters.com`. Do **not** add a trailing slash, as the meeting URLs will not work!
3. Create a new app password in Nextcloud `Settings -> Security` and paste your credentials into eM Client.
