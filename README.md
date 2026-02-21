# C Turismo - Fullstack (React + Python FastAPI + SQLite)

Este projeto agora possui uma estrutura completa com Backend para persistência real de dados em um banco de dados SQLite.

## Estrutura do Projeto

- `/` : Frontend em React (Vite)
- `/backend_cturismo` : Backend em Python (FastAPI + SQLAlchemy + SQLite)

## Como executar

### 1. Iniciar o Backend (Python)

Você precisará do Python instalado. No terminal, entre na pasta do backend:

```bash
cd backend_cturismo
pip install -r requirements.txt
uvicorn main:app --reload
```
O servidor backend rodará em `http://localhost:8000`.

### 2. Iniciar o Frontend (React)

Em outro terminal, na pasta raiz do projeto:

```bash
npm install
npm run dev
```
O site rodará em `http://localhost:3000`.

## Funcionalidades Integradas
- **Persistência Real**: Os clientes são salvos no arquivo SQLite dentro da pasta backend.
- **Admin**: O painel administrativo agora busca e salva dados diretamente do servidor.
- **Logo Corrigido**: O logo "C Turismo" está atualizado em todo o sistema.
- **Exportação**: Mantidas as funcionalidades de exportação para PDF, Word e Excel.
