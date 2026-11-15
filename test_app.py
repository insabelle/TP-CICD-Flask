from app import app


# Test 1 : Vérifier la page d'accueil
def test_accueil():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


# Test 2 : Vérifier la liste des étudiants
def test_afficher_etudiants():
    client = app.test_client()
    response = client.get("/etudiants")

    assert response.status_code == 200
    assert len(response.json) == 3


# Test 3 : Rechercher un étudiant existant
def test_chercher_etudiant():
    client = app.test_client()
    response = client.get("/etudiants/1")

    assert response.status_code == 200
    assert response.json["nom"] == "Ahmed"


# Test 4 : Rechercher un étudiant inexistant
def test_etudiant_introuvable():
    client = app.test_client()
    response = client.get("/etudiants/100")

    assert response.status_code == 404
