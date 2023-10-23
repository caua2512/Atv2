import streamlit as st
import pandas as pd
from view import View

class AbrirAgendaUI:
    def main():
        st.header("Abrir Agenda do dia")
        data = st.text_input("Informe a data em formato dd/mm/aaaa")
        HorarioI = st.text_input("Informe o horário inicial em formato HH:MM ")
        HorarioF = st.text_input("Informe o horário final em formato HH:MM ")
        data = st.number_input("Informe o intervalo entre os horários(min)")
        if st.button("Inserir Horários"):
            pass
