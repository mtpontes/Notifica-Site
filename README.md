Claro, minha parceira! Aqui está o `README.md` completo em **formato de código** pra você só copiar e colar onde quiser:

````markdown
# API de Notificação de Visitas por E-mail

Este projeto é uma API simples desenvolvida com Flask (Python) que detecta acessos e envia notificações por e-mail sobre as visitas.

## 📊 O que ela faz?

Agora, ao invés de enviar um e-mail a cada acesso, a API gera um **relatório diário às 18h**, contendo:

- ✅ Quantidade total de acessos do dia  
- 🕓 Lista com os **horários das visitas** e quantas vezes ocorreram  

## ✨ Funcionalidades

- Detecta acessos via rotas HTTP (`/` e `/track-visit`)
- Envia e-mails de forma segura via SMTP (Gmail)
- Gera **relatórios diários automáticos às 18h**
- Mostra os horários exatos das visitas e a quantidade por horário
- Suporte a Senhas de Aplicativo do Google
- Variáveis de ambiente gerenciadas com `python-dotenv`
- Pode ser integrada facilmente com front-ends usando `fetch`

## ⚙️ Tecnologias Utilizadas

- Python 3  
- Flask  
- Flask-CORS  
- python-dotenv  
- smtplib (para envio de e-mail)  
- Gmail SMTP  

## 📌 Observações

- O servidor precisa estar rodando para que a API responda às requisições.
- As seguintes variáveis de ambiente devem estar corretamente configuradas:

```env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
````

---

## 🔄 ATUALIZAÇÕES

### 🕒 Relatório Diário Programado às 18h

Graças à sugestão do [**Atevilson Araujo**](https://www.linkedin.com/in/atevilson-araujo/), agora o envio de e-mails acontece **somente uma vez ao dia, às 18h**, agrupando todos os acessos. Isso evita sobrecarga no e-mail e dá uma visão geral do tráfego do portfólio de forma organizada.

### 🤖 Proteção contra Bots

Essa funcionalidade foi desenvolvida após o [**Angelo Mendes**](https://www.linkedin.com/in/mangelodev/) me questionar sobre a possibilidade de bloquear acessos automatizados. Graças à visão dele, foi implementada uma verificação simples de User-Agent para impedir bots/crawlers indesejados. Resultado? Segurança reforçada e visitas mais precisas! 


Agradeço a cada um pelo estimulo e contribuição, sintam-se sempre a vontade para participar!
---
