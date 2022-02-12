-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `website`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `website` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `website`;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',0,'2022-01-25 17:06:15'),(2,'Tom','tom123','tom123',20,'2022-01-25 17:08:42'),(3,'Sam','sam123','sam123',105,'2022-01-25 17:09:37'),(4,'Lily','lily123','lily123',320,'2022-01-25 17:12:08'),(5,'Joy','joy123','joy123',260,'2022-01-25 17:12:34'),(51,'Roy','roy','roy',0,'2022-02-11 18:14:19'),(53,'Juju','juju','juju',0,'2022-02-11 20:46:23'),(54,'Jul','juju','juju',0,'2022-02-11 20:50:35'),(55,'Juju','juju','juju',0,'2022-02-11 20:51:28'),(56,'Juju','juju','juju',0,'2022-02-11 20:51:39'),(57,'Tom','tom123','tom123',0,'2022-02-11 20:52:15'),(58,'Tom','tom123','tom123',0,'2022-02-11 20:52:38'),(59,'juju','juju','juju',0,'2022-02-11 20:55:07'),(60,'juju','juju','juju',0,'2022-02-11 20:57:00'),(61,'yo','yo','yo',0,'2022-02-11 22:13:13'),(62,'Ollie','ollie','ollie',0,'2022-02-12 00:58:36');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memberlist`
--

DROP TABLE IF EXISTS `memberlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `memberlist` (
  `id` bigint DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `account` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memberlist`
--

LOCK TABLES `memberlist` WRITE;
/*!40000 ALTER TABLE `memberlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `memberlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,2,'Hello~','2022-01-26 14:49:53'),(2,4,'Trying to do MySQL','2022-01-26 14:52:05'),(3,1,'My username is test','2022-01-26 14:53:43'),(4,3,'Happy Chinese New Year','2022-01-26 14:55:03'),(5,5,'um...','2022-01-26 14:56:20');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-12 20:22:43
