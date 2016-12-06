import datetime
from flask import Flask, render_template
from db_connect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
	try:
		cursor, conn = connection()
	except Exception as e:
		return(str(e))

	#Build the google chart from data in the database
	cursor.execute("SELECT time, temp FROM readings WHERE node_id=%s AND time > DATE_SUB(CURDATE(), INTERVAL 1 DAY)", (str(0)))
	#cursor.execute("SELECT time, temp FROM readings WHERE node_id=%s ORDER BY time ASC LIMIT 1440", (str(0)))
	numrows = cursor.rowcount
	node0 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s AND time > DATE_SUB(CURDATE(), INTERVAL 1 DAY)", (str(1)))
	#cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time ASC LIMIT 1440", (str(1)))
	node1 = cursor.fetchall()

	tableData = [[] for _ in range(numrows+1)]
	tableData[0] = ['Time', 'Living Room', 'Bedroom']

	runTotal0 = 0
	runTotal1 = 0
	avgTemp0 = 0
	avgTemp1 = 0

	for n in xrange(0, numrows):
		if node0[n][1] > 100 or node0[n][1] < 32:
			avgTemp0 = runTotal0 / (n+1)
		else:
			avgTemp0 = 0 + node0[n][1]

		if node1[n][0] > 100 or node1[n][0] < 32:
			avgTemp1 = runTotal1 / (n+1)
		else:
			avgTemp1 = 0 + node1[n][0]

		tempList = [node0[n][0], avgTemp0, avgTemp1]
		tableData[n+1] = tempList
		runTotal0 = runTotal0 + avgTemp0
		runTotal1 = runTotal1 + avgTemp1

	'''
	for n in xrange(0, numrows):
		if node0[n][1] == 666 or node0[n][1] == 0:
			print "GOT GARBAGE in node0: " + str(node0[n][1])
			avgTemp = 69.69 #runTotal0 / (n + 1)
			print "avgTemp: " + str(avgTemp)
			tempList = [node0[n][0], avgTemp, node1[n][0]]
		elif node1[n][0] == 666 or node1[n][0] == 0:
			print "GOT GARBAGE in node1: " + str(node1[n][0])
			avgTemp = 69.69 #runTotal1 / (n + 1)
			print "avgTemp: " + str(avgTemp)
			tempList = [node0[n][0], node0[n][1], avgTemp]
		else:
			tempList = [node0[n][0], node0[n][1], node1[n][0]]
		
		tableData[n+1] = tempList
		runTotal0 = runTotal0 + node0[n][1]
		runTotal1 = runTotal1 + node1[n][0]
	'''
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
	app.run(debug=True)