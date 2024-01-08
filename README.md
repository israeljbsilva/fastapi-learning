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
