---
url: /making-changes.md
description: >-
  Guidelines for contributing changes to the handbook, including sensitivity and
  review expectations.
---

# Making changes

## Implement small changes immediately

Don't keep them for later (it won't happen). If you don't have the time to document a larger topic, consider [creating an issue](https://gitlab.internal.syslifters.com/docs/public/-/issues) to not forget about it.

The handbook doesn't have to include everything at once. Make small changes iteratively.

## Present large changes in the daily standup

If you make significant changes, or add large content pieces, please present them in our daily standup.

## Don't publish sensitive information

Our documentation should be public by default.\
However, don't add contents that:

* are out there on the Internet (rather add links)
* have copyright restrictions
* contain sensitive information, like
  * customer names or data (without agreement)
  * URLs or targets or our pentesting projects
  * security findings
  * personal information (without agreement)
  * data that might pose a relevant risk to us or our company.

Link to non-public content (like the [Syslifters Knowledge Base](https://syslifters.sysre.pt/projects/5086e509-4fca-4d99-aa2a-404feeda69a7/notes/)), if necessary.
If non-public documentation is non-public intentionally, document it there. In markdown files, use the frontmatter syntax, e.g.:

```yaml
---
note: Non-public due to copyright reasons
---
```

## Merge requests for change reviews

Create a new branch and ask for a merge request review from colleagues if:

* The contents might contain sensitive information, like
  * redacted screenshots (is there anything unredacted left)
  * shell commands (might contain sensitive options)
* The change contains significant changes in our working procedures.
* You are unsure, need further inputs, etc.
* Never merge data to the main branch that is not supposed to be public (yet).

## Use content pieces for documentation

Add your information to existing or new `.md` files. Add new markdown files to the correct directory (e.g., `/pentesting-manual/`, `/organization/`; otherwise the navigation in the sidebar breaks when opening the page).

All content files should have a frontmatter block, at least with a `title` and a `description` attribute:

```yaml
---
title: 
description: 
---
```

You can use AI to generate a suitable description. The description is used for html `meta` tags and in [llms.txt](/llms.txt). All titles and menu entries should be in sentence case.

Add `search: false` to frontmatter to exlude the page from the handbook search.

Images and files should have human-readable names. Images live in the /docs/public/images directory, binary files in /docs/public/assets.

## Use blog posts for short-lived information

The contents of handbook articles should kept up to date as long as it is feasible for us. If we want to publish contents that might change in the future, are one-shot initiatives, or it is foreseeable that we have no interest in keeping it up to date, we can publish the information as a [blog post](/blog/).

Blog posts have a timestamp and readers can judge for themselves if the content is up-to-date.\
We don't have a target of writing X blog posts per month.

Use or adapt the following prompt to generate a cover image (e.g., using Gemini 3.1 Pro):

```
Create a cover image in format 1920 x 1080px for this blog post.
* Monochrome minimalist vector illustration: black shapes on a light gray background with no color accents.
* Flat, high-contrast silhouettes: icons and symbols rendered as solid geometric forms.
* Modernist / Bauhaus-inspired: simple geometry, strong negative space, balanced composition.
* Poster/icon aesthetic: clean edges, minimal detail, a few abstract line/dot elements for texture and motion. 
* No text
```

Blog posts have the following frontmatter/metadata fields:

```
---
pageClass: blog-page
title: 
author: 
tags: 
date: YYYY-MM-DD
cover: /images/xyz.png
---
```

## How to implement a change

The easiest way to implement a change is to use the [GitLab web IDE](https://gitlab.internal.syslifters.com/-/ide/project/docs/public/edit/main/-/) (the link if for the main branch).

The contents are in `.md` files in the `/docs/` directory. Put images to `/docs/public/images/` and other files to `/docs/public/assets/`.\
Navigation and other site settings are in `/docs/.vitepress/config.ts`.

Fix typos and make small changes that don't need approval directly in the main branch. Create a new branch and a merge request for other changes.

You can also check out the project to your developer machine and run the dev server using `npm run de` (`npm run dev -- --host 0.0.0.0` to bind the port to all interfaces).

### Redirect after renaming files and directories

If you rename a files or a directory, make sure that the old path redirects to the new destination. Add the old and the new path to `/docs/redirects.txt` and VitePress will handle the redirect for you.
