#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конвертер markdown файлов для MkDocs

Преобразует:
- {INTERFACE} → !!! interface "Интерфейс"
- {TECHNICAL} → !!! technical "Техническое"
- Скриншоты **Name.png** → ![Name](../images/name.png)
- Внутренние ссылки
"""

import os
import re
import shutil
from pathlib import Path
import json


class MkDocsConverter:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.source_path = self.base_path / "Части_инструкции"
        self.docs_path = self.base_path / "docs"
        self.images_path = self.docs_path / "images"
        self.screenshots_path = self.base_path / "СКРИНШОТЫ"

        # Загружаем маппинг скриншотов
        mapping_file = self.base_path / "scripts" / "screenshot_mapping.json"
        if mapping_file.exists():
            with open(mapping_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.screenshot_mapping = data.get('screenshot_mapping', {})
        else:
            self.screenshot_mapping = {}

        # Маппинг файлов на пути в docs/
        self.file_mapping = {
            "00_Что_такое_Цифровой_РОП": "start/about.md",
            "00_Регистрация_и_вход": "start/registration.md",
            "00_Первые_шаги": "start/first-steps.md",
            "01_Настройки_Шаблоны_скриптов": "settings/scripts-templates.md",
            "01_Настройки_Скрипты_и_промты": "settings/scripts-prompts.md",
            "01_Настройки_Конверсия": "settings/conversion.md",
            "01_Настройки_Дополнительные_промты": "settings/additional-prompts.md",
            "01_Настройки_Таблицы": "settings/tables.md",
            "01_Настройки_Пользователи": "settings/users.md",
            "02_Аналитика_Коммуникации": "analytics/communications.md",
            "02_Аналитика_История_сделок": "analytics/deals-history.md",
            "02_Аналитика_Менеджеры": "analytics/managers.md",
            "02_Аналитика_Таблицы": "analytics/tables.md",
            "03_Графики_Оценка": "charts/score.md",
            "03_Графики_Менеджеры": "charts/managers.md",
            "04_Тесты": "tests/index.md",
            "05_Биллинг": "billing/index.md",
            "06_FAQ": "faq.md",
            "07_Словарь_терминов": "glossary.md",
        }

        # Маппинг якорей на пути
        self.anchor_mapping = {
            "#что-такое-цифровой-роп": "start/about.md",
            "#регистрация-и-вход": "start/registration.md",
            "#первые-шаги": "start/first-steps.md",
            "#настройки-шаблоны-скриптов": "settings/scripts-templates.md",
            "#настройки-скрипты-и-промты": "settings/scripts-prompts.md",
            "#настройки-конверсия": "settings/conversion.md",
            "#настройки-дополнительные-промты": "settings/additional-prompts.md",
            "#настройки-таблицы": "settings/tables.md",
            "#настройки-пользователи": "settings/users.md",
            "#аналитика-коммуникации": "analytics/communications.md",
            "#аналитика-история-сделок": "analytics/deals-history.md",
            "#аналитика-менеджеры": "analytics/managers.md",
            "#аналитика-таблицы": "analytics/tables.md",
            "#графики-оценка": "charts/score.md",
            "#графики-менеджеры": "charts/managers.md",
            "#тесты": "tests/index.md",
            "#биллинг": "billing/index.md",
            "#faq": "faq.md",
            "#словарь-терминов": "glossary.md",
            "#шаблоны-скриптов": "settings/scripts-templates.md",
            "#скрипты": "settings/scripts-prompts.md",
            "#промты": "settings/additional-prompts.md",
            "#чек-листы": "settings/scripts-templates.md",
            "#таблицы": "settings/tables.md",
            "#пользователи": "settings/users.md",
            "#конверсия": "settings/conversion.md",
            "#коммуникации": "analytics/communications.md",
            "#звонки": "analytics/communications.md",
            "#менеджеры": "analytics/managers.md",
            "#история-сделок": "analytics/deals-history.md",
        }

    def copy_screenshots(self):
        """Копирует все скриншоты в docs/images/"""
        print("Копирование скриншотов...")
        self.images_path.mkdir(parents=True, exist_ok=True)

        copied = 0
        for name, rel_path in self.screenshot_mapping.items():
            source = self.base_path / rel_path
            if source.exists():
                # Создаём безопасное имя файла
                safe_name = self.make_safe_filename(name)
                dest = self.images_path / safe_name
                shutil.copy2(source, dest)
                copied += 1

        print(f"  Скопировано: {copied} файлов")

    def make_safe_filename(self, name):
        """Создаёт безопасное имя файла"""
        # Убираем проблемные символы
        safe = name.lower()
        safe = safe.replace(' ', '-')
        safe = safe.replace('ё', 'е')
        safe = re.sub(r'[^\w\-.]', '', safe)
        return safe

    def convert_content(self, content, current_file_depth=1):
        """Конвертирует контент markdown файла"""
        lines = content.split('\n')
        result = []

        i = 0
        while i < len(lines):
            line = lines[i]

            # Конвертируем {INTERFACE}
            if line.startswith('{INTERFACE}'):
                text = line[11:].strip()
                result.append('')
                result.append('!!! interface "Интерфейс"')
                result.append(f'    {text}')
                result.append('')
                i += 1
                continue

            # Конвертируем {TECHNICAL}
            if line.startswith('{TECHNICAL}'):
                text = line[11:].strip()
                result.append('')
                result.append('!!! technical "Техническое"')
                result.append(f'    {text}')
                result.append('')
                i += 1
                continue

            # Конвертируем скриншоты **Name.png**
            if '.png' in line and '**' in line:
                match = re.search(r'\*\*([^*]+\.png)\*\*', line)
                if match:
                    screenshot_name = match.group(1)
                    safe_name = self.make_safe_filename(screenshot_name)

                    # Определяем относительный путь к images
                    prefix = '../' * current_file_depth

                    result.append('')
                    result.append(f'![{screenshot_name}]({prefix}images/{safe_name})')
                    result.append(f'<figcaption>{screenshot_name}</figcaption>')
                    result.append('')
                    i += 1
                    continue

            # Конвертируем внутренние ссылки [text](#anchor)
            if '](#' in line:
                for anchor, path in self.anchor_mapping.items():
                    if anchor in line:
                        prefix = '../' * current_file_depth
                        line = line.replace(f'({anchor})', f'({prefix}{path})')

            result.append(line)
            i += 1

        return '\n'.join(result)

    def get_file_depth(self, path):
        """Возвращает глубину файла относительно docs/"""
        return path.count('/')

    def convert_file(self, source_name, dest_path):
        """Конвертирует один файл"""
        source_file = self.source_path / f"{source_name}.md"

        if not source_file.exists():
            print(f"  ПРОПУЩЕН: {source_name} (файл не найден)")
            return

        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        depth = self.get_file_depth(dest_path)
        converted = self.convert_content(content, depth)

        dest_file = self.docs_path / dest_path
        dest_file.parent.mkdir(parents=True, exist_ok=True)

        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(converted)

        print(f"  {source_name} → {dest_path}")

    def convert_all(self):
        """Конвертирует все файлы"""
        print("=" * 60)
        print("Конвертация markdown для MkDocs")
        print("=" * 60)

        # Копируем скриншоты
        self.copy_screenshots()

        # Конвертируем файлы
        print("\nКонвертация файлов...")
        for source_name, dest_path in self.file_mapping.items():
            self.convert_file(source_name, dest_path)

        print("\n" + "=" * 60)
        print("ГОТОВО!")
        print("=" * 60)


if __name__ == "__main__":
    base_path = Path(__file__).parent.parent
    converter = MkDocsConverter(base_path)
    converter.convert_all()
