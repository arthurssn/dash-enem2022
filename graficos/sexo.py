import plotly.express as px

def sexo(dfMA):

  sexo_counts = dfMA['TP_SEXO'].value_counts()
  fig_sexo = px.pie(sexo_counts, labels=sexo_counts.index, values=sexo_counts.values,
      title='Porcentagem por gênero de quem realizou a prova no Maranhão',
      color=sexo_counts.index,
      color_discrete_map={'M': 'blue', 'F': 'pink'},
      )

  fig_sexo.update_traces(textinfo='label+percent', hoverinfo='label+percent')

  return fig_sexo
