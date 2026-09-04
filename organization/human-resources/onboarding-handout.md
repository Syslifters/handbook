---
url: >-
  https://handbook.syslifters.com/organization/human-resources/onboarding-handout.md
description: >-
  Copy-pasteable boilerplate for new hires covering equipment confirmation,
  usage rules, and setup checklists for accounts, laptop, smartphone, and
  YubiKey.
---

# Onboarding handout (boilerplate)

## Confirmation

I confirm that I have received:

* Laptop (Model TODO) + Sleeve
* Smartphone (Model TODO)
* 2 Yubikeys

## Guidance

* The equipment and accounts must be used for work-related tasks only. Private usage is not allowed.
* If you lose equipment, please notify us immediately.

### Documentation

You find most of our documentation in our...

* [public handbook](https://handbook.syslifters.com/)
* [internal knowledge base](https://syslifters.sysre.pt/projects/5086e509-4fca-4d99-aa2a-404feeda69a7/notes/)

We are a [public first](https://handbook.syslifters.com/about-the-handbook) company and document everything in public, except if we have a good reason for keeping it private. Take your time to skim and read through topics that you find interesting.

We try to keep our documentation up to date. This is a shared responsibility. If you spot errors, find room for improvement, missing topics that should be documented, please feel empowered to update it.\
This is especially important, as you bring your own views and ideas into our company, while we might already be blind or act on unwritten conventions that you as our new colleague cannot know if undocumented.

You find the sources of our handbook in our [GitLab](https://gitlab.internal.syslifters.com/docs/public). Follow our [making changes](https://handbook.syslifters.com/making-changes) guide. If in doubt, ask your colleagues.

### Accounts

* Use new passwords for all accounts. Never reuse previously used passwords.
* Never use passwords of work-related accounts for private accounts.
* Use our password manager at https://vaultwarden.external.syslifters.com/
  * Never enter your password manager master password on private devices.
  * Optional: Create an emergency contact in Vaultwarden
* Use MFA for all accounts (incl. your password manager).
* Use both Yubikeys for all accounts to prevent lockout in case of loss.
* Do not store MFA data in your password manager.
* Use the following MFA mechanisms in descending order of preference:
  * FIDO2
  * Yubico OTP
  * TOTP

### Laptop

#### Usage

* We use local users for login
  * You are allowed to use biometrics (e.g., face, fingerprint)
* Sync your important data to NextCloud (e.g., specific folders)

#### Setup

* \[ ] Make sure the hard drive is encrypted using BitLocker and PIN (no TPM only)
* \[ ] Make sure AV/EDR (IKARUS/Harfanglabs) is installed and active
* \[ ] create a vaultwarden account at <https://vaultwarden.external.syslifters.com/>
* \[ ] Install the following software packages (or check if installed)
  * \[ ] Tailscale client for VPN (your client must be unlocked on the server on the first connection)
  * \[ ] Signal messenger
    * Connect with your work-related Signal account
  * \[ ] OnlyOffice Desktop App
  * \[ ] Docker Desktop
    * Needed for our "pentestbox". Follow [setup guide](https://handbook.syslifters.com/organization/human-resources/pentestbox-setup)
    * (incl. Microsoft WSL2)
  * \[ ] Burp Professional
    * \[ ] Install Extensions listed [here](https://handbook.syslifters.com/pentesting-manual/pentesting-toolset)
  * \[ ] YubiKey Authenticator
  * \[ ] emClient (recommended) or Thunderbird
    * Create app password via [email management](https://mail.internal.syslifters.com/)
    * Follow [setup guide](https://handbook.syslifters.com/organization/human-resources/email-setup)
  * \[ ] Claude Code CLI
    * Follow [setup guide](https://handbook.syslifters.com/organization/human-resources/ai-tool-setup)
  * \[ ] Set up "Project Sense" for project retention
    * Follow [setup guide](https://handbook.syslifters.com/organization/human-resources/project-retention)

Additional optional software:

* Notepad++
* 7zip
* Python
* Visual Studio Code
* Cursor
* VirtualBox
* GNU Privacy Guard
* Meld
* Flameshot
* VLC media player
* Wireshark
* Microsoft Teams

### Smartphone

#### Usage

* Never mix private and work-related accounts
* Use MFA for Google, Samsung accounts (FIDO2)
* Use sensitive apps in the secure folder only
  * Password managers
  * Authenticator apps (Yubico Authenticator)
* Use disappearing messages in messengers
  * Also with customers
  * Four weeks by default
  * Max. 1 day for sensitive information (like passwords; less if possible)
* The device is not meant to be used as a device for pentesting apps
  * Do not install custom certificates or debugging tools for pentest purposes
  * Do not unlock the bootloader or root your device

#### Setup

* \[ ] Create a new work-related Play Store account
* \[ ] Create a new work-related Samsung account
* \[ ] Enable Secure Folders (Samsung Knox)
* \[ ] Install Signal messenger

### External drives

* You receive an external drive at request
* External drives (hard drives, USB drives, etc.) must be encrypted using BitLocker and a long-enough password
* Never connect your external hard drive at non-work-related devices or customer equipment if used for backups
* After connecting drives to potentially untrusted devices (e.g., customer equipment), consider formatting the device. In any case, change the BitLocker password if you entered it on the customer device.

### YubiKey

#### Usage

* Use PIV or GPG for SSH authentication (prefer PIV)
  * See our [setup guide](https://handbook.syslifters.com/organization/human-resources/yubikey-setup)
* Private keys should never leave the key
* Always setup both of your YubiKey:
  * One primary
  * One backup key
* Leave the backup key at your main work place (don't carry it to customers to lose both at the same time)
* Always use the longest possible key lengths
* Store secrets (PIN, PUK, etc) in Vaultwarden
* Add a password to protect TOTP accounts if you have any
* If you use the GPG module, change PIN, PUK and the admin key
* If you use the PIV module, change PIN, PUK and the management key

#### Setup

On both SSH keys:

* \[ ] [Verify your Yubikey](https://www.yubico.com/genuine/)
* \[ ] Set a FIDO2 PIN (via Yubico Authenticator/Passkeys)
* \[ ] Set PIV PIN, PUK and Management Key
* \[ ] Set GPG PIN, PUK, admin key
* \[ ] Generate certificates for SSH authentication (e.g., on slot 9a). Use [this](https://handbook.syslifters.com/organization/human-resources/yubikey-setup) guide.

## MISC

Do this, after you have completed this checklist:

* \[ ] Generate Archiving Key for Sysreptor [here](https://syslifters.sysre.pt/users/self/publickeys/) using the yubikey

## Links and resources

* Account management: https://login.syslifters.com/
* Password Manager: https://vaultwarden.external.syslifters.com/
* NextCloud (E-Mails, Files, Talk, etc.): https://cloud.syslifters.com/
* E-Mail account management: https://mail.internal.syslifters.com/
* Mailserver (SMTP/IMAP): mail.syslifters.com
* GitLab: https://gitlab.internal.syslifters.com/
* SysReptor: https://syslifters.sysre.pt
* LXCBox: https://lxcbox.internal.syslifters.com/
* PentestAI: https://pentestai.internal.syslifters.com/
* Handbook/Pentesting Manual: https://handbook.syslifters.com/pentesting-manual/
* Handbook/Organization: https://handbook.syslifters.com/organization/
