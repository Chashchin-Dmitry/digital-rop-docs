# Генератор финальной инструкции

## Быстрый старт

```bash
# Активация окружения
source venv/bin/activate

# Запуск генерации всей инструкции
python scripts/generate_instruction.py

# Генерация только конкретных разделов
python scripts/generate_instruction.py --sections intro analytics

# Принудительная перезапись всех разделов
python scripts/generate_instruction.py --force

# Полный сброс и новая генерация
python scripts/generate_instruction.py --reset

# Список доступных разделов
python scripts/generate_instruction.py --list
```

## Возможности скрипта

### ✅ Умная генерация по частям
- Пропускает уже созданные разделы
- Продолжает с места остановки
- Сохраняет прогресс в `scripts/progress.json`

### ✅ Качественное форматирование
- Профессиональные стили Word
- Автоматическое оглавление
- Правильная структура документа
- Разрывы страниц между разделами

### ✅ Гибкое управление
- Генерация конкретных разделов
- Принудительная перезапись
- Полный сброс проекта

## Доступные разделы

- `intro` - РАЗДЕЛ I: БЫСТРЫЙ СТАРТ
- `analytics` - РАЗДЕЛ II: АНАЛИТИКА И ОТЧЁТЫ  
- `charts` - РАЗДЕЛ III: ГРАФИКИ И ВИЗУАЛИЗАЦИЯ
- `tables` - РАЗДЕЛ IV: НАСТРОЙКА АНАЛИТИЧЕСКИХ ТАБЛИЦ
- `tools` - РАЗДЕЛ V: ДОПОЛНИТЕЛЬНЫЕ ИНСТРУМЕНТЫ
- `settings` - РАЗДЕЛ VI: АДМИНИСТРИРОВАНИЕ СИСТЕМЫ
- `additional` - РАЗДЕЛ VII: ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ
- `processes` - РАЗДЕЛ VIII: БИЗНЕС-ПРОЦЕССЫ
- `examples` - РАЗДЕЛ IX: ПРАКТИЧЕСКИЕ ПРИМЕРЫ  
- `technical` - РАЗДЕЛ X: ТЕХНИЧЕСКАЯ ИНФОРМАЦИЯ

## Примеры использования

```bash
# Создать только разделы для новичков
python scripts/generate_instruction.py --sections intro processes examples

# Перезаписать раздел настроек
python scripts/generate_instruction.py --sections settings --force

# Начать с чистого листа
python scripts/generate_instruction.py --reset
```

## Результат

Финальный документ: `Финальная_инструкция.docx`
- Готов к печати и публикации
- Качественное форматирование
- Автоматическое оглавление
- Все скриншоты подписаны