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


## Executando a aplicação (Docker)


Antes de instalar a aplicação no container, instalar também no ambiente local.
```
pip install -e .
```

Buildar o container
```
docker build -f Dockerfile.dev -t microblog:latest .
```

Executar o container
```
docker run --rm -it -v $(pwd):/home/app/api -p 8000:8000 microblog
```

Acesse: http://0.0.0.0:8000/docs