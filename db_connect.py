import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="heatMap")
	c = conn.cursor()

	return c, conn