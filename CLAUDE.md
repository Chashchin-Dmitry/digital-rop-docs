# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Documentation project for the cloud version of "Цифровой РОП" (Digital SOP) — an AI-powered phone call analysis platform.

**Platform URL:** https://rop.bvmax.ru/login
**Developer:** BVMax (https://bvmax.ru)

## Build and Generation Commands

```bash
# Setup (first time)
python3 -m venv venv
source venv/bin/activate
pip install python-docx Pillow

# Generate Word document
python scripts/generate_instruction.py

# Generate specific sections only
python scripts/generate_instruction.py --sections intro settings

# Force regeneration of all content
python scripts/generate_instruction.py --force

# Reset progress and start fresh
python scripts/generate_instruction.py --reset

# List available sections
python scripts/generate_instruction.py --list
```

## Architecture

### Document Generation Pipeline

1. **Source Content**: Markdown files in `Части_инструкции/` contain documentation text
2. **Screenshot Mapping**: `scripts/screenshot_mapping.json` maps screenshot names to file paths
3. **Hyperlink Mapping**: `hyperlink_mapping.json` maps anchor links to section headings
4. **Generator**: `scripts/generate_instruction.py` processes markdown → Word with corporate styling
5. **Output**: `Финальная_инструкция.docx` and `.pdf`

### Special Formatting Tags

In markdown files:
- `{INTERFACE}` — Creates blue-bordered blocks for UI descriptions
- `{TECHNICAL}` — Creates orange-bordered blocks for technical details

### Screenshot References

```markdown
**Screenshot Name.png**
```
Generator looks up actual path in `screenshot_mapping.json`.

### Internal Hyperlinks

```markdown
[link text](#anchor-name)
```
Generator creates Word bookmarks using `hyperlink_mapping.json`.

## Key Differences from On-Premise Example

The `ИНСТРУКЦИЯ - пример/` folder contains reference implementation for on-premise (Setl Group). This cloud version differs:
- Registration via Telegram bot (not LDAP)
- "История сделок" section (new)
- "Биллинг" section (new)
- No webhooks/API configuration
- Universal URL instead of internal IP

**Important:** Use example folder for architecture/formatting reference only. Do NOT copy content or screenshots.

## Section Naming Convention

Files in `Части_инструкции/`:
- `00_*` — Introduction, registration, first steps
- `01_*` — Settings (scripts, prompts, users, tables)
- `02_*` — Analytics (communications, managers, deals history)
- `03_*` — Charts
- `04_*` — Tests
- `05_*` — Billing
- `06_*` — FAQ
- `07_*` — Glossary

Files with `*_NEW.md` suffix take precedence over base files during generation.

## Support Contacts

- Telegram: @tchashchin
- Phone: +79670047879
