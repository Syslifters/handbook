---
url: /organization/human-resources/yubikey-setup.md
description: >-
  Setup guide for using a YubiKey for PIV/SSH (Windows) and basic GPG/SSH agent
  configuration.
---

# YubiKey setup

## PIV

### Windows

Prerequisites:

* Install [OpenSC Library for PKCS11](https://github.com/OpenSC/OpenSC/releases/latest) ([Documentation](https://github.com/OpenSC/OpenSC/wiki))
* Install [Yubikey Manager CLI](https://github.com/Yubico/yubikey-manager/releases/latest)
* Yubico Authenticator
* Have your PIN and Management Key ready (store in Vaultwarden)
* Make sure, OpenSC ignores Windows Hello (see Troubleshooting below)
* Make sure, you use supported algorithms (see Troubleshooting below)

***

1. Generate a keypair (select one of the working algos: prefer `eccp384` over `rsa3072` over `rsa2048`):

```
ykman piv keys generate --touch-policy never --pin-policy once -a eccp384 9a pubkey.pem
```

2. Create a self signed cert based on this key:

```
ykman piv certificates generate 9a pubkey.pem --subject "CN=SSH Key" --valid-days 36500
```

3. Retrieve your public key and add to `~/.ssh/authorized_keys` on the remote host:

```
ssh-keygen -D "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll"
```

4. Connect with ssh:

```
ssh -I "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll" user@IP
```

5. (Recommended) Add to your `~\.ssh\config` (create file if it doesn't exist):

```
PKCS11Provider "C:\Program Files\Yubico\Yubico PIV Tool\bin\libykcs11.dll"
```

#### Troubleshooting

***

##### Windows Hello

It is possible that OpenSC recognizes "Windows Hello" as its own device, thus you extract its RSA key. To prevent this, modify `C:\Program Files\OpenSC Project\OpenSC\opensc.conf` to:

```
app default {
	# debug = 3;
	# debug_file = opensc-debug.txt;
	ignored_readers = "Windows Hello" ; # Ignore all readers containing "Windows Hello"
}
```

To list all devices, run `& "C:\Program Files\OpenSC Project\OpenSC\tools\opensc-tool.exe" --list-readers` (PowerShell).

##### Error: signing failed for RSA "PRIV AUTH pubkey: error in libcrypto"

Don't forget to youch your key, when authenticating ;). It may be possible that you use unsupported algos, such as:

* rsa4096
* ed25519
* x25519 (failed on certificate creation)

Known working algos are:

* rsa1024 (probably, pls. don't use)
* rsa2048 (default)
* rsa3072
* eccp384 (sign-only, no de/encryption, prefer this for ssh)

#### Agent forwarding

You can forward the YubiKey's authentication capabilities to the remote server, so that you can use this server as a jump host to another remote destination.\
A classic example is developing on a remote machine and using SSH to push the changes to GitLab.

You must set your `pin-policy` to `once` (not `always`). You cannot change this setting after key creation (you must create new keys).

To enable agent forwarding you must load your SSH the key into your agent using:

```powershell
ssh-add -s "C:\Program Files\Yubico\Yubico PIV Tool\bin\libykcs11.dll"
```

You can check if this was successfull using `ssh-add -L` and, if necessary, clear the key using `ssh-add -D`.

Your client must know to which remote hosts it should forward the agent. Use `ssh -A user@ip` to forward the agent.
You can optionally add `ForwardAgent yes` to your `~\.ssh\config`, e.g.:

```
Host alias1 alias2
    HostName HostOrIp
    PKCS11Provider "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll"
    User username
    ForwardAgent yes
```

::: warning
Don't forward the agent to all destinations. Only to destinations where needed.
:::

Now the remote host also needs to accept your forwarded agent. Add `AllowAgentForwarding yes` to `/etc/ssh/sshd_config` on the remote host.
Reconnect and check if the agent was forwarded:

```bash
ssh-add -L
ssh-rsa AAAAB...
```

Your agent was forwarded successfully. You can now connect to other destinations from there. 🍵

### Linux

TODO\
See also: [YubiKey SSH guide](https://github.com/pavel-odintsov/yubikey-ssh)

## GPG

Setup only.

```
sudo apt update
sudo apt install -y \
  gnupg2 \
  gnupg-agent \
  scdaemon \
  pcscd \
  pcsc-tools \
  yubikey-personalization


sudo systemctl enable --now pcscd

~/.gnupg/gpg-agent.conf
enable-ssh-support
default-cache-ttl 600
max-cache-ttl 7200
pinentry-program /usr/bin/pinentry-gnome3

gpgconf --kill gpg-agent

in .bashrc /.zshrc
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)

gpgconf --launch gpg-agent
```

Certificate creation: TODO
