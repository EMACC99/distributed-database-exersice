-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Morelia
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-1:10.3.27+maria~bionic

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Clientes`
--

DROP TABLE IF EXISTS `Clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clientes` (
  `Id` int(6) NOT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `ApellidoPaterno` varchar(100) DEFAULT NULL,
  `ApellidoMaterno` varchar(100) DEFAULT NULL,
  `RFC` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clientes`
--

LOCK TABLES `Clientes` WRITE;
/*!40000 ALTER TABLE `Clientes` DISABLE KEYS */;
INSERT INTO `Clientes` VALUES (1,'Leonard','Hofstadter','Perez','CUPU800825569'),(2,'Juan','Lopez','Chavez','CUPU800827069'),(3,'Maria','Herrera','Garcia','CUPU800859569'),(4,'Javier','Jimenez','Sanchez','CUPU800825999'),(5,'Francisco','Ramirez','Hirt','CUPU800825577'),(6,'Edgar','Vargas','Juarez','CUPU800826969');
/*!40000 ALTER TABLE `Clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Direcciones`
--

DROP TABLE IF EXISTS `Direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Direcciones` (
  `Id` int(6) NOT NULL,
  `Calle` varchar(100) DEFAULT NULL,
  `Numero` varchar(10) DEFAULT NULL,
  `Colonia` varchar(100) DEFAULT NULL,
  `Estado` varchar(40) DEFAULT NULL,
  `CP` varchar(10) DEFAULT NULL,
  `idCliente` int(6) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `Direcciones_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `Clientes` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Direcciones`
--

LOCK TABLES `Direcciones` WRITE;
/*!40000 ALTER TABLE `Direcciones` DISABLE KEYS */;
INSERT INTO `Direcciones` VALUES (1,'Buena vista','56','Sierra','Michoacan','58195',1),(2,'Ortogonal','18','La joya','Michoacan','58155',2),(3,'Vertical','100-A','Ajusco','Michoacan','58175',3),(4,'Escarlate','99','Axteca','Michoacan','58184',4),(5,'Madera','555','Nuevo vallejo','Michoacan','58196',5),(6,'Quinta','1234','San Pedro','Michoacan','58156',6);
/*!40000 ALTER TABLE `Direcciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-17 20:19:35
