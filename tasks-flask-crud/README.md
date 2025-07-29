# 📝 Task Manager API

Uma API simples para gerenciamento de tarefas, construída com **Flask** e arquitetura **MVC**.

## 📋 Funcionalidades

- ✅ CRUD de tarefas (criar, ler, atualizar e excluir)  
- 🔄 Marcar tarefas como completas/incompletas  
- 🔍 Filtro de tarefas por status  
- 📖 Documentação de API intuitiva

## 🚀 Como Executar

### 🔧 Pré-requisitos

- Python 3.8+  
- Pipenv ou pip  
- Git

### 📥 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/CaioQuerino/tasks-flask-crud.git
cd tasks-flask-crud
```

2. Crie e ative o ambiente virtual:

**Linux/Mac**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
flask run
```

A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📚 Endpoints da API

### 🔹 Tarefas

| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
| POST   | `/tasks`          | Cria uma nova tarefa          |
| GET    | `/tasks`          | Lista todas as tarefas        |
| GET    | `/tasks/<id>`     | Busca uma tarefa pelo ID      |
| PUT    | `/tasks/<id>`     | Atualiza uma tarefa existente |
| DELETE | `/tasks/<id>`     | Deleta uma tarefa pelo ID     |

## 📦 Exemplo de Request/Response

### 🔸 Requisição: `POST /tasks`
```json
{
  "title": "Estudar Python",
  "description": "Completar exercícios de Flask"
}
```

### 🔹 Resposta: `201 Created`
```json
{
  "id": 1,
  "title": "Estudar Python",
  "description": "Completar exercícios de Flask",
  "completed": false
}
```

## 🏗️ Estrutura do Projeto

```
tasks-flask-crud/
├── app.py                # Ponto de entrada da aplicação
├── requirements.txt      # Lista de dependências
├── .gitignore
├── README.md             # Este arquivo
├── controllers/          # Lógica de negócios
│   └── task_controller.py
├── models/               # Modelos de dados
│   └── task.py
└── routes/               # Definição de rotas/endpoints
    └── task.py
```

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3  
- 🌐 Flask  
- 📡 RESTful API  
- 🧱 Arquitetura MVC

## 🤝 Como Contribuir

1. Faça um **fork** do projeto  
2. Crie sua branch:  
```bash
git checkout -b feature/nova-feature
```
3. Faça commit das suas alterações:  
```bash
git commit -m "Adiciona nova feature"
```
4. Envie para o GitHub:  
```bash
git push origin feature/nova-feature
```
5. Abra um **Pull Request**

