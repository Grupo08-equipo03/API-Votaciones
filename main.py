from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorVoto import ControladorVoto

miControladorCandidatos = ControladorCandidato()
miControladorPartidos = ControladorPartido()
miControladorMesas = ControladorMesa()
miControladorVotos = ControladorVoto()

# ---------------------------------------------------------- #
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
# ---------------------------------------------------------- #










# ---------------------------------------------------------- #
# URLS de Camilo
@app.route("/votos", methods=['GET'])
def getVotos():
    json = miControladorVotos.index()
    return jsonify(json)

@app.route("/votos/<string:id>", methods=['GET'])
def getVoto(id):
    json = miControladorVotos.show(id)
    return jsonify(json)

@app.route("/votos/candidatos/<string:id_candidato>/mesas/<string:id_mesa>", methods=['POST'])
def crearVoto(id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorVotos.create(data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/votos/<string:id_voto>/candidatos/<string:id_candidato>/mesas/<string:id_mesa>", methods=['PUT'])
def modificarVoto(id_voto, id_candidato, id_mesa):
    data = request.get_json()
    json = miControladorVotos.update(id_voto, data, id_candidato, id_mesa)
    return jsonify(json)

@app.route("/votos/<string:id_voto>", methods=['DELETE'])
def eliminarInscripcion(id_voto):
    json=miControladorVotos.delete(id_voto)
    return jsonify(json)
# ---------------------------------------------------------- #

def loadFileConfig():
    with open('configuracion.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

# ---------------------------------------------------------- #