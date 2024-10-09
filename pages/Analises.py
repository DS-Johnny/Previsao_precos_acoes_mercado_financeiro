import streamlit as st
import utils as u
import plotly_express as px
import pandas as pd

st.sidebar.title('Análises')
st.title("Análise")


st.markdown("---")
ticket, period, interval = st.columns(3)
with ticket:
    tic = st.selectbox(
        "Selecione a ação:",
        ["VALE3.SA", "BBAS3"]
    )

with period:
    per = st.selectbox(
        "Selecione o periodo:",
        ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    )

with interval:
    inter = st.selectbox(
        "Selecione o intervalo:",
        ["1m", "5m", "15m", "30m", "60m", "90m", "1d", "5d", "1wk", "1mo", "3mo"]
    )

st.write(tic, per, inter)

fig = u.plot_graph(tic, per, inter)
st.plotly_chart(fig, use_container_width=True)

# web scraping 
ws = {'Anos' : [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
      'ROE' : [0.65, -33.81, 10.46, 12.26, 15.06, -4.37, 15.16, 63.01, 51.27, 20.91, 23.72],
      'ROIC' : [7.7, -19.7, 5.01, 13.72, 18.33, -0.13, 19.31, 43.08, 29.65, 19.46, 22.11],
      'ROA' : [0.07, -13.31, 4.12, 5.39, 7.53, -2.35, 5.21, 24.33, 21.25, 8.89, 10.17]
      }

ws = pd.DataFrame(ws)

fig2 = px.line(ws, 'Anos', y=['ROE', 'ROIC', 'ROA'])
st.plotly_chart(fig2, use_container_width=True)



tab1, tab2 = st.tabs(['Gráficos', 'Tabelas'])

with tab1:
    g1, g2, g3 = st.tabs(['ROE', 'ROIC', 'Outro'])