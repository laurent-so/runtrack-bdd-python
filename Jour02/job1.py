import mysql.connector


# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2206",
  database="LaPlateforme"
)

# Récupération des étudiants
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiants")
result = mycursor.fetchall()

# Affichage des résultats
for row in result:
  print(row)