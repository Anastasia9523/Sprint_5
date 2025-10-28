# Stellar Burgers Testing Project

Проект для автоматизированного тестирования веб-приложения **Stellar Burgers** с использованием Selenium и pytest.  

## Описание

Проект содержит тесты для:  

- Проверки регистрации пользователя
- Проверки входа пользователя  
- Проверки перехода в личный кабинет и конструктор
- Проверки выхода пользователя
- Проверки работы конструктора бургеров  

Тесты написаны с использованием **Selenium WebDriver** и **pytest**.  

## Технологии и инструменты

- Python 3.14  
- Selenium  
- pytest  
- Git и GitHub для контроля версий  

## Запуск тестов

- Запуск всех тестов:
pytest -v

- Запуск конкретного теста:
pytest -v tests/test_account.py

## Структура проекта

Sprint_5/
├── conftest.py           # Настройки и фикстуры pytest
├── data.py               # Тестовые данные
├── locators.py           # Локаторы элементов
├── helpers.py            # Вспомогательные функции
├── tests/                # Папка с тестами
│   ├── test_account.py
│   ├── test_constructor_sections.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_constructor.py
│   └── test_registration
└── README.md             # Документация проекта
