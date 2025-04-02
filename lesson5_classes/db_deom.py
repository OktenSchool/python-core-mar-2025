import mysql.connector


# connect = mysql.connector.connect(host='localhost', user='root', password='rootroot', database='world')

def connection_to_databse(database, table):

    connection_data = {'host': 'localhost', 'user': 'root', 'password': 'rootroot', 'database': database}

    connect = mysql.connector.connect(**connection_data)
    if connect.is_connected():
        print('Connected to MySQL Server')
        cursor = connect.cursor()
        cursor.execute('select * from ' + table)

        results = cursor.fetchall()
        for row in results:
            print(row)

    connect.close()


connection_to_databse('world', 'city')
connection_to_databse('sakila', 'actor')
connection_to_databse('sys', 'sys_config')
