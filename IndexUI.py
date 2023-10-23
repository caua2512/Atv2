import streamlit as st
from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterAgendaUI import ManterAgendaUI
#from templates.AbrirAgendaUI import AbrirAgendaUI

class IndexUI:
  def sidebar():
    op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços","Manter Agenda", "Abrir Agenda do Dia","Confirmar Agendamento"])
    if op == "Manter Clientes": st.session_state["page"] = "manter_clienteUI"
    if op == "Manter Serviços": st.session_state["page"] = "manter_servicoUI"
    if op == "Manter Agenda": st.session_state["page"] = "manter_agendaUI"
    if op == "Abrir Agenda do Dia": st.session_state["page"] = "abrir_agendaUI"


  def main():
    IndexUI.sidebar()
    if "page" not in st.session_state: st.session_state["page"] = "ManterClienteUI"
    if st.session_state["page"] == "manter_clienteUI": ManterClienteUI.main()
    if st.session_state["page"] == "manter_servicoUI": ManterServicoUI.main()
    if st.session_state["page"] == "manter_agendaUI": ManterAgendaUI.main()
    #if st.session_state["page"] == "abrir_agendaUI": AbrirAgendaUI.main()

IndexUI.main()
