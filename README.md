# Projeto de Gerenciamento de Festas MyParty🎉

Este é um projeto web feito em Django para o gerenciamento de festas e eventos. Os usuários podem criar e gerenciar eventos, incluindo informações detalhadas como local, data de início, data de término, produtor, entre outros. O sistema exibe uma lista dos eventos cadastrados e permite a manipulação de dados por meio de uma API RESTful.

## Funcionalidades Principais

- **Criação de Festas/Eventos**: Usuários podem adicionar novas festas, especificando o nome do evento, local, data e outros detalhes importantes.
- **Listagem de Festas**: Os eventos cadastrados são listados com suas informações como local, nome do criador, data de início, data de fim e CEP.
- **Gerenciamento de Usuários**: Possibilidade de adicionar, editar e remover usuários (clientes) que cadastraram eventos.
- **Manipulação de Eventos**: CRUD (Create, Read, Update, Delete) completo para os eventos.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do backend.
- **Django Rest Framework**: Utilizado para construir a API RESTful.
- **SQLite**: Banco de dados padrão para armazenamento das informações.

## Instalação e Configuração

### Pré-requisitos

- Python 3.x
- Django 4.x
- Django Rest Framework

### Passo a Passo

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/gerenciamento-festas.git
    cd gerenciamento-festas
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

Agora você pode acessar a aplicação em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

### Models

#### `clients` (Tabela de Clientes)
- `clientId`: ID único para cada cliente.
- `clientName`: Nome do cliente.
- `clientPass`: Senha do cliente.
- `clientEmail`: E-mail do cliente.
- `clientNumber`: Número de contato do cliente.
- `clientCPF`: CPF do cliente.

#### `events` (Tabela de Eventos)
- `eventId`: ID único para cada evento.
- `eventName`: Nome do evento.
- `eventInicio`: Data de início do evento.
- `eventFim`: Data de término do evento.
- `eventLocal`: Local onde o evento será realizado.
- `eventCEP`: CEP do local do evento.
- `eventProdutor`: Nome do produtor responsável pelo evento.

### Serializers

Os serializers são usados para converter os modelos em JSON e vice-versa.

- `clientsSerializer`: Serializa os dados dos clientes.
- `eventsSerializer`: Serializa os dados dos eventos.

### Views

As views manipulam as requisições HTTP, permitindo que o usuário interaja com a API.

- `clientsApi`: View que permite listar, adicionar, editar e deletar clientes via requisições GET, POST, PUT e DELETE.

### Exemplos de Requisições

#### Listar todos os eventos:
```http
GET /events/
```

#### Adicionar um novo evento:
```http
POST /events/
{
  "eventName": "Festa de Ano Novo",
  "eventInicio": "2024-12-31 22:00",
  "eventFim": "2025-01-01 04:00",
  "eventLocal": "Rua das Festas, 123",
  "eventCEP": "12345678",
  "eventProdutor": "João Produtor"
}
```

#### Editar um evento existente:
```http
PUT /events/<id>/
{
  "eventName": "Festa Atualizada",
  "eventInicio": "2024-12-31 22:00",
  "eventFim": "2025-01-01 04:00",
  "eventLocal": "Rua das Festas, 123",
  "eventCEP": "12345678",
  "eventProdutor": "João Produtor"
}
```

#### Deletar um evento:
```http
DELETE /events/<id>/
```

## Melhorias Futuras

- Implementar autenticação para gerenciar permissões de acesso às funcionalidades da API.
- Adicionar uma interface de administração para facilitar o gerenciamento dos eventos e usuários.
- Incluir opções de filtragem e busca de eventos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
