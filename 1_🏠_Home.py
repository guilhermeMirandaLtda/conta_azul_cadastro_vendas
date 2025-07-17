import streamlit as st
from utils.oauth import gerar_url_autorizacao
import uuid

st.set_page_config(page_title="Conectar Conta Azul", layout="centered")
st.title("🔗 Conectar Conta Azul")

state = uuid.uuid4().hex  # gera um identificador único por cliente
if st.button("🔐 Conectar Conta Azul"):
    url = gerar_url_autorizacao(state)
    st.markdown(f"""
        <meta http-equiv="refresh" content="0; url='{url}'" />
        """, unsafe_allow_html=True)
    st.session_state["oauth_state"] = state
    st.write("Redirecionando...")  # opcional
