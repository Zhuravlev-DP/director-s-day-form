### Форма director-s-day-form
Данная форма предназначена для сотрудников, которые задают вопросы на День Директора.

#### Планы по доработке что не удалось реализовать
- Сделать выпадающий список предприятий, который формируется в зависимости от выбранного дивизиона. Нашел как один из вариантов по реализации(https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html)

#### Запуск проекта в dev-режиме
- Клонирование удаленного репозитория
```bash
git clone git@github.com:Zhuravlev-DP/director-s-day-form.git
```
- Создание виртуального окружения и установка зависимостей
```bash
python -m venv venv (windows)
python3 -m venv venv (linux)
. source venv/Scripts/activate (windows)
. source venv/bin/activate (linux)
pip install --upgade pip
pip install -r -requirements.txt
```
- Примените миграции
```bash
cd director/
python manage.py makemigrations
python manage.py migrate
```
- Создайте суперюзера
```bash
python manage.py createsuperuser
```
- Запуск сервера
```bash
python manage.py runserver
```

#### Для работы с формой
- Перейдите в админку http://127.0.0.1:8000/admin/
- Заполните дивизионы
- Далее по адресу http://127.0.0.1:8000/ можно работать с формой