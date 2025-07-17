import streamlit as st
from utils.oauth import trocar_token
import sqlite3
import time

st.set_page_config(page_title="Callback Conta Azul")

st.title("🔐 Callback de autorização")

# 🎯 1. Captura o code e state via query params
params = st.experimental_get_query_params()
code = params.get("code", [None])[0]
state = params.get("state", [None])[0]

if not code:
    st.error("Código 'code' não encontrado na URL.")
    st.stop()

st.success(f"Código recebido: {code}")
st.write(f"State fornecido: {state}")

# 🔄 2. Troca o código por tokens
try:
    token_data = trocar_token(code)
except Exception as e:
    st.error(f"Erro ao trocar token: {e}")
    st.stop()

access_token = token_data["access_token"]
refresh_token = token_data["refresh_token"]
expires_in = token_data["expires_in"]
created_at = int(time.time())

st.success("✅ Tokens recebidos com sucesso!")

# 🔐 3. Armazena tokens no SQLite
conn = sqlite3.connect("data/tokens.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        state TEXT PRIMARY KEY,
        access_token TEXT,
        refresh_token TEXT,
        expires_at INTEGER
    )
""")
expires_at = created_at + expires_in
cursor.execute("""
    INSERT OR REPLACE INTO tokens (state, access_token, refresh_token, expires_at)
    VALUES (?, ?, ?, ?)
""", (state, access_token, refresh_token, expires_at))
conn.commit()
conn.close()

st.success(f"Tokens salvos para `{state}`.")
st.write("Você pode fechar esta aba e voltar ao painel principal.")
