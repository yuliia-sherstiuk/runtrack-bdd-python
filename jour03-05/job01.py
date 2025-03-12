import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dbpassword = os.getenv("pass")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password= dbpassword,
    database='',
)

cursor = connection.cursor()



cursor.close()
connection.close()  