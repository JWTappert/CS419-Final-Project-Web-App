/*
id: This is the primary, auto-generated key for each entry

node_id: This wil distinguish which node the reading came from

temp: This is the temperature being recorded

time: The time when the entry was taken
    NOTE: This is actually the time the entry was made, but will be done within a second
    of the temp reading from a node, so accurate enough for our application
*/
CREATE TABLE `readings` (
	`id` INT NOT NULL auto_increment,
	`node_id` INT(4) NOT NULL,
	`temp` FLOAT(8) NOT NULL,
	`time` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

/*Set database timezone*/
SET TIME_ZONE = '-08:00';

/*entries for each node over 30 days ago*/
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.02, '2016-10-29 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 70.01, '2016-10-29 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.78, '2016-10-29 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.78, '2016-10-29 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 70.94, '2016-10-29 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.72, '2016-10-29 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.69, '2016-10-29 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 70.02, '2016-10-29 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.89, '2016-10-29 14:57:04');

/*entries for each node within 30 days*/
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.02, '2016-11-19 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 70.01, '2016-11-19 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.78, '2016-11-19 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.78, '2016-11-19 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 70.94, '2016-11-19 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.72, '2016-11-19 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.69, '2016-11-19 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 70.02, '2016-10-29 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.89, '2016-10-29 14:57:04');

/*entries for each node within 7 days*/
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.02, '2016-11-30 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 70.01, '2016-11-30 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (0, 69.78, '2016-11-30 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.78, '2016-11-30 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 70.94, '2016-11-30 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (1, 69.72, '2016-11-30 14:57:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.69, '2016-11-30 14:55:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 70.02, '2016-10-29 14:56:04');
INSERT INTO readings (node_id, temp, time) VALUES (2, 69.89, '2016-10-29 14:57:04');
