from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Récupération des secrets (Configurés dans Docker Compose)
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        nom = request.form.get('nom')
        # Ici, tu pourrais insérer 'nom' dans ta DB en utilisant DB_USER et DB_PASSWORD
        message = f"Merci {nom}, formulaire reçu !"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)