Exercices pratiques FastAPI
Exo 1: une API base de données

Construire une API pour une base de données simple d'une bibliothèque avec SQLAlchemy. La base de données :

    2 entités :
        lecteur : nom, prénom, mail, password  --> db_user
        livres : titre, auteur, isbn           --> db_book
    un lecteur peut emprunter un livre avec une date d'emprunt et une date de retour                       --> param 'date(s)' dans liste d'emprunt
    un lecteur peut consulter ses emprunts en cours et passés 
    un lecteur peut consulter si un livre est disponible (pour simplifier on considère qu'il n'y a qu'un seul exemplaire de chaque livre) --> param 'disponible' dans la db_books

Contraintes :

    Intégrer toutes les requêtes CRUD nécessaires.
    Gérer les schémas de récupération des données du client et les schémas de réponse au client.
    Intégrer l'authentification pour permettre à un lecteur authentifié de consulter ses emprunts

Exo 2: une API de prédiction ML/DL

Créer une API de prédiction d'analyse de sentiments à partir du dataset déjà labellisé et qui recense 1,6M de tweets.

Vous pouvez utiliser un simple modèle ML pour commencer puis si vous avez le temps essayer d'améliorer le modèle avec un LSTM par exemple.

Contraintes : On doit pouvoir requêter l'API soit avec du texte brut en paramètres, soit avec un fichier contenant 1 ou plusieurs tweets à prédire.readers