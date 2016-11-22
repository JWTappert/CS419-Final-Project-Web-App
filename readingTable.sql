CREATE TABLE `readings` (
	`id` INT NOT NULL,
	`node_id` INT(4) NOT NULL,
	`temp` FLOAT(8) NOT NULL,
	`time` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

