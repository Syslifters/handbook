---
url: >-
  https://handbook.syslifters.com/organization/human-resources/yubikey-pc-setup.md
description: >-
  Configure a PC to use an already provisioned YubiKey for PIV/SSH (Windows) and
  basic GPG/SSH agent use.
---

# YubiKey PC setup

Do this on every PC you use with your YubiKey (for example after getting a new machine). The key itself must already be provisioned: [YubiKey setup](./yubikey-setup).

## PIV

### Windows

Prerequisites:

* Install [OpenSC Library for PKCS11](https://github.com/OpenSC/OpenSC/releases/latest) ([Documentation](https://github.com/OpenSC/OpenSC/wiki))
* Install [YubiKey Manager CLI](https://github.com/Yubico/yubikey-manager/releases/latest)
* Yubico Authenticator
* Have your PIN ready (stored in Vaultwarden)
* Make sure OpenSC ignores Windows Hello (see [Troubleshooting](#troubleshooting) below)

1. Connect with ssh:

```
ssh -I "C:\Program Files\OpenSC Project\OpenSC\pkcs11\opensc-pkcs11.dll" user@IP
```

2. (Recommended) Add to your `~\.ssh\config` (create file if it doesn't exist):

```
PKCS11Provider "C:\Program Files\Yubico\Yubico PIV Tool\bin\libykcs11.dll"
```

#### Troubleshooting

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

Don't forget to touch your key when authenticating. If that does not help, the key may use an unsupported algorithm. See [Supported algorithms](./yubikey-setup#supported-algorithms) on the initial setup page.

#### Agent forwarding

You can forward the YubiKey's authentication capabilities to the remote server, so that you can use this server as a jump host to another remote destination.\
A classic example is developing on a remote machine and using SSH to push the changes to GitLab.

Your YubiKey must have been created with `pin-policy` set to `once` (not `always`). That is set during [initial setup](./yubikey-setup) and cannot be changed afterwards.

To enable agent forwarding you must load your SSH key into your agent using:

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

### Windows

#### Setup

1. Install gpg4win (Download here: [gpg4win](https://gpg4win.org/download.html))

2. After installing gpg4win you need to edit `C:\Users\<user>\AppData\Roaming\gnupg\gpg-agent.conf` and add following content:

```
enable-ssh-support
enable-putty-support
enable-win32-openssh-support
use-standard-socket
default-cache-ttl 600
max-cache-ttl 7200
```

3. Restart the gpg-connect-agent:

```
gpg-connect-agent killagent /bye
```

```
gpg-connect-agent /bye
```

4. Create a startup script to restart the agent after every login.
   The script must be placed under `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.\
   Startup script: [gpg-agent-login.cmd](/assets/gpg-agent-login.cmd)

```
@echo off
REM Runs after every Windows login.
REM Restarts gpg-agent: kill the old one, then start a fresh one.

set "GPG_CONNECT=C:\Program Files\GnuPG\bin\gpg-connect-agent.exe"

REM Give the user session a moment to finish starting.
timeout /t 3 /nobreak >nul

"%GPG_CONNECT%" killagent /bye
"%GPG_CONNECT%" /bye
```

#### Known Issues

* **Cloning repositories using SSH-Keys**

  The error message "`git@ssh.gitlab.internal.syslifters.com: Permission denied (publickey).`"
  most likely indicates that Git is using a different ssh command to clone the repo. However, verify first if authentication with the SSH-Key works.

  ```
  ssh -T git@ssh.gitlab.internal.syslifters.com
  ```

  If the server returns no errors, your authentication with a SSH-Key is working correctly. Overwrite the `core.sshCommand` setting for git:

  ```
  git config --global core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"
  ```

### Linux

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
