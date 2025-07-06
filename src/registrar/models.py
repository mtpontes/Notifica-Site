import uuid
import time

from src.common.utils import obter_datetime_now_br_sp


def criar_objeto_de_visita(ip: str, user_agent: str) -> dict[str, any]:
    """Cria e retorna um dicionário representando uma visita para persistência no DynamoDB"""
    return {
        'visita_id': _criar_visita_id(),
        'tempo': _criar_timestamp(),
        'ip': ip,
        'user_agent': user_agent,
        'ttl': _criar_ttl()
    }


def _criar_visita_id() -> str:
    """Gera UUID único para visita"""
    return str(uuid.uuid4())


def _criar_timestamp() -> str:
    """Cria timestamp atual em formato ISO"""
    return obter_datetime_now_br_sp().isoformat()


def _criar_ttl(hours: int = 24) -> int:
    """Cria TTL baseado em horas a partir de agora"""
    return int(time.time()) + (60 * 60 * hours)
