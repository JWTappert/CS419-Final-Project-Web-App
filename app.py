import datetime
from flask import Flask, render_template
from db_connect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
	#Connect to the database, throw exception if it fails
	try:
		cursor, conn = connection()
	except Exception as e:
		return(str(e))

	#Build the google chart from data in the database

	#query the db for last 24hours worth of data for sensor 1
	cursor.execute("SELECT time, temp FROM readings WHERE node_id=%s AND time > DATE_SUB(CURDATE(), INTERVAL 1 DAY)", (str(0)))
	#store the number of rows that are returned
	numrows = cursor.rowcount
	#save the massive tuple of data values
	node0 = cursor.fetchall()
	#repeat for node2
	cursor.execute("SELECT temp FROM readings WHERE node_id=%s AND time > DATE_SUB(CURDATE(), INTERVAL 1 DAY)", (str(1)))
	node1 = cursor.fetchall()

	#create an empty list to store the data for Google Charts API
	tableData = [[] for _ in range(numrows+1)]
	#first row is header information
	tableData[0] = ['Time', 'Living Room', 'Bedroom']

	#variables that are used to filter out garbage data
	runTotal0 = 0 #gets the runnnin total of all temps from node 1
	runTotal1 = 0 #get the running total of all temps from node 2
	avgTemp0 = 0 #average temperature of node 1
	avgTemp1 = 0 #average temperatre of node 2

	#iterate over the tuple od data values, if there is any garbage data replace it with an average temperature

	for n in xrange(0, numrows):
		if node0[n][1] > 100 or node0[n][1] < 32:
			avgTemp0 = runTotal0 / (n+1)
		else:
			avgTemp0 = 0 + node0[n][1]

		if node1[n][0] > 100 or node1[n][0] < 32:
			avgTemp1 = runTotal1 / (n+1)
		else:
			avgTemp1 = 0 + node1[n][0]
		#save a list of [timeStamp, temp1, temp2]
		tempList = [node0[n][0], avgTemp0, avgTemp1]
		#add it to the list of lists for the google chart
		tableData[n+1] = tempList
		#sum the total temps for each node
		runTotal0 = runTotal0 + avgTemp0
		runTotal1 = runTotal1 + avgTemp1

	#Get current temps
	cursor.execute("SELECT temp, time FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(0))) 
	curr0 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(1))) 
	curr1 = cursor.fetchall()

	temp0 = curr0[0][0]
	temp1 = curr1[0][0]

	conn.close()

	return render_template('index.html', temp0=temp0, temp1=temp1, data=tableData)


if __name__ == "__main__":
	app.run()