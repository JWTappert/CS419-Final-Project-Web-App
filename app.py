from flask import Flask, render_template
from db_connect import connection

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/test/')
def test():
	try:
		c, conn = connection()
		return ('okay')
	except Exception as e:
		return(str(e))


if __name__ == "__main__":
	app.run()