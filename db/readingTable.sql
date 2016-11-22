CREATE TABLE `readings` (
	`id` INT NOT NULL auto_increment,
	`node_id` INT(4) NOT NULL,
	`temp` FLOAT(8) NOT NULL,
	`time` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

SET TIME_ZONE = '-08:00';
