# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation project for creating an instruction manual for the on-premise version of "Цифровой РОП" (Digital SOP) system deployed at Setl Group. The system analyzes phone calls using AI against company checklists.

## Project Structure

- **СКРИНШОТЫ/** - Contains all screenshots organized by sections
  - 0. Вход - Login/authentication screens
  - 1. Аналитика - Analytics sections (Коммуникации, Менеджеры, Тесты)
  - 2. Графики - Charts and visualizations (Менеджеры, Оценка, Статус тестов, Динамика тестов)
  - 3. Таблицы - Custom analytics tables with AI prompts
  - 4. Другое - Additional tools (Статистика файлов, Чат с ИИ)
  - 5. Настройки - System configuration (Офисы и руководители, Подключение, Пользователи, Скрипты и промты, Таблицы)
  - 6. Доп. Настройки - Additional settings (Слова-паразиты)

- **Части_инструкции/** - Documentation parts being created
  - Files are named with format: `XX_Section_Name.md`
  - These will be combined into a final Word document
  - **All sections completed** ✅: 
    - 00_Вход.md
    - 01_Аналитика_Коммуникации.md
    - 01_Аналитика_Менеджеры.md
    - 01_Аналитика_Тесты.md
    - 02_Графики_Менеджеры.md
    - 02_Графики_Динамика_тестов.md
    - 02_Графики_Оценка.md
    - 02_Графики_Статус_тестов.md
    - 03_Таблицы.md
    - 04_Другое.md
    - 05_Настройки_Офисы_и_руководители.md
    - 05_Настройки_Подключение.md
    - 05_Настройки_Пользователи.md
    - 05_Настройки_Скрипты_и_промты.md
    - 05_Настройки_Таблицы.md
    - 06_Доп_Настройки_Слова_паразиты.md

- **Тех чат (экспорт)/** - Technical chat export with API documentation (result.json)
- **ТЗ Версия 4/** - Technical specification document (.docx format, use Python extraction method)

## Key System Information

- **System URL**: http://10.28.32.81/
- **Login URL**: http://10.28.32.81/login
- **API Key**: LS6gz1bkpG3lZI6uXetEoLtoVtVXYuWO
- **Super Admin**: Дмитрий Авдеев
- **Authentication**: LDAP integration with Setl Group CRM

## API Endpoints

### Incoming (CRM → Цифровой РОП)

1. **Audio Upload**: `POST http://10.28.32.81/api/v1/calls/audio-upload?apiKey={API_KEY}`
   - Fields: manager_id, call_id, deal_id, deal_stage_id, audio_url
   
2. **Office Update**: `POST http://10.28.32.81/api/v1/settings/offices-update?apiKey={API_KEY}`
   - Structure: offices array with office_title, office_id, leader_ids[], managers_ids[]
   
3. **Managers Update**: `POST http://10.28.32.81/api/v1/settings/managers-update?apiKey={API_KEY}`
   - Structure: managers array with manager_id, name, surname, middlename
   
4. **Table Ready Check**: `GET http://10.28.32.81/api/v1/tables/call-ready?tab={TABLE_ID}&call={CALL_ID}`

### Outgoing Webhooks (Цифровой РОП → CRM)

- Two types: checklist results and analytics results
- Checklist webhook: configured in Scripts and Prompts settings
- Analytics webhooks: configured individually per table
- Results contain structured data based on configured prompts

## Development Environment

### Setup Commands
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**⚠️ IMPORTANT**: Always activate the virtual environment (`source venv/bin/activate`) before running any scripts. The prompt should show `(venv)` prefix.

### Dependencies
- **python-docx==1.1.0** - Core library for Word document generation
- **Pillow==10.3.0** - Image processing for screenshot insertion

### Reference Implementation
The `python-docx-examples/` folder contains the full python-docx library source with examples. Useful for:
- Advanced formatting techniques
- Understanding docx internals
- Finding undocumented features

### Word Document Generation System

**Main Generator**: `scripts/generate_instruction.py`
- Converts markdown documentation to professional Word document
- Supports incremental generation with progress tracking
- Includes corporate styling and professional formatting
- Automatic image insertion from screenshot directories

**Key Commands**:
```bash
# Generate full instruction manual
python scripts/generate_instruction.py

# Generate specific sections only
python scripts/generate_instruction.py --sections intro analytics

# Force regeneration of all content
python scripts/generate_instruction.py --force

# Reset progress and start fresh
python scripts/generate_instruction.py --reset

# List available sections
python scripts/generate_instruction.py --list
```

**Available Sections**:
- `intro` - Quick start guide for new users
- `analytics` - Core analytics features (communications, managers, tests)
- `charts` - Data visualization sections
- `tables` - Custom analytics table configuration
- `tools` - Additional tools (file statistics, AI chat)
- `settings` - System administration (offices, connections, users, scripts)
- `additional` - Advanced settings (word parasites detection)
- `processes` - Business process flows
- `examples` - Role-based usage scenarios and FAQ
- `technical` - API documentation and troubleshooting

### Generator Architecture

**InstructionGenerator Class Key Methods**:
- `setup_document_styles()` - Configures corporate colors, fonts, and spacing
- `create_document()` - Builds title page with company information  
- `add_table_of_contents()` - Generates structured TOC with Word automation instructions
- `add_section_to_doc()` - Processes markdown sections with intelligent parsing
- `read_part_content()` - Handles missing files gracefully with placeholder messages (checks for `*_NEW.md` files first)
- `add_interface_block()` - Creates blue-bordered blocks for UI descriptions
- `add_technical_block()` - Creates orange-bordered blocks for technical details

**Markdown Processing Features**:
- Screenshot reference detection and formatting
- URL and code highlighting with monospace fonts
- Multi-level list handling with proper indentation
- Important note styling for warnings and technical details
- Automatic paragraph justification for professional appearance

## Documentation Standards

### Special Formatting Tags:
- `{INTERFACE}` - Creates blue-bordered blocks for UI descriptions
- `{TECHNICAL}` - Creates orange-bordered blocks for technical details
- Use these tags to highlight important interface or technical information

### Screenshot Naming Convention:
- `Section. Description.png`
- Always reference as: `**Screenshot_Name.png** - Brief description`

### Section Structure Template:
1. **Title** - Clear section name
2. **Overview screenshot** - Main interface view  
3. **Purpose** - What this section is for
4. **Key features** - Bulleted list
5. **Step-by-step guides** - With numbered screenshots
6. **Related sections** - Cross-references

## System Features to Document

- Call analysis with AI against company checklists
- Manager performance tracking and scoring (rating from maximum possible)
- Test generation based on errors (one test per call, based on checklist stages)
- Custom analytics tables with AI prompts
- Conversion tracking (configured via prompts)
- LDAP-based role management (managers, office leaders, super admin)
- Word-parasite detection with red highlighting in transcripts
- Integration with Setl Group CRM via API

## Important Context

- This is an on-premise installation (not cloud)
- System is specifically configured for Setl Group
- Documentation should reflect the actual deployed system at 10.28.32.81
- All examples should use real data visible in screenshots
- Tests require manager approval before being sent to employees
- Rating system: actual points earned out of maximum possible (e.g., 16 out of 20)
- One test is generated per call even if multiple errors exist
- Role-based access: Administrators (full access), Office Leaders (office data + test approval), Managers (own data only)
- Tags system for call classification (configured via prompts in Settings)

## System Flow Architecture

1. **Audio Input**: CRM → API → Digital ROP
2. **Processing**: 
   - Transcription
   - Checklist analysis (configured in Settings → Scripts)
   - Custom analytics (configured in Settings → Tables)  
   - Word-parasite detection (configured in Additional Settings)
3. **Output**:
   - Test generation (requires approval)
   - Analytics dashboards
   - Webhook notifications to CRM

## Current Architecture

### Document Generation Pipeline
1. **Source Content**: Markdown files in `Части_инструкции/` reference screenshots by name
2. **Screenshot Organization**: Hierarchical structure in `СКРИНШОТЫ/` matches system navigation
3. **Generation Engine**: `InstructionGenerator` class processes markdown and applies corporate styling
4. **Progress Tracking**: JSON-based incremental generation prevents duplicate work
5. **Output**: Professional Word document with proper formatting, styles, and structure

## File Processing

### File Naming Convention for Updates
When updating documentation sections, the generator checks for `*_NEW.md` files first. This allows you to:
- Create updated versions without overwriting originals
- Test changes before replacing production files
- Example: `01_Аналитика_Коммуникации_NEW.md` will be used instead of `01_Аналитика_Коммуникации.md`

### Reading .docx files:
```python
python3 -c "
import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile('path/to/file.docx', 'r') as docx:
    content = docx.read('word/document.xml')
root = ET.fromstring(content)
text_parts = []
for elem in root.iter():
    if elem.text:
        text_parts.append(elem.text)
full_text = ' '.join(text_parts)
print(full_text[:5000])  # First 5000 chars
"
```

### Using TodoWrite tool:
- Always track progress with TodoWrite tool for multi-step tasks
- Mark tasks in_progress when starting, completed when finished  
- Keep only one task in_progress at a time
- Use for document corrections and content validation tasks

## Complete Documentation Sections

### All Required Sections Now Available:
1. ✅ **00_Что_такое_Цифровой_РОП.md** - System overview and value proposition
2. ✅ **00_Первые_5_минут.md** - New user onboarding flow
3. ✅ **00_Интерфейс_и_навигация.md** - UI navigation guide
4. ✅ **00_Роли_и_права_доступа.md** - Permission system explanation
5. ✅ **08_Полный_цикл_обработки_звонка.md** - End-to-end call processing workflow
6. ✅ **08_Процесс_создания_тестов.md** - Test generation and approval process
7. ✅ **03_Создание_промтов_пошагово.md** - AI prompt creation tutorial
8. ✅ **09_Сценарии_для_ролей.md** - Role-specific usage patterns
9. ✅ **09_FAQ.md** - Common questions and troubleshooting
10. ✅ **10_Словарь_терминов.md** - Technical terminology glossary

### Advanced Formatting System:
- **JSON Screenshot Mapping**: `scripts/screenshot_mapping.json` provides exact image paths
- **Markdown Processing**: Intelligent parsing with bold text preservation (`**text**`)
- **Special Block Formatting**: `{INTERFACE}` and `{TECHNICAL}` tags create bordered blocks with corporate colors
- **Visual Borders**: Full-height table borders (blue for interface, orange for technical) 
- **Code Block Styling**: API endpoints in gray background tables
- **Corporate Colors**: Setl Group red (#ed1c24) for headings, proper color hierarchy
- **Progress Tracking**: `scripts/progress.json` enables incremental generation

## ✅ ЗАВЕРШЕНО: Исправление всех основных разделов по эталону "Коммуникации"

### Что было сделано:

**1. Раздел "Коммуникации" (эталон):**
- Убраны все выдумки: гиперссылки на менеджеров, сортировка, "запоминание позиции"
- Добавлены {INTERFACE} блоки с синими границами (4 блока)
- Добавлены {TECHNICAL} блоки с оранжевыми границами (1 блок)
- Создана система гиперссылок на связанные разделы
- Раздел "См. также" с полной навигацией

**2. Исправлены по тому же образцу:**
- ✅ **01_Аналитика_Менеджеры.md** - убраны выдумки про интерактивность, добавлены блоки и гиперссылки
- ✅ **01_Аналитика_Тесты.md** - структурированы блоки, добавлена навигация
- ✅ **02_Графики_Менеджеры.md** - убраны выдумки про интерактивную легенду
- ✅ **03_Таблицы.md** - убраны примеры конкретных данных, добавлены технические блоки
- ✅ **04_Другое.md** - структурировано содержание, добавлена навигация

### Принципы исправления (применены ко всем разделам):

1. **Убрать выдумки** - только факты, видимые на скриншотах
2. **Добавить форматирование:**
   - {INTERFACE} блоки для описания интерфейса
   - {TECHNICAL} блоки для технических деталей
3. **Добавить навигацию:**
   - Гиперссылки в тексте на связанные разделы
   - Раздел "См. также" с перекрестными ссылками
4. **Структурировать контент** - логичные заголовки и описания

### Результат:

- Все разделы аналитики теперь соответствуют качеству эталона
- Система генерации успешно обрабатывает {INTERFACE} и {TECHNICAL} блоки
- Создана единообразная навигационная система
- Документация стала точной и профессиональной

## ✅ ФИНАЛЬНЫЕ ИСПРАВЛЕНИЯ (17.09.2025)

### Устранены проблемы пользователя:

**1. Убраны серые API endpoints из раздела "Примеры качественных промтов":**
- ✅ Найдены и заменены блоки кода (```) на {TECHNICAL} блоки
- ✅ Убраны серые прямоугольники из файла 03_Создание_промтов_пошагово.md
- ✅ Примеры промтов теперь в едином стиле с остальными разделами

**2. Исправлена система гиперссылок:**
- ✅ Улучшен код обработки гиперссылок в generate_instruction.py
- ✅ Добавлен метод _create_internal_hyperlink для реальных Word ссылок
- ✅ Обновлен hyperlink_mapping.json с правильными заголовками
- ✅ Гиперссылки теперь стилизованы синим цветом с подчеркиванием

**3. Добавлена нумерация заголовков:**
- ✅ Исправлен заголовок "# 3. Создание промтов пошагово"
- ✅ Обновлен соответствующий маппинг в hyperlink_mapping.json
- ✅ Обеспечено соответствие между якорями ссылок и заголовками

**4. Обновлен CLAUDE.md:**
- ✅ Задокументированы все основные изменения
- ✅ Добавлены примеры кода и архитектурные решения
- ✅ Описаны процессы генерации документации

## ✅ ИТОГОВЫЕ УЛУЧШЕНИЯ (17.09.2025)

### Финальная доработка документации:

**1. Убраны все маркеры [ТРЕБУЕТ УТОЧНЕНИЯ]:**
- ✅ Из файла 09_FAQ.md убран маркер в контактной информации
- ✅ Из файла 10_Словарь_терминов.md убраны все маркеры и заменены реальными определениями
- ✅ Добавлены конкретные определения для терминов CRM, организационной структуры и продуктовых терминов

**2. Добавлена контактная информация:**
- ✅ Telegram: @tchashchin
- ✅ Телефон: +79670047879
- ✅ Ссылка на техническую поддержку: BVMax (https://bvmax.ru)
- ✅ Информация о заказчике: Setl Group

**3. Добавлены ссылки на сайты:**
- ✅ В начало документа добавлены ссылки на сайт заказчика [Setl Group](https://setlgroup.ru) 
- ✅ Добавлена ссылка на разработчика [BVMax](https://bvmax.ru)
- ✅ Обеспечена единообразная подача информации о системе

**4. Улучшена система таблиц:**
- ✅ Добавлен парсинг Markdown таблиц в Word документ
- ✅ HTTP коды ответов и форматы данных API теперь отображаются как таблицы
- ✅ Улучшено визуальное восприятие технической документации

### Результат финальной доработки:

- **Полная готовность документации** - убраны все плейсхолдеры и технические заметки
- **Профессиональное оформление** - добавлены реальные контакты и ссылки
- **Техническое совершенство** - корректная обработка таблиц и гиперссылок
- **Соответствие корпоративным стандартам** - единый стиль и профессиональная подача

### Архитектура генератора (итоговое состояние):

**Основные компоненты:**
- `generate_instruction.py` - главный генератор с поддержкой таблиц и гиперссылок
- `hyperlink_mapping.json` - маппинг ссылок на точные заголовки
- `progress.json` - система отслеживания прогресса генерации
- `screenshot_mapping.json` - точные пути к изображениям

**Поддерживаемые форматы:**
- {INTERFACE} и {TECHNICAL} блоки с цветными границами
- Markdown таблицы → Word таблицы с форматированием
- Внутренние гиперссылки с закладками
- Корпоративное стилевое оформление
- ✅ Добавлена информация о финальных исправлениях
- ✅ Задокументированы все изменения для будущих сессий

### Финальное состояние проекта:
- 📄 **Документ готов**: "Финальная_инструкция.docx" с корректным форматированием
- 🔗 **Гиперссылки работают**: система маппинга обеспечивает точные ссылки
- 🎨 **Профессиональное оформление**: корпоративные цвета и стили Setl Group
- 📋 **Убраны технические детали**: API endpoints вынесены в отдельный раздел

## ✅ ПРОЕКТ ЗАВЕРШЕН: Финальная инструкция готова (обновлено)

### Финальные исправления (последняя итерация):

**1. Критические исправления по замечаниям пользователя:**
- ✅ Исправлен раздел "Интерфейс и навигация" по эталону "Коммуникации" с {INTERFACE}/{TECHNICAL} блоками
- ✅ Исправлен раздел "Роли и права доступа" - убраны ИИшные заголовки на фактические
- ✅ Убраны API ключи из пользовательских разделов (заменены на ссылки)
- ✅ Исправлена функция генерации для обработки гиперссылок в спец блоках
- ✅ Удалены все проблемные паттерны ["текст"](#ссылка) - заменены на [текст](#ссылка)

**2. Исправления в коде генератора:**
- ✅ Функция `_add_formatted_text_to_paragraph` теперь обрабатывает гиперссылки
- ✅ Все спец блоки {INTERFACE} и {TECHNICAL} поддерживают внутренние ссылки
- ✅ Система создает настоящие Word XML гиперссылки с рабочими закладками

**3. Финальная генерация документа:**
- ✅ **Финальная_инструкция.docx** - обновленный документ с исправлениями
- ✅ Все проблемы с гиперссылками устранены
- ✅ API ключи убраны, заменены ссылками на техническую документацию
- ✅ Добавлена рабочая гиперссылка из раздела "Подключение" на API документацию

**4. Качественные улучшения:**
- ✅ Заголовки приведены к фактическому стилю (убраны ИИшные "Типы ролей в системе")
- ✅ Все разделы теперь следуют единому эталону раздела "Коммуникации"
- ✅ Профессиональный тон без теоретических рассуждений ИИ
- ✅ Точное соответствие функционалу, видимому на скриншотах

### Результат:
**Финальная_инструкция.docx** - профессиональная интерактивная инструкция с:
- 📖 Полным описанием системы "Цифровой РОП" 
- 🔗 Полностью рабочими гиперссылками между разделами и в спец блоках
- 🎨 Единым корпоративным дизайном по эталону
- ✅ Убранными API ключами из пользовательских разделов
- 🎯 Точным соответствием фактическому функционалу без ИИшных додумок
- 📝 Профессиональными {INTERFACE} и {TECHNICAL} блоками во всех разделах

## Quick Task Reference

- **Generate documentation**: Use `scripts/generate_instruction.py` with appropriate flags
- **Environment setup**: `source venv/bin/activate` before running scripts  
- **Test formatting**: Generate single sections for style verification with `--sections` flag
- **Progress tracking**: Monitor `scripts/progress.json` for completion status
- **Force regeneration**: Use `--force` flag to override existing progress
- **Content validation**: Always verify against actual screenshots in `СКРИНШОТЫ/`
- **Hyperlink validation**: Full document generation required for working cross-references

## Troubleshooting

### Common Issues:
- **Missing screenshots**: Check `scripts/screenshot_mapping.json` for correct paths
- **Formatting issues**: Ensure `{INTERFACE}` and `{TECHNICAL}` tags are at start of line
- **Progress problems**: Use `--reset` flag to clear progress and start fresh
- **Virtual environment**: Always activate venv before running scripts

### Debug Commands:
```bash
# Check available sections
python scripts/generate_instruction.py --list

# Generate with full output
python scripts/generate_instruction.py --force --sections intro

# Reset everything
python scripts/generate_instruction.py --reset
```