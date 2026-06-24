# Medria AI

This repository contains an initial MVP scaffold for Medria AI built as a monorepo.

## Structure
- `apps/web` — Next.js frontend shell
- `services/api` — FastAPI backend shell
- `docs` — product and architecture notes

## Run locally
```bash
cd medria
pnpm install
pnpm --filter @medria/web dev
```

```bash
cd medria/services/api
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload --port 8000
```
