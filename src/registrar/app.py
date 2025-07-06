from flask import Flask, jsonify, request
from flask_cors import CORS

from src.common.config import criar_cliente_de_tabela_dynamodb
from src.registrar.services import processar_visita_do_request


app = Flask(__name__)
CORS(app)


@app.route('/api/visitas', methods=['POST'])
def handle_visit():
    """
    Handler principal para processar visitas.
    Recebe uma requisição POST e registra a visita no banco.
    """
    success, response = processar_visita_do_request(request, criar_cliente_de_tabela_dynamodb())

    if not success:
        return "Acesso negado: Bots não são permitidos.", 403
    
    return jsonify({ "message": "Visita registrada com sucesso!" })

