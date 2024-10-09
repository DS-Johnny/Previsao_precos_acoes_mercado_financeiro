import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px


# Função para gerar o gráfico com base nas opções escolhidas
def plot_graph(ticket, period, interval):
    dados = yf.download(ticket, period=period, interval=interval)

    # Remover finais de semana e feriados (dias sem negociação)
    dados = dados.dropna().reset_index()

    fig = px.line(dados, x='Date', y='Close')
    return fig