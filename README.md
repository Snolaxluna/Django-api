# Django REST API - Sistema Escolar

Este repositório contém uma API para um sistema escolar, desenvolvida com Django e Django REST Framework. A API permite a gestão de estudantes, cursos e matrículas, facilitando a administração dos dados escolares.

## Tecnologias Utilizadas

- **Django** 5.1.2
- **Django REST Framework** 3.15.2
- **asgiref** 3.8.1
- **django-filter** 24.3
- **drf-yasg** 1.21.8 (para documentação da API)
- **Faker** 30.8.2
- **inflection** 0.5.1
- **Markdown** 3.7
- **packaging** 24.1
- **python-dateutil** 2.9.0.post0
- **pytz** 2024.2
- **PyYAML** 6.0.2
- **setuptools** 75.3.0
- **six** 1.16.0
- **sqlparse** 0.5.1
- **typing_extensions** 4.12.2
- **tzdata** 2024.2
- **uritemplate** 4.1.1
- **validate-docbr** 1.10.0

## Funcionalidades

Este projeto inclui:

- **API RESTful**: Implementada com Django REST Framework.
- **Documentação interativa**: Gerada automaticamente com `drf-yasg`.
- **Filtros avançados**: Utilizando o `django-filter`.
- **Geração de dados fictícios**: Com a biblioteca `Faker`.
- **Validação de documentos brasileiros**: Usando `validate-docbr`.
- **Suporte a Markdown**: Para renderizar conteúdo Markdown em respostas.

## Rotas Disponíveis

Este sistema escolar possui as seguintes rotas principais:

1. **Estudantes** (`/estudantes/`): Gestão de informações dos estudantes, como nome, idade e documentos.
2. **Cursos** (`/cursos/`): Registro de cursos oferecidos, com detalhes sobre cada curso.
3. **Matrículas** (`/matriculas/`): Controle de matrículas de estudantes em cursos específicos.

## Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Snolaxluna/Django-api.git
   cd Django-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```
