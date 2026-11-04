# 📘 Atividade: Persistência com FastAPI e PostgreSQL

## 🎯 Objetivo

Amplie uma API REST com FastAPI para armazenar dados de livros em um banco PostgreSQL usando SQLAlchemy. Pratique mapeamento objeto-relacional, sessões de banco de dados e operações CRUD com dados que continuam disponíveis após reiniciar o servidor.

## 📝 Tarefas

### 🛠️ Conectar a API ao PostgreSQL

#### Descrição
Prepare um banco PostgreSQL chamado `book_catalog` e configure a variável de ambiente `DATABASE_URL` para apontar para ele. Use o starter code para definir um modelo ORM de livro e criar a tabela necessária.

Instale as dependências:

```bash
python -m pip install fastapi uvicorn sqlalchemy "psycopg[binary]"
```

Configure a conexão antes de iniciar a aplicação. Exemplo para Linux ou macOS:

```bash
export DATABASE_URL="postgresql+psycopg://usuario:senha@localhost:5432/book_catalog"
```

No PowerShell:

```powershell
$env:DATABASE_URL = "postgresql+psycopg://usuario:senha@localhost:5432/book_catalog"
```

#### Requisitos
O programa concluído deve:

- Usar SQLAlchemy e o driver Psycopg para conectar ao PostgreSQL
- Ler a URL de conexão de `DATABASE_URL`, sem incluir credenciais diretamente no código
- Definir um modelo `Book` com `id`, `title` e `author`
- Criar a tabela do modelo no banco de dados
- Iniciar com `uvicorn starter-code:app --reload` quando o banco estiver disponível

### 🛠️ Implementar operações CRUD com sessões

#### Descrição
Substitua o armazenamento em memória por consultas ao PostgreSQL. Crie uma dependência que forneça uma sessão por requisição e use-a nas rotas do catálogo.

#### Requisitos
O programa concluído deve:

- Fechar a sessão do banco ao final de cada requisição
- Implementar `GET /books` para listar os livros
- Implementar `POST /books` para salvar um livro e retornar o registro criado
- Implementar `GET /books/{book_id}` para consultar um livro pelo identificador
- Implementar `PUT /books/{book_id}` e `DELETE /books/{book_id}`
- Retornar HTTP `404 Not Found` quando uma atualização, consulta ou exclusão buscar um livro inexistente
- Confirmar as gravações com a transação do banco de dados

### 🛠️ Verificar validação e persistência

#### Descrição
Teste o ciclo completo de um livro pela documentação interativa do FastAPI e confirme que os registros continuam no banco mesmo depois de encerrar e iniciar o servidor novamente.

#### Requisitos
O programa concluído deve:

- Validar que `title` e `author` não sejam valores vazios
- Retornar os dados persistidos depois de reiniciar o servidor
- Demonstrar criação, listagem, consulta, atualização e exclusão em `/docs`
- Confirmar que erros para identificadores inexistentes retornam status `404`
