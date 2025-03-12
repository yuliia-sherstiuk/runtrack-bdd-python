import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dbpassword = os.getenv("pass")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password= dbpassword,
    database='LaPlateforme',
)

cursor = connection.cursor()

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

if ('etudiant',) in tables:
    cursor.execute("SELECT * FROM etudiant")  
    etudiants = cursor.fetchall()

    print("\n Liste des étudiants :")
    for etudiant in etudiants:
        print(etudiant) 

else:
    print(" Table 'etudiant' non trouvée.")

cursor.close()
connection.close()  