# 🛒 Compraki

**Compraki** é uma plataforma web inspirada no modelo de aplicativos como iFood, voltada para conectar clientes e mercados locais da cidade de **Boa Viagem - CE**, promovendo praticidade, agilidade e incentivo à economia local.

> ⚠️ Este é um protótipo acadêmico em desenvolvimento. Algumas funcionalidades estão em fase inicial e o design será aprimorado nas próximas versões.

---

## 📱 Sobre o projeto

O **Compraki** oferece uma solução eficiente para que usuários possam realizar compras em mercados locais através de uma interface simples e intuitiva. A plataforma permite o cadastro de clientes e mercados, listagem de produtos, adição ao carrinho e pagamento via Pix.

---

## 🚀 Funcionalidades principais

### 👤 Cliente
- Cadastro e login de usuário
- Visualização de mercados disponíveis
- Adição de produtos ao carrinho
- Finalização de pedidos
- Histórico de compras

### 🏪 Mercado
- Cadastro e login com CNPJ
- Gerenciamento de produtos (CRUD)
- Visualização dos pedidos realizados pelos clientes
- Gestão de entregas (em desenvolvimento)

### 💼 Admin (futuramente)
- Aprovação de mercados
- Monitoramento de transações e desempenho da plataforma

---

## ⚙️ Tecnologias Utilizadas

### 💻 Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 🌐 Frontend
- [Angular](https://angular.io/)
- [TypeScript](https://www.typescriptlang.org/)
- Design responsivo mobile-first
- Navegação entre componentes com Angular Router

---

## 🌍 Benefícios do Compraki

- ✅ Incentivo ao comércio local e regional
- 🛒 Facilidade de acesso a produtos de mercados da região
- ⚡ Alternativa mais simples e leve em comparação com apps de grande escala
- 💰 Integração com pagamento via Pix
- 👨‍💻 Interface amigável para usuários com diferentes níveis de familiaridade com tecnologia

## 🧱 Estrutura do Projeto

compraki/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── main.py
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   └── pages/
│   └── Dockerfile
├── docker-compose.yml
└── README.md

## 📦 Como executar o projeto

### ✅ Pré-requisitos

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/) instalado

### ▶️ Passos para rodar o projeto

# Clonar o repositório
git clone https://github.com/gabrielymorais/compraki.git
cd compraki

# Subir os serviços com Docker
docker-compose up --build

## 📌 Próximas funcionalidades

- 📦 Rastreamento de pedidos  
- 💳 Integração com gateways de pagamento  
- 🔔 Notificações em tempo real  
- 📱 Versão mobile (PWA)  


## 👨‍🎓 Projeto acadêmico

Este projeto foi desenvolvido como parte de uma atividade prática para a disciplina de **desenvolvimento web/fullstack**.  
O objetivo é aplicar conhecimentos de **frontend**, **backend** e **orquestração com Docker**, simulando um ambiente real de produção.

