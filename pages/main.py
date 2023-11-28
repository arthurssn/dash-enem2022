import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('ENEM 2022 no Maranhão')

df = pd.read_csv('../../../../Downloads/microdados_enem_2022/DADOS/MICRODADOS_ENEM_2022.csv', sep=';', encoding="ISO-8859-1", chunksize=1000000)
# st.line_chart

df = pd.concat(df, ignore_index=True)

CL_selecionadas = ['TP_FAIXA_ETARIA','TP_SEXO','TP_COR_RACA','TP_ST_CONCLUSAO','TP_ESCOLA','NO_MUNICIPIO_PROVA',
'SG_UF_PROVA','TP_PRESENCA_CN','TP_PRESENCA_CH','TP_PRESENCA_LC','TP_PRESENCA_MT','NU_NOTA_CN',
'NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']


new_df = df.filter(items = CL_selecionadas)
new_df.head()

dfMA = new_df[new_df['SG_UF_PROVA'] == 'MA']
dfMA.head()

dfMA = dfMA.dropna()  
dfMA.info()

cidades = dfMA['NO_MUNICIPIO_PROVA'].value_counts().head(5)
cidades_ordenadas = dfMA.groupby('NO_MUNICIPIO_PROVA').size().sort_values(ascending=False).head(5)

fig = px.bar(x=cidades_ordenadas.index, y=cidades_ordenadas, labels={'x': 'Cidades', 'y': 'Inscritos por cidade'},
             title='Cidades com Mais Inscritos no Maranhão')

for i, v in enumerate(cidades_ordenadas):
    fig.add_annotation(x=cidades_ordenadas.index[i], y=v + 0.1, text=str(v), showarrow=False, xanchor='center', yanchor='bottom')

st.plotly_chart(fig)
