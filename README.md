# Cadastro de Clientes (Django + Tailwind CDN)

Sistema profissional de **cadastro de clientes** feito com **Django** e interface com **TailwindCSS via CDN** (sem build, sem instalação de frontend).
Inclui base de UI, mensagens, listagem de clientes e arquitetura preparada para CRUD completo com validações e soft delete (arquivar/reativar).

---

## ✅ Funcionalidades (atual)

- Listagem de clientes ativos (`/clientes/`)
- Modelo `Cliente` com:
  - campos principais (nome, documento, contato, endereço)
  - índices para busca
  - **soft delete** via `archived_at` (arquivar/reativar)
- Django Admin configurado com filtro e busca

---

## 🧱 Stack

- Python 3.10+ (recomendado)
- Django 5+
- SQLite (padrão do Django para dev)
- TailwindCSS via CDN

---

## 📦 Requisitos

- Python instalado (3.10 ou superior recomendado)
- Git instalado
- (Opcional) VS Code

Para verificar:

```bash
python --version
git --version
