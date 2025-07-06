from typing import Tuple


def extrair_dados_do_request(request_obj) -> Tuple[str, str]:
    """Extrai dados relevantes do request de forma funcional"""
    return (
        request_obj.remote_addr or 'unknown',
        request_obj.headers.get('User-Agent', '')
    )