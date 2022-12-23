import psycopg2
from psycopg2 import Error

con_settings = dict(database='pyth_test',
                user='db_user',
                password='123456',
                host='localhost'
                    )
with psycopg2.connect(**con_settings) as conn:
    with conn.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS')
        result = cursor.fetchall()
        print(result)

try:
    conn = psycopg2.connect(database='pyth_test',
                            user='db_user',
                            password='123456',
                            host='localhost')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS')
    # cursor.execute("INSERT INTO phone(id, model, date_of_purchase, price) VALUES (10, 'Iphone 11', '30.11.2017', 14700)")
    # cursor.execute("UPDATE phone SET price = 44444 WHERE ID >3")
    # conn.commit()
    # create_table_query = '''CREATE TABLE item (
    # 	    item_id serial NOT NULL PRIMARY KEY,
    # 	    item_name VARCHAR (100) NOT NULL,
    #     	    purchase_time timestamp NOT NULL,
    # 	    price INTEGER NOT NULL
    #     );'''
    # cursor.execute(create_table_query)
    # item_purchase_time = datetime.datetime.now()
    # insert_query = """ INSERT INTO item (item_Id, item_name, purchase_time, price)
    #                               VALUES (%s, %s, %s, %s)"""
    # item_tuple = (15, "Жопа", item_purchase_time, 150)
    # cursor.execute(insert_query, item_tuple)
    # conn.commit()
    # print(f'Добавили строку')
    # cursor.execute("SELECT purchase_time from item where item_id = 12")
    # purch_time = cursor.fetchone()
    # print(purch_time[0].date())
    # count = cursor.rowcount
    # print(count, "Запись успешно удалена")
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    # conn.commit()


except (Error, Exception) as error:
    print(f'Появилась ошибка {error}')
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
