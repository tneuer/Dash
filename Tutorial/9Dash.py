#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 9Dash.py
    # Creation Date : Mit 24 Okt 2018 00:27:25 CEST
    # Last Modified : Mit 24 Okt 2018 08:10:07 CEST
    # Description : Dynamic button binding
"""
#==============================================================================

import re

import dash
import dash_html_components as html
import dash_core_components as dcc

from collections import OrderedDict
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def serve_layout():
    layout = html.Div([
    dcc.Input(id="input", value=1),

    html.Div(id="content"),

    html.Div(id="output")
    ])

    return layout


app.layout = serve_layout

app.config.supress_callback_exceptions = True


@app.callback(Output('content', 'children'),
        [Input("input", "value")])
def create_buttons(nr_buttons):

    try:
        nr_buttons = int(nr_buttons)
        buttons = [html.Button(id="button-{}".format(i), children="Button {}".format(i)) for i in range(nr_buttons)]

        button_ids = ["button-{}".format(i) for i in range(nr_buttons)]

        @app.callback(Output('output', 'children'),
                [Input(button_id, "n_clicks") for button_id in button_ids])
        def create_buttons(clicks):
            print("Here")
            return clicks

        return buttons
    except ValueError:
        return "Input should be an integer"


def_buttons = ["button-{}".format(i) for i in range(10)]

if __name__ == '__main__':
    app.run_server(debug=True)




