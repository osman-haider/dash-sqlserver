import dash
from dash import dcc
from dash import html


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='database-data-graph'),
    html.Button('Update Data', id='update-button')
])
