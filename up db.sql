/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - mc
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`mc` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mc`;

/*Table structure for table `aupload` */

DROP TABLE IF EXISTS `aupload`;

CREATE TABLE `aupload` (
  `cname` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `landmarks` varchar(100) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `uid` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `aupload` */

insert  into `aupload`(`cname`,`city`,`landmarks`,`remarks`,`mobile`,`image`,`uid`) values ('c2','hyd','hyd','mole on neck','8639966858','a.jpg','myra123');

/*Table structure for table `authority` */

DROP TABLE IF EXISTS `authority`;

CREATE TABLE `authority` (
  `oname` varchar(100) DEFAULT NULL,
  `uid` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varbinary(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `authority` */

insert  into `authority`(`oname`,`uid`,`password`,`email`,`mobile`) values ('myra','myra123','chotu','moulalicce225@gmail.com','8639966858');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `cname` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `landmarks` varchar(100) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `uid` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`cname`,`city`,`landmarks`,`remarks`,`mobile`,`image`,`uid`) values ('c1','hyd','hyd','mole on neck','8639966858','a.jpg','myra123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
