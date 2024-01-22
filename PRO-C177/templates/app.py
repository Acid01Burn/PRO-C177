from flask import Flask, render_templates, jsonify, request
import random

app= Flask(__name__)

templates = [
    {
         "inputs": 7,
        "category": "Deportes",
        "word": "Ajedrez"
    },
    {
        "inputs": 7,
        "category": "Nombre del país europeo",
        "word": "Francia"
    },
]

@app.route("/")
def index():
    return render_templates("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })

if __name__ == '__main__':
    app.run()