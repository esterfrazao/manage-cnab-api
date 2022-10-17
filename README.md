# Manage CNAB API

Este projeto, realizado em Django, propõe uma API que suporta o recebimento de arquivo CNAB versão tal e converte esse arquivo em transações separadas para dentro do seu banco de dados.
No momento atual o banco de dados utilizado é SQLite.

### Requisitos

Python 3.0+
Pip

### Configurando seu Database

1. Ao clonar este repositório você deve, primeiramente, adaptar sua aplicação:

   ```bash
       #criando seu ambiente virtual
       python -m venv venv --upgrade-deps

       #Ativando seu ambiente virtual (usando bash)
       source venv/bin/activate #no Linux
       source venv/Scripts/activate #no Windows

       #Instalando dependências
       pip install -r requirements.txt
   ```

2. Depois disso você deve definir suas váriaveis de ambiente no .env (utilize o modelo do .env.example)
3. Agora você já consegue rodar suas migrações:
   ```bash
       python manage.py migrate
   ```
4. E rodar sua API:
   ```bash
       python manage.py runserver
   ```

Agora é só abrir o link http://127.0.0.1:8000/ !

Obs: Caso o formulário se encontre assim:

```
{
    "file": null
}
```

Basta clicar em HTML Form no canto superior direito desse formulário
