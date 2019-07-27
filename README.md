# Bem vindo ao desafio DevOps da Engineering do Brasil.
Esse é o projeto desenvolvido para Engineering do Brasil. Esse desafio utilizei os seguintes serviços:
1. - Kong API
2. - Konga Dashboard (Interface gráfica do kong)
3. - Banco PostgreSQL para o kong.
4. - Serviço book_manager
5. - Banco MySQL para o book_manager

### **Pré-requisitos e instalação**

Necessário possuir o python3 e pip3 instalados. [python3 e pip](https://python.org.br/instalacao-linux/)

Também é necessário possuir docker e docker-compose instalados. [docker](https://docs.docker.com/v17.12/install/) [docker-compose](https://docs.docker.com/compose/install/)

## HOW TO

Será necessário clonar o repositorio para a sua máquina 
```
https://github.com/adriell/desafio-devops-senior.git

```
Acesse o diretorio do projeto e execute o comando abaixo para subir toda a infra:

```
docker-compose up -d

```
Após o ambiente disponivel, executar os comandos abaixo para criar as rotas no kong api

```bash
# Cria o serviço no kong api
python add_service.py

# Adiciona as rotas no kong api
python add_route.py

#Execute o comando abaixo para validar o funcionamento da api.
curl -i -X GET --url http://localhost:8000/desafio 

#Comando abaixo habilita o plugin auth-key
python add_consumer.py

```
Caso o banco de dados não tiver sido criado, o mesmo deverá ser criado com o comando abaixo:

```bash
docker exec -it <id container> mysql -u root -p #Use a senha que está setado no docker-compose.yml

#Execute os comandos abaixo
CREATE DADABASE IF NOT EXISTS book;

CREATE TABLE book (title VARCHAR(80) PRIMARY KEY NOT NULL);
```

