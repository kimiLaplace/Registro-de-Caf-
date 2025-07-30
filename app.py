import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Nome do arquivo Excel
excel_file = "registro_dados.xlsx"

# Cria o arquivo Excel com cabeçalhos se ele não existir
if not os.path.exists(excel_file):
    df_init = pd.DataFrame(columns=["Data", "Horário", "Flag", "Observações", "Registrado em"])
    df_init.to_excel(excel_file, index=False)

# Título da aplicação
st.title("📅 Registro do Café")

# Formulário
data = st.date_input("Selecione a data")
horario_input = st.text_input("Digite o horário (HH:MM ou HH:MM:SS)", value="08:00")

try:
    # Tenta converter para hora válida
    horario = datetime.strptime(horario_input.strip(), "%H:%M:%S").time()
except ValueError:
    try:
        horario = datetime.strptime(horario_input.strip(), "%H:%M").time()
    except ValueError:
        st.error("⛔ Horário inválido. Use o formato HH:MM ou HH:MM:SS.")
        st.stop()

flag = st.radio("Flag (Sim/Não)", ["Sim", "Não"])
observacao = st.text_area("Observações")

# Botão de envio
if st.button("Registrar"):
    novo_registro = pd.DataFrame([{
        "Data": data.strftime("%Y-%m-%d"),
        "Horário": horario.strftime("%H:%M:%S"),
        "Flag": flag,
        "Observações": observacao,
        "Registrado em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    # Adiciona novo registro no Excel
    df_existente = pd.read_excel(excel_file)
    df_atualizado = pd.concat([df_existente, novo_registro], ignore_index=True)
    df_atualizado.to_excel(excel_file, index=False)

    st.success("✅ Registro salvo com sucesso!")
