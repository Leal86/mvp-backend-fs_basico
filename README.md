# API de Chamados

Este projeto faz parte do MVP da disciplina **Desenvolvimento Full Stack Básico**.

O objetivo da aplicação é implementar uma API REST para gerenciamento de:

* Departamentos
* Usuários
* Chamados

A API permite realizar operações de criação, listagem, busca, atualização e remoção (CRUD), seguindo boas práticas de desenvolvimento de APIs REST.

---

## 📌 Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flask-CORS
* Pydantic (validação de dados)
* Swagger (documentação da API)
* SQLite (banco de dados)

---

## 🗂️ Estrutura do projeto

A aplicação foi organizada seguindo separação de responsabilidades:

```plaintext
mvp-backend/
│
├── app.py
├── logger.py
├── README.md
├── requirements.txt
├── swagger.json
│
├── models/
│   ├── __init__.py
│   ├── departamento.py
│   ├── usuario.py
│   └── chamado.py
│
├── routes/
│   ├── usuario.py
│   ├── departamento.py
│   └── chamado.py
│
├── schemas/
│   ├── __init__.py
│   ├── base.py
│   ├── departamento.py
│   ├── usuario.py
│   └── chamado.py
│
├── schemas/request/
│   ├── usuario.py
│   ├── departamento.py
│   └── chamado.py
│
├── instance/
│   └── database.db
```

---

## 🚀 Como executar

Será necessário ter todas as bibliotecas listadas no `requirements.txt` instaladas.

Após clonar o repositório, acesse o diretório raiz pelo terminal.

> É fortemente recomendado o uso de ambientes virtuais.

### 🔧 Criar ambiente virtual (opcional)

```bash
python -m venv env
```

### ▶️ Ativar ambiente virtual

**Windows:**

```bash
env\Scripts\activate
```

**Linux/Mac:**

```bash
source env/bin/activate
```

---

### 📦 Instalar dependências

```bash
pip install -r requirements.txt
```

---

### ▶️ Executar a aplicação

```bash
python app.py
```

---

## 📚 Acessar a API

A API estará disponível em:

`http://localhost:5000`

---

## 📖 Documentação (Swagger)

A documentação interativa pode ser acessada em:

`http://localhost:5000/docs`

---

## 🔄 Fluxo da aplicação

Request → Pydantic → Model → Banco de Dados → Schema → Response

### Explicação:

* **Request**: dados enviados pelo cliente
* **Pydantic**: validação automática dos dados de entrada
* **Model (SQLAlchemy)**: interação com o banco
* **Schema**: formatação da resposta
* **Response**: retorno em JSON

---

## 📌 Endpoints principais

### 🔹 Departamentos

* GET /departamentos
* POST /departamentos
* GET /departamentos/<id>
* PUT /departamentos/<id>
* DELETE /departamentos/<id>

### 🔹 Usuários

* GET /usuarios
* POST /usuarios
* GET /usuarios/<id>
* PUT /usuarios/<id>
* DELETE /usuarios/<id>

### 🔹 Chamados

* GET /chamados
* POST /chamados
* GET /chamados/<id>
* PUT /chamados/<id>
* DELETE /chamados/<id>

---

## 📌 Exemplo de requisição

### Criar usuário

```json
{
  "nome": "Alexsander",
  "id_depto": 1,
  "matricula": "123",
  "funcao": "Analista"
}
```

---

## ⚠️ Validação de dados

A API utiliza **Pydantic** para validação automática.

```json
{
  "error": [
    {
      "loc": ["id_depto"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

## 📌 Boas práticas aplicadas

* Separação de responsabilidades (models, routes, schemas)
* Uso de Blueprint para modularização das rotas
* Validação de dados com Pydantic
* Tratamento de erros padronizado
* Organização em camadas (entrada → processamento → saída)

---

## 📌 Observações

* O banco de dados é criado automaticamente ao executar a aplicação
* Caso a pasta `instance/` seja removida, ela será recriada ao iniciar o projeto
* Foi utilizado o **Flask-CORS** para permitir a comunicação entre o frontend e o backend, evitando bloqueios de requisições pelo navegador
* A API foi desenvolvida com foco didático e organização de código

---

## 👨‍💻 Autor

Projeto desenvolvido por **Alexsander Leal da Silva**
