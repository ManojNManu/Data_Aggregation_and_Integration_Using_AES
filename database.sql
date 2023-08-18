/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.1.61-community : Database - healthmonitoring
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`healthmonitoring` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `healthmonitoring`;

/*Table structure for table `adminlogin` */

DROP TABLE IF EXISTS `adminlogin`;

CREATE TABLE `adminlogin` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `ausername` varchar(200) DEFAULT NULL,
  `apassword` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `adminlogin` */

insert  into `adminlogin`(`aid`,`ausername`,`apassword`) values (1,'admin','admin');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `doctorname` varchar(200) DEFAULT NULL,
  `doctoraddrs` varchar(200) DEFAULT NULL,
  `doctorphone` varchar(200) DEFAULT NULL,
  `SpecialistIn` varchar(200) DEFAULT NULL,
  `doctoremail` varchar(200) DEFAULT NULL,
  `dpasswrd` varchar(200) DEFAULT NULL,
  `hospitalname` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`did`,`doctorname`,`doctoraddrs`,`doctorphone`,`SpecialistIn`,`doctoremail`,`dpasswrd`,`hospitalname`) values (5,'jafar','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','shilp@gmail.com',NULL),(6,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','shilp@gmail.com',NULL),(8,'Suma','Kesare Mysore','08212545981','ENT','sumabharathi123@gmail.com','suma123',NULL),(9,'Divya','J P nagar','9621487589','Skin','divyarj@gmail.com','Divyashree@123',NULL),(10,'xsfdsf','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','sdsdfsf',NULL),(11,'divya','mysore','9945901254','eye','divya32@gmail.com','divya',NULL),(12,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Shilpa@gmail.com','shilpa@123',NULL),(13,'abhi','jss','8197418140','ENT','abhi1234@gmail.com','abhi1234',NULL),(14,'Nisarga','hunsur','8326662377','ENT','Nisarga12@gmail.com','nisarga','jsss'),(15,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','shilp@gmail.com','sdgfdg','sdfdg'),(16,'divya','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','eye','Kamakshi@gmail.com','1234','gh'),(17,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','Eyes','Kamakshi@gmail.com','123456','jss'),(18,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','Eyes','Kamakshi@gmail.com','123456','jss'),(19,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','ENT','Kamakshi@gmail.com','562148','jsss'),(20,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','ENT','Kamakshi@gmail.com','562148','jsss'),(21,'Shilpa','Adichunchanagiri Road, Jayanagar, Kuvempu Nagara','08212568888','ENT','Kamakshi@gmail.com','562148','jsss'),(22,'Shilpa','AGRAHARA','82654756','Eyes','Kamakshi@gmail.com','12334','jsss'),(23,'Shilpa','AGRAHARA','82654756','Eyes','Kamakshi@gmail.com','12334','jsss'),(24,'Shilpa','tumkur','413736169','ENT','Kamakshi@gmail.com','6586826dsfd','jsss'),(25,'Shilpa','tumkur','413736169','ENT','Kamakshi@gmail.com','6586826dsfd','jsss'),(26,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(27,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(28,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(29,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(30,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(31,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(32,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(33,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(34,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(35,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(36,'Shilpa','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','08212545981','Eyes','Kamakshi@gmail.com','ghvjh','jss'),(37,'Divyashree','AGRAHARA','82654756','Eyes','divyashree123@gmail.com','divyuashree@12345','4'),(38,'dsfvd','xdcdfv','6929868828','sdfs','asdsdf@gmail.com','asdas','3');

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `hospitalname` varchar(200) DEFAULT NULL,
  `hospitaladdrs` varchar(200) DEFAULT NULL,
  `hcity` varchar(200) DEFAULT NULL,
  `hstate` varchar(200) DEFAULT NULL,
  `hzcode` varchar(200) DEFAULT NULL,
  `hcountry` varchar(200) DEFAULT NULL,
  `hphone` varchar(200) DEFAULT NULL,
  `hemail` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`hid`,`hospitalname`,`hospitaladdrs`,`hcity`,`hstate`,`hzcode`,`hcountry`,`hphone`,`hemail`) values (2,'Kamakshi ','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','Mysuru','Karnataka','570009','India','08212545981','Kamakshi@gmail.com'),(3,'Apollo BGS ','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','Mysuru','Karnataka','570009','India','08212545981','Kamakshi@gmail.com'),(4,'BGS','tumkur','tumkur','karnataka','156787','india','413736169','bgs@gmail.com'),(6,'Kamakshi ','Kamakshi Hospital Rd, Kuvempunagara North, Kuvempu Nagara','Mysuru','Karnataka','570009','India','08212545981','Kamakshi@gmail.com'),(7,'JSS','AGRAHARA','Mysore','karnataka','571122','india','82654756','manoj11234@gmail.com');

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(200) DEFAULT NULL,
  `pemail` varchar(200) DEFAULT NULL,
  `page` varchar(200) DEFAULT NULL,
  `pgender` varchar(200) DEFAULT NULL,
  `pcontact` varchar(200) DEFAULT NULL,
  `pkey` varchar(2000) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`pid`,`pname`,`pemail`,`page`,`pgender`,`pcontact`,`pkey`,`password`) values (1,'Üü¤’73é7ëL,íq„´s','BèNy«Õúú¼H[¬›ž´öÅš“Þ üŒrNÐ?\"5','21','Male','Ž®¨~Ö3×<u2\'w','22559u86767hy1','*852'),(2,'I¬8ÝÛÌ¦Ì1$\r8ñž†Ž','ŽÎ&¦-”èo©Å{Ô²)*VAÌ¡y1˜ê=Ý(','21','Female',',p«k?5œ—FZ€','6FT79N9','77'),(3,'ÐYeóE²ªÕ«l8“H','Dn Ã!…OÄâÃRo©jü”Aëÿæ‹»€!²²‘ùY','21','Female','ÑÓÕ+â]Ä>Iò ','YAZKPKN','124'),(4,'…Ñ+Í½.B¶|µ‘/','°¦	¬KçW}MÌSµ¦','dsf','Female','WíbäòŠƒ,Ua	ÇM-»','7C3SJNN','756'),(5,'Ñ÷tó4óÜbÒ_ŽŠ ','<Áž¸¡ëãY6;ÔÏV','21','Male','É/ˆÑ$„Þa)Æ\\Åpz÷Œ','GT1RLI6','4587'),(6,'ú OìeY‚z§Ý)Êbëe','>{L0;»dèéœd IW.{Ï)hÅÁïzøAˆ *s','22','Female','ø_M V$—Ïv7Žÿr','Y1WQKCP','158'),(7,'„ý×¾ÿw±,Èéú)Sî','ä÷(]/áÂ—ù¾ Jô','20','Male','±±Šw(oyRò@ã˜†¦õ»','AG9DX0A','manoj'),(8,'EÔ©xëäÌOpÆGôp¶','}CÌ\'ÓM£0à¦ÓA¥éë®¸Š*Á¥0	ö“\r‘G ','20','Male','î8MÚGºÌ]ñÛæ#0–{','QDOWTJX','naga1234'),(9,'ôN]\Z¸9aÍc²\0*žC×ö','-H”Òz°Ÿ#òú¨yÄ[ˆº5Yæ5jó¼¡Û\rÔ”','20','Male','¿¸…O¦‘Ã	†¤â\'“‡p','GZ9PHHI','niru1234'),(10,'aÂƒÂªLv$Zlm+K','Ìøu·21ûhzý6)^Äl²»hvY5—î~Ž3¿','40','Male','$¬ÎXmýí¨À7¥O_:','9N9YPYQ','ramesh@123'),(11,'‹eNMûJ‡z	¾/á','gþ8’»{mnàV¿yj®Í•¹·ŒI¼Ùá’[ê!‰‰','20','Female','ö–U·³=rbØdØ1‹ß','9ELNK0X','spoorthi@123'),(12,'¹î†µÉã¥Ã«ÂØ*Œ‘M¼','Œà7?è{µªë¤Á*çžYH,ÐÙ>y˜ð¡ð:ÌÔ¨','25','Female','¾Ÿ‡°¢]Á\Z¬Š¢Õ|J\\','6CWZNJH','mahima@123'),(13,'0Úõ–ÛâO²Ð>±½û','ïÄ_\\fÔ¹“R¹4jã\rp º®°¸ö†½§Z','21','Male','^‚à€”ÚO×ðÌ!ÙÁšã','39FB3V6','ssdsds'),(14,'¶¿¦/ˆÍ½4]ž±½(t ','ìŽc¹ŽÏT=2/ÃÒCq»#R°m˜Í«GËÑlÔ','dfdg','Female','º÷„>™‘óøäRƒrÎË','99GY9HB','admin'),(15,'†¡™éþþ±í2¢u','\'Èj¦yßvµ5$Ïûeßó-¾‡Óà\r=JÁõÞÝã','20','Male','»³Ù‘¡ôû>¥ò ¥·Ç+','3XCO2EJ','praju'),(16,'\'ÀãzÉ‚ÉXD?’g','C2â ÞØ;” ²Ópð»Ê8äˆ\\W2ÚO0=™_Ø¸k','21','Female','8¸zÈÛO‡™ä2!»hý>','FDW3WMA','123456');

/*Table structure for table `patientmedicaldetails` */

DROP TABLE IF EXISTS `patientmedicaldetails`;

CREATE TABLE `patientmedicaldetails` (
  `pmid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `bp` varchar(200) DEFAULT NULL,
  `heartrate` varchar(200) DEFAULT NULL,
  `bloodgruop` varchar(200) DEFAULT NULL,
  `temperature` varchar(200) DEFAULT NULL,
  `healthissue` varchar(200) DEFAULT NULL,
  `responsetomedication` varchar(200) DEFAULT NULL,
  `doctorname` varchar(200) DEFAULT NULL,
  `hospitalname` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`pmid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `patientmedicaldetails` */

insert  into `patientmedicaldetails`(`pmid`,`pid`,`bp`,`heartrate`,`bloodgruop`,`temperature`,`healthissue`,`responsetomedication`,`doctorname`,`hospitalname`) values (1,1,'40','60','A+','100','headache','gud','divya','jss'),(2,1,'60','75','B-','90','Fever','bad','shilpa','apolo'),(3,15,'120','75','O+','70','Fever','Bad','Narendra','JSS'),(4,15,'140','50','O+','80','Headache','Good','Shilpa','Apollo'),(5,1,'120','60','B+','70','headache','dhsj','Shilpa','None'),(6,15,'160','65','A-','70','headache','bad','Shilpa','4'),(7,15,'120','75','B+','70','headache','dhsj','8','3'),(8,1,'120','67','120','78','headache','dfdg','fsdfsdf','Apollo'),(9,15,'140','60','O+','44','headache','bad','Suma','JSS'),(10,16,'130','116','O+','70','axxx','goood','9','4');

/*Table structure for table `userlogin` */

DROP TABLE IF EXISTS `userlogin`;

CREATE TABLE `userlogin` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `uemail` varchar(200) DEFAULT NULL,
  `upswd` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `userlogin` */

insert  into `userlogin`(`uid`,`uemail`,`upswd`) values (1,'divyarj@gmail.com','divya');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
