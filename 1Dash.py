#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 1Dash.py
    # Creation Date : Die 16 Okt 2018 17:16:23 CEST
    # Last Modified : Die 16 Okt 2018 19:17:24 CEST
    # Description :
"""
#==============================================================================

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash("my_app")

app.layout = html.Div(children=[
    html.H1("Dash Tutorials"),
    dcc.Graph(id="Example",
        figure={
            "data": [
                {"x": [1,2,3,4,5], "y": [5,6,7,8,9], "type": "line", "name": "boats"},
                {"x": [1,2,3,4,5], "y": [8,3,2,3,5], "type": "bar", "name": "cars"},
                ],
            "layout": {
                "title": "Basic Dash Example"
                }
            })
    ])

if __name__ == "__main__":
    app.server.run(debug=True)

