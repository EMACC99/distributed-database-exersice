import mysql.connector as mariadb
from mysql.connector import errorcode
from PyQt5.QtWidgets import QMessageBox

config = {"user": "", "password":"", "host":"127.0.0.1", "raise_on_warnings": True}

def error(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        # QMessageBox.critical(None, "DATABASE ERROR", "Something is wrong with your user name or password")
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        QMessageBox.critical(None, "DATABASE ERROR", "Database does not exist")
        print("Database does not exist")
    else:
        QMessageBox.critical(None, "DATABASE ERROR", str(err))
        print(err)

def verify_credentials(user, password):
    try:
        mariadb.connect(host = "127.0.0.1", user = user, passwd = password)
        return True
    except mariadb.Error as err:
        error(err)
        return False    

def get_databases():
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query = (f"SELECT Nombre FROM Sucursales.Sucursales")
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

# def is_repeated(table, values):
#     try:
#         cnx = mariadb.connect(**config)
#         cursor = cnx.cursor()
#         # query  = f"INSERT INTO {table} VALUES (" + "%s, "*(len(values) -1) + "%s)"
#         databases = get_databases()
#         columns = get_column_names(table)
#         query = "SELECT COUNT(*) FROM "
#         for i in range(len(databases) - 1):
#             query += f"{databases[i]}.{table} WHERE " + "%s = %s UNION ALL SELECT COUNT(*) FROM"
#         query += f"{databases[-1]}.{table} WHERE "
#         query += '%s = %s'
#         query_values = []
#         for i in range(len(columns)):
#             query_values.append(columns[i])
#             query_values.append(values[i])
#         for i in range(len(databases)):
#             query_values.append(query_values[-1])
#         cursor.execute(query, tuple(query_values))
#         items = [item[0] for item in cursor.fetchall()]
#         cnx.commit()
        
#         return len(items) == 0

#     except mariadb.Error as err:
#         error(err)

def nuevo_registro(table, values):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query  = f"INSERT INTO {table} VALUES (" + "%s, "*(len(values) -1) + "%s)"
        cursor.execute(query, tuple(values))
        cnx.commit()
    
    except mariadb.Error as err:
        error(err)

def list_all(table, databases):
    try:
        items = []
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        # query  = f"SELECT * FROM {databases[0]}.{table} UNION SELECT * FROM {databases[1]}.{table}"
        query  = "SELECT *  FROM "
        for i in range(len(databases) - 1):
            query += f"{databases[i]}.{table} UNION SELECT * FROM "

        query += f"{databases[-1]}.{table}"
        
        cursor.execute(query)
        for row in cursor:
            items.append(list(row))
        cnx.commit()
        return items
    except mariadb.Error as err:
        error(err)

# def editar_registro(table, values, columns, id): #esta funcion no se utiliza, se reemplazo con la de abajo
#     try:
#         cnx = mariadb.connect()
#         cursor = cnx.cursor()
#         query = f"UPDATE {table} SET" + "%s = %s" *len(values) + f"WHERE Id = {id}"
#         query_values = []
#         for i in range(len(columns)):
#             query_values.append(columns[i])
#             query_values.append(values[i])

#         cursor.execute(query, tuple(query_values))
#         cnx.commit()
#     except mariadb.Error as err:
#         error(err)

def edit_registro(value, column, table,idr):
    try:
        cnx = mariadb.connect(**config)
        cursor = cnx.cursor()
        query  = f"UPDATE {table} SET {column} = '{value}' WHERE id = {idr}"
        #query  = f"UPDATE {table} SET (" + "%s, "*(len(values) -1) + "%s)"
        # UPDATE Clientes SET Nombre = 'Maria' WHERE id = 6;
        cursor.execute(query)#, tuple(values))
        cnx.commit()
    
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
            # query = f"SELECT * FROM {databases[0]}.{table} WHERE {column} = '{value}' UNION SELECT * FROM {databases[1]}.{table} WHERE {column} = '{value}'"
            # cursor.execute(query, tuple([databases[0], table, databases[1], table, column, value]))
            query = "SELECT * FROM "
            for i in range(len(databases) -1):
                query += f"{databases[i]}.{table} WHERE {column} = '{value}' UNION SELECT * FROM "
            query += f"{databases[-1]}.{table} WHERE {column} = '{value}'"
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
        for i in range(len(columns) - 1):
            contents += f"{columns[i]} {data_types[i][0]}({data_types[i][1]}),"
        # query = f"CREATE TABLE {Name} ("  + "%s %s(%s)," * (len(columns) - 1) + "%s %s(%s) )"
        # aux = []
        # for i in range(len(columns)):
        #     aux.append(columns[i]) #column name
        #     aux.append(data_types[i][0]) #data type
        #     aux.append(data_types[i][1]) #data size
        # cursor.execute(query, tuple(aux))
        contents += f"{columns[-1]} {data_types[-1][0]}({data_types[-1][1]})"
        query = header_commit + contents
        if keys is not None:
            for key in keys:
                if key[0] == 'Primaria':
                    query += f', PRIMARY KEY ({columns[key[-1]]})'
                elif key[0] == 'Foranea':
                    query += f', FOREIGN KEY ({columns[key[-1]]}) REFERENCES {key[1]}({key[2]})'
            
        query += ')'
        print(query)
        cursor.execute(query)
        cnx.commit()


    except mariadb.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            return
        else:
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
