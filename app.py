import pandas as pd
from dash import Dash, dcc, html
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

values = pd.read_csv("values.csv")
dates = pd.read_csv("dates.csv")
d = {'values' : values.squeeze(), 'dates' : dates.squeeze()}
df2 = pd.DataFrame(data = d)

app = Dash(__name__)

app.layout = html.Div(
     children=[
        html.H1(children="Analyse des résultats"),
        html.P(
            children=(
                "Analyse du cours de l'indice du CAC 40"
            ),
        ),
        dcc.Graph(
            figure={
            "data": [
                    {
                        "x": df2['dates'],
                        "y": df2['values'],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)