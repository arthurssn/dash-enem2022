import plotly.express as px

def menos_inscritos(dfMA):
  cidadesM_ordenadas = dfMA.groupby('NO_MUNICIPIO_PROVA').size().sort_values().head(5)

  fig_menos_inscritos = px.bar(x=cidadesM_ordenadas.index, y=cidadesM_ordenadas,
      labels={'x': 'Cidades', 'y': 'Inscritos por cidade'},
      title='5 cidades com menos inscritos no Maranhão',
      color=cidadesM_ordenadas.values,  
      color_continuous_scale='reds',  
      )

  for i, v in enumerate(cidadesM_ordenadas):
      fig_menos_inscritos.add_annotation(x=cidadesM_ordenadas.index[i], y=v + 0.1, text=str(v),
      showarrow=False, xanchor='center', yanchor='bottom')

  return fig_menos_inscritos