import mysql.connector as mariadb
from mysql.connector import errorcode, FieldType


config = {"user": "emacc", "password":"12345", "host":"127.0.0.1", "raise_on_warnings": True}

def error(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)

def get_databases():
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = (f"SHOW DATABASES")
        cursor.execute(query)
        databases = [database[0] for database in cursor.fetchall()]
        cnx.commit()

        return databases
    except mariadb.Error as err:
        error(err)

def get_tables(database):
    try: 
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = (f"USE {database}")
        config["database"] = str(database)
        cursor.execute(query)
        cnx.commit()
        
        query = (f"SHOW TABLES")
        cursor.execute(query)
        tables = [table[0] for table in cursor.fetchall()]
        cnx.commit()

        return tables
    
    except mariadb.Error as err:
        error(err)

def get_column_names(table):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()

        query = (f"SHOW columns FROM {table}")

        cursor.execute(query)
        columns = [column[0] for column in cursor.fetchall()]
        cnx.commit()

        return columns
  
    except mariadb.Error as err:
        error(err)

def todos(table):
    try:
        items = []
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = (f"SELECT * FROM {table}")
        tables = (table)
        cursor.execute(query, tables)
        for row in cursor:
            items.append(list(row))
        cnx.commit()
        return items
    except mariadb.Error as err:
        error(err)

def count_items(table):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query =  (f"SELCT COUNT(*) FROM {table}")
        cursor.execute(query)
        items = len(cursor)
        cnx.commit()
        return items
    except mariadb.Error as err:
        error(err)

def nuevo_registro(table, values, columns):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query  = f"INSERT INTO {table} VALUES " + "%s "*len(values)
        cursor.execute(query, tuple(values))
        cnx.commit()
    
    except mariadb.Error as err:
        error(err)

