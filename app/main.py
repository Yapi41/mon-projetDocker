from flask import Flask, render_template, request
import os

# On précise le dossier des templates explicitement
app = Flask(__name__, template_folder='templates')

# Récupération des secrets
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        nom = request.form.get('nom')
        message = f"Merci {nom}, formulaire reçu !"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    # Le debug=True est super utile en local pour voir les erreurs
    app.run(host='0.0.0.0', port=5000, debug=True)