# 🚀 API RESTful de Gestão de Chamados

API desenvolvida em **Python** utilizando **FastAPI** para o gerenciamento, triagem e controle de chamados de atendimento ao cliente. Projeto estruturado com foco em boas práticas de arquitetura de software, validação rigorosa de dados e documentação automatizada.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** (Framework web moderno e de alta performance)
* **Pydantic** (Validação e tipagem de dados)
* **Uvicorn** (Servidor ASGI)
* **Git & GitHub** (Controle de versão)

---

## ⚙️ Funcionalidades da API

* **Health Check (`GET /`)**: Verifica o status operacional da aplicação.
* **Cadastro de Chamados (`POST /chamados`)**: Registra novas solicitações com validação de tamanho de texto, categoria e prioridade.
* **Listagem de Chamados (`GET /chamados`)**: Retorna todos os chamados registrados no sistema.
* **Consulta por ID (`GET /chamados/{id}`)**: Busca um chamado específico de forma otimizada.
* **Atualização de Status (`PATCH /chamados/{id}/status`)**: Permite alterar o andamento de um atendimento (Aberto, Em Andamento, Resolvido).

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/dlorodrigues/api-gestao-chamados.git](https://github.com/dlorodrigues/api-gestao-chamados.git)
   cd api-gestao-chamados

2. **Crie e ative o ambiente virtual:**

    No Windows (Git Bash):

    Bash
    python -m venv venv
    source venv/Scripts/activate

3. **Instale as dependências:**

    Bash
    pip install -r requirements.txt

4. **Inicie o servidor da API:**

    Bash
    uvicorn app.main:app --reload

5. **Acesse a documentação interativa:**

    Abra o navegador e acesse: http://127.0.0.1:8000/docs (Swagger UI).

👨‍💻 Desenvolvido por

Douglas Luiz | Projeto construído como parte do portfólio de Engenharia de Software e IA.