from datetime import datetime
from zoneinfo import ZoneInfo


def obter_datetime_now_br_sp() -> datetime:
    """
    Retorna a data e hora atual no fuso horário do Brasil (SP).
    """
    return datetime.now(ZoneInfo("America/Sao_Paulo"))