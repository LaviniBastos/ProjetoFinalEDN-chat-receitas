# Chef Bot 
##Chatbot de Receitas com IA e AWS
####Um chatbot interativo que gera sugestões de receitas com base nos ingredientes que o usuário tem disponíveis. O sistema permite salvar receitas favoritas para consultas posterior.

1. Índice
2. Arquitetura
3. Tecnologias Utilizadas
4. Execução e Utilização
5. Desafios e Dificuldades
6. Contribuidores
7. Objetivo
   
Desenvolver um chatbot capaz de sugerir receitas criativas com base nos ingredientes que o usuário possui. O chatbot também permitirá que os usuários salvem suas receitas favoritas para acesso futuro.

# Arquitetura AWS


# Tecnologias Utilizadas
1. AWS Lex
Utilizado para criar o chatbot, permitindo a interação do usuário via texto dentro do Slack.

2. Amazon Bedrock
Usado para gerar receitas dinamicamente com base nos ingredientes inseridos pelo usuário, utilizando modelos de linguagem avançados.

3. AWS Lambda
Executa funções serverless para processar a lógica do chatbot, integrar o Bedrock e armazenar receitas favoritas.

4. Amazon DynamoDB
Banco de dados NoSQL para armazenar receitas favoritas e histórico de interação dos usuários.

5. Amazon API Gateway
Exponibiliza um endpoint seguro para receber requisições do Slack e encaminhá-las ao AWS Lambda.

6. AWS Secrets Manager
Armazena credenciais seguras para acessar a API do Slack e outros serviços sensíveis.




🚧 Desafios e Dificuldades
Treinar a IA para gerar receitas coerentes e variadas.
Integração segura com o Slack garantindo autenticidade e segurança dos dados.
Otimização de latência, garantindo respostas rápidas mesmo em picos de uso.
