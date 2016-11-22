CREATE TABLE `readings` (
	`id` INT NOT NULL auto_increment,
	`node_id` INT(4) NOT NULL,
	`temp` FLOAT(8) NOT NULL,
	`time` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

SET TIME_ZONE = '-08:00';

INSERT INTO readings (node_id, temp, time) VALUES (0, 69.02, '2016-10-16 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 70.02, '2016-11-16 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 68.02, '2016-11-16 14:57:04');
