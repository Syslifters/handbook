---
url: 'https://handbook.syslifters.com/organization/secure-coding.md'
description: >-
  Secure coding requirements and OWASP checklist baseline for Syslifters
  projects.
---

# 👩‍💻 Secure Coding Policy

We use the [OWASP Secure Coding Practices Checklist](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist) as the baseline, then apply a risk-based approach and improve continuously.

See also [Information Security Policy](/organization/information-security-policy) and [incident response](/organization/incident-response).

Applies to anyone committing to [SysReptor](https://docs.sysreptor.com/), [SysReptor Portal](https://sysreptor.com/), [reptor](https://docs.sysreptor.com/cli/getting-started/), or [SysLeaks](https://sysleaks.com/).

Additionally, the following requirements must be met:

* Every API endpoint has automated authorization tests. In Django projects that means covering it in `test_api.py`, gating with `permission_classes` in `views.py`, and adding explicit tests when class-level permissions are not enough.
* If users with the same permission level can use one endpoint but only with a limited dataset (e.g., list their own projects, not those of others), cover that with explicit tests. In Django projects that means `get_queryset` in `views.py`, preferably using `only_permitted` (in `queryset.py`).
* Do not commit secrets. Tokens, keys, and connection strings stay out of git.
* Do not ship dependencies with known exploitable vulnerabilities. Patch or replace on a risk basis.

## Further conventions

* We use [ruff](https://open-vsx.org/extension/charliermarsh/ruff) for linting and formatting

Last reviewed: 03/09/2026
