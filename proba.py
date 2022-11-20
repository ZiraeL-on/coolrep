import pymysql
from config import host, user, password, db_name
from functions import UPDATEMEAN,DELETESTR,DELETETABLE,PRINTTABLE,CREATETABLE,ADDSTR,OUTNAMES


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    
    try:
        cursor = connection.cursor()
        
        while True:
            print('''
        1.Добавить таблицу
        2.Добавить строку в таблицу
        3.Заменить значение в строке
        4.Удалить строку
        5.Удалить таблицу
        6.Вывести таблицу
        7.Вывести названия таблиц
        8.Завершить сеанс
        ''')
            choise = int(input("Что вы хотите сделать: "))
            
            if choise == 1:
                print("Первый столбец=id добавлен автоматически!")
                name = str(input("Введите имя таблицы: "))
                quantity = int(input("Введите кол-во столбцов: "))
                CREATETABLE(name,quantity)

            if choise == 2:
                name = str(input("Введите имя таблицы: "))
                ADDSTR(name)

            if choise == 3:
                name = str(input("Введите имя таблицы: "))
                Column_name = str(input("Введите имя столбца: "))
                id = str(input("Введите id: "))
                mean = str(input("Введите на что хотите заменить: "))
                UPDATEMEAN(name,Column_name,id,mean)
            
            if choise == 4:
                name= str(input("Введите имя таблицы: "))
                id = str(input("Введите id: "))
                DELETESTR(name,id)
            
            if choise == 5:
                name = str(input("Введите имя таблицы: "))
                DELETETABLE(name)

            if choise == 6:
                name = str(input("Введите имя таблицы: "))
                PRINTTABLE(name)
            
            if choise == 7:
                
                OUTNAMES()

            
            if choise ==8:
                break 


                
                
        
    
    
    
    
    
    
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)



