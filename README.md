# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, 
так как у вас нет достпуа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

# Запуск

- Скачайте код
- Добавьте в папку с кодом файл .env скрытые параметры из settings.py для доступа к БД, указанные ниже.
```bash
ENGINE=here define the database 
HOST=here is the host of server
PORT=here is the port of server
NAME=here is the name of server
US=here is the username
PASSWORD=here is the user password
SECRET_KEY=here is the secret key of your site
```
- У вас должен быть установлен  Python3
- Установите необходимые пакеты:
```bash
$pip install -r requirements.txt
```
- Запустите сайт командой
```bash
$ python3 manage.py runserver
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
