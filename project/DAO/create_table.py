import DAO.conn as connection

from config import * 

def create_table():
    conn = connection.connection_mysql() 
    query = "CREATE TABLE IF NOT EXISTS {} (VARCHAR (80) NOT NULL )".format(table_name, 'title')
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.close()
        except Exception as e:
            conn.close()
            print(e.__context__)
            return False
        return True
    else:
        return False
