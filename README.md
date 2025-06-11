# 💧 Drink Water Project

Este é um projeto Full-Stack para ajudar pessoas a lembrarem de beber água, com meta diária calculada automaticamente a partir do peso.

## 🚀 Tecnologias

- **Backend:** FastAPI + SQLAlchemy
- **Banco de Dados:** PostgreSQL
- **Frontend Web:** React (em desenvolvimento)
- **Mobile:** React Native (simplificado)
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

# Estrutura Básica do Projeto

```bash
drink_water_app/
├── .github/
│   ├── workflows/          # GitHub Actions workflows
│   └── dependabot.yml      # Configuração de atualizações de dependências
├── apps/
│   ├── frontend/           # Aplicação React
│   │   ├── public/
│   │   ├── src/
│   │   ├── package.json
│   │   └── ...
│   ├── mobile/             # Aplicação React Native
│   │   ├── android/
│   │   ├── ios/
│   │   ├── src/
│   │   ├── package.json
│   │   └── ...
│   └── backend/            # Aplicação FastAPI
│       ├── app/
│       ├── tests/
│       ├── requirements.txt
│       └── ...
├── packages/               # Código compartilhado
│   ├── shared/             # Código compartilhado entre frontend/mobile
│   │   ├── src/
│   │   └── package.json
│   └── api-client/         # Client API compartilhado
│       ├── src/
│       └── package.json
├── scripts/                # Scripts utilitários
├── .gitignore
├── package.json            # Root package.json (gerenciamento global)
├── README.md
└── turbo.json              # Configuração do Turborepo (opcional)
```
