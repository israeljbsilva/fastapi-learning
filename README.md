# fastapi-learning
Projeto para aplicação de aprendizado sobre framework fastapi

Utilizando [projeto de microblog (estilo twitter)](https://github.com/rochacbruno/fastapi-workshop) como exemplo.


# Configurando ambiente
```
python -m venv .venv
source .venv/bin/activate
```

## Dependências
Instalar dependências locais:
```
pip install --upgrade pip
pip install -r requirements-dev.txt
```

Instalar dependências do projeto:
```
pip-compile requirements.in
pip install -r requirements.txt
```


## Ambiente de Desenvolvimento Docker

#### Caso tenha o Postgres instalado local, deve parar o serviço, pois será utilizado o MySQL do Docker.
* comando para parar o serviço:
    * ```sudo service postgresql stop```
* comando para verificar o status do serviço
    * ```sudo service postgresql status```

#### Para fazer o build na primeira vez
* ```docker-compose build```

#### Para subir o ambiente, execute o seguinte comando. E se caso queira parar o ambiente, utilize ctrl + c.
* ```docker-compose up```

#### Para derrubar o ambiente, execute o seguinte comando.
* ```docker-compose down -v```


## Migrações

Estamos utilizando o alembic para gerenciar as migrações.

Para criar as migrações ou executá-las, precisamos estar dentro do container, para isso, execute:
* ```docker compose exec api /bin/bash```

Para criar migrações:
* ```alembic revision --autogenerate -m "initial"```

Para executar migrações:
* ```alembic upgrade head```
