import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import lib.macros.bedtime as bedtime

app = dash.Dash()

app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.Div(id='my-div'),
    html.P(id='placeholder')
])


@app.callback(
    Output(component_id='placeholder', component_property='children'),
    [Input('button', 'n_clicks')]
)
def update_output_div(n_clicks):
    bedtime()
    return None


if __name__ == '__main__':
    # app.run_server(host='0.0.0.0')
    app.run_server()
