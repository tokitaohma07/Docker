from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/wish")
def pleaseWish():
    return "Good Evening, Doctor!"

@app.route("/connect")
def pleaseConnect():
    try:
        connection = mysql.connector.connect(
        port=3306,
        host="mysql-container",
        user="root",
        password="mypassword",
        database="studentDB" 
        )
        if connection:
            return "Flask application successfully connect to MySQL!"
        else:
            return "Flask application not connected to MySQL!"
    except mysql.connector.Error as err:
        return f"{err}"



if __name__ == "__main__":
    app.run(host="0.0.0.0")