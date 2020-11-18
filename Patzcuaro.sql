-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Patzcuaro
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
INSERT INTO `Clientes` VALUES (1,'Roberto','Gonzalez','Martinez','CUPU800820069'),(2,'Diego','Rodriguez','Brown','CUPU800827169'),(3,'Jalisco','Da silva','Lopez','CUPU800856569'),(4,'Agustin','Garcia','Smith','CUPU800825989'),(5,'Alan','Hernandez','Hansen','CUPU800825477'),(6,'Alberto','Ramirez','Rossi','CUPU800827469');
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
INSERT INTO `Direcciones` VALUES (1,'Navarrete','69','Asuncion','Michoacan','16319',1),(2,'Padre Pro','97','Libertad','Michoacan','16322',2),(3,'Alcantarilla','10','Olivar','Michoacan','61604',3),(4,'Cedro','969','Tolteca','Michoacan','61606',4),(5,'Teran','546','Nuevo navio','Michoacan','61608',5),(6,'Cipres','12896','Bonanza','Michoacan','16321',6);
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

-- Dump completed on 2020-11-17 20:44:42
