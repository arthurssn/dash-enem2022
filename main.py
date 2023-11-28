import streamlit as st
import pandas as pd
from graficos.mais_inscritos import mais_inscritos
from graficos.menos_inscritos import menos_inscritos
from graficos.sexo import sexo
from graficos.racas import racas

st.title('Maranhão no ENEM 2022')

df = pd.read_csv('../../../../Downloads/microdados_enem_2022/DADOS/MICRODADOS_ENEM_2022.csv', sep=';', encoding="ISO-8859-1", chunksize=1000000)

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

cidades_ordenadas = dfMA.groupby('NO_MUNICIPIO_PROVA').size().sort_values(ascending=False).head(5)

st.plotly_chart(mais_inscritos(dfMA))

st.plotly_chart(menos_inscritos(dfMA))

st.plotly_chart(sexo(dfMA))

st.plotly_chart(racas(dfMA))