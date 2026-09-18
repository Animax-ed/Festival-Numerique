# Créé par 2607932, le 16/09/2026 en Python 3.7
page = """
<!DOCTYPE html>
<html lang="fr">
 <head>
  <meta charset="utf-8">
  <title>La K-pop</title>
 </head>
 <body>
 <img src="fond-couleur-rose-violet.JPG" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; object-fit: cover; z-index: -1;">
  <h1 style="color: black; font-size: 200px; text-align: center">La K-pop !</h1>
 </body>
 </html>
"""
fichier = open("page-kpop.html", "w", encoding="utf-8")
fichier.write(page)
fichier.close()