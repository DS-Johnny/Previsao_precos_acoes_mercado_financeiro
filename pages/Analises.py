import streamlit as st


st.sidebar.title('Análises')
st.title("Análise")


st.markdown("---")
ticket, period, interval = st.columns(3)
with ticket:
    tic = st.selectbox(
        "Selecione a ação:",
        ("VALE3.SA", "BBAS3")
    )

with period:
    per = st.selectbox(
        "Selecione o periodo:",
        ("1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max")
    )

with interval:
    inter = st.selectbox(
        "Selecione o intervalo:",
        ("1m", "5m", "15m", "30m", "60m", "90m", "1d", "5d", "1wk", "1mo", "3mo")
    )



tab1, tab2 = st.tabs(['Gráficos', 'Tabelas'])

with tab1:
    g1, g2, g3 = st.tabs(['ROE', 'ROIC', 'Outro'])