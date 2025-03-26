Chef Bot

Chatbot de Receitas com IA e AWS

Equipe

Scrum Master:

Líder Técnica:

Desenvolvedores:

Arquitetura:

Design:

Objetivo do Projeto

O Chef Bot é um chatbot interativo projetado para sugerir receitas criativas com base nos ingredientes que o usuário possui. Além disso, permite que os usuários salvem suas receitas favoritas para acesso futuro. O projeto utiliza tecnologias de Inteligência Artificial (IA) e serviços da AWS para oferecer interação eficiente e em tempo real.

Índice

Equipe

Objetivo do Projeto

Tecnologias Utilizadas

Arquitetura AWS

Execução e Utilização

Requisitos Funcionais

Requisitos Não Funcionais

Melhorias Futuras

Tecnologias Utilizadas

AWS Route 53 - Registro de domínio do chatbot.

AWS CloudFront - Distribuição escalável e de baixa latência do conteúdo do chatbot.

AWS Lex - Criar o chatbot para interação via texto ou voz.

AWS Lambda - Executa funções serverless para processar a lógica do chatbot, integrar o Bedrock e armazenar receitas favoritas.

Boto3 - Biblioteca Python para interagir com serviços AWS e modelos de IA.

Amazon Bedrock - Gera receitas dinamicamente com base nos ingredientes inseridos.

Amazon DynamoDB - Banco de dados NoSQL para armazenar receitas favoritas e histórico de interação.

Amazon CloudWatch - Monitoramento e registro de métricas e logs para análise de desempenho.

Amazon S3 - Armazena a base de conhecimento para consulta do Amazon Bedrock.

OpenSearch - Organiza e retorna informações do S3 para o Amazon Bedrock.

Segurança da Aplicação

AWS IAM - Controle de acesso dos administradores.

AWS WAF - Proteção contra ataques como SQL Injection.

AWS Shield - Prevenção contra ataques DDoS.

Arquitetura AWS



Execução e Utilização

Fluxo da estrutura do chatbot com a integração dos serviços:

O usuário acessa a aplicação pelo Route 53 e CloudFront.

O usuário interage com o Amazon Lex via texto ou voz.

O Amazon Lex aciona uma função AWS Lambda para processar a entrada.

Logs e métricas são registrados no Amazon CloudWatch para monitoramento.

A função AWS Lambda salva a solicitação no Amazon DynamoDB, conforme necessário.

A função AWS Lambda solicita ao Amazon Bedrock a geração de uma receita baseada nos ingredientes fornecidos.

O Amazon Bedrock consulta o OpenSearch, que busca informações no Amazon S3.

A resposta é enviada do Amazon Bedrock para o Amazon Lex, que retorna o resultado ao usuário via CloudFront.

Requisitos Funcionais

O chatbot deve permitir interações via texto e voz.

O usuário pode inserir uma lista de ingredientes para obter sugestões de receitas.

Possibilidade de salvar receitas favoritas.

As receitas devem ser geradas dinamicamente com base nos ingredientes informados.

O chatbot deve oferecer suporte a perguntas frequentes sobre culinária.

A plataforma deve ser acessível via navegador e responsiva para dispositivos móveis.

Requisitos Não Funcionais

O sistema deve responder às solicitações em até 2 segundos.

Os dados dos usuários devem ser armazenados de forma segura.

A arquitetura deve ser escalável para suportar um grande número de usuários simultâneos.

O chatbot deve ter alta disponibilidade e ser resiliente a falhas.

O monitoramento dos serviços deve ser realizado continuamente via CloudWatch.

Melhorias Futuras

Implementar um sistema de recomendação personalizado baseado no histórico de interação do usuário.

Envio periódico de receitas personalizadas por e-mail para usuários cadastrados.

Integração com assistentes de voz como Alexa e Google Assistant.

Expansão do chatbot para sugestões de harmonização de vinhos e bebidas.





