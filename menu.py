import streamlit as st

st.set_page_config(page_title="Menú Principal Yupi", layout="centered")

st.title("🌈 Menú Principal - Catálogos Yupi")

st.markdown("---")

st.markdown("### Elige una de las siguientes vistas:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧸 Juegos Yupi"):
        st.markdown('[Ir a Juegos Yupi](https://yupijump.streamlit.app/)', unsafe_allow_html=True)

with col2:
    if st.button("☕ Café Yupi"):
        st.markdown('[Ir a Café Yupi](https://yupicafeall.streamlit.app/)', unsafe_allow_html=True)

with col3:
    if st.button("🛠️ Equipamiento Yupi"):
        st.markdown('[Ir a Equipamiento Yupi](https://yupiequipalmientoall.streamlit.app/)', unsafe_allow_html=True)