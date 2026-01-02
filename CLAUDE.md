# Project Overview

Personal resume website for Rick Muller at https://rmuller.net

## Tech Stack

- **Templating**: Pystache (Mustache templates for Python)
- **CSS Framework**: Bootstrap 5.3.8
- **Icons**: Font Awesome 6.3.0
- **Build**: Python script + Makefile
- **Hosting**: Static HTML deployed via scp to mullermail.xyz

## Project Structure

- `rpmuller.py` - Data and build script. Contains resume content (jobs, education, publications) and renders all templates.
- `template.html` - Main template (single-page with fixed navbar)
- `template.sidebar.html` - Alternative layout with left sidebar
- `template.right.sidebar.html` - Alternative layout with right sidebar
- `template.md` - Markdown version of resume
- `rpmuller.html` - Generated output (deployed to server)
- `Makefile` - Build and deploy commands

## Common Commands

```bash
make          # Build and deploy
make build    # Build only (runs rpmuller.py)
make install  # Deploy only (scp to server)
```

## Template Variables

All templates use Mustache syntax. Key variables defined in `rpmuller.py`:
- `{{Name}}`, `{{PageTitle}}`, `{{PageSummary}}`
- `{{HomeURL}}`, `{{ScholarURL}}`, `{{LinkedInURL}}`, `{{GithubURL}}`, `{{TwitterURL}}`
- `{{NPubs}}`, `{{HIndex}}`
- `{{#Jobs}}...{{/Jobs}}`, `{{#Schools}}...{{/Schools}}`
- `{{#QuantumPapers}}`, `{{#TheoryPapers}}`, `{{#MaterialsPapers}}`

## Notes

- Always run `make` after template changes to regenerate and deploy
- The main deployed template is `template.html`; sidebar variants are alternatives
- Bootstrap integrity hashes must match the version - get from https://getbootstrap.com/docs/5.3/getting-started/download/
