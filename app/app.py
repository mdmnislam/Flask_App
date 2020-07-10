# from typing import List, Dict
import mysql.connector
# import simplejson as json
# import str as str
# from flask import Flask, Response, request, redirect
from flask import Flask, render_template

app = Flask(__name__ , template_folder='templates')

from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'afu2'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'heightWeight'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    # user = {'username': 'Height Weight Data'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM hw10')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', output=result)


@app.route('/view/<int:Index>', methods=['GET'])
def view(Index):
    cursor = mysql.get_db().cursor()
    # id = city_id.id
    # id = request.args.get('city_id')
    # id = request.form('city_id')
    cursor.execute('SELECT * FROM hw10 WHERE `Index`= %s', Index)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', output=result[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5030, debug= True)
