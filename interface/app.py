from typing import Dict, Iterator, Literal
import streamlit as st
import requests
import time


# type _

_Role = Literal['assistant', 'user']


# constant _

_API_HOST = 'http://localhost:5000'


# misc _

def _get_avatar(role: _Role) -> str:
    return {
        'assistant': '🤖',
        'user': '👤'
    }[role]


def _yield_chars(content: str) -> Iterator[str]:
    for char in content:
        yield char
        time.sleep(0.005)


# session _

def initialize_session() -> None:
    st.session_state.setdefault('messages', [])


def _store_message(content: str, role: _Role) -> None:
    st.session_state.messages.append({
        'content': content,
        'role': role
    })


# request _

def _fetch(url: str) -> Dict[str, str]:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def _get_answer(statement: str) -> str:
    url = f'{_API_HOST}/bot/{statement}'
    try:
        data = _fetch(url)
        answer = data.get('answer')
    except:
        answer = 'Bip bop! ' \
            + 'Estou passando por um "esgotamento" temporário ' \
            + 'e, infelizmente, não consigo responder agora.'
    return answer


# head _

def configure_page() -> None:
    st.set_page_config(
        page_title='Treinador Twin',
        page_icon='🦾'
    )


# body _

def hide_header() -> None:
    st.markdown(
        '''
        <style>
            header {visibility: hidden;}
        </style>
        ''',
        unsafe_allow_html=True
    )


def display_learn_more() -> None:
    with st.expander('💡 Saiba mais...'):
        st.markdown('''
            **Treinador Twin** é um assistente virtual de código 
            aberto, desenvolvido como parte de um projeto 
            acadêmico, com o objetivo de responder a perguntas 
            relacionadas ao universo fitness. O bot que alimenta 
            este assistente foi treinado com um conjunto de dados 
            limitado, focado em fornecer respostas precisas a 
            consultas específicas.

            🤔 Não sabe como começar? Experimente perguntar:

            - O que devo comer para ganhar músculos?
            - Como perder gordura e ganhar definição?
            - Quais suplementos devo tomar para aumentar minha 
            massa muscular?
            - Quais são os grupos musculares do corpo?
            - Quais são os principais exercícios de musculação?
            - Como desenvolver o peitoral?
            - Em qual horário eu devo treinar?
            - Quais as trocas emergenciais de exercícios?
            - Fiquei doente, o que fazer?
        ''')


def display_history() -> None:
    for message in st.session_state.messages:
        content, role = message['content'], message['role']
        avatar = _get_avatar(role)
        with st.chat_message(role, avatar=avatar):
            st.markdown(content)


def _display_statement(content: str) -> None:
    avatar = _get_avatar('user')
    st.chat_message('user', avatar=avatar).write(content)


def _display_spinner() -> Iterator[None]:
    return st.spinner(
        'Trazendo uma resposta  roboticamente fantástica...'
    )


def _display_answer(content: str) -> None:
    avatar = _get_avatar('assistant')
    chars = _yield_chars(content)
    with st.chat_message('assistant', avatar=avatar):
        st.write_stream(chars)


def display_input() -> None:
    if statement := st.chat_input(
        'Enviar mensagem...',
        max_chars=90
    ):
        _display_statement(statement)
        _store_message(statement, 'user')
        with _display_spinner():
            answer = _get_answer(statement)
        _display_answer(answer)
        _store_message(answer, 'assistant')


# execution _

if __name__ == '__main__':
    configure_page()
    initialize_session()
    hide_header()
    display_learn_more()
    display_history()
    display_input()
