1 Запуск проекта команда: make up (выполнить в той же директории что и файл Makefile)
2 Запуск миграций make migrate
Далее необходимо добавить данные в бд.

регистрация нового пользователя: 
postman: 
post -> http://localhost:8000/auth/register 
raw/json
{
    "name":"str",
    "email":"str",
    "password":"str",
    "role": "str"
}

Авторизаци - получение токена: 
post -> http://localhost:8000/auth/login
raw/json
{
    "name":"str",
    "password":"str"
}

Добавление товара:
post -> http://localhost:8000/create-product
raw/json
{
    "name":"str",
    "description":"str",
    "price":int,
    "quantity":int
}

поиск товара:
get -> http://localhost:8000/search/products
query: str


