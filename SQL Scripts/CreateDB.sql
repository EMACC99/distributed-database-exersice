CREATE DATABASE IF NOT EXISTS Sucursales;
USE Sucursales;
CREATE TABLE Sucursales(
    Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    IP INT UNSIGNED DEFAULT INET_ATON('127.0.0.1')
);
INSERT INTO Sucursales(Nombre) VALUES ('Moreliadb'), ('Patzcuarodb');
-- para las consulatas de la ip se hace de esta manera
--  SELECT Id, Nombre, INET_NTOA(IP) FROM Sucursales;

CREATE DATABASE IF NOT EXISTS Moreliadb;
USE Moreliadb;
CREATE TABLE Clientes (Id INT(6) PRIMARY KEY NOT NULL, Nombre VARCHAR(100),ApellidoPaterno VARCHAR(100),ApellidoMaterno VARCHAR(100),RFC VARCHAR(13));
CREATE TABLE Direcciones (Id INT(6) PRIMARY KEY NOT NULL,Calle VARCHAR(100),Numero VARCHAR(10),Colonia VARCHAR(100),Estado VARCHAR(40),CP VARCHAR(10),idCliente INT(6),FOREIGN KEY (idCliente) REFERENCES Clientes(Id) );
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000001,'Leonard','Hofstadter','Perez','CUPU800825569');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000002,'Juan','Lopez','Chavez','CUPU800827069');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000003,'Maria','Herrera','Garcia','CUPU800859569');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000004,'Javier','Jimenez','Sanchez','CUPU800825999');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000005,'Francisco','Ramirez','Hirt','CUPU800825577');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000006,'Edgar','Vargas','Juarez','CUPU800826969');
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000001,'Buena vista','56','Sierra','Michoacan','58195',000001);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000002,'Ortogonal','18','La joya','Michoacan','58155',000002);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000003,'Vertical','100-A','Ajusco','Michoacan','58175',000003);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000004,'Escarlate','99','Axteca','Michoacan','58184',000004);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000005,'Madera','555','Nuevo vallejo','Michoacan','58196',000005);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000006,'Quinta','1234','San Pedro','Michoacan','58156',000006);

CREATE DATABASE IF NOT EXISTS Patzcuarodb;
USE Patzcuarodb;
CREATE TABLE Clientes (Id INT(6) PRIMARY KEY NOT NULL, Nombre VARCHAR(100),ApellidoPaterno VARCHAR(100),ApellidoMaterno VARCHAR(100),RFC VARCHAR(13));
CREATE TABLE Direcciones (Id INT(6) PRIMARY KEY NOT NULL,Calle VARCHAR(100),Numero VARCHAR(10),Colonia VARCHAR(100),Estado VARCHAR(40),CP VARCHAR(10),idCliente INT(6),FOREIGN KEY (idCliente) REFERENCES Clientes(Id) );
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000001,'Roberto','Gonzalez','Martinez','CUPU800820069');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000002,'Diego','Rodriguez','Brown','CUPU800827169');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000003,'Jalisco','Da silva','Lopez','CUPU800856569');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000004,'Agustin','Garcia','Smith','CUPU800825989');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000005,'Alan','Hernandez','Hansen','CUPU800825477');
INSERT INTO  Clientes(Id,Nombre,ApellidoPaterno,ApellidoMaterno,RFC) VALUES (000006,'Alberto','Ramirez','Rossi','CUPU800827469');
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000001,'Navarrete','69','Asuncion','Michoacan','16319',000001);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000002,'Padre Pro','97','Libertad','Michoacan','16322',000002);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000003,'Alcantarilla','10','Olivar','Michoacan','61604',000003);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000004,'Cedro','969','Tolteca','Michoacan','61606',000004);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000005,'Teran','546','Nuevo navio','Michoacan','61608',000005);
INSERT INTO  Direcciones(Id,Calle,Numero,Colonia,Estado,CP,idCliente) VALUES (000006,'Cipres','12896','Bonanza','Michoacan','16321',000006);
-- quit;
