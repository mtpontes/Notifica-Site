from serverless_wsgi import handle_request

from src.registrar.app import app


def handler(event, context):
    """
    Handler AWS Lambda para aplicações Flask via Serverless Framework.

    Usa `serverless-wsgi` para adaptar a aplicação Flask (`app`) ao formato esperado
    pela Lambda, convertendo eventos do API Gateway em requisições WSGI.

    Parâmetros:
        event (dict): Evento da Lambda (ex: API Gateway).
        context (LambdaContext): Contexto da execução.

    Retorna:
        dict: Resposta HTTP formatada para o API Gateway.
    """
    return handle_request(app, event, context)