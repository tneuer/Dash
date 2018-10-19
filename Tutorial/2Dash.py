"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 2Dash.py
    # Creation Date : Die 16 Okt 2018 19:17:23 CEST
    # Last Modified : Die 16 Okt 2018 19:51:45 CEST
    # Description :
"""
#==============================================================================

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash("my_app")

app.layout = html.Div(children=[
    dcc.Input(id="input", value="Enter something", type="text"),
    html.Div(id="output")
    ])

@app.callback(
        Output(component_id="output", component_property="children"),
        [Input(component_id="input", component_property="value")]
        )
def update_value(input_data):
    return "Input: {}".format(input_data)


if __name__ == "__main__":
    app.server.run(debug=True)

