import os

import boto3
from boto3.resources.base import ServiceResource


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

def criar_cliente_de_tabela_dynamodb():
    """
    Cria e retorna um cliente da tabela DynamoDB com base no ambiente de execução.

    Em ambiente offline (local), conecta-se a uma instância local do DynamoDB (em `http://localhost:8000`)
    usando credenciais falsas, e cria a tabela `Envs.VISITAS_TABLE` se ela ainda não existir.

    Em ambiente online (AWS), conecta-se diretamente ao DynamoDB da AWS usando a região especificada.

    Returns:
        boto3.resources.factory.dynamodb.Table: Instância da tabela DynamoDB configurada conforme o ambiente.
    """
    resource: ServiceResource = None
    
    if Envs.IS_OFFLINE:
        resource = boto3.resource(
            "dynamodb",
            region_name=Envs.REGION,
            endpoint_url="http://localhost:8000",
            aws_access_key_id="fake",
            aws_secret_access_key="fake"
        )
        
        # Verifica se a tabela existe antes de criar
        existing_tables = resource.meta.client.list_tables()['TableNames']
        if Envs.VISITAS_TABLE not in existing_tables:
            resource.create_table(
                TableName=Envs.VISITAS_TABLE,
                KeySchema=[{'AttributeName': 'visita_id', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'visita_id', 'AttributeType': 'S'}],
                ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
            )
            # Espera a tabela ficar ativa antes de continuar
            resource.meta.client.get_waiter('table_exists').wait(TableName=Envs.VISITAS_TABLE)

        return resource.Table(Envs.VISITAS_TABLE)

    else:
        resource = boto3.resource("dynamodb", region_name=Envs.REGION)
        return resource.Table(Envs.VISITAS_TABLE)