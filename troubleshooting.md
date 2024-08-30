on veut authentication
    -> oauth2.py (fastapi.security)

    --> necessaire d'avoir (from db.database import get_db) ::: instanciation BD
    --> necessaire d'avoir (from db import db_user) ::: SQL CRUD Queries qui envoi les infos avec argument 'request'

    ---> besoin de (from db.hash import Hash) pour créer user ::: class to hash password
    ---> besoin de (from schemas import UserBase) pour recupérer info du client ::: utilise pydantic pour data validation
    ---> besoin de (from db.models import BdUser) qui defini la table User de la BDD ::: name + surname + pass (+ items, a list of books)

    ----> besoin de DbArticles dans models.py pour faire la relation avec DbUser :: title + autheur + isbn + 

    ----> besoin de route pour envoyer les info a fastapi

    -> authentication.py need post request (using router) and 'oauth2.create_access_token'


    -> pour ajouter un user on a besoin de routes (router/users.py) ::: permet d'envoyer/recevoir des infos avec fastapi

    --> chaque route utilise un schema spécifique (voir en parallele les CRUD db_user)

    -> pour ajouter un article(livre) on a besoin de routes (router/article.py) ::: 

=> finalement on a besoin de main pour lancer l'api

* NameError: name 'Article' is not defined (class UserDisplay(BaseModel):)
