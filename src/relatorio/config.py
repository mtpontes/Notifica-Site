import os


class EmailConfig:
    """
    Carrega e valida configurações de e-mail a partir de variáveis de ambiente.

    Atributos de classe:
        EMAIL_ADDRESS (str): Endereço de e-mail do remetente.
        EMAIL_PASSWORD (str): Senha ou token do e-mail.
        SMTP_SERVER (str): Servidor SMTP usado para envio.
        SMTP_PORT (int): Porta do servidor SMTP.

    Métodos:
        as_dict() -> dict: Retorna as configurações como um dicionário.

    Validação:
        No momento da importação, valida se todas as variáveis obrigatórias estão definidas.
        Se alguma estiver ausente ou inválida (ex: porta = 0), lança um `EnvironmentError`.
    """
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "0"))

    @classmethod
    def as_dict(cls):
        return {
            "EMAIL_ADDRESS": cls.EMAIL_ADDRESS,
            "EMAIL_PASSWORD": cls.EMAIL_PASSWORD,
            "SMTP_SERVER": cls.SMTP_SERVER,
            "SMTP_PORT": cls.SMTP_PORT
        }


for key, value in EmailConfig.as_dict().items():
    if value is None or (isinstance(value, int) and value == 0):
        raise EnvironmentError(f"Variável de ambiente obrigatória não definida: {key}")