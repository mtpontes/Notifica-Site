def salvar_visita_no_db(db_client, visit_item: dict) -> dict:
    """Salva visita no DynamoDB e retorna resposta"""
    return db_client.put_item(Item=visit_item)