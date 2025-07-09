# API de Notificação de Visitas por E-mail

Este projeto é uma API simples desenvolvida com Flask (Python) que detecta acessos e envia notificações por e-mail sobre as visitas.

## O que ela faz?

A API gera um relatório diário de acessos ao seu portifólio, contendo:
-  Quantidade total de acessos do dia  
-  Lista com os **horários das visitas** e quantas vezes ocorreram  

##  Funcionalidades

- Detecta acessos via rotas HTTP (`/` e `/track-visit`)
- Envia e-mails de forma segura via SMTP (Gmail)
- Gera **relatórios diários automáticos às 00:00h**
- Os registros no DynamoDB são **automáticamente deletados** após 24h de vida utilizando o recurso nativo de **ttl (Time To Live)**
- Mostra os horários exatos das visitas, regiões e User-Agents
- Suporte a Senhas de Aplicativo do Google
- Variáveis de ambiente gerenciadas via `Serverless Framework`
- Pode ser integrada facilmente com front-ends usando `fetch`
- Proteção contra bots via verificação de User-Agent

## Tecnologias Utilizadas

- Python 3.12
- Flask
- Serverless Framework
- AWS Lambda
- AWS DynamoDB
- AWS API Gateway
- AWS EventBridge

## Como rodar

### Configure seu Serverless Framework
Instale o serverless framework via NPM globalmente:
```bash
npm install -g serverless@^4
```

Faça login no serverless framework (exclusividade da versão 4.0 ou superior) e retorne ao terminal quando no browser sinalizar sucesso na autenticação:
```bash
sls login
```

Instale as dependências do Serverless Framework::
```bash
npm install -y
```

<details>
  <summary><h3>Offline</h3></summary>

### Requisitos
- Python 3.12
- Node.js 18+
- Docker

#### Deploy
Instale as dependências do projeto para evitar problemas:
```bash
pip install -r ./requirements/local.txt
```

Iniciar aplicação:
```bash
npm run offline:start
```

Finalizar aplicação por completo:
```bash
npm run offline:stop
```

</details>

<details>
  <summary><h3>AWS</h3></summary>

### Requisitos
- Python 3.12
- Node.js 18+

### Variáveis de ambiente
As seguintes variáveis de ambiente devem estar corretamente configuradas:

```env
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

#### [Configure o AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions)

- Crie um usuário no IAM e gere uma chave de acesso
- Configure as credenciais no seu AWS CLI
```bash
aws configure
```

#### Possíveis políticas AWS para o projeto:
- AmazonAPIGatewayAdministrator
- AmazonAPIGatewayPushToCloudWatchLogs
- AmazonS3FullAccess
- AmazonS3ObjectLambdaExecutionRolePolicy
- AWSCloudFormationFullAccess
- AWSLambda_FullAccess
- CloudWatchLogsFullAccess
- IAMFullAccess

### Gere os artefatos da aplicação

### Deploy
O Serverless Framework está configurado para buscar os artefatos no nível corrente no diretório `./artifacts`. Para facilitar o deploy da aplicação por via local, foi criado um script em Node.JS para automatizar a construção dos artefatos de forma otimizada. Execute o script de construção dos artefatos com o seguinte comando:

#### Faça o deploy
```bash
npm run deploy:prod
```

#### Desfaça o deploy
```bash
sls remove --stage prod
```

</details>

