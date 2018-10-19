#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 3Dash.py
    # Creation Date : Die 16 Okt 2018 19:57:36 CEST
    # Last Modified : Die 16 Okt 2018 20:42:50 CEST
    # Description :
"""
#==============================================================================


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import datetime
import pandas_datareader.data as web


app = dash.Dash("my_app")

app.layout = html.Div(children=[
    html.H1("Dash Tutorials"),

    html.Div(children="""
        Symbol to graph:
        """),

    dcc.Input(id="input", value="", type="text"),
    html.Div(id="output-graph")

    ])

@app.callback(
        Output(component_id="output-graph", component_property="children"),
        [Input(component_id="input", component_property="value")]
        )
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()

    df = web.DataReader(input_data, 'iex', start, end)

    return dcc.Graph(id="Graph",
        figure={
            "data": [
                {"x": df.index, "y": df.close, "type": "line", "name": input_data},
                ],
            "layout": {
                "title": input_data
                }
            })

if __name__ == "__main__":
    app.server.run(debug=True)
