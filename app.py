import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('./data/vehicles_us.csv')  # leitura dos dados
header = st.header('Análise Veiculos US')  # cabeçalho geral

build_hist = st.checkbox('Criar histograma')  # criar um botão

if build_hist:  # se a caixa de seleção for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar gráfico de dispersão')  # criar um botão

if build_scatter:  # se a caixa de seleção for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
