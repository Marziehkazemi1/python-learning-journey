import os
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user=os.getenv("MYSQL_USER", "root"),
    password=os.environ["MYSQL_PASSWORD"]
)