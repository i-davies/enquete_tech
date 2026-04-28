from flask import Flask, jsonify, request
from pydantic import BaseModel, ValidationError
from database import app, db
from models import TecnologiaModel

class VotoRequest(BaseModel):
    tecnologia: str


@app.route('/api/votos', methods=['GET'])
def buscar_placar():
    """ GET JSON Placar """
    # SELECT * FROM tecnologia
    tecnologias = TecnologiaModel.query.all()
    banco_formatado = {tech.nome: tech.votos for tech in tecnologias}
    return jsonify(banco_formatado)


@app.route('/api/votar', methods=['POST'])
def registrar_voto():
    """POST para votação"""
    try:
        dados_validados = VotoRequest(**request.json)
    except ValidationError as e:
        return jsonify({"sucesso": False, "mensagem": "Formato inválido de votação"}), 400
    
    tecnologia_votada = dados_validados.tecnologia

    tech_alvo = TecnologiaModel.query.filter_by(nome=tecnologia_votada).first()

    if tech_alvo:
        tech_alvo.votos += 1
        db.session.commit()
        return jsonify({"Sucesso": True, "mesagem": f"Voto para {tecnologia_votada} computado!"})
    
    return jsonify({"sucesso": False, "mesagem": "Tecnologia não encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

