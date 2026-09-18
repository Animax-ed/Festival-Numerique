# Créé par 2607932, le 16/09/2026 en Python 3.7
page = """
<!DOCTYPE html>
<html lang="fr">
 <head>
  <meta charset="utf-8">
  <title>Festival numérique</title>
 </head>
 <body>
  <h1 style="color: black"><br>Bienvenue au festival numérique !</h1>
  <p style="color: black"><strong>notre classe prépare son stand.</strong></p>
  <p style="color: black;">Notre groupe va présenté la musique au stand.</p>
  <p style="color: black;"><strong>Comme style de musique, il y aura :</strong></p>
  <div style="display: flex; gap: 20px;">
   <a href="page-folk.html">
    <p style="color: green; font-size: 100px; margin-left: 150px; margin-right: 110px; background-image: url(fond-couleur-vert-pastel.JPG); width: 300px; height: 150px; border-radius: 40px">Le folk</p>
   </a>
   <a href="page-kpop.html">
    <p style="color: purple; font-size: 100px; text-align: right; margin-left: 150px; background-image: url(fond-couleur-rose-pastel.JPG); width: 400px; height: 150px; border-radius: 40px">La K-pop</p>
   </a>
  </div>
  <div style="display: flex; gap: 20px">
   <a href="page-rap.html">
    <p style="color: black; font-size: 100px; text-align: right; margin-left: 170px; margin-right: 140px; background-image: url(fond-couleur-rouge-pastel.JPG); width: 270px; height: 150px; border-radius: 40px">Le rap</p>
   </a>
   <a href="page-j-pop.html">
    <p style="color: red; font-size: 100px; margin-left: 150px; background-image: url(fond-couleur-blanc-pastel.JPG); width: 370px; height: 150px; border-radius: 40px">La J-pop</p>
   </a>
  </div>
   <button onclick="document.getElementById('fenetreContact').showModal()" style="position: fixed; left: 20px; bottom: 10px; z-index: 20">Contacter</button>
  <dialog id="fenetreContact" style="position: fixed; top: 20px; right: 20px">
   <h2>Plus d'info ?</h2>
   <p>Voici comment nous joindre...</p>
   <button onclick="document.getElementById('fenetreContact').close()">Fermer</button>
  </dialog>
   <button onclick="document.getElementById('fenetreReseauxSociaux').showModal()" style="position: fixed; left: 100px; bottom: 10px; z-index: 20">Réseaux Sociaux</button>
   <dialog id="fenetreReseauxSociaux" style="position: fixed; top: 20px; right: 20px">
    <h2>Où nous retrouver ?</h2>
    <p>Voici nos différents réseaux sociaux :</p>
    <p>Instagram :</p>
   <button onclick="document.getElementById('fenetreReseauxSociaux').close()">Fermer</button>
  </dialog>
  <img src="fond-couleur-tache.JPG" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; object-fit: cover; z-index: -1;">
 <img src="bande-blanche.JPG" style="position: fixed; top: 515px; left: 0; width: 100vw; height: 50px; object-fit: cover; z-index: 10;">
 </body>
</html>
"""
fichier = open("index.html", "w", encoding="utf-8")
fichier.write(page)
fichier.close()