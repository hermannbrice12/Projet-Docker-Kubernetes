from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/data')
def data():
    connection = mysql.connector.connect(
        host='db',
        user='user',
        password='password',
        database='mydatabase'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello, MySQL!'")
    result = cursor.fetchone()
    connection.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

