# Chef Bot 
## Chatbot de Receitas com IA e AWS

---

# Equipe:
- Scrum Master: 
- Líder Técnica: 
- Desenvolvedores: 
- Arquitetura: 
- Design: 

## Objetivo do projeto
#### Desenvolvemos neste projeto um chatbot interativo capaz de sugerir receitas criativas com base nos ingredientes que o usuário possui. O chatbot também permitirá que os usuários salvem suas receitas favoritas para acesso futuro.

1. Equipe
2. Objetivo
3. Índice
4. Tecnologias Utilizadas
5. Arquitetura
6. Execução e Utilização
7. Melhorias futuras

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


# Arquitetura AWS

![Captura de tela 2025-03-26 155726](https://github.com/user-attachments/assets/0ff5a7d6-3558-4275-a82e-222b031e9d39)


# Execução e Utilização

Fluxo da estrutura do Chatbot com a integração dos serviços:






# Melhorias futuras
- Em um futuro próximo, enviar semanalmente ou até diariamente por e-mail para um cliente cadastrado ou assinante, receitas novas e diferentes para ele se manter atualizado e sempre com idéias do que cozinhar.





