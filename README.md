# Premier-League-matches

# Проект "Hello World API"

Це простий проект, який надає API з одним маршрутом для відображення "Hello World" разом із номером варіанту.

## Вимоги

- Python (рекомендовано використовувати версію 3.x)
- `pip` для управління пакетами Python

## Кроки по розгортанню

1. **Клонування репозиторію**

   Клонуйте репозиторій на свій локальний комп'ютер:

   ```bash
   git clone https://github.com/your-username/hello-world-api.git
Створення та активація віртуального середовища (опціонально)

Рекомендується створити та активувати віртуальне середовище для проекту:

python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
Встановлення Flask та інших залежностей

Встановіть Flask та інші залежності проекту:

pip install -r requirements.txt
Запуск сервера з використанням WSGI сервера waitress

Запустіть сервер з використанням WSGI сервера waitress:

waitress-serve --call main:app
Ваш сервер буде доступний за адресою http://localhost:8080.

Перевірка API

Відкрийте браузер або використовуйте curl для перевірки API:

В браузері: http://localhost:5000/api/v1/hello-world-{номер варіанту}

За допомогою curl:

Copy code
curl -v -X GET http://localhost:5000/api/v1/hello-world-3
Відповідь має містити текст "Hello World {номер варіанту}" та HTTP статус код 200.

Завершення роботи

Для завершення роботи сервера натисніть Ctrl+C у терміналі, де сервер був запущений.
