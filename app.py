import dash
from dash.dependencies import Input, Output
import dash_html_components as html
from macros import bedtime

app = dash.Dash()

app.layout = html.Div([
    html.Button('bedtime', id='bedtime_button'),
    html.Div(id='my-div'),
    html.P(id='placeholder')
])


@app.callback(
    Output(component_id='placeholder', component_property='children'),
    [Input('bedtime_button', 'n_clicks')]
)
def update_output_div(n_clicks):
    # callback executes on server startup unless use n_clicks filter
    if n_clicks is None:
        pass
    else:
        bedtime()
    # callback forces an output, so returning None to placeholder paragraph
    return None


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
    # app.run_server()
