from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output #Módulos de interactividad con Dash

df_temp = pd.read_excel(r'Temperaturas.xlsx')

#Creación de la app de dash
app = Dash(__name__)

app.layout=html.Div([
    dcc.Graph(id='graph_linea'),
    dcc.DatePickerRange(id='selector_fecha', start_date=df_temp['FECHA'].min(), end_date=df_temp['FECHA'].max())
])

@app.callback(
        Output('graph_linea', 'figure'),
        [Input('selector_fecha','start_date'),Input('selector_fecha','end_date')]
)

def actulizar_graph(fecha_min, fecha_max):
    filtered_df = df_temp[(df_temp["FECHA"]>=fecha_min) & (df_temp["FECHA"]<=fecha_max)]

    traces = []
    for nombre_ciudad in filtered_df["Ciudad"].unique():
        df_ciudad = filtered_df[filtered_df['Ciudad']== nombre_ciudad]
        traces.append(go.Scatter(
            x=df_ciudad["FECHA"],
            y=df_ciudad["T_Promedio"],
            text=df_ciudad["Ciudad"],
            mode='lines',
            opacity=0.7,
            marker={'size':15},
            name=nombre_ciudad
        ))
    return {
        'data':traces,
        'layout':go.Layout(
            xaxis={'title': 'Fecha'},
            yaxis={'title': 'Temperatura media'},
            hovermode='closest'
        )
    }

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
