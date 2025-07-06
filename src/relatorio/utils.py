from datetime import datetime
from email.mime.text import MIMEText

from src.common.log import log
from src.common.config import Envs
from src.relatorio.config import EmailConfig


def template_email(visitas: list[dict], agora: datetime) -> MIMEText:
    """Gera o corpo completo do e-mail com o relatório diário baseado nas visitas"""
    log.info('Valor de visitas: %s', visitas)
    
    total_visitas: int = len(visitas)
    detalhes_visitas: str = _agrupar_visitas(visitas)
    gif_html: str = _tratar_gif_html()

    template: str = _criar_html_de_email(total_visitas, agora, detalhes_visitas, gif_html)
    return _montar_email(template)

def _agrupar_visitas(visitas) -> str:
    """Monta a seção HTML com os detalhes de cada visita formatada"""
    detalhes_visitas: str = ""
    for visita in visitas:
        tempo: str = datetime.fromisoformat(visita.get("tempo")).strftime("%d/%m/%Y %H:%M:%S")
        detalhes_visitas += f"<p>Visita em: {tempo}</p>"
    return detalhes_visitas

def _tratar_gif_html() -> str:
    """Insere o GIF no corpo do e-mail se o caminho estiver configurado"""
    return f'<img src="{Envs.GIF_PATH}" alt="Torcida GIF" style="width:200px;">' if Envs.GIF_PATH else ""

def _criar_html_de_email(total_visitas: int, agora: datetime, detalhes_visitas: str, gif_html: str) -> str:
    """Cria o template HTML final do e-mail unindo estatísticas, detalhes e GIF"""
    return f"""
        <html>
        <body>
        <h2>Relatório Diário de Visitas</h2>
        <p>Total de Visitas: {total_visitas}</p>
        <p>Data do Relatório: {agora.strftime('%d/%m/%Y')}</p>
        <p>Vamos torcer por uma entrevista!!</p>

        <h3>Detalhes das Visitas:</h3>
        {detalhes_visitas}
        {gif_html}
        </body>
        </html>
        """

def _montar_email(conteudo_html: str) -> MIMEText:
    """Constrói o objeto MIME do e-mail com o conteúdo HTML e configura os cabeçalhos"""
    msg = MIMEText(conteudo_html, "html")
    msg["Subject"] = "Relatório Diário de Visitas"
    msg["From"] = EmailConfig.EMAIL_ADDRESS
    msg["To"] = EmailConfig.EMAIL_ADDRESS
    return msg