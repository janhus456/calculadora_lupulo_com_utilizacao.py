import streamlit as st
import pandas as pd

def calcular_quantidade_nova(volume_cerveja, lupulos_atuais, quantidades_atuais, aa_atuais, oleo_atuais, utilizacoes_atuais,
                              lupulos_novos, aa_novos, oleo_novos, utilizacoes_novas):
    resultados = []
    total_oleo = 0
    total_amargor = 0

    for i in range(len(lupulos_atuais)):
        qnt = quantidades_atuis[i]
        aa = aa_atuais[i]
        utilizacao = utilizacoes_atuais[i]
        oleo = oleo_atuais[i] if i > 0 else 0

        ibu = (qnt * aa * utilizacao) / (volume_cerveja / 1000)
        total_amargor += ibu
        if i > 0:
            total_oleo += (qnt * oleo) / 100

    for i in range(len(lupulos_novos)):
        nome = lupulos_novos[i]
        aa_novo = aa_novos[i]
        utilizacao_novo = utilizacoes_novas[i]
        oleo_novo = oleo_novos[i] if i > 0 else 0

        if aa_novo == 0 or utilizacao_novo == 0:
            resultados.append((nome, "Erro: AA% ou Utilização não pode ser zero"))
            continue

        qnt_amargor_novo = (total_amargor * (volume_cerveja / 1000)) / (aa_novo * utilizacao_novo)
        qnt_oleo_novo = (total_oleo * 100) / oleo_novo if i > 0 and oleo_novo != 0 else 0

        if i == 0:
            resultados.append((nome, round(qnt_amargor_novo, 2)))
        else:
            resultados.append((nome, round(qnt_oleo_novo, 2)))

    return resultados

st.title("Calculadora de Substituição de Lúpulos")

volume_cerveja = st.number_input("Volume de Cerveja (em litros)", min_value=1.0, value=2000.0)

st.header("Lúpulos Atuais")
n_lupulos_atuais = st.number_input("Quantos lúpulos atualmente?", min_value=1, value=3)
lupulos_atuais = []
quantidades_atuais = []
aa_atuais = []
oleo_atuais = []
utilizacoes_atuais = []

for i in range(n_lupulos_atuais):
    nome_padrao = "Lúpulo de Amargor Atual" if i == 0 else f"Lúpulo Atual {i+1}"
    st.subheader(nome_padrao)
    nome = st.text_input(f"Nome do {nome_padrao}", value=nome_padrao, key=f"nome_atual_{i}")
    lupulos_atuais.append(nome)
    quantidades_atuais.append(st.number_input(f"Quantidade (g) do {nome}", min_value=0.0, value=1000.0, key=f"qtd_atual_{i}"))
    aa_atuais.append(st.number_input(f"Alfa Ácido (%) do {nome}", min_value=0.0, value=5.0, key=f"aa_atual_{i}"))
    utilizacoes_atuais.append(st.number_input(f"Fator de Utilização do {nome}", min_value=0.01, max_value=1.0, value=0.3 if i == 0 else (0.15 if i == 1 else 0.1), step=0.01, key=f"utl_atual_{i}"))
    if i > 0:
        oleo_atuais.append(st.number_input(f"Óleo (ml/100g) do {nome}", min_value=0.0, value=0.8, key=f"oleo_atual_{i}"))
    else:
        oleo_atuais.append(0)

st.header("Lúpulos Novos")
n_lupulos_novos = st.number_input("Quantos lúpulos novos?", min_value=1, value=2)
lupulos_novos = []
aa_novos = []
oleo_novos = []
utilizacoes_novas = []

for i in range(n_lupulos_novos):
    nome_padrao = "Lúpulo de Amargor Novo" if i == 0 else f"Lúpulo Novo {i+1}"
    st.subheader(nome_padrao)
    nome = st.text_input(f"Nome do {nome_padrao}", value=nome_padrao, key=f"nome_novo_{i}")
    lupulos_novos.append(nome)
    aa_novos.append(st.number_input(f"Alfa Ácido (%) do {nome}", min_value=0.0, value=5.0, key=f"aa_novo_{i}"))
    utilizacoes_novas.append(st.number_input(f"Fator de Utilização do {nome}", min_value=0.01, max_value=1.0, value=0.3 if i == 0 else (0.15 if i == 1 else 0.1), step=0.01, key=f"utl_novo_{i}"))
    if i > 0:
        oleo_novos.append(st.number_input(f"Óleo (ml/100g) do {nome}", min_value=0.0, value=0.8, key=f"oleo_novo_{i}"))
    else:
        oleo_novos.append(0)

if st.button("Calcular Quantidade dos Lúpulos Novos"):
    resultados = calcular_quantidade_nova(volume_cerveja, lupulos_atuais, quantidades_atuais, aa_atuais, oleo_atuais, utilizacoes_atuais,
                                          lupulos_novos, aa_novos, oleo_novos, utilizacoes_novas)
    st.subheader("Resultado da Substituição")
    for nome, quantidade in resultados:
        st.write(f"{nome}: {quantidade} g")
