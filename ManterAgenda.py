import streamlit as st
import pandas as pd
from view import View

class ManterAgendaUI:
    def main():
        st.header("Cadastro de Agendas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAgendaUI.listar()
        with tab2:
            ManterAgendaUI.inserir()
        with tab3:
            ManterAgendaUI.atualizar()
        with tab4:
            ManterAgendaUI.excluir()
    def listar():
        agendas = View.agenda_listar()
        dic = []
        for c in agendas:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        date = st.text_input("Informe a data:")
        confirmado = st.text_input("Confirmado:")
        id_cliente = st.text_input("Id do cliente:")        
        id_servico = st.text_input("id do serviço")
        if st.button("Inserir"):
            View.agenda_inserir(date, confirmado, id_cliente, id_servico)
    def atualizar():
        st.header("Atualizar")
        option = st.selectbox('Selecione a agenda que desejar atualizar',(View.agenda_listar()))
        date = st.text_input("Informe a data:")
        confirmado = st.text_input("informe o novo nome:")
        id_cliente = st.text_input("informe o novo email:")
        id_servico = st.text_input("informe o novo Telefone:")
        if st.button("Atualizar"):
            View.agenda_atualizar(option.get_id(), date, confirmado, id_cliente, id_servico)
    def excluir():
            st.header("Excluir")
            option = st.selectbox('Selecione a Agenda que desejar exluir', (View.agenda_listar()))
            if st.button("Excluir"): 
                View.agenda_excluir(option.get_id())
