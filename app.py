from flask import Flask
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import os
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)

# Carrega variáveis de ambiente
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

# Controle para evitar envio repetido em menos de 10 segundos
lock = threading.Lock()
last_email_time = None  # armazena datetime do último envio

def send_email():
    global last_email_time

    with lock:
        now = datetime.now()
        if last_email_time and (now - last_email_time) < timedelta(seconds=10):
            print("Email não enviado para evitar repetição em menos de 10 segundos.")
            return
        last_email_time = now

    try:
        html_content = f"""
        <html>
        <body>
        <p>MENSAGEM DO CORPO DO EMAIL</p>
        <p>Momento da visita: {now.strftime('%d/%m/%Y %H:%M:%S')}</p>"seu gif">
        </body>
        <img src="
        </html>
        """
        msg = MIMEText(html_content, 'html')
        msg['Subject'] = 'Você tem uma nova visita!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"E-mail enviado em {now.strftime('%d/%m/%Y %H:%M:%S')}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

@app.route('/')
def home():
    send_email()
    return "TITULO DO EMAIL"

@app.route('/track-visit')
def track_visit():
    send_email()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)