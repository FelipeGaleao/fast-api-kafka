# fast-api-kafka

## 🐱‍👤 Nesse projeto

Esse repositório foi criado para a disciplina de Gerência de Configuração de Software (GCS) do curso de Engenharia de Software da [FACOM](https://facom.ufms.br/).

## 😎 Sobre o projeto

Esse projeto é um exemplo de um consumidor e produtor kafka que utiliza requisições HTTP para consumir e produzir mensagens na plataforma [Apache Kafka](https://kafka.apache.org/)
O projeto utiliza o framework [FastAPI](https://fastapi.tiangolo.com/) para criar uma API REST que recebe requisições HTTP e as transforma em mensagens kafka.
O projeto utiliza o [Docker](https://www.docker.com/) para criar os containers do kafka e do fast-api.

## ❓ Como executar o projeto

Execute o projeto utilizando o comando:

```bash
docker compose up -d
```

## ✨ Exemplo de uso

```curl
curl -X POST https://reqbin.com/echo/post/json
   -H 'Content-Type: application/json'
   -d '{"login":"my_login","password":"my_password"}'
```

## 📝 Documentações

- [Commit Semânticos](docs/commits_semanticos.md)
- [Modelo de Ramificação](docs/modelo_ramificacao.md)
- [Modelo de Severidade](docs/modelo_severidade.md)

## 🎯 TO-DO para desenvolvimento

- [ ] Discutir sobre o [Modelo de Severidade](docs/modelo_severidade.md) no Discord
- [ ] Discutir sobre o [Modelo de Ramificação](docs/modelo_ramificacao.md) no Discord
- [ ] Discutir sobre os [Commits Semânticos](docs/commits_semanticos.md) no Discord
- [ ] Criar seis issues no [repositório do projeto](https://github.com/FelipeGaleao/fast-api-kafka)
- [ ] Reagir e comentar em uma issue criada por outro membro
- [ ] Revisar uma issue com o status "Closed"
- [ ] Registrar como comentário na issue revisada, os ajustes que precisam ser feitos. Essa revisão deve ser feita por duas pessoas em uma issue de outra pessoa. Este item só será validado como nota caso as duas pessoas que revisaram façam os comentários de possíveis ajustes na issue.
- [ ] Criar um arquivo dentro do projeto
- [ ] Alterar um arquivo dentro do projeto
- [ ] Revisar e aprovar um pull request
- [ ] Criar um pull request
- [ ] Realizar uma alteração que resolva duas issues cadastradas por outro membro
- [ ] Resolver ao menos dois conflitos
