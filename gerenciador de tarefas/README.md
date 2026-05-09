# 📋 Gerenciador de Tarefas — CDC.3NA

Aplicação desktop para gerenciamento de tarefas, desenvolvida com Python, CustomTkinter e MySQL. Permite criar, listar, atualizar e deletar tarefas com prioridade e status.

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.10+**
- **CustomTkinter** — interface gráfica moderna (tema dark)
- **MySQL** — banco de dados relacional
- **mysql-connector-python** — conexão Python ↔ MySQL
- **pytest** — testes automatizados
- **GitHub Actions** — CI/CD

---

## 📁 Estrutura do Projeto

```
projeto_cdc/
├── app.py               # Aplicação principal (lógica + interface)
├── PROJETO_CDC.sql      # Script SQL para criar o banco de dados
├── test_app.py          # Testes automatizados com pytest
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline de CI (GitHub Actions)
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior
- MySQL Server em execução local
- pip

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install customtkinter mysql-connector-python
```

### 3. Configure o banco de dados

Acesse o MySQL e execute o script SQL:

```bash
mysql -u root -p < PROJETO_CDC.sql
```

> O script cria o banco `projeto_cdc`. A tabela `tbl_tarefas` é criada automaticamente ao iniciar a aplicação.

### 4. Configure a conexão

No arquivo `app.py`, ajuste as credenciais na função `conectar()` se necessário:

```python
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin', 
        database='projeto_cdc',
    )
```

### 5. Execute a aplicação

```bash
python app.py
```

---

## 🗃️ Banco de Dados

**Banco:** `projeto_cdc`

**Tabela:** `tbl_tarefas`

| Coluna         | Tipo          | Descrição                        |
|----------------|---------------|----------------------------------|
| `id_tarefa`    | INT (PK, AI)  | Identificador único              |
| `nome_tarefa`  | VARCHAR(100)  | Nome da tarefa                   |
| `descricao`    | TEXT          | Descrição detalhada              |
| `prioridade`   | VARCHAR(10)   | `Baixa`, `Média` ou `Alta`       |
| `status`       | VARCHAR(15)   | `Pendente` ou `Concluída`        |
| `data_criacao` | DATE          | Data de criação (automática)     |

---

## 🧪 Testes

Os testes são executados com **pytest** e cobrem:

- Validação de prioridades válidas e inválidas
- Conexão com o banco de dados
- Criação de tabelas no MySQL

### Executar os testes

```bash
pip install pytest
python -m pytest
```

### Testes disponíveis (`test_app.py`)

| Teste                  | Descrição                                      |
|------------------------|------------------------------------------------|
| `test_prioridade_valida`   | Verifica se `Alta`, `Média` e `Baixa` são aceitos |
| `test_prioridade_invalida` | Verifica rejeição de valores inválidos         |


> ⚠️ Os testes de banco exigem que o MySQL esteja rodando com as credenciais configuradas em `app.py`.

---

## 🔄 CI/CD — GitHub Actions

O pipeline definido em `.github/workflows/ci.yml` é acionado automaticamente em cada `push` e `pull_request`.

**Etapas do pipeline:**

1. Checkout do código
2. Instalação do Python 3.10
3. Instalação do pytest
4. Execução dos testes com `python -m pytest`

---

## 📌 Funcionalidades

- ✅ Criar tarefa com nome, descrição, prioridade e status
- 📋 Listar todas as tarefas cadastradas
- ✏️ Atualizar tarefa existente pelo ID
- 🗑️ Deletar tarefa pelo ID
- 🧹 Limpar campos do formulário

---

## 👨‍💻 Autor

Tiago Silva
