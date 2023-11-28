import plotly.express as px
import pandas as pd

def racas(dfMA):
  RACA = {
      '0': 'Não Declarada',
      '1': 'Branca',
      '2': 'Preta',
      '3': 'Parda',
      '4': 'Amarela',
      '5': 'Indígena'}

  TP_COR_RACA = dfMA['TP_COR_RACA'].astype(str).value_counts()

  contagem_por_cor_raca = {RACA[codigo]: contagem for codigo, contagem in TP_COR_RACA.items()}

  dados_grafico = pd.DataFrame(list(contagem_por_cor_raca.items()), columns=['Categoria', 'Contagem'])

  fig_raca = px.bar(dados_grafico, x='Contagem', y='Categoria', orientation='h',
      title='Número de Inscritos por Cor e Raça no ENEM 2022 no Maranhão',
      labels={'Contagem': 'Número de Inscritos', 'Categoria': 'Categoria'},
      color='Contagem',  
      color_continuous_scale='viridis',  
      )

  fig_raca.update_layout(height=800, width=1000)

  fig_raca.update_layout(annotations=[dict(text=str(value), x=value, y=index, showarrow=False, xanchor='left', font=dict(size=10)) for index, value in enumerate(dados_grafico['Contagem'])])
  
  return fig_raca
