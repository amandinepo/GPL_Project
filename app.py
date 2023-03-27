import pandas as pd
from dash import Dash, dcc, html
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

values = pd.read_csv("values.csv")
dates = pd.read_csv("dates.csv")
d = {'values' : values, 'dates' : dates}
df2 = pd.DataFrame(data=d)
data = df2.query("type == 'conventional' and region == 'Albany'")
data["dates"] = pd.to_datetime(data["dates"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = Dash(__name__)

app.layout = html.Div(
     children=[
        html.H1(children="Avocado Analytics"),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
            "data": [
                    {
                        "x": data['values'],
                        "y": data['dates'],
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