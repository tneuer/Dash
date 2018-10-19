#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 5Dash.py
    # Creation Date : Die 16 Okt 2018 21:12:29 CEST
    # Last Modified : Die 16 Okt 2018 21:15:38 CEST
    # Description : Application
"""
#==============================================================================


import dash
import time
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from pandas_reader import DataReader

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Dash Tutorials"),

    dcc.Graph(id="live-graph", animate=True),
    dcc.Interval(
        id="graph-update",
        interval=100
        )
    ])

@app.callback(
        Output(component_id="live-graph", component_property="figure"),
        events = [Event("graph-update", "interval")]
        )
def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+random.uniform(-0.1, 0.1))

    data = go.Scatter(
            x=list(X),
            y=list(Y),
            name="Scatter",
            mode = "lines+markers"
            )

    return {
            "data": [data],
            "layout": go.Layout(xaxis = dict(range=[min(X), max(X)]),
                                yaxis = dict(range=[min(Y), max(Y)])
                                )
            }

if __name__ == "__main__":
    app.server.run(debug=True)
