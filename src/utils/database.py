from src.utils.config import MysqlDatabaseConfig

import mysql

def get_connection():
    connection = None
    try:  
        connection = mysql.connector.connect(
            user=MysqlDatabaseConfig.USER,
            password=MysqlDatabaseConfig.PASSWORD,
            host=MysqlDatabaseConfig.HOST,
            port=MysqlDatabaseConfig.PORT,
            database=MysqlDatabaseConfig.DATABASE,
        )
        return connection
    except mysql.connector.Error as err:
        print("Error creating the connection to Mysql. Details: {e}")
        raise err
