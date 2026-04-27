from flask import Flask, render_template, request
import os
import psycopg2

app = Flask(__name__)

# Fonction pour se connecter à la base de données
def get_db_connection():
    # On récupère les variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASSWORD')

    # Vérification de sécurité pour le débogage
    if not db_pass:
        raise ValueError("Le mot de passe de la base de données est vide ou non trouvé !")

    conn = psycopg2.connect(
        host='db',
        database=db_name,
        user=db_user,
        password=db_pass # C'est ici que l'erreur se produit si db_pass est vide
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        profession = request.form.get('profession')

        try:
            # Connexion et insertion des données
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO inscriptions (nom, email, profession)'
                        'VALUES (%s, %s, %s)',
                        (nom, email, profession))
            conn.commit()
            cur.close()
            conn.close()
            message = f"Félicitations {nom}, vos données ont été enregistrées en base !"
        except Exception as e:
            message = f"Erreur lors de l'enregistrement : {e}"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)