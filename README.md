# Transformar texto em áudio (Django + gTTS)

Este projeto é uma aplicação web simples para conversão de texto em fala (Text-to-Speech - TTS)
utlizando Django e a biblioteca gTTS do Google.

## Funcionalidades

- Conversão de texto para áudio com opção de ouvir e baixar 
- Suporte a múltiplos idiomas (pt-BR, en-US, es-ES)
- Interface web simples para entrada de texto

## Instalação

1. Clone o repositório:
    ```bash
    git clone git@github.com:danniloraphael/tts_django.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Faça as migrações:
    ```bash
    python manage.py migrate
    ```
4. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

## Uso

Acesse `http://localhost:8000` no navegador, insira o texto desejado, ouça ou faça o download do áudio gerado.
