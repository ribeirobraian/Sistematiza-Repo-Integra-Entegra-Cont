# Python CI Sample

Pequeno projeto em Python para publicar no GitHub com validação automática a cada alteração no código.

## O que o projeto faz

Este exemplo implementa um módulo simples de calculadora com testes automatizados.

## Estrutura

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements-dev.txt
└── README.md
```

## Como rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements-dev.txt
python -m pytest
ruff check .
```

## Workflow do GitHub Actions

O pipeline executa automaticamente quando houver:

- `push` na branch `main`
- `pull_request` para `main`

Etapas do pipeline:

1. Checkout do código
2. Setup do Python
3. Instalação das dependências
4. Lint com Ruff
5. Testes com Pytest

## Como publicar no GitHub

1. Crie um novo repositório.
2. Copie os arquivos deste projeto para o repositório.
3. Faça `git add .`
4. Faça `git commit -m "feat: initial project"`
5. Faça `git push origin main`

Depois do push, o workflow aparecerá na aba **Actions** do GitHub.
