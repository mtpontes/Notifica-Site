import smtplib

from src.relatorio.config import EmailConfig


def enviar_email(msg) -> None:
    if not all([EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT, EmailConfig.EMAIL_ADDRESS, EmailConfig.EMAIL_PASSWORD]):
        raise ValueError("Algumas chaves de configuração das credenciais de email estão vazias ou nulas")

    with smtplib.SMTP(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT) as servidor:
        servidor.starttls()
        servidor.login(EmailConfig.EMAIL_ADDRESS, EmailConfig.EMAIL_PASSWORD)
        servidor.send_message(msg)

