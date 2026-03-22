# Python CI Sample

Pequeno projeto em Python para exposição do trabalho da aula de Integração e Entrega Contínuas com GitHub Actions, realizando validação automática a cada alteração no código.

## O que o projeto faz

Este exemplo implementa um módulo simples de calculadora com testes automatizados, cobrindo operações básicas e tratamento de exceções.

## Estrutura

``` text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements-dev.txt
└── README.md
```

## Como rodar localmente

``` bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements-dev.txt
PYTHONPATH=. python -m pytest
ruff check .
```

## Workflow do GitHub Actions

O pipeline executa automaticamente quando houver:

-   push na branch main
-   pull_request para main

Etapas do pipeline:

1.  Checkout do código\
2.  Setup do Python\
3.  Instalação das dependências\
4.  Lint com Ruff\
5.  Testes com Pytest

## Como publicar no GitHub

1.  Crie um novo repositório\
2.  Copie os arquivos deste projeto para o repositório\
3.  Execute git add .\
4.  Execute git commit -m "feat: initial project"\
5.  Execute git push origin main

Após o push, o workflow estará disponível na aba Actions do GitHub.

## Reflexão Técnica

### Decisões técnicas mais relevantes na construção do pipeline

A construção do pipeline priorizou simplicidade e clareza, utilizando GitHub Actions como ferramenta de integração contínua devido à sua integração nativa com o repositório. A escolha por separar dependências de desenvolvimento em um arquivo dedicado permite maior controle do ambiente. A inclusão de lint com Ruff antes da execução dos testes garante que problemas de qualidade de código sejam identificados precocemente. Além disso, a configuração do PYTHONPATH assegura consistência entre o ambiente local e o ambiente de execução no CI.

### Impactos da ausência de testes automatizados

A ausência de testes automatizados compromete diretamente a confiabilidade do software. Sem testes, erros podem ser introduzidos silenciosamente durante alterações no código, aumentando o risco de falhas em produção. Além disso, dificulta a manutenção e evolução do sistema, uma vez que não há garantias de que funcionalidades existentes continuam operando corretamente após mudanças.

### Possibilidades reais de evolução para Entrega Contínua

Este projeto pode evoluir para um modelo de Entrega Contínua com a inclusão de etapas adicionais no pipeline, como geração de artefatos, versionamento automático e publicação em ambientes de homologação ou produção. Também é possível integrar ferramentas de análise estática mais avançadas, cobertura de testes e validações de segurança. A automatização de deploy após aprovação em pull requests é um caminho natural para essa evolução.

### Riscos técnicos mitigados pela Integração Contínua

A Integração Contínua reduz riscos relacionados à integração tardia de código, conflitos entre alterações e regressões funcionais. Ao validar automaticamente cada mudança, o pipeline garante que o código permaneça em um estado funcional ao longo do tempo. Isso melhora a qualidade geral do software, reduz o retrabalho e aumenta a confiança no processo de desenvolvimento.
