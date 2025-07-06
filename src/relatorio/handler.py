from datetime import datetime

from src.common.log import log
from src.common.utils import obter_datetime_now_br_sp
from src.common.config import criar_cliente_de_tabela_dynamodb
from src.relatorio.utils import template_email
from src.relatorio.database import carregar_visitas_do_db
from src.relatorio.email_service import enviar_email


def handler(event, context):
    visitas = carregar_visitas_do_db(criar_cliente_de_tabela_dynamodb())
    
    if not visitas:
        log.info("Nenhuma visita para relatar hoje.")
        return

    try:
        agora: datetime = obter_datetime_now_br_sp()
        conteudo_email = template_email(visitas, agora)
        enviar_email(conteudo_email)
        log.info("Relatório diário enviado em %s", agora.strftime('%d/%m/%Y %H:%M:%S'))
    except Exception as e:
        log.error("Erro ao enviar relatório diário: %s", e)