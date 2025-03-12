import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dbpassword = os.getenv("pass")

# Connexion à la base de données LaPlateforme
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password= dbpassword,
    database="LaPlateforme"
)

cursor = connection.cursor()

# Requête pour calculer la superficie totale des étages
cursor.execute("SELECT SUM(superficie) FROM etage")

# Affichage du résultat
result = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {result} m2")

# Fermeture de la connexion
cursor.close()
connection.close()
