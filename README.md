[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
![size-shield]
![commit-shield]

<br/>

<p align="center">
  <h1 align="center">🛒 ZapStore | Assistant</h1>
</p>

## Tabela de Conteúdos

* [Sobre o ZapStore](#sobre-o-zapstore)
* [Funcionalidades](#funcionalidades)
* [Arquitetura](#arquitetura)
* [Tecnologias](#tecnologias)
* [Contato](#contato)

## Sobre o ZapStore

**ZapStore** é uma loja de tecnologia especializada na venda de hardware e periféricos. Ademais, fornece o atendimento
automatizado e inteligente aos clientes sobre os produtos vendidos, utilizando um **chatbot via Whatsapp** conectado a base
de dados da ZapStore.

## Funcionalidades

- Listar produtos/categorias/marcas com filtros (via API);
- Registrar saídas/entradas de produtos (via API);

| Método | Endpoint               | Descrição                      |
| ------ | ---------------------- | ------------------------------ |
| GET    | `/api/v1/product`      | Lista produtos (com filtros)   |
| POST   | `/api/v1/product`      | Cria um novo produto           |
| GET    | `/api/v1/product/<id>` | Recupera um produto específico |
| PUT    | `/api/v1/product/<id>` | Atualiza um produto            |
| DELETE | `/api/v1/product/<id>` | Remove um produto              |
| GET    | `/api/v1/all_data`     | Retorna todas as entidades     |


## Arquitetura

## Tecnologias

* Framework Backend: [FastAPI](https://fastapi.tiangolo.com/), [Django](https://www.djangoproject.com/)
* Banco de dados: [PostgreSQL](https://www.postgresql.org/), [MongoDB](https://www.mongodb.com/)
* Inteligência Artificial: [OpenAI](https://openai.com/api/)
* API do Whatsapp: [Evolution API](https://doc.evolution-api.com/v1/pt/get-started/introduction)

## Contato

Vinícius Perrone - [LinkedIn](https://www.linkedin.com/in/vinicius-perrone/) - perronevinicius2018@gmail.com

[contributors-shield]: https://img.shields.io/github/contributors/viniciusperrone/zapstore-assistant?style=flat-square
[contributors-url]: https://github.com/viniciusperrone/zapstore-assistant/graphs/contributors

[issues-shield]: https://img.shields.io/github/issues/viniciusperrone/zapstore-assistant?style=flat-square
[issues-url]: https://github.com/viniciusperrone/zapstore-assistant/issues

[size-shield]: https://img.shields.io/github/repo-size/viniciusperrone/zapstore-assistant?style=flat-square

[commit-shield]: https://img.shields.io/github/last-commit/viniciusperrone/zapstore-assistant?style=flat-square
