import streamlit as st
import pandas as pd
from view import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de servicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.listar()
        with tab2:
            ManterServicoUI.inserir()
        with tab3:
            ManterServicoUI.atualizar()
        with tab4:
            ManterServicoUI.excluir()
    def listar():
        servicos = View.servico_listar()
        dic = []
        for c in servicos:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        Descrição = st.text_input("Descrição:")
        valor = st.number_input("Valor:")
        Duração = st.text_input("Duração:")
        if st.button("Inserir"):
            View.servico_inserir(Descrição, valor, Duração)
    def atualizar():
        st.header("Atualizar")
        option = st.selectbox('Selecione o cliente que desejar atualizar',(View.servico_listar()))
        Descrição = st.text_input("Nova Descrição:")
        valor = st.number_input("Nova Descrição:")
        Duração = st.text_input("Nova Duração:")
        if st.button("Atualizar"):
            View.servico_atualizar(option.get_id(), Descrição, valor, Duração)
    def excluir():
            st.header("Excluir")
            option = st.selectbox(
                'Selecione o cliente que desejar exluir',
                (View.servico_listar()))
            if st.button("Excluir"):
                View.servico_excluir(option.get_id())
