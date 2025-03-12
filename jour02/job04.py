import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dbpassword = os.getenv("pass")

# Connexion à la base de données LaPlateforme
connection= mysql.connector.connect(
    host="localhost",
    user="root",
     password= dbpassword,
    database="LaPlateforme"
)

cursor = connection.cursor()

# Requête pour récupérer les noms et les capacités des salles
cursor.execute("SELECT nom, capacite FROM salle")

# Affichage du résultat
for row in cursor.fetchall():
    print(f"Salle: {row[0]}, Capacité: {row[1]}")

# Fermeture de la connexion
cursor.close()
connection.close()