
from flask import Flask, jsonify

app = Flask(__name__)

etudiants = [
    {"id": 1, "nom": "Ahmed", "moyenne": 15},
    {"id": 2, "nom": "Sara", "moyenne": 17},
    {"id": 3, "nom": "Youssef", "moyenne": 9}
]


@app.route("/")
def accueil():
    return "Bienvenue dans l'application de gestion des étudiants !"


@app.route("/etudiants")
def afficher_etudiants():
    return jsonify(etudiants)


@app.route("/etudiants/<int:id>")
def chercher_etudiant(id):
    for etudiant in etudiants:
        if etudiant["id"] == id:
            return jsonify(etudiant)

    return jsonify({"message": "Etudiant introuvable"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
