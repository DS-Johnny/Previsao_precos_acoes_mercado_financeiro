import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("PROJETO INTEGRADOR IV")
st.markdown("---")
st.sidebar.title("Home")
# ---------------------------------------------- Dados 
# Função para gerar o gráfico com base nas opções escolhidas
def plot_graph(ticket, period, interval):
    dados = yf.download(ticket, period=period, interval=interval)

    # Remover finais de semana e feriados (dias sem negociação)
    dados = dados.dropna()

    # Criar gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(dados.index, dados['Close'], label=f'Cotação de Fechamento ({interval})')

    plt.title(f'Cotação de {ticket} ({period})')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (R$)')
    plt.xticks(rotation=45)

    # Formatar e ajustar o eixo X para datas
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%Y'))  # Formato das datas
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.WeekdayLocator())  # Mostrar apenas dias úteis (semanas)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



col1, col2, col3 = st.columns(3)

with col1:
    st.write('Indicador 1')
with col2:
    st.write('Indicador 2')
with col3:
    st.write('Indicador 3')

st.markdown("---")


col1, col2 = st.columns(2)
with col1:
    st.write('Gráfico 1')
    st.write('Gráfico matplot')

with col2:
    st.write('Gráfico 2')
    st.write('linha 2')
    st.write('linha 3')