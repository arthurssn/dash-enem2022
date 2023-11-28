import plotly.express as px

def mais_inscritos(dfMA):
    cidades_ordenadas = dfMA.groupby('NO_MUNICIPIO_PROVA').size().sort_values(ascending=False).head(5)

    fig = px.bar(x=cidades_ordenadas.index, y=cidades_ordenadas,
      labels={'x': 'Cidades', 'y': 'Inscritos por cidade'},
      title='5 Cidades com mais inscritos no Maranhão',
      color=cidades_ordenadas.values,
      color_continuous_scale='blues',
      )

    for i, v in enumerate(cidades_ordenadas):
        fig.add_annotation(x=cidades_ordenadas.index[i], y=v + 0.1, text=str(v),
        showarrow=False, xanchor='center', yanchor='bottom')

    return fig