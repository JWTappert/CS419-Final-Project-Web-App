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
	cursor.execute("SELECT time, temp FROM readings WHERE node_id=%s ORDER BY time ASC LIMIT 1440", (str(0)))
	numrows = cursor.rowcount
	node0 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time ASC LIMIT 1440", (str(1)))
	numrows = cursor.rowcount
	node1 = cursor.fetchall()

	tableData = [[] for _ in range(numrows+1)]
	tableData[0] = ['Time', 'Living Room', 'Bedroom']

	runTotal0 = 0
	runTotal1 = 0

	for n in xrange(0, numrows):
		if node0[n][1] == 666 or node0[n][1] == 0:
			node0[n][1] = float(runTotal0) / n+1
			continue
		elif node1[n][0] == 666 or node1[n][0] == 0:
			node1[n][0] = float(runTotal1) / n+1
			continue

		tempList = [node0[n][0], node0[n][1], node1[n][0]]
		tableData[n+1] = tempList
		runTotal0 = node0[n][1]
		runTotal1 = node1[n][0]

	'''
	for n in xrange(0, numrows):
		if node1[n][0] == 666 or node1[n][0] == 0:
			continue
		tableData[n+1].append(node1[n][0])
	'''

	#Get current temps
	cursor.execute("SELECT temp, time FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(0))) 
	curr0 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(1))) 
	curr1 = cursor.fetchall()

	temp0 = curr0[0][0]
	temp1 = curr1[0][0]

	return render_template('index.html', temp0=temp0, temp1=temp1, data=tableData)


if __name__ == "__main__":
	app.run(debug=True)