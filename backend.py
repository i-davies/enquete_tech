from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado em memória
PLACAR = {
    "Flask" : 0,
    "FastAPI": 0,
    "Flet": 0
}

@app.route('/api/votos', methods=['GET'])
def buscar_placar():
    """ GET JSON Placar """
    return jsonify(PLACAR)


@app.route('/api/votar', methods=['POST'])
def registrar_voto():
    """POST para votação"""
    dados = request.json
    tecnologia = dados.get('tecnologia')

    if tecnologia in PLACAR:
        PLACAR[tecnologia] += 1
        return jsonify({"Sucesso": True, "mesagem": f"Voto para {tecnologia} computado!"})
    
    return jsonify({"sucesso": False, "mesagem": "Tecnologia não encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

