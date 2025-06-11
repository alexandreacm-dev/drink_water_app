# 💧 Drink Water App (FastAPI + PostgreSQL)

Este é um projeto Full-Stack para ajudar pessoas a lembrarem de beber água, com meta diária calculada automaticamente a partir do peso.

## 🚀 Tecnologias

- **Backend:** FastAPI + SQLAlchemy
- **Banco de Dados:** PostgreSQL
- **Migrations:** Alembic

## 📦 Requisitos

- Python 3.3+
- PostgreSQL
- Virtualenv (opcional)
- Docker (opcional)

## 📐 Meta diária

> Fórmula: `peso_kg * 35ml`

Ex: 70 kg → 2.450ml por dia.

---

## 🔧 Setup Local

```bash
# Clone o projeto
git clone https://github.com/seuusuario/drink-water-app.git
cd drink-water-app

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt

# Configure o .env com suas credenciais do PostgreSQL
cp .env.example .env

# Execute as migrations
alembic upgrade head

# Inicie a API
uvicorn app.main:app --reload
```

Diagrama ERD (Entidade-Relacionamento)

```bash
┌────────────┐        ┌────────────────┐
│   users    │        │   water_logs   │
├────────────┤        ├────────────────┤
│ id (PK)    │◄───────│ user_id (FK)   │
│ name       │        │ id (PK)        │
│ weight_kg  │        │ date           │
└────────────┘        │ amount_ml      │
                      └────────────────┘

```

<br />

# Project Structure

```bash
drink_water_app/
├── backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       ├── user.py
│       └── water.py
├── alembic/ (migrações)
├── .env
├── requirements.txt
└── README.md

```
