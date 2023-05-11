from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'WEBAPP'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'PublicIp'

mysql = MySQL(app)
 

@app.route('/host/client-ip', methods=['GET', 'POST'])
def add():
    msg=''
    if request.method == 'POST' :
        details = request.form
        ip = details['PublicIP']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute (""" INSERT INTO list (public_ip) VALUES ('"""+str(ip)+"""');""")
        mysql.connection.commit()
        msg = 'You have successfully added !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('add.html', msg=msg)
 
 
@app.route("/")
def index():
    return render_template("index.html")

 
 
@app.route("/host/client-ip/list" ,methods=['GET','POST'])
def list():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM list')
    data=cursor.fetchall()
    return render_template("list.html", data=data)

 
 
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))