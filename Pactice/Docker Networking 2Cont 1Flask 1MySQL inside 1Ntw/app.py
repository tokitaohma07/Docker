from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/connect")
def pleaseConnect():
    try:
        connection = mysql.connector.connect(
        port=3306,
        host="mysql-container",
        user="root",
        password="welcome",
        database="empdb" 
        )
        if connection:
            return "Flask application successfully connect to MySQL!"
        else:
            return "Flask application not connected to MySQL!"
    except mysql.connector.Error as err:
        return f"Error: {err}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)