from boto3.resources.factory import dynamodb

from src.common.log import log


def carregar_visitas_do_db(dynamodb_table_client: dynamodb.Table) -> list[dict[str, str]]:
    """Busca visitas do DynamoDB"""
    try:
        result = dynamodb_table_client.scan()
        return result.get("Items", [])
    except Exception as e:
        log.error("Erro ao buscar visitas: %s", e)
        return []