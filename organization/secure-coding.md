---
url: /organization/secure-coding.md
description: >-
  Secure coding requirements and OWASP checklist alignment for Syslifters
  projects.
---

# 👩‍💻 Secure Coding Policy

We adhere to the [OWASP Secure Coding Practices Checklist](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist) and improve security following a risk-based approach and continuous improvement process.

Additionally, the following requirements must be met:

* All API endpoints must be added to `test_api.py`
  * We limit endpoints to certain user permissions using `permission_classes` in `views.py`
  * This ensures that only users with defined permission levels can use the endpoints
  * If this is not possible, explicit test cases must be defined
* If users with the same permission level can use one endpoint, but only with a limited dataset (e.g., list their own projects, but not those of others), this must be covered by explicit test cases.
  * We limit the available dataset using `get_queryset` methods in `views.py` perferably using `only_permitted` methods (in `queryset.py`).

This policy applies to the projects:

* [SysReptor](https://docs.sysreptor.com/)
* [SysReptor Portal](https://sysreptor.com/)
* [SysLeaks](https://sysleaks.com/)

Last reviewed: 13/04/2026
