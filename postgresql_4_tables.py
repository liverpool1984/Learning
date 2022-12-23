import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host='localhost', db_port="5432"):
    connection = None

    try:
        connection = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        print("Подключение к базе данных PostgreSQL прошло успешно")
    except OperationalError as error:
        print(f'При подключении возникла ошибка {error}')
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f'Запрос выполнен')
    except OperationalError as error:
        print(f'Ошибка при выполнении запроса {error}')


conn = create_connection('pyth_test', 'postgres', '123456')

create_user_table = """CREATE TABLE IF NOT EXISTS comments(
id SERIAL PRIMARY KEY,
text TEXT NOT NULL,
user_id INTEGER REFERENCES users(id), 
post_id INTEGER REFERENCES posts(id)
)"""

create_user_table = """CREATE TABLE IF NOT EXISTS likes(
id SERIAL PRIMARY KEY,
user_id INTEGER REFERENCES users(id), 
post_id INTEGER REFERENCES posts(id)
)"""

execute_query(conn, create_user_table)
