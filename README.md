# API de Notificação de Visitas por E-mail

Este projeto é uma API simples feita com Flask (Python) que detecta acessos e envia um e-mail notificando sobre a visita, incluindo o momento exato do acesso.  
Para evitar envio excessivo, o sistema limita o envio para no máximo um e-mail a cada 10 segundos.

---

##  Funcionalidades

-  Detecta acessos via rotas HTTP
- Envia e-mails via SMTP (Gmail)
- Envio seguro usando **Senhas de Aplicativo do Google**
- Variáveis de ambiente configuradas com **python-dotenv**
-  Controle para evitar múltiplos envios em menos de 10 segundos
- Pode ser integrada a front-ends com `fetch`, como:

```js
const res = await fetch('https://api-gbrh.onrender.com/');

Tecnologias utilizadas:

Python 3

Flask

Flask-CORS

python-dotenv

smtplib (para envio de e-mail)

Gmail SMTP
------------------------------
Observações
O servidor deve estar rodando para que a API responda às requisições.

Garanta que as variáveis de ambiente estejam corretamente configuradas.

A limitação de 10 segundos evita spam de e-mails.

