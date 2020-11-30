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

def get_column_type(table, database, column_name):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()

        query = "SELECT DATA_TYPE FROM information_schema.columns WHERE TABLE_NAME = %s AND TABLE_SCHEMA = %s AND COLUMN_NAME = %s"
        cursor.execute(query, tuple((table, database, column_name)))
        data_types = [data_type[0] for data_type in cursor.fetchall()]
        cnx.commit()
        return data_types[0]
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
        query  = f"INSERT INTO {table} VALUES (" + "%s, "*(len(values) -1) + "%s)"
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

        items = [list(row) for row in cursor]
        cnx.commit()
        return items

    except mariadb.Error as err:
        error(err)

def new_table(Name : str, columns : list, data_types : list, database : str, keys : list = None ):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = f"USE {database}"
        cursor.execute(query)
        cnx.commit()
        header_commit = f"CREATE TABLE {Name} ("
        contents = ""
        for i in range(len(columns)):
            contents += f"{columns[i]} {data_types[i][0]}({data_types[i][1]}),"
        # query = f"CREATE TABLE {Name} ("  + "%s %s(%s)," * (len(columns) - 1) + "%s %s(%s) )"
        # aux = []
        # for i in range(len(columns)):
        #     aux.append(columns[i]) #column name
        #     aux.append(data_types[i][0]) #data type
        #     aux.append(data_types[i][1]) #data size
        # cursor.execute(query, tuple(aux))
        query = header_commit + contents
        if keys is not None:
            for key in keys:
                if key[0] == 'Primaria':
                    query += f'PRIMARY KEY ({columns[key[-1]]}),'
                elif key[0] == 'Foranea':
                    query += f'FOREIGN KEY ({columns[key[-1]]}) REFERENCES {key[1]}({key[2]})'
            
        query += ')'
        print(query)
        cursor.execute(query)
        cnx.commit()


    except mariadb.Error as err:
        error(err)


def get_table_pk(table_name : str, database : str):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = " SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = %s AND TABLE_SCHEMA = %s AND COLUMN_KEY = 'PRI'"
        cursor.execute(query, tuple((table_name, database)))
        cols = [col[0] for col in cursor.fetchall()]
        return cols

    except mariadb.Error as err:
        error(err)