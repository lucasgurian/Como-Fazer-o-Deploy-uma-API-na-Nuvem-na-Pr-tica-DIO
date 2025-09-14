# Estágio 1: Builder - Instala as dependências de forma otimizada
FROM python:3.9-slim as builder

WORKDIR /app

# Instala o 'pip' mais recente
RUN pip install --upgrade pip

# Copia o arquivo de dependências
COPY requirements.txt .

# Cria 'wheels' para as dependências. Isso acelera a instalação no próximo estágio.
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# Estágio 2: Final - Monta a imagem final e leve para produção
FROM python:3.9-slim

WORKDIR /app

# Copia as dependências pré-compiladas do estágio 'builder'
COPY --from=builder /wheels /wheels

# Instala as dependências a partir dos 'wheels' locais
RUN pip install --no-cache /wheels/*

# Copia o código da aplicação
COPY ./app /app

# Expõe a porta que a aplicação vai rodar dentro do contêiner
EXPOSE 8000

# Comando para iniciar a aplicação quando o contêiner for executado
# O host 0.0.0.0 permite que a aplicação seja acessível de fora do contêiner
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
