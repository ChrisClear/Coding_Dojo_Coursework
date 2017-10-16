-- MySQL Script generated by MySQL Workbench
-- Wed Oct 11 14:22:54 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema email_validation_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema email_validation_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `email_validation_db` DEFAULT CHARACTER SET utf8 ;
USE `email_validation_db` ;

-- -----------------------------------------------------
-- Table `email_validation_db`.`emails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `email_validation_db`.`emails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 59
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
