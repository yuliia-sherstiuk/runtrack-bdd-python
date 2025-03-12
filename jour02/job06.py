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

# Requête pour calculer la capacité totale des salles
cursor.execute("SELECT SUM(capacite) FROM salle")

# Affichage du résultat
result = cursor.fetchone()[0]
print(f"La capacité totale des salles est de {result} personnes")

# Fermeture de la connection
cursor.close()
connection.close()