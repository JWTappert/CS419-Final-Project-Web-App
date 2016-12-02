import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="heatMap")
	cursor = conn.cursor()

	return cursor, conn