import streamlit as st
import google.generativeai as genai
import os

key = os.getenv("API_KEY")
print(key)
genai.configure(api_key="AIzaSyB1qSn76_l5VSKdXRUr-qdMY01jbSQjNVY")

st.title("Papo com a IA")

# Criar ou recuperar histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Mostrar histórico
for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# Input do usuário
user_input = st.chat_input("Digite aqui sua mensagem")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.mensagens.append({"role": "user", "content": user_input})

    # Criar o modelo
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Enviar todo o histórico como contexto
    resposta = model.generate_content(
        [{"role": m["role"], "parts": [m["content"]]} for m in st.session_state.mensagens]
    )

    resposta_ia = resposta.text
    st.chat_message("assistant").write(resposta_ia)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_ia})
