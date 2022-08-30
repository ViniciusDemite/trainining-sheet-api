# O projeto

O projeto tem como propósito criar uma ficha de treinamento digital, sendo usado uma API em Python e um front-end estruturado com algum framework javascript.

## Estrutura

- O diretório **app/** é onde se encontra a lógica do aplicativo
- O arquivo **run.py** é o arquivo utilizado para inicializar o aplicativo
- O arquivo **requirements.txt** é onde estão os pacotes e suas versões para instalação

## Como executar

### Docker

Tendo o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compos](https://docs.docker.com/compose/install/compose-desktop/) e instalados é possível utilizar o container para rodar a aplicação.
Execute o comando `docker compose up` para iniciar o ambiente.

### Virtual env

Caso decida rodar utilizando um ambiente virtual e já tenha o [Python3.8](https://www.python.org/downloads/) instalado, siga os seguintes comandos:

- `python3.8 - venv venv`
- `pip install -r requirements.txt`
- `python3 run.py`
