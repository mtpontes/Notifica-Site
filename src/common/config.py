import os

import boto3
from boto3.resources.base import ServiceResource
from boto3.resources.factory import dynamodb


class Envs:
    """
    Classe utilitária para carregar e centralizar variáveis de ambiente usadas na aplicação.

    Atributos de classe:
        IS_OFFLINE (bool): Indica se a aplicação está sendo executada em ambiente offline (ex: local).
        REGION (str): Região AWS utilizada pelos serviços.
        VISITAS_TABLE (str): Nome da tabela DynamoDB usada para armazenar visitas.
        GIF_PATH (str): Caminho para o GIF a ser utilizado (opcional, não validado aqui).

    Métodos:
        as_dict() -> dict:
            Retorna um dicionário com as principais variáveis de ambiente usadas pela aplicação.

    Validação:
        Ao carregar a classe, verifica se as variáveis obrigatórias (IS_OFFLINE, REGION, VISITAS_TABLE)
        estão definidas. Se alguma estiver ausente, uma exceção `EnvironmentError` é lançada.
    """
    IS_OFFLINE = os.environ.get("IS_OFFLINE") == "true"
    REGION = os.getenv("REGION")
    VISITAS_TABLE = os.getenv("VISITAS_TABLE")
    GIF_PATH = os.getenv("GIF_PATH")

    @classmethod
    def as_dict(cls) -> dict:
        return {
            "IS_OFFLINE": cls.IS_OFFLINE,
            "VISITAS_TABLE": cls.VISITAS_TABLE,
            "REGION": cls.REGION,
        }

for key, value in Envs.as_dict().items():
    if value is None:
        raise EnvironmentError(f"Variável de ambiente obrigatória não definida: {key}")

def criar_cliente_de_tabela_dynamodb() -> dynamodb.Table:
    """Factory function para criar resource.Table DynamoDB baseado no ambiente"""
    resource: ServiceResource = None
    if Envs.IS_OFFLINE:
        resource = boto3.resource(
            "dynamodb",
            region_name=Envs.REGION,
            endpoint_url="http://localhost:8000",
            aws_access_key_id="fake",
            aws_secret_access_key="fake"
        )

    resource = boto3.resource("dynamodb", region_name=Envs.REGION)
    return resource.Table(Envs.VISITAS_TABLE)