import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input('button', 'n_clicks')]
)
def update_output_div(n_clicks):
    return 'You\'ve clicked {} times'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
