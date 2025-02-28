import pymysql

def get_db_connection():
    return pymysql.connect(
        host="Lumine",
        user="admin",
        password="123456",
        database="task_db",
        cursorclass=pymysql.cursors.DictCursor
    )
