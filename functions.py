import pymysql
from config import host, user, password, db_name

connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
)

def CREATETABLE(name,quantity):
    centre = ''

    for i in range(quantity):
        nametable = str(input("Введите имя столбца: "))
        nametable += ' varchar(32), '
        centre += nametable
    with connection.cursor() as cursor:
        create_table_query = f'CREATE TABLE `{name}`(id int AUTO_INCREMENT,{centre}PRIMARY KEY (id));'
        cursor.execute(create_table_query)
        print("Table created successfully")

def UPDATEMEAN(name,Column_name,id,mean):
    with connection.cursor() as cursor:
            update_query = f'UPDATE `{name}` SET {Column_name} = "{mean}" WHERE id = "{id}"'
            cursor.execute(update_query)
            connection.commit()

def DELETESTR(name,id):
    with connection.cursor() as cursor:
        delete_query = f'DELETE FROM `{name}` WHERE id = {id};'
        cursor.execute(delete_query)
        connection.commit()


def DELETETABLE(name):
    with connection.cursor() as cursor:
        drop_table_query = f'DROP TABLE `{name}`;'
        cursor.execute(drop_table_query)

def PRINTTABLE(name):
    with connection.cursor() as cursor:
            select_all_rows = f'SELECT * FROM `{name}`'
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)

def ADDSTR(name):
    z = ''
    cen = ''
    with connection.cursor() as cursor:
            select_all_rows = f'SELECT * FROM `{name}`'
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
    sp = rows[0]
    sp.pop('id')
    names = list(sp.keys())
    for i in names:
        if i == names[len(sp.keys())-1]:
            i = str(i)
            z = z + i
        else:    
            i = str(i)
            z = z + i + ','
    print(z)
    
    for i in range(len(names)):
        if i == len(sp.keys())-1:
            mean = str(input(f'Введите значение {names[i]}: '))
            cen += "'"+ mean +"'"
        else:
            mean = str(input(f'Введите значение {names[i]}: '))
            cen += "'"+ mean +"',"
        
    print(cen)
    with connection.cursor() as cursor:
        insert_query = f'INSERT INTO `{name}` ({z}) VALUES ({cen});'
        cursor.execute(insert_query)
        connection.commit()

def OUTNAMES():
    with connection.cursor() as cursor:
        cursor.execute("Show tables;")
        myresult = cursor.fetchall()
        
        for i in range(len(myresult)):
            print(myresult[i]['Tables_in_autobpcountry'])
