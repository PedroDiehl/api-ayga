<img src="./images/Ayga Logo.png" alt="isolated" width="500"/>

## 📖 Sumário

- [📖 Sumário](#-sumário)
- [📍 Introdução](#-introdução)
- [👨‍💻 Candidato](#-candidato)
- [💻 Tecnologias empregadas](#-tecnologias-empregadas)
- [🕐 Linha do Tempo](#-linha-do-tempo)
- [📐 Desenvolvidos](#-desenvolvidos)
  - [▶️ Legenda](#️-legenda)
- [📥 Endpoints HTTP 📤](#-endpoints-http-)

## 📍 Introdução
Desafio de desenvolver uma API REST com prazo de uma semana a partir das documentações e instruções fornecidas pela AYGA.

## 👨‍💻 Candidato

Nome: Pedro Henrique Diehl

Idade: 21 anos

Faculdade: Universidade Federal de Pelotas

Curso: Engenharia de Controle e Automação

## 💻 Tecnologias empregadas

Apresentando as teconlogias utilizadas para desenvolver esse projeto

* Python
  * flask
* PostgresSQL

## 🕐 Linha do Tempo

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Estudar o brieffing do projeto
- [x] Configurar o ambiente de desenvolvimento (VSCode, Git, Github, Heroku)
- [x] Criar debuggers intuitivos para API, Banco de Dados e .json
- [x] Interpretar formato .json enviado através do POST e documentação fornecida
- [x] Configurar Base de dados no Postgres integrado com Heroku
- [x] Integrar todas tecnlogias desenvolvidas
- [x] Desenvolver filtros para requisições tipo GET
- [ ] Ajustes finais
- [ ] Deploy final no Heroku

## 📐 Desenvolvidos
Diferentes filtros para o método GET

- Filtro por data - ✔️
- Filtro por valor - ✔️
- Filtro por menor que valor  - ❌
- Filtro por maior que valor  - ❌
- Filtro por intervalo de datas - ✔️
- Filtro por intervalo de valores - ❌
- Filtro por tipo do sinal do dispositivo - ✔️
- Filtro por tipo do sinal e intervalo de datas - ✔️

### ▶️ Legenda
✔️ - Disponível
❌ - Indisponível

## 📥 Endpoints HTTP 📤

* https://ayga-api.herokuapp.com/get_saved_data 
  *  Retorna todos os dados armazenados até o momento

* https://ayga-api.herokuapp.com/get_saved_data_by_date/data_busca
  * Retorna os dados armazenados até o momento para data enviada como argumento

* https://ayga-api.herokuapp.com/get_saved_data_by_type/tipo
  * Retorna os dados armazenados até o momento para o tipo enviado como argumento

* https://ayga-api.herokuapp.com/get_saved_data_by_value/valor
  * Retorna os dados armazenados até o momento para o valor enviado como argumento

* https://ayga-api.herokuapp.com/get_saved_data_by_date_interval/data_inicial/data_final
  * Retorna os dados armazenados até o momento para o intervalo de datas enviado como argumento

* https://ayga-api.herokuapp.com/get_saved_data_by_type_date_interval/tipo/data_inicial/data_final
  * Retorna os dados armazenados até o momento para o tipo e intervalo de datas enviado como argumento