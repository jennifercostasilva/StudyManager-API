# StudyManager API

API RESTful desenvolvida para gerenciamento de usuários, cursos e matrículas.

O projeto foi desenvolvido como atividade acadêmica utilizando FastAPI e SQLAlchemy, aplicando conceitos de Arquitetura Limpa, Clean Code, ORM, validação de dados e tratamento de erros.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

## Funcionalidades

A API permite:

- Cadastrar, listar, buscar, atualizar e excluir usuários
- Cadastrar, listar, buscar, atualizar e excluir cursos
- Realizar matrículas de usuários em cursos
- Consultar os cursos em que um usuário está matriculado
- Validar o formato dos dados recebidos
- Impedir cadastro de email duplicado
- Impedir matrícula duplicada
- Verificar a existência do usuário e do curso antes de realizar uma matrícula

## Estrutura do projeto

```text
app/
├── controllers/
├── exceptions/
├── infrastructure/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py
```

A aplicação foi organizada em camadas para separar as responsabilidades do sistema. Os controllers recebem as requisições da API, os services concentram as regras de negócio, os repositories realizam o acesso ao banco de dados e os models representam as tabelas utilizadas pelo ORM. Os schemas são responsáveis pela validação dos dados de entrada e saída, a pasta infrastructure contém a configuração do banco de dados e exceptions concentra o tratamento dos erros da aplicação.

## Modelagem

O sistema possui três entidades principais:

### User

- id
- name
- email
- created_at

### Course

- id
- title
- description
- workload

### Enrollment

- id
- user_id
- course_id
- enrolled_at

Um usuário pode possuir várias matrículas e um curso pode possuir várias matrículas. Cada matrícula pertence a um usuário e a um curso.

## Endpoints

### Usuários

- POST /users
- GET /users
- GET /users/{id}
- PUT /users/{id}
- DELETE /users/{id}
- GET /users/{id}/courses

### Cursos

- POST /courses
- GET /courses
- GET /courses/{id}
- PUT /courses/{id}
- DELETE /courses/{id}

### Matrículas

- POST /enrollments

## Códigos HTTP

A API utiliza códigos HTTP de acordo com o resultado das requisições:

- 200 - Requisição realizada com sucesso
- 201 - Registro criado com sucesso
- 204 - Registro excluído com sucesso
- 404 - Registro não encontrado
- 409 - Conflito, como email ou matrícula duplicada
- 422 - Erro de validação dos dados

## Tratamento de erros

Os erros de negócio possuem uma resposta padronizada.

Exemplo:

```json
{
  "success": false,
  "message": "User not found",
  "data": null
}
```

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

A documentação da API pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Banco de dados

O projeto utiliza SQLite como banco de dados e SQLAlchemy como ORM. O arquivo do banco é criado localmente durante a execução da aplicação.

## Repositório no GitHub
https://github.com/jennifercostasilva/StudyManager-API

## Autor

Jennifer