# API документация

Система "Цифровой РОП" предоставляет REST API для интеграции с внешними системами. В этом разделе описаны все доступные методы и форматы данных.

## Общие принципы работы

{TECHNICAL} Все запросы к API должны содержать параметр `apiKey` с ключом доступа. API ключ можно получить в разделе ["Настройки → Подключение"](#настройки-подключение). Для Setl Group используется ключ: `LS6gz1bkpG3lZI6uXetEoLtoVtVXYuWO`.

{INTERFACE} API использует стандартные HTTP методы:
- **POST** - для отправки данных в систему
- **GET** - для получения информации
- **Webhooks** - для автоматической отправки результатов

## Входящие методы API

### Загрузка аудиозаписей

{TECHNICAL}
```
POST http://10.28.32.81/api/v1/calls/audio-upload?apiKey={API_KEY}
Content-Type: application/json
```

**Параметры запроса:**
- `manager_id` (string) - идентификатор менеджера из CRM
- `call_id` (string) - уникальный идентификатор звонка
- `deal_id` (string) - идентификатор сделки в CRM
- `deal_stage_id` (string) - идентификатор этапа сделки
- `audio_url` (string) - URL для скачивания аудиофайла

**Пример запроса:**
```json
{
  "manager_id": "12345",
  "call_id": "call_789456",
  "deal_id": "deal_456789",
  "deal_stage_id": "stage_123",
  "audio_url": "https://crm.setl.ru/files/call_789456.mp3"
}
```

### Обновление структуры офисов

{TECHNICAL}
```
POST http://10.28.32.81/api/v1/settings/offices-update?apiKey={API_KEY}
Content-Type: application/json
```

**Параметры запроса:**
- `offices` (array) - массив офисов с их структурой

**Структура офиса:**
- `office_title` (string) - название офиса
- `office_id` (string) - идентификатор офиса
- `leader_ids` (array) - массив ID руководителей
- `managers_ids` (array) - массив ID менеджеров

**Пример запроса:**
```json
{
  "offices": [
    {
      "office_title": "Офис продаж Центр",
      "office_id": "office_001",
      "leader_ids": ["leader_123", "leader_456"],
      "managers_ids": ["manager_789", "manager_012", "manager_345"]
    }
  ]
}
```

### Обновление данных менеджеров

{TECHNICAL}
```
POST http://10.28.32.81/api/v1/settings/managers-update?apiKey={API_KEY}
Content-Type: application/json
```

**Параметры запроса:**
- `managers` (array) - массив менеджеров

**Структура менеджера:**
- `manager_id` (string) - идентификатор менеджера
- `name` (string) - имя
- `surname` (string) - фамилия
- `middlename` (string) - отчество

**Пример запроса:**
```json
{
  "managers": [
    {
      "manager_id": "manager_789",
      "name": "Иван",
      "surname": "Иванов",
      "middlename": "Иванович"
    }
  ]
}
```

### Проверка готовности результатов таблицы

{TECHNICAL}
```
GET http://10.28.32.81/api/v1/tables/call-ready?tab={TABLE_ID}&call={CALL_ID}
```

**Параметры запроса:**
- `tab` - идентификатор таблицы
- `call` - идентификатор звонка

**Ответ:**
```json
{
  "ready": true,
  "data": {
    "field1": "значение1",
    "field2": "значение2"
  }
}
```

## Исходящие Webhooks

### Результаты проверки по чек-листу

{INTERFACE} Настраивается в разделе ["Настройки → Скрипты и промты"](#скрипты-и-промты) для каждого чек-листа отдельно.

{TECHNICAL} При завершении анализа звонка система отправляет POST запрос на указанный URL:

**Формат данных:**
```json
{
  "call_id": "call_789456",
  "manager_id": "12345",
  "total_score": 18,
  "max_score": 20,
  "stages": [
    {
      "stage_name": "Приветствие",
      "score": 1,
      "comment": "Менеджер корректно представился",
      "quote": "Добрый день, компания Сэттл..."
    },
    {
      "stage_name": "Выявление потребностей",
      "score": -1,
      "comment": "Не выявлены потребности клиента",
      "quote": ""
    }
  ]
}
```

### Результаты аналитических таблиц

{INTERFACE} Настраивается индивидуально для каждой таблицы в разделе ["Настройки → Таблицы"](#настройки-таблицы).

{TECHNICAL} После извлечения данных из звонка система отправляет результаты:

**Формат данных:**
```json
{
  "call_id": "call_789456",
  "table_id": "table_conversion",
  "extracted_data": {
    "client_name": "Иван Петров",
    "budget": "5-7 млн руб",
    "object_type": "квартира",
    "conversion_stage": "заинтересован",
    "custom_field": "значение"
  }
}
```

## Коды ответов

{TECHNICAL} Система использует стандартные HTTP коды:
- **200** - успешная обработка запроса
- **400** - некорректные параметры запроса
- **401** - неверный API ключ
- **404** - запрашиваемый ресурс не найден
- **500** - внутренняя ошибка сервера

## Ограничения и рекомендации

{INTERFACE} При работе с API следует учитывать:
- Максимальный размер аудиофайла - 100 МБ
- Поддерживаемые форматы: MP3, WAV, OGG
- Рекомендуемая частота обновления данных - не чаще 1 раза в минуту
- Все временные метки в формате Unix timestamp

{TECHNICAL} Для обеспечения надежности интеграции:
- Реализуйте повторные попытки при ошибках 5xx
- Логируйте все запросы и ответы
- Используйте таймауты для предотвращения зависаний
- Проверяйте целостность данных перед отправкой

## Примеры интеграции

### Отправка звонка на анализ

{TECHNICAL}
```python
import requests
import json

api_key = "LS6gz1bkpG3lZI6uXetEoLtoVtVXYuWO"
url = f"http://10.28.32.81/api/v1/calls/audio-upload?apiKey={api_key}"

data = {
    "manager_id": "12345",
    "call_id": "call_789456",
    "deal_id": "deal_456789",
    "deal_stage_id": "stage_123",
    "audio_url": "https://crm.setl.ru/files/call_789456.mp3"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Звонок успешно отправлен на анализ")
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
```

### Получение результатов таблицы

{TECHNICAL}
```python
import requests

table_id = "table_conversion"
call_id = "call_789456"
url = f"http://10.28.32.81/api/v1/tables/call-ready?tab={table_id}&call={call_id}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data["ready"]:
        print("Результаты готовы:", data["data"])
    else:
        print("Результаты еще не готовы")
```

## См. также

- [Настройки - Подключение](#настройки-подключение) - получение API ключа
- [Настройки - Скрипты и промты](#настройки-скрипты-и-промты) - настройка webhooks для чек-листов
- [Настройки - Таблицы](#настройки-таблицы) - настройка webhooks для таблиц
- [Администрирование системы](#администрирование-системы) - управление интеграциями