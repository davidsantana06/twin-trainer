### 🦾 Twin Trainer

- 🇧🇷 — Treinador Twin
- 🇺🇸 — Twin Trainer

Assistente virtual centrado no universo fitness, desenvolvido para responder a um conjunto de perguntas de propósito geral e específico sobre exercícios. Desenvolvido como um projeto acadêmico, o ecossistema é composto por duas frentes: a API, que hospeda o bot e todas as suas dependências, e a interface, que permite a interação do usuário por meio de um chat. O nome e o tema do sistema são inspirados no **@LeandroTwin**, que, na minha opinião, é o melhor produtor de conteúdo no que diz respeito à educação física.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ChatterBot](https://img.shields.io/badge/legacy-CHATTERBOT-300a24?style=for-the-badge)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

### 🛠️ Instalação e Configuração

O sistema foi desenvolvido utilizando **Python 3.12**, sendo recomendada a utilização dessa versão para garantir compatibilidade. Será necessário obter uma cópia local do código-fonte, que pode ser obtida com o seguinte comando:

```bash
git clone https://github.com/davidsantana06/twin-trainer
```

No diretório da aplicação, instale as dependências utilizando o `pip`:

```bash
pip install -r requirements.txt
```

Além disso, será necessário instalar o pacote `en_core_web_sm`. O comando pode variar conforme o sistema operacional.

- Para sistemas 🐧 **Linux**:

  ```bash
  python3 -m spacy download en_core_web_sm
  ```

- Para sistemas 🪟 **Windows**:

  ```bash
  python -m spacy download en_core_web_sm
  ```

Após concluir as etapas anteriores, você poderá inicializar os servidores com o seguinte comando:

```bash
python run.py
```

### ⚖️ Licença

Este repositório adota a **Licença MIT**, permitindo o uso e a modificação do código como desejar. Peço apenas que seja dado o devido crédito, reconhecendo o esforço e o tempo investidos no desenvolvimento.
