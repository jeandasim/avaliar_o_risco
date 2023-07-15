import streamlit as st
import pandas as pd

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f5f5f5;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
    <p>Plataforma em Desenvolvimento pela AISIM ENGENHARIA utilizando Python</p>
    <p>@aisimengenharia | (81) 995041310 </p>
    </div>
""", unsafe_allow_html=True)

st.title('Avaliação do Potencial de Risco')
st.write('Gusmão Filho et. al., (1992)')

with st.expander('Fatores Topográficos'):
    altura_encosta = st.selectbox('Altura da encosta (m):', ['< 5', '5 - 10', '10 - 20', '20 - 30', '> 30'])
    extensao_encosta = st.selectbox('Extensão da encosta (m):', ['< 100', '100 - 250', '250 - 350', '350 - 500', '> 500'])
    declividade_encosta = st.selectbox('Declividade da encosta (%):', ['< 20', '20 - 30', '30 - 40', '40 - 50', '> 50'])
    perfil_encosta = st.selectbox('Perfil da encosta:', ['Côncavo', 'Retilíneo', 'Côncavo-Convexo', 'Convexo'])
    morfologia_encosta = st.selectbox('Morfologia da encosta:', ['Convexa', 'Retilínea', 'Sinuosa', 'Côncava'])

with st.expander('Fatores Geológicos'):
    litologia = st.selectbox('Litologia:', ['Calcário (Fm. Gramame)', 'Conglomerado (Fm. Cabo)', 'Solo Residual (Emb. Crist.)', 'Sedimento (Fm. Beberibe)', 'Sedimento (Fm. Barreiras)'])
    estrutura = st.selectbox('Estrutura:', ['Maciça', 'Mergulho Oposto', 'Subhorizontal', 'Subvertical', 'Mergulho Concordante'])
    textura = st.selectbox('Textura:', ['Areno-Argilosa', 'Areno-Siltosa', 'Arenosa/Argilosa', 'Topo arenoso','Topo argiloso'])
    evidencias_movimento = st.selectbox('Evidências de movimento:', ['Ravinamento sup. ', 'Cicatrizes', 'Voçorocas', 'Fendas', 'Surgências N.A', 'Ausentes'])

with st.expander('Fatores Ambientais'):
    vegetacao = st.selectbox('Vegetação (%):', ['100', '100 - 70', '70 - 30', '30 - 0', 'Ausente'])
    drenagem = st.selectbox('Drenagem:', ['Extensiva', 'Parcial', 'Insuficiente', 'Tópica', 'Inexistente'])
    cortes = st.selectbox('Cortes:', ['Isolados', 'Dispersos-', 'Dispersos+', 'Desordenados-', 'Desordenados+'])
    densidade_populacional = st.selectbox('Densidade populacional (hab/ha):', ['< 100', '100 - 200', '200 - 300', '300 - 500', '> 500'])
    tratamento = st.selectbox('Tratamento:', ['Extensivo', 'Parcial', 'Insuficiente', 'Tópico', 'Inexistente'])

# Dicionários para mapear as opções para os graus de risco

# Risco Topografico
risco_altura = {
    '< 5': 1,
    '5 - 10': 2,
    '10 - 20': 3,
    '20 - 30': 4,
    '> 30': 5
}

risco_extensao = {
    '< 100': 1,
    '100 - 250': 2,
    '250 - 350': 3,
    '350 - 500': 4,
    '> 500': 5
}

risco_declividade = {
    '< 20': 1,
    '20 - 30': 2,
    '30 - 40': 3,
    '40 - 50': 4,
    '> 50': 5
}

risco_perfil = {
    'Côncavo': 1,
    'Retilíneo': 2,
    'Côncavo-Convexo': 3,
    'Convexo': 4
}

risco_morfologia = {
    'Convexa': 1,
    'Retilínea': 2,
    'Sinuosa': 3,
    'Côncava': 4
}

# Risco Geológicos
risco_litologia = {
    'Calcário (Fm. Gramame)': 1,
    'Conglomerado (Fm. Cabo)': 2,
    'Solo Residual (Emb. Crist.)': 3,
    'Sedimento (Fm. Beberibe)': 4,
    'Sedimento (Fm. Barreiras)': 5
}

risco_estrutura = {
    'Maciça': 1,
    'Mergulho Oposto': 2,
    'Subhorizontal': 3,
    'Subvertical': 4,
    'Mergulho Concordante': 5
}

risco_textura = {
    'Areno-Argilosa': 1,
    'Argilo-Arenosa': 2,
    'Arenosa/Argilosa': 3,
    'Argilosa/Arenosa': 4,
    'Topo arenoso': 5,
    'Topo argiloso': 5
}

risco_evidencias = {
    'Ravinamento sup. ': 1,
    'Rav. Prof.': 2,
    'Cicatrizes': 3,
    'Voçorocas': 4,
    'Fendas': 4,
    'Surgências N.A': 5,
    'Ausentes': 5
}

# Riscos Ambientais

risco_vegetacao = {
    '100': 1,
    '100 - 70': 2,
    '70 - 30': 3,
    '30 - 0': 4,
    'Ausente': 5
}

risco_drenagem = {
    'Extensiva': 1,
    'Parcial': 2,
    'Insuficiente': 3,
    'Tópica': 4,
    'Inexistente': 5
}

risco_cortes = {
    'Isolados': 1,
    'Dispersos-': 2,
    'Dispersos+': 3,
    'Desordenados-': 4,
    'Desordenados+': 5
}

risco_densidade_populacional = {
    '< 100': 1,
    '100 - 200': 2,
    '200 - 300': 3,
    '300 - 500': 4,
    '> 500': 5
}

risco_tratamento = {
    'Extensivo': 1,
    'Parcial': 2,
    'Insuficiente': 3,
    'Tópico': 4,
    'Inexistente': 5
}

st.title('Grau e Classificação de Risco')
if st.button('Calcular Grau de Risco'):
    with st.expander('Valores dos Fatores'):
        topograficos_table = pd.DataFrame({
            'Fatores Topográficos': ['Altura da encosta', 'Extensão da encosta', 'Declividade da encosta', 'Perfil da encosta', 'Morfologia da encosta'],
            'Valor': [altura_encosta, extensao_encosta, declividade_encosta, perfil_encosta, morfologia_encosta]
        })
        st.table(topograficos_table)

        geologicos_table = pd.DataFrame({
            'Fatores Geológicos': ['Litologia', 'Estrutura', 'Textura', 'Evidências de movimento'],
            'Valor': [litologia, estrutura, textura, evidencias_movimento]
        })
        st.table(geologicos_table)

        ambientais_table = pd.DataFrame({
            'Fatores Ambientais': ['Vegetação', 'Drenagem', 'Cortes', 'Densidade populacional', 'Tratamento'],
            'Valor': [vegetacao, drenagem, cortes, densidade_populacional, tratamento]
        })
        st.table(ambientais_table)

    GR_T = (risco_altura[altura_encosta] + risco_extensao[extensao_encosta] + risco_declividade[declividade_encosta] + risco_perfil[perfil_encosta] + risco_morfologia[morfologia_encosta]) / 5
    GR_G = (risco_litologia[litologia] + risco_estrutura[estrutura] + risco_textura[textura] + risco_evidencias[evidencias_movimento]) / 4
    GR_A = (risco_vegetacao[vegetacao] + risco_drenagem[drenagem] + risco_cortes[cortes] + risco_densidade_populacional[densidade_populacional] + risco_tratamento[tratamento]) / 5

    P1 = 1  # Peso para o fator topográfico
    P2 = 2  # Peso para o fator geológico
    P3 = 3  # Peso para o fator ambiental
    GRF_ENC = (P1 * GR_T + P2 * GR_G + P3 * GR_A) / (P1 + P2 + P3)

    with st.expander('Resultado da Avaliação'):
        risk_table = pd.DataFrame({
            'Risco': ['Grau de Risco da Encosta', 'Classificação de Risco'],
            'Valor': [GRF_ENC, '']
        })

        # Classificar o grau de risco
        if GRF_ENC < 1.74:
            risco = 'Muito Baixo'
        elif 1.74 <= GRF_ENC < 2.25:
            risco = 'Baixo'
        elif 2.25 <= GRF_ENC < 2.75:
            risco = 'Médio'
        elif 2.75 <= GRF_ENC < 3.25:
            risco = 'Alto'
        else:
            risco = 'Muito Alto'

        risk_table['Valor'][1] = risco
        st.table(risk_table)
