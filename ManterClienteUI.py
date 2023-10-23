import streamlit as st
import pandas as pd
from view import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()
    def listar():
        clientes = View.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
    def atualizar():
            st.header("Atualizar")
            option = st.selectbox(
                'Selecione o cliente que desejar atualizar',
                (View.cliente_listar()))
            nome = st.text_input("informe o novo nome")
            email = st.text_input("informe o novo email")
            fone = st.text_input("informe o novo Telefone")
            if st.button("Atualizar"):
                View.cliente_atualizar(option.get_id(), nome, email, fone)
    def excluir():
            st.header("Excluir")
            option = st.selectbox('Selecione o cliente que desejar exluir',(View.cliente_listar()))
            if st.button("Excluir"):
                    View.cliente_excluir(option.get_id())
