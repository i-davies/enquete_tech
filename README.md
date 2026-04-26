# Enquete Tech

Aplicação de enquete desenvolvida com arquitetura separada: **Flask** no backend e **Flet** no frontend.

## Tecnologias

| Camada    | Tecnologia | Função                                  |
|-----------|------------|-----------------------------------------|
| Backend   | Flask      | API REST que expõe os dados na porta 5000 |
| Frontend  | Flet       | Interface visual que consome a API      |
| HTTP Client | httpx    | Comunicação assíncrona entre as camadas |

## Pré-requisitos

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) instalado

## Instalação

Clone o repositório e instale as dependências
```bash
uv sync
```

## Executando a Aplicação

Como a arquitetura é separada ("Cozinha" e "Cardápio" independentes), é necessário abrir **dois terminais** na mesma pasta do projeto.

### Terminal 1 — Backend (a "Cozinha")

```bash
uv run backend.py
```

> Este terminal registrará as requisições recebidas em texto. Pode ser minimizado após a inicialização.

### Terminal 2 — Frontend (o "Cardápio")

```bash
uv run frontend.py
```

> O Flet abrirá a interface estritamente no **Navegador Web**.