<?php
	include_once("/Includes/db.php");
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width = device-width, intial-scale = 1">
		<title>CS419 Final</title>

		<!-- Bootstrap -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	</head>

	<body>
		<div class="container">
			<div class="page-header">
				<h1>CS419 Final Project: Heat Mapping</h1>
			</div>

			<div class="row">
				<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
          <p>This is a web application for our final project in CS419: Internet of Things. We have decided to create a heat map of a residence using a wireless sensor network. We are using a <a href="https://www.raspberrypi.org/products/raspberry-pi-3-model-b/">Raspberry Pi 3</a>, two <a href="https://www.arduino.cc/en/Main/ArduinoBoardUno">Arduino Uno</a> boards with <a href="https://www.sparkfun.com/products/10988">TMP36 Temperate sensors</a> attached to them, as well as <a href="https://www.digi.com/products/xbee-rf-solutions/modules/xbee-wi-fi">Xbee WiFi radios.</a> The RP3 is acting as the base station for the sensors and queries the data that is stored in a MySQL database. The base station code is written in Python, the code on each of the nodes is C++/Arduino, and finally the web application is using the LAMP stack. Our team consists of Adam Duquette and Justin Tappert.</p>
				</div>
			</div>

			<div class="row">

				<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
					<h2>Living Room</h2>
				</div>

				<div class="col-lg-4 col-md-3 col-sm-6 col-xs-12">
					<h2>Bedroom 1</h2>
				</div>

				<div class="col-lg-4 col-md-3 col-sm-6 col-xs-12">
					<h2>Bedroom 2</h2>
				</div>

			</div>
		</div>

	</body>

</html>
