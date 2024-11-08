from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output #Módulos de interactividad con Dash


#Creación de la app de dash
app = Dash(__name__)

df = pd.read_excel(r'Info_pais.xlsx')

variables = df.columns #Lista con las columnas del dataframe que estarán en los dropdowns

app.layout = html.Div([
                html.Div([
                   dcc.Dropdown(
                       id='ejex',
                       options=[{'label': i, 'value':i} for i in variables],
                       value='Renta per capita'
                   ) 
                ],style={'width':'48%', 'display': 'inline-block'}),

                html.Div([
                   dcc.Dropdown(
                       id='ejey',
                       options=[{'label': i, 'value':i} for i in variables],
                       value='Esperanza de vida'
                   ) 
                ],style={'width':'48%', 'float':'right', 'display': 'inline-block'}),

                dcc.Graph(id='grafico_var'),

                dcc.Graph(id='grafico_var2')

], style={'padding':10})

@app.callback(
        Output('grafico_var', 'figure'),
        [Input('ejex', 'value'), Input('ejey', 'value')]
)

def actualizar_graf(nombre_ejex, nombre_ejey):
    return {
        'data':[go.Scatter(
            x=df[nombre_ejex], #La selección realizada en el primer dropdown
            y=df[nombre_ejey], #La selección realizada en el segundo dropdown
            text=df['País'],
            mode='markers',
            marker={
                'size':15,
                'opacity':0.5,
                'line':{'width': 0.5, 'color':'white'}
            }

        )],
        'layout':go.Layout(
            xaxis={'title':nombre_ejex, 'tickangle': 45}, #Definir el ángulo de las etiquetas
            yaxis={'title':nombre_ejey},
            margin={'l': 40, 'b':80, 't':10, 'r':0}, #Márgenes del gráfico
            hovermode='closest'
        )
    }

##Callback para segunda salida
@app.callback(
        Output('grafico_var2', 'figure'),
        [Input('ejey', 'value')]
)

def actualizar_graf2(nombre_ejey):
    return {
        'data':[go.Scatter(
            x=df['País'], #La selección realizada en el primer dropdown
            y=df[nombre_ejey], #La selección realizada en el segundo dropdown
            text=df['País'],
            mode='markers',
            marker={
                'size':15,
                'opacity':0.5,
                'line':{'width': 0.5, 'color':'white'}
            }

        )],
        'layout':go.Layout(
            xaxis={'title':'País', 'tickangle': 45}, #Definir el ángulo de las etiquetas
            yaxis={'title':nombre_ejey},
            margin={'l': 40, 'b':80, 't':10, 'r':0}, #Márgenes del gráfico
            hovermode='closest'
        )
    }



# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
