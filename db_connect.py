import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost", user="root", passwd="Rubean1", db="tempReadings")
	cursor = conn.cursor()

	return cursor, conn