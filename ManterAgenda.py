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
        data = st.text_input("Informe a data:")
        confirmado = st.text_input("Confirmado:")
        id_cliente = st.selectbox('Selecione o Id do cliente que desejar',(View.cliente_listar()))       
        id_servico = st.selectbox('Selecione o Id do serviço que desejar',(View.servico_listar()))
        if st.button("Inserir"):
            View.agenda_inserir(data, confirmado, id_cliente, id_servico)
    def atualizar():
        st.header("Atualizar")
        option = st.selectbox('Selecione a agenda que desejar atualizar',(View.agenda_listar()))
        data = st.text_input("Informe a nova data:")
        confirmado = st.text_input("confirmado:")
        id_cliente = st.selectbox('Selecione o Id do cliente que atualizar',(View.cliente_listar()))       
        id_servico = st.selectbox('Selecione o Id do serviço que atualizar',(View.servico_listar()))
        if st.button("Atualizar"):
            View.agenda_atualizar(option.get_id(), data, confirmado, id_cliente, id_servico)
    def excluir():
            st.header("Excluir")
            option = st.selectbox('Selecione a Agenda que desejar exluir', (View.agenda_listar()))
            if st.button("Excluir"): 
                View.agenda_excluir(option.get_id())
