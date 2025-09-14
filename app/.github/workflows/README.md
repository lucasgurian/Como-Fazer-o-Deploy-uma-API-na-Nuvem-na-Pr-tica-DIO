# Template de API Containerizada com FastAPI e Azure

Este repositório é um template completo para construir, containerizar e implantar APIs de alta performance com **FastAPI** na nuvem da **Microsoft Azure**, utilizando o serviço serverless **Azure Container Apps**.

A automação de build e deploy (CI/CD) é totalmente gerenciada pelo **GitHub Actions**.

## ✨ Features

-   **API Moderna**: Construída com [FastAPI](https://fastapi.tiangolo.com/), oferecendo alta performance, documentação automática e validação de dados.
-   **Containerização Pronta**: `Dockerfile` otimizado com build multi-estágio para imagens leves e seguras.
-   **Infraestrutura como Código**: Comandos para criar toda a infraestrutura necessária na Azure.
-   **CI/CD Automatizado**: Workflow de GitHub Actions que compila, publica e implanta a imagem Docker a cada push na branch `main`.
-   **Serverless e Escalável**: Roda no Azure Container Apps, que escala automaticamente (inclusive para zero) e simplifica a gestão.

---

## 🚀 Como Usar a API de Exemplo

A API possui dois endpoints principais para teste. Após o deploy, você terá acesso a uma documentação interativa (Swagger UI) em `https://<SEU_APP_URL>/docs`.

**Endpoint de Health Check (GET)**: `https://<SEU_APP_URL>/`
**Endpoint de Saudação (POST)**: `https://<SEU_APP_URL>/api/hello`

### Exemplo de Requisição (usando `curl`)

```bash
# Teste de Health Check
curl https://<SEU_APP_URL>/

# Resposta: {"status":"ok","message":"Bem-vindo à API!"}

# Teste da saudação
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "Marie Curie"}' \
  https://<SEU_APP_URL>/api/hello

# Resposta: {"message":"Olá, Marie Curie! Sua requisição POST foi recebida."}
