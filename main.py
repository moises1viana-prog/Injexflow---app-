import streamlit as st
import pyrebase

# Configurações do seu Firebase
firebaseConfig = {
  "apiKey": "AIzaSyBywcXR0UlvX3Z...", 
  "authDomain": "injexflow-73084.firebaseapp.com",
  "projectId": "injexflow-73084",
  "storageBucket": "injexflow-73084.appspot.com",
  "messagingSenderId": "947545352624",
  "appId": "1:947545352624:web:..." 
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

st.title("🚀 InjexFlow - Monitoramento")

with st.form("producao"):
    st.write("Registro de Injeção - Haitian 01")
    boas = st.number_input("Peças Boas", min_value=0, step=1)
    ruins = st.number_input("Peças Ruins", min_value=0, step=1)
    
    if st.form_submit_button("Salvar Produção"):
        dados = {"boas": boas, "ruins": ruins, "maquina": "Haitian 01"}
        db.child("historico").push(dados)
        st.success("Dados enviados ao Firebase!")
