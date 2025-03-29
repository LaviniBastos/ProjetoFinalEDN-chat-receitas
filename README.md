# 🍲🤖 Chatbot de Receitas com IA e AWS

<p align="center"><i>Um chatbot interativo que gera sugestões de receitas com base nos ingredientes que o usuário tem disponíveis. O sistema permite salvar receitas favoritas para consulta posterior.</i></p>

## 📖 Índice

1. [🏛️ Arquitetura](#-arquitetura-preliminar-aws)
2. [🛠️ Tecnologias Utilizadas](#-tecnologias-utilizadas)
3. [🚀 Execução e Utilização](#-execucao-e-utilizacao)
4. [🧱 Requisitos](#-requisitos)
5. [🚧 Melhorias Futuras](#-melhorias-futuras)
6. [👥 Contribuidores](#-contribuidores)


## 🌟 Objetivo

O Chef Bot é um chatbot interativo projetado para sugerir receitas criativas com base nos ingredientes que o usuário possui. Além disso, permite que os usuários salvem suas receitas favoritas para acesso futuro. O projeto utiliza tecnologias de Inteligência Artificial (IA) e serviços da AWS para oferecer interação eficiente e em tempo real.


### Proposta de valor

O Chef Bot facilita o dia a dia na cozinha, fornecendo sugestões de receitas personalizadas com base nos ingredientes disponíveis. Ele otimiza o tempo dos usuários, reduz o desperdício de alimentos e incentiva a criatividade culinária. Além disso, a integração com a AWS garante escalabilidade, segurança e alto desempenho para a aplicação.

## 🏛️ Arquitetura Preliminar AWS

![Captura de tela 2025-03-26 155726](https://github.com/user-attachments/assets/9acdd512-a7fd-4dbf-9ce2-63a77c510ed4)

## 🛠️ Tecnologias Utilizadas

### **AWS Route 53** 
Registro de domínio do chatbot.

### **AWS CloudFront** 
Distribuição escalável e de baixa latência do conteúdo do chatbot.

### **AWS Lex** 
Criar o chatbot para interação via texto ou voz.

### **AWS Lambda**  Executa funções serverless para processar a lógica do chatbot, integrar o Bedrock e armazenar receitas favoritas.

### **Boto3** 
Biblioteca Python para interagir com serviços AWS e modelos de IA.

### **Amazon Bedrock** 
Gera receitas dinamicamente com base nos ingredientes inseridos.

### **Amazon DynamoDB** 
Banco de dados NoSQL para armazenar receitas favoritas e histórico de interação.

### **Amazon CloudWatch** 
Monitoramento e registro de métricas e logs para análise de desempenho.

### **Amazon S3** 
Armazena a base de conhecimento para consulta do Amazon Bedrock.

### **OpenSearch** 
Organiza e retorna informações do S3 para o Amazon Bedrock.

## Segurança da Aplicação

### **AWS IAM**  
Controle de acesso dos administradores.

### **AWS WAF**  
Proteção contra ataques como SQL Injection.

### **AWS Shield**  
Prevenção contra ataques DDoS.


## 🚀 Execução e Utilização

## Fluxo da estrutura do chatbot com a integração dos serviços:

1- O usuário acessa a aplicação pelo Route 53 e CloudFront.

2- O usuário interage com o Amazon Lex via texto ou voz.

3- O Amazon Lex aciona uma função AWS Lambda para processar a entrada.

4- Logs e métricas são registrados no Amazon CloudWatch para monitoramento.

5- A função AWS Lambda salva a solicitação no Amazon DynamoDB, conforme necessário.

5- A função AWS Lambda solicita ao Amazon Bedrock a geração de uma receita baseada nos ingredientes fornecidos.

6- O Amazon Bedrock consulta o OpenSearch, que busca informações no Amazon S3.

7- A resposta é enviada do Amazon Bedrock para o Amazon Lex, que retorna o resultado ao usuário via CloudFront.

## 🧱 Requisitos

### Requisitos Funcionais

- O chatbot deve permitir interações via texto e voz.
- O usuário pode inserir uma lista de ingredientes para obter sugestões de receitas.
- Possibilidade de salvar receitas favoritas.
- As receitas devem ser geradas dinamicamente com base nos ingredientes informados.
- O chatbot deve oferecer suporte a perguntas frequentes sobre culinária.
- A plataforma deve ser acessível via navegador e responsiva para dispositivos móveis.

### Requisitos Não Funcionais

- O sistema deve responder às solicitações em até 2 segundos.
- Os dados dos usuários devem ser armazenados de forma segura.
- A arquitetura deve ser escalável para suportar um grande número de usuários simultâneos.
- O chatbot deve ter alta disponibilidade e ser resiliente a falhas.
- O monitoramento dos serviços deve ser realizado continuamente via CloudWatch.

## 🚧 Melhorias Futuras

- Implementar um sistema de recomendação personalizado baseado no histórico de interação do usuário.

- Envio periódico de receitas personalizadas por e-mail para usuários cadastrados.

- Integração com assistentes de voz como Alexa e Google Assistant.

- Expansão do chatbot para sugestões de harmonização de vinhos e bebidas.


## 👥 Contribuidores

- Scrum Master: Talyta e Lavini
- Líder Técnica: Olivia Oliva
- Desenvolvedores: Daniel e Talyta
- Arquitetura: Lavini Bastos
- Design: Daniel Villegas
- Documentação: Débora e Leonardo

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Daniel-Marim" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/186893500?v=4" width="100px;" alt="Foto Daniel"/><br>
        <sub>
          <b>Daniel Marim</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/DevDan7" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/152210372?v=4" width="100px;" alt="Foto Daniel"/><br>
        <sub>
          <b>Daniel Villegas</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/deboralopesdev" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/196735456?v=4" width="100px;" alt="Foto Debora"/><br>
        <sub>
          <b>Débora Lopes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LaviniBastos" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/160741212?v=4" width="100px;" alt="Foto Lavini"/><br>
        <sub>
          <b>Lavini Bastos </b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/oliviaoliva" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/89538707?v=4" width="100px;" alt="Foto Olivia"/><br>
        <sub>
          <b>Olivia Oliva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Apenassam" title="GitHub">
        <img src="https://avatars.githubusercontent.com/u/176727412?v=4" width="100px;" alt="Foto Talyta Sampaio"/><br>
        <sub>
          <b>Talyta Sampaio</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

📌 **Versão 1.0**


