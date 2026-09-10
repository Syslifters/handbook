---
url: 'https://handbook.syslifters.com/organization/human-resources/yubikey-setup.md'
description: One-time setup of a YubiKey for PIV/SSH (key generation and certificate).
---

# YubiKey setup

Do this once when you receive a new YubiKey. After that, configure each PC separately: [YubiKey PC setup](./yubikey-pc-setup).

Verify that you have a [genuine YubiKey](https://www.yubico.com/genuine/).

## PIV

Prerequisites:

* Install [YubiKey Manager CLI](https://github.com/Yubico/yubikey-manager/releases/latest)
* Have your PIN and Management Key ready (store in Vaultwarden)
* Use a supported algorithm (see [Supported algorithms](#supported-algorithms) below)

You must set your `pin-policy` at key creation. You cannot change it afterwards (you must create new keys). Use `once` (not `always`) if you need [agent forwarding](./yubikey-pc-setup#agent-forwarding).

1. Generate a keypair (select one of the working algos: prefer `eccp384` over `rsa3072` over `rsa2048`):

```
ykman piv keys generate --touch-policy never --pin-policy once -a eccp384 9a pubkey.pem
```

2. Create a self signed cert based on this key:

```
ykman piv certificates generate 9a pubkey.pem --subject "CN=SSH Key" --valid-days 36500
```

3. On a PC with OpenSC installed (see [YubiKey PC setup](./yubikey-pc-setup)), retrieve your public key and add it to `~/.ssh/authorized_keys` on the remote host:

```
ssh-keygen -D "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll"
```

### Supported algorithms

Known working algos are:

* rsa1024 (probably, pls don't use)
* rsa2048 (default)
* rsa3072
* eccp384 (sign-only, no de/encryption, prefer this for ssh)

Unsupported (or known to fail):

* rsa4096
* ed25519
* x25519 (failed on certificate creation)

## GPG

### Create OpenPGP Key

You can create a GPG-Key (e.g. for Sysreptor Archiving) as described here: [Archiving | SysReptor](https://docs.sysreptor.com/insights/archiving#how-to-use) (Tab: "Generate private keys on YubiKey 5").

List your Public-Key with

```
ssh-add -L
```

If the command returns "`The agent has no identities.`", make sure you complete the [YubiKey-PC-Setup](./yubikey-pc-setup#gpg) first.

For every Key you want to use as a SSH-Key add its Keygrip to `C:\Users<user>\AppData\Roaming\gnupg\sshcontrol`.
![Add Keygrip to sshcontrol file](/images/yubikey_gpg_keygrip.png).
