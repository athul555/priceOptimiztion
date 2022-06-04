
from subprocess import call
import dash
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
from layout import layout, df
from callback import callback
import pandas as pd

import dash_bootstrap_components as dbc




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    
app.layout= html.Div(layout)
callback(app)  



if __name__ == '__main__': 
    app.run_server(host='0.0.0.0', port= 8080)