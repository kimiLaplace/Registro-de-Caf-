import streamlit as st
import requests
from datetime import datetime
from zoneinfo import ZoneInfo 

st.title("📋 Registro de Térmicas")

fuso_horario_brasil = ZoneInfo('America/Sao_Paulo')

data_e_hora_atuais = datetime.now(fuso_horario_brasil)

# Coleta dos dados
data = st.date_input("Data", value=data_e_hora_atuais.date())

#    - 'value': Define o horário padrão como o horário atual no fuso correto.
#    - 'step=60': Define que o intervalo de seleção é de 1 em 1 minuto (60 segundos).
hora = st.time_input(
    "Horário", 
    value=data_e_hora_atuais.time(), 
    step=60
)

flag = st.radio("Flag", ["Sim", "Não"])
obs = st.text_area("Observações")

if st.button("Enviar"):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeuSOidOlvY80Ae5ZcKgUjOP1XPxRPmtcdjVsTlZtRoij3MsA/formResponse"

    # Para simplificar, vou usar a "Opção B" da resposta anterior, 
    # anexando o horário exato nas observações.
    horario_formatado = hora.strftime('%H:%M') # Formatando sem segundos, ajuste se precisar
    obs_final = f"Horário exato: {horario_formatado}\n\nObservações:\n{obs}"

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
        "entry.2094178778": obs_final,
    }

    response = requests.post(form_url, data=form_data)

    if response.status_code == 200:
        st.success("✅ Registro enviado com sucesso!")
    else:
        st.warning(f"⚠️ Algo deu errado. Código de status: {response.status_code}")
        st.info("Verifique a URL do formulário e o mapeamento dos campos 'entry'.")
