# Distributed Databases
## Authors:
* ## Cesar Arcos: racec9999@gmail.com
* ## Eduardo Ceja: lalitoceja@gmaill.com
## License :
CC BY-NC
## Introductio
## Requirements:
The proyect needs the following packages, this projects run on linux.:
* Python 3: sudo apt-get install python3.8
* Pyqt5:pip3 install PyQt5
* Pandas:pip3 install pandas 
* MySQL Connector (python version):pip3 install mysql-connector-python
* A Mariadb or MYSQL server running, with tables like the ones in `Moreliadb.sql` and `Patzcuaro.sql`. Alternatively, import the databases, make sure to create the databases beforehand, using `mysql -u <user> -p <database name> <  Morelia.sql` replacing `<user>` and `<database name>` with your SQL user (or Mariadb user) and name of the databse you're going to import to. Other option is to use the sript named `CreateDB.sql` like this `mariadb -u <user> -p < CreateDB.sql`.
## Instrucctions:
Tu run it, in a terminal type `python3 main.py` 
