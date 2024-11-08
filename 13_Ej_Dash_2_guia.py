#Importar librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

# CARGA DE DATOS
df_sp500 = pd.read_csv(r'...',encoding = 'ISO-8859-1',delimiter=',')

# DEFINICIÓN LAYOUT
app.layout = html.Div([
                    html.Div([
                    html.Label('Selección'),
                    dcc.Dropdown(id='selector',
                        ...
                    )],style={'width': '48%', 'display': 'inline-block'}),

                    html.Div([
                    html.Label('Rango fechas'),
                    dcc.DatePickerRange(...),
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

                    ...,

                    ...


                    ])

# CREACIÓN DE GRÁFICOS E INTERACTIVIDAD
#Callback para actualizar gráfico de cotización en función del dropdown eligiendo apertura o cierre de sesión y según selector de fechas
@app.callback(Output(...),
              [Input(...])
def actualizar_graph_line(fecha_min, fecha_max, seleccion):
    filtered_df = ... #Filtrar dataframe en base a fecha_min, fecha_max

    # Seleccionar fecha en función del dropdown "selector"
    if seleccion == "Open":
        return{
            ...





            )}

    else:
        return{
            ...





    }

#Callback para actualizar gráfico de volumen según selector de fechas
@app.callback(Output(...),
              [Input(...])
def actualizar_graph_bar(fecha_min, fecha_max):
    filtered_df = ... #Filtrar dataframe en base a fecha_min, fecha_max
    return{
        'data': [...],

        'layout': ...
            }

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server()
