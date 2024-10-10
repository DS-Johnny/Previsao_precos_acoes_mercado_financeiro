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

col1, col2, col3 = st.columns(3)
with col1:
    fig = u.plot_graph(tic, per, inter)
    st.plotly_chart(fig, use_container_width=True)

    # web scraping 
    ws = {'Anos' : [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'ROE' : [0.65, -33.81, 10.46, 12.26, 15.06, -4.37, 15.16, 63.01, 51.27, 20.91, 23.72],
        'ROIC' : [7.7, -19.7, 5.01, 13.72, 18.33, -0.13, 19.31, 43.08, 29.65, 19.46, 22.11],
        'ROA' : [0.07, -13.31, 4.12, 5.39, 7.53, -2.35, 5.21, 24.33, 21.25, 8.89, 10.17]
        }

    ws = pd.DataFrame(ws)

    fig2 = px.line(ws, 'Anos', y=['ROE', 'ROIC', 'ROA'], title='ROE, ROIC e ROA ao Longo dos Anos')
    st.plotly_chart(fig2, use_container_width=True)

    

with col2:
    tabela = pd.read_excel('Vale3_2024_10_17.xlsx')
    tabela = tabela[['VALE3', 'Atual']]
    st.table(tabela)

with col3:
    modelos = {'ML1': 'Compra', 'ML2' : 'Compra', 'ML3' : 'Venda'}
    modelos = pd.DataFrame(modelos, index=[0,1,2])
    st.table(modelos)

    preco = {'Preço' : ['Preço Teto', 'Preço Médio'],
         'Reais' : [65.25, 57.27]}
    preco = pd.DataFrame(preco)
    st.table(preco)

    

col1, col2 = st.columns(2)
with col1:
    grafico_3 = {"anos" : [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
            "divida_bruta_patrimonio" : [0.52, 0.86, 0.75, 0.52, 0.35, 0.39, 0.44, 0.4, 0.35, 0.35, 0.41],
            "divida_liquida_ebitda" : [2.48, -6.1, 2.81, 1.36, 0.67, 1.78, 0.11, 0.07, 0.36, 0.62, 0.56]}

    g3 = pd.DataFrame(grafico_3)
    fig3 = px.line(g3, x='anos', y=['divida_bruta_patrimonio', 'divida_liquida_ebitda'], title='Dívida Líquida/EBITDA e Dívida Bruta/Patrimônio')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    g4 = {"dy_numerico" : [8.62, 7.49, 0.65, 3.29, 3.86, 2.65, 2.75, 18.79, 8.53, 7.87, 11.47],
        "anos" : [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]}

    g4 = pd.DataFrame(g4)
    fig4 = px.line(g4, x='anos', y='dy_numerico', title='Dividend Yield (DY) ao Longo dos Anos')
    st.plotly_chart(fig4, use_container_width=True)



tab1, tab2 = st.tabs(['Gráficos', 'Tabelas'])

with tab1:
    g1, g2, g3 = st.tabs(['ROE', 'ROIC', 'Outro'])