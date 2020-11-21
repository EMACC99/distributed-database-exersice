import mysql.connector as mariadb
from mysql.connector import errorcode

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
        # tables = (table)
        cursor.execute(query)
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

def nuevo_registro(table, values):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query  = f"INSERT INTO {table} VALUES " + "%s "*len(values)
        print(query)
        cursor.execute(query, tuple(values))
        cnx.commit()
    
    except mariadb.Error as err:
        error(err)

def editar_registro(table, values, columns, id):
    try:
        cnx = mariadb.connect()
        cursor = cnx.cursor()
        query = f"UPDATE {table} SET" + "%s = %s" *len(values) + f"WHERE Id = {id}"
        query_values = []
        for i in range(len(columns)):
            query_values.append(columns[i])
            query_values.append(values[i])

        cursor.execute(query, tuple(query_values))
        cnx.commit()
    except mariadb.Error as err:
        error(err)

def list_all(table, databases):
    try:
        items = []
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query  = f"SELECT * FROM {databases[0]}.{table} UNION SELECT * FROM {databases[1]}.{table}" #this is flawed but it has an easy fix
        cursor.execute(query)
        for row in cursor:
            items.append(list(row))
        cnx.commit()
        return items
    except mariadb.Error as err:
        error(err)

def list_find(value, column, table, databases = None):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        if databases is None:
            query = f"SELECT * FROM {table} WHERE {column} = '{value}'"
            # cursor.execute(query, tuple([table, column, value]))
            cursor.execute(query)

        elif databases is not None:
            query = f"SELECT * FROM {databases[0]}.{table} WHERE {column} = '{value}' UNION SELECT * FROM {databases[1]}.{table} WHERE {column} = '{value}'"
            # cursor.execute(query, tuple([databases[0], table, databases[1], table, column, value]))
            cursor.execute(query)

        items =[list(row) for row in cursor]
        cnx.commit()
        return items

    except mariadb.Error as err:
        error(err)