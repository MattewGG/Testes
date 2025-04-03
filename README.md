# Testes de Nivelamento

## Índice
1. [💻 Sobre o projeto](#sobre-o-projeto)
2. [🔧 Tecnologias utilizadas](#tecnologias-utilizadas)
3. [🚀 Tutorial de inicialização](#tutorial-de-inicialização)
4. [⚙️ Funcionalidades](#funcionalidades)
5. [👨‍💻 Minha experiência como desenvolvedor](#minha-experiência-como-desenvolvedor)
6. [💬 Desenvolvedores](#desenvolvedores)

## Sobre o projeto
O projeto "Testes de Nivelamento" consiste em uma série de desafios técnicos que envolvem Web Scraping, Transformação de Dados, Banco de Dados e APIs. Os testes foram desenvolvidos utilizando Java e Python, com bibliotecas gerenciadas pelo Maven em java.

### Estrutura dos Testes

1. **Teste de Web Scraping**
   - Implementado em Java.
   - Realiza acesso ao site da ANS.
   - Faz download dos Anexos I e II em PDF.
   - Compacta os arquivos em um único arquivo ZIP/RAR.

2. **Teste de Transformação de Dados**
   - Implementado em python.
   - Extrai dados do Anexo I (PDF) e os converte para CSV.
   - Substitui abreviações conforme legenda.
   - Compacta o CSV gerado.

3. **Teste de Banco de Dados**
   - Implementado com scripts SQL compatíveis com MySQL 8 e PostgreSQL >10.0.
   - Estrutura tabelas para os arquivos baixados.
   - Importa os dados corretamente formatados.
   - Executa consultas analíticas sobre operadoras.

4. **Teste de API**
   - Desenvolvido com Vue.js (frontend) e Python (backend).
   - Permite busca textual na lista de operadoras cadastradas.
   - Disponibiliza uma coleção no Postman para demonstração.

## Tecnologias utilizadas

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)


## Tutorial de inicialização

### 📋 Pré-requisitos
Certifique-se de ter os seguintes softwares instalados em sua máquina:
- JDK 17
- Maven
- MySQL 8 ou PostgreSQL 10+
- Python 3.8+
- Node.js e Vue.js (para frontend)

### 🔧 Instalação

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/seu-usuario/testes-de-nivelamento.git
   ```

2. **Instale as dependências do Java via Maven.**

3. **Execute nos serviços necessários**:
   - Para o teste 2 e 4 em Python instale as dependencias:
     ```sh
     pip install -r requirements.txt
     ```
   - Para o frontend em Vue.js do teste 4:
     ```sh
     npm install
     ```
3. **Altere o caminho dos scripts de importe de dados**:
   - Para o teste 3, altere o caminho dos arquivos de acordo com as suas necessidades:
     ```sh
     use TesteTres;
     LOAD DATA INFILE 'Altere aqui para o caminho correto'
     ```

         



## Funcionalidades
- Extração e transformação de dados.
- Consultas SQL otimizadas para análise de dados.
- API para busca e manipulação de informações.

## Minha experiência como desenvolvedor
Durante o desenvolvimento deste projeto, enfrentei desafios interessantes, principalmente na extração de dados estruturados a partir de PDFs e na aplicação do front em vue que por eu não entender a ferramenta. A integração entre os diferentes componentes foi de grande aprendizado.

## Desenvolvedores
* Mateus

<p align="right">(<a href="#top">voltar ao topo</a>)</p>

