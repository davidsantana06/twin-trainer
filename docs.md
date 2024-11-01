### 📚 Documentação

Esta documentação fornece uma visão geral do funcionamento da aplicação, incluindo a divisão entre seus dois segmentos.

### 🗄️ API

Abriga o chatbot, juntamente com os arquivos brutos contendo as conversas. O acesso é realizado através do endereço `localhost:5000`, sendo restrito à interface, o que significa que não é possível acessá-la diretamente. A primeira requisição tende a ser mais demorada, pois inicia o treinamento do bot.

##### <img src="https://img.shields.io/badge/GET-61AFFE?style=flat-square" alt="GET" height="24px"> <img src="https://img.shields.io/badge//bot/%3Cstring:statement%3E-EBF3FB?style=flat-square" alt="/bot/<string:statement>" height="24px">

Responde à declaração informada como **`statement`**.

- **📤 Saída**: _JSON contendo a declaração normalizada e a resposta_

  ```json
  {
    "statement": "oi",
    "answer": "Olá, sou o Treinador Twin. Como posso te ajudar?"
  }
  ```

### 💻 Interface

Possibilita o acesso do usuário por meio de uma página web que dispõe dos seguintes elementos: conversas, seu respectivo histórico e uma seção de ajuda com exemplos de comandos disponíveis. Sua utilização é prática e intuitiva, permitindo uma navegação simples entre os componentes.
