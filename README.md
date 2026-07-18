# FRIDAY — AI Life Operating System

An AI-first personal operating system that understands your goals, remembers your journey, and helps you make better decisions.

## Architecture

- **Frontend:** Next.js · React · TypeScript · Tailwind CSS · shadcn/ui
- **Backend:** FastAPI · Python · SQLAlchemy · PostgreSQL
- **AI:** OpenAI · pgvector · RAG

## Structure

```
friday/
├── frontend/     # Next.js application
├── backend/      # FastAPI application
└── docs/         # Project documentation
```

## Documentation

See the [`/docs`](./docs) folder for full project specifications:

- [VISION.md](./docs/VISION.md) — Why this exists
- [PRD.md](./docs/PRD.md) — What we're building
- [ARCHITECTURE.md](./docs/ARCHITECTURE.md) — How it's built
- [DESIGN.md](./docs/DESIGN.md) — How it looks
- [RULES.md](./docs/RULES.md) — Engineering standards
- [PHASES.md](./docs/PHASES.md) — Development roadmap
- [MEMORY.md](./docs/MEMORY.md) — Session context

## Getting Started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
