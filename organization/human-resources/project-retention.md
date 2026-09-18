---
url: >-
  https://handbook.syslifters.com/organization/human-resources/project-retention.md
description: >-
  Keep local pentest project files only as long as needed. Set up Project Sense
  to delete stale data after 90 days.
---

# Project retention

Customer and project data on your machine should not outlive its purpose. The [Pentest operation rules](/pentesting-manual/operation-rules) suggests a dedicated directory for local pentest files. Delete anything you no longer need.

## Project Sense

[Project Sense](https://gitlab.internal.syslifters.com/tools/project-sense) is a small tool for Windows, Linux, and macOS that watches configured directories and deletes stale content. It runs on a schedule and writes a log of what it deleted, skipped, or kept.

Each direct child folder of an observation root counts as one **project folder**. The tool deletes a project folder when all files inside are older than `MaxAgeDays` (90 by default), or when the folder is empty.

To keep a project longer, place an empty `SKIP_DELETION` file in the project folder root. The folder is then skipped until you remove that file. Delete this flag file if the project is no longer needed.

## Setup

### Windows

1. Clone the repository and open `config.json`.
2. Set `ObservationRoots` to the directory where you store pentest projects (absolute path).
3. Set `Logfile` to an absolute path where you want the run log (e.g. `C:\Logs\ProjectSense.log`).
4. Leave `MaxAgeDays` at `90` unless agreed otherwise with the team.
5. Test without deleting:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\ProjectSense.ps1 -ConfigPath config.json -WhatIf
```

6. Run once manually to confirm the log looks right:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\ProjectSense.ps1 -ConfigPath config.json
```

7. Register automatic runs at login: open `shell:startup`, create a shortcut with this target (adjust paths):

```
powershell.exe -ep Bypass -WindowStyle hidden C:\Path\To\ProjectSense\scripts\ProjectSense.ps1 -ConfigPath C:\Path\To\ProjectSense\config.json
```

Check the log file after the first scheduled run. Full configuration options and troubleshooting are in the [repository README](https://gitlab.internal.syslifters.com/tools/project-sense/-/blob/master/README.md).

### Linux

Prerequisites: `bash`, `jq`, and optionally `notify-send` for desktop notifications.

```bash
chmod +x scripts/project-sense.sh
./scripts/project-sense.sh --config config.json --what-if   # dry run
./scripts/project-sense.sh --config config.json             # run for real
```

Register a daily cron job, for example at 11:00. Use absolute paths:

```cron
0 11 * * * /full/path/to/scripts/project-sense.sh --config /full/path/to/config.json
```

See [`config.example.json`](https://gitlab.internal.syslifters.com/tools/project-sense/-/blob/master/config.example.json) in the repository for path examples.

### macOS

Prerequisites: `bash`, `jq`.

Cron jobs are unreliable on macOS, so use the LaunchAgent template in the repository instead.

Install Project Sense outside protected folders (`~/Documents`, `~/Desktop`, `~/Downloads`), for example `~/ProjectSense`. The same applies to `Logfile` and `ObservationRoots` in `config.json`.

1. Test without deleting:

```bash
chmod +x scripts/project-sense.sh
./scripts/project-sense.sh --config config.json --what-if
```

2. Run once manually to confirm the log looks right:

```bash
./scripts/project-sense.sh --config config.json
```

3. Edit [`launchd/com.project-sense.plist`](https://gitlab.internal.syslifters.com/tools/project-sense/-/blob/master/launchd/com.project-sense.plist): set the script and config paths. Keep `WorkingDirectory` as `/tmp`.
4. Install and load the LaunchAgent:

```bash
cp launchd/com.project-sense.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.project-sense.plist
```

5. Trigger a test run:

```bash
launchctl kickstart -k gui/$(id -u)/com.project-sense
```

The job runs daily at 11:00 while you are logged in. Debug output goes to `/tmp/project-sense.launchd.err.log`.

After changing the plist, reload it:

```bash
launchctl bootout gui/$(id -u)/com.project-sense
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.project-sense.plist
```

If the job fails, check the err log, use absolute paths everywhere, ensure the plist `PATH` includes `/opt/homebrew/bin` if you use Homebrew.

See [`config.example.json`](https://gitlab.internal.syslifters.com/tools/project-sense/-/blob/master/config.example.json) in the repository for path examples.

## Before you rely on it

* Store pentest files only under your configured observation root(s).
* Run with `-WhatIf` / `--what-if` after changing `config.json` or moving projects.
* Review the log when a project you expected to keep was deleted (usually the newest file was still within 90 days, or `SKIP_DELETION` was missing).
* Remove customer data from other locations manually; Project Sense only watches the paths you configure.
