import mysql.connector as msc
import os

def init_db_connection():
    try:
        connection = msc.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=os.environ.get("DB_NAME", "LateComersDB")
        )
        return connection
    except msc.Error as err:
        print(f"Database Error: {err}")
        return None

def execute_query(connection, query, params=None):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query, params) if params else cursor.execute(query)
        connection.commit()
        return cursor
    except msc.Error as err:
        print(f"Query Error: {err}")
        return None

def fetch_one(connection, query, params=None):
    cursor = execute_query(connection, query, params)
    return cursor.fetchone() if cursor else None

def fetch_all(connection, query, params=None):
    cursor = execute_query(connection, query, params)
    return cursor.fetchall() if cursor else []

def close_db_connection(connection):
    if connection:
        connection.close()
