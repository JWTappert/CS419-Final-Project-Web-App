from flask import Flask, render_template
from db_connect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
	try:
		cursor, conn = connection()
	except Exception as e:
		return(str(e))

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(0))) 
	node0 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(1))) 
	node1 = cursor.fetchall()

	cursor.execute("SELECT temp FROM readings WHERE node_id=%s ORDER BY time DESC LIMIT 1", (str(2))) 
	node2 = cursor.fetchall()

	temp0 = node0[0][0]
	temp1 = node1[0][0]
	temp2 = node2[0][0]

	return render_template('index.html', temp0=temp0, temp1=temp1, temp2=temp2)


if __name__ == "__main__":
	app.run(debug=True)