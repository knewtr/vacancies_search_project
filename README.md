# Проект 2. Поиск вакансий
## Описание:
Данное приложение предназначено для работы с вакансиями, 
информацию о которых можно получить с платформы hh.ru. 
Приложение сохраняет данные о вакансии в json-файле, 
а также позволяет добавлять новые, фильтровать и удалять существующие.
## Установка:
1. Клонируйте репозиторий
```
https://github.com/knewtr/vacancies_search_project.git
```
2. Установите зависимости: mypy, flake8, black, isort, pytest, pytest-cov, requests
### Применение:
1. Запустите модуль main.py.
2. Введите ключевое поисковый запрос, ключевые слова, диапазон зарплат и количество вакансий для вывода.
3. Класс `HeadHunterAPI` отправляет запрос API на сайт HH.ru и получает данные, метод get_vacancies возвращает список словарей.
4. Методы класса `JSONSaver` позволяют читать, записывать и удалять полученную информацию.
5. Класс `Vacancy` создан для непосредственной работы с данными, методы которого позволяют: выводить необходимую информацию о вакансии,
сравнивать вакансии между собой по заработной плате, валидировать данные о наличии информации о заработной плате,
инициализировать новую вакансию.
6. В модуле utils.py находятся вспомогательные функции для фильтрации по ключевым словам, сортировки по заработной плате, выводить топ-N вакансий.
### Тестирование:
Для запуска тестирования введите в консоль команду pytest
### Документация:
Дополнительную информацию об API и структуре проекта можно найти в [документации](README.md)