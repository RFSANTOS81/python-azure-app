# python-azure-app

## Configuração local

1. Copie `.env.example` para `.env`:
   ```powershell
   copy .env.example .env
   ```
2. Atualize o `DATABASE_URL` no arquivo `.env` com as credenciais do Azure PostgreSQL.
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Rode o servidor:
   ```powershell
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

## Conexão com o Azure PostgreSQL

O projeto lê `DATABASE_URL` do ambiente ou do arquivo `.env`.
Use o formato:

```text
postgresql://<usuario>@<servidor>:<senha>@<host>:5432/<banco>?sslmode=require
```

No Azure, é comum precisar codificar caracteres especiais no usuário e na senha:
- `@` → `%40`
- `:` → `%3A`

Exemplo seguro:

```text
DATABASE_URL=postgresql://<USER_ENCODED>:<PASSWORD_ENCODED>@<HOST>:5432/<DBNAME>?sslmode=require
```

## Publicar no GitHub

Após validar localmente, use:

```powershell
git add .
git commit -m "Fix PUT routes and add Azure DB env support"
git push origin main
```
