from flask import Request

from src.common.log import log
from src.registrar.utils import extrair_dados_do_request
from src.registrar.models import criar_objeto_de_visita
from src.registrar.database import salvar_visita_no_db
from src.registrar.validators import is_bot_user_agent


def processar_visita_do_request(request_obj: Request, dynamo_table_client) -> tuple[bool, dict | None]:
    """
    Processa uma requisição HTTP para registrar uma visita no DynamoDB, ignorando bots.

    Valida o User-Agent para evitar acessos automatizados. Se não for um bot,
    extrai IP e User-Agent, monta o objeto de visita e persiste no banco.

    Parâmetros:
        request_obj (Request): Objeto da requisição contendo headers e IP.
        dynamo_table_client: Instância de boto3.Table usada para salvar o item.

    Retorna:
        tuple[bool, dict | None]: 
            - `True` e a resposta do DynamoDB em caso de sucesso.
            - `False` e `None` se a visita for ignorada (ex: bot).
    """
    user_agent = request_obj.headers.get('User-Agent')
    
    if is_bot_user_agent(user_agent):
        log.warning('ACESSO NEGADO: Bot detectado')
        return False, None
    
    ip, user_agent_clean = extrair_dados_do_request(request_obj)
    visit_item = criar_objeto_de_visita(ip, user_agent_clean)
    
    response = salvar_visita_no_db(dynamo_table_client, visit_item)
    log.info('Resposta do banco: %s', response)
    
    return True, response