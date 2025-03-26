# Chef Bot 
## Chatbot de Receitas com IA e AWS
####Um chatbot interativo que gera sugestões de receitas com base nos ingredientes que o usuário tem disponíveis. O sistema permite salvar receitas favoritas para consultas posterior.

1. Índice
2. Arquitetura
3. Tecnologias Utilizadas
4. Execução e Utilização
5. Desafios e Dificuldades
6. Contribuidores
7. Objetivo
   
Desenvolvemos neste projeto um chatbot capaz de sugerir receitas criativas com base nos ingredientes que o usuário possui. O chatbot também permitirá que os usuários salvem suas receitas favoritas para acesso futuro.

Equipe
Scrum Master: 
Líder Técnica: 
Desenvolvedores: 
Arquitetura: 
Design: 


# Arquitetura AWS




# Tecnologias Utilizadas
1. AWS Route 53


2. AWS CloudFront

3. AWS Lex
Utilizado para criar o chatbot, permitindo a interação do usuário via texto ou voz.

4. AWS Lambda
Executa funções serverless para processar a lógica do chatbot, integrar o Bedrock e armazenar receitas favoritas.

5. Boto3
Biblioteca em python que interage com os modelos de IA  

6. Amazon Bedrock
Usado para gerar receitas dinamicamente com base nos ingredientes inseridos pelo usuário, utilizando modelos de linguagem avançados.

7. Amazon DynamoDB
Banco de dados NoSQL para armazenar receitas favoritas e histórico de interação dos usuários.

8. Amazon CloudWatch
    
9. Amazon S3
Armazena a base de conhecimento para que o modelo de IA do bedrock busque as informações de receita que o usuário precisa

10 - OpenSearch


Para  garantir a segurança da aplicação:
11. IAM
12. WAF
13. Shield





🚧 Desafios e Dificuldades
Treinar a IA para gerar receitas coerentes e variadas.
Integração segura com o Slack garantindo autenticidade e segurança dos dados.
Otimização de latência, garantindo respostas rápidas mesmo em picos de uso.
