# Test Global Tech

Este é um projeto full-stack desenvolvido para gerenciar informações de pessoas, incluindo funcionalidades de inclusão, alteração, exclusão e pesquisa. O backend utiliza Django com Django REST Framework (DRF) e PostgreSQL, enquanto o frontend é construído com Vue 3 e Vite. O projeto é conteinerizado com Docker para facilitar a execução e o deploy.

## Funcionalidades
- **Incluir**: Adiciona uma nova pessoa com campos como nome, data de nascimento, CPF, sexo, altura e peso.
- **Alterar**: Permite editar os dados de uma pessoa existente.
- **Excluir**: Remove uma pessoa da lista com confirmação.
- **Pesquisar**: Busca pessoas no backend por nome ou CPF em tempo real.
- **Ponto Extra**: Calcula o peso ideal de uma pessoa selecionada com base na fórmula:
  - Homens: `(72.7 * altura) - 58`
  - Mulheres: `(62.1 * altura) - 44.7`
  - Resultado exibido em um popup.

## Tecnologias Utilizadas
- **Backend**: Python 3.11, Django 5.1.7, Django REST Framework, PostgreSQL 13
- **Frontend**: Vue 3, Vite, Axios, ESLint, Prettier
- **Containerização**: Docker, Docker Compose
- **Outras Ferramentas**: Swagger (drf-yasg) para documentação da API

## Estrutura do Projeto
```
testGlobalTech/
├── backend/
│   ├── apps/
│   │   └── people/
│   │       ├── migrations/
│   │       ├── init.py
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── services.py
│   │       └── views.py
│   ├── backend/
│   │   ├── init.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── views/
│   │   │   ├── AboutView.vue
│   │   │   └── HomeView.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── Dockerfile
│   ├── eslint.config.js
│   ├── package.json
│   ├── vite.config.js
│   └── .prettierrc
├── docker-compose.yml
└── README.md
```

- **backend/**: Contém a aplicação Django com o app `people` (modelos, serializers, views e services).
- **frontend/**: Contém a aplicação Vue 3 com Vite, incluindo componentes e serviços de API.
- **docker-compose.yml**: Define os serviços (backend, frontend e banco de dados).

## Requisitos
- Docker e Docker Compose instalados.
- Node.js 18 (para desenvolvimento local do frontend, se necessário).
- Python 3.11 (para desenvolvimento local do backend, se necessário).

## Como Executar

### Usando Docker
1. Clone o repositório:
```bash
   git clone https://github.com/joseandrepereira/testGlobaTech.git
   cd testGlobalTech
```
2. Suba os containers:
```bash
   docker compose up --build
```
3. Acesse as interfaces:
 -Frontend: http://localhost:5174
 - Backend API: http://localhost:8000/api/people/
 - Swagger: http://localhost:8000/swagger/

4. Para parar os containers:
```bash
   docker-compose down
```

## Endpoints da API

- GET /api/people/: Lista todas as pessoas ou filtra por ?search=valor.
- POST /api/people/: Cria uma nova pessoa.
- PUT /api/people/{id}/: Atualiza uma pessoa existente.
- DELETE /api/people/{id}/: Exclui uma pessoa.
- GET /api/people/{id}/calculate_ideal_weight/: Calcula o peso ideal de uma pessoa.

## Ponto Extra
O botão "Peso Ideal" na lista de pessoas chama o endpoint /api/people/{id}/calculate_ideal_weight/, calcula o peso ideal no backend e exibe o resultado em um popup no frontend.

## Notas
- O campo height no backend é tratado como float para cálculos precisos.
- O frontend usa máscaras para CPF (000.000.000-00) e data (DD/MM/AAAA).
- A pesquisa no frontend dispara requisições ao backend em tempo real.

## Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias!

## Licença
Este projeto está sob a [Licença MIT](LICENSE).
