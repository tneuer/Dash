#!/home/thomas/anaconda3/bin/python

"""
    # Author : Thomas Neuer (tneuer)
    # File Name : 8Dash.py
    # Creation Date : Mon 22 Okt 2018 13:15:39 CEST
    # Last Modified : Die 23 Okt 2018 21:22:08 CEST
    # Description : Open tab on click
"""
#==============================================================================

import re

import dash
import dash_html_components as html
import dash_core_components as dcc

from collections import OrderedDict
from dash.dependencies import Input, Output, State

clicked_on_open = 0
clicked_on_close = 0
clicked_on_close2 = 0
tabdict = OrderedDict()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(id="Buttons_Open_Close",
        children=[
            html.Button(id="open", children="Open tab"),
            html.Button(id="close", children="Close tab")
            ]
        ),

    html.Div(
        id="tabs-div",
        children=dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Tab 1", value="tab-1")
                ]
            )),

    html.Div(id='tabs-content')
])

@app.callback(Output('tabs', 'value'),
        [Input("close", "n_clicks")],
        [State("tabs", "value")])
def switch_tab(clicks_close, current_tab):
    global clicked_on_close2
    if clicks_close is None:
        clicks_close = 0
    close_tab = bool(clicked_on_close2 - clicks_close)
    print(clicked_on_close2)
    print(clicks_close)
    if close_tab:
        r = re.compile("[0-9]+")
        curr_tab_number = re.search(r, current_tab).group(0)
        value = "tab-{}".format(int(curr_tab_number)+1)
        clicked_on_close2 = clicks_close
    else:
        value = current_tab

    print(value)
    return value

@app.callback(Output('tabs', 'children'),
        [Input("open", "n_clicks"), Input("close", "n_clicks")],
        [State("tabs", "children"), State("tabs", "value")])
def open_and_close_tab(clicks_open, clicks_close, current_tabs, selected_tab):
    global clicked_on_open
    global clicked_on_close
    global tabdict
    if clicks_open is None:
        clicks_open = 0
    if clicks_close is None:
        clicks_close = 0
    open_tab = bool(clicked_on_open - clicks_open)
    close_tab = bool(clicked_on_close - clicks_close)
    nr_current_tabs = len(current_tabs)
    if open_tab:
        clicked_on_open = clicks_open
        tabdict = {"tab-{}".format(t+1): dcc.Tab(label="Tab {}".format(t+1), value="tab-{}".format(t+1)) for t in range(nr_current_tabs+1)}
        children = list(tabdict.values())
    elif close_tab:
        clicked_on_close = clicks_close
        if selected_tab == "tab-1":
            print("NO!")
        else:
            tabdict.pop(selected_tab)
            children = list(tabdict.values())
    else:
        tabdict["Tab-1"] = [dcc.Tab(label="Tab 1", value="tab-1")]
        children = list(tabdict.values())

    return children

if __name__ == '__main__':
    app.run_server(debug=True)





