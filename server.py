from flask import Flask, request
from flask_cors import CORS
from api.controllers.Indicador import Indicador

app = Flask(__name__)
CORS(app)

@app.route('/indicadores', methods=['GET'])
def getAll():
    print("indicadores get")
    return (Indicador.list())

@app.route('/indicadores', methods=['POST'])
def postOne():
    print("indicadores post")
    body = request.json
    return (Indicador.crear(body))

app.run(port=5000, debug=True)