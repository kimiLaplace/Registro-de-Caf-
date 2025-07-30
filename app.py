import streamlit as st
import requests
from datetime import datetime

st.title("📋 Registro de Café")

# Coleta dos dados
data = st.date_input("Data")
hora = st.time_input("Horário")
flag = st.radio("Flag", ["Sim", "Não"])
obs = st.text_area("Observações")

if st.button("Enviar"):
    # URL correta para o envio de respostas do formulário
    # Note que termina com "formResponse" em vez de "viewform"
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeuSOidOlvY80Ae5ZcKgUjOP1XPxRPmtcdjVsTlZtRoij3MsA/formResponse"

    # Mapeamento corrigido dos entrys do formulário
    form_data = {
        # Campos de data (ano, mês, dia)
        "entry.1753921748_year": data.year,
        "entry.1753921748_month": data.month,
        "entry.1753921748_day": data.day,

        # Campos de horário (hora, minuto)
        "entry.1810654528_hour": hora.hour,
        "entry.1810654528_minute": hora.minute,

        # Campo da Flag (Sim/Não)
        "entry.451192745": flag,

        # Campo de Observações
        "entry.2094178778": obs,
    }

    response = requests.post(form_url, data=form_data)

    if response.status_code == 200:
        st.success("✅ Registro enviado com sucesso!")
    else:
        st.warning(f"⚠️ Algo deu errado. Código de status: {response.status_code}")
        st.info("Verifique a URL do formulário e o mapeamento dos campos 'entry'.")
