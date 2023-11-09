from flask import Flask, render_template
import redis
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379)

@app.route('/')
def index():
    # Récupérer toutes les clés du modèle "vlibid:*"
    all_keys = redis_client.keys("vlibid:*")

    # Initialiser une liste pour stocker toutes les données
    all_data = []

    # Parcourir toutes les clés et récupérer les données associées
    for key in all_keys:
        data_raw = redis_client.hgetall(key)
        data = {key.decode('utf-8'): value.decode('utf-8') for key, value in data_raw.items()}
        all_data.append(data)

    return render_template('index_all.html', all_data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
