import argparse
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import macros

# use optional command line arg to toggle between local and remote server
# default to local
parser = argparse.ArgumentParser()
parser.add_argument('--remote', help='Run server remotely.  Otherwise, runs locally.', action='store_true')
args = parser.parse_args()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('bedtime', id='bedtime_button'),
    html.Div(className='divider'),
    html.Button('turn everything off', id='everything_off_button'),
    html.P(id='placeholder')
])


# external_css = ['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
#                 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']
#
# for css in external_css:
#     app.css.append_css({"external_url": css})


# tying a callback to a button requires testing n_clicks, passing if None, otherwise running a function,
# and then returning None.  click_button() generalizes this
def click_button(n_clicks, action):
    # callback executes on server startup unless use n_clicks filter
    if n_clicks is None:
        pass
    else:
        action()

# TODO: generalize this better.  Probably could use a dictinary that maps to a function or something so that each
# button button id maps to a specific function.  Or build my own class for this.


@app.callback(
    Output(component_id='placeholder', component_property='children'),
    [Input('bedtime_button', 'n_clicks')]
)
def bedtime_button_click(n_clicks, action=macros.bedtime):
    click_button(n_clicks, action)
    # callback forces an output, so returning None to placeholder paragraph
    return None


@app.callback(
    Output(component_id='placeholder', component_property='children'),
    [Input('everything_off_button', 'n_clicks')]
)
def everything_off_button_click(n_clicks, action=macros.turn_everything_off):
    click_button(n_clicks, action)
    # callback forces an output, so returning None to placeholder paragraph
    return None


if __name__ == '__main__':
    if args.remote:
        app.run_server(host='0.0.0.0')
    else:
        app.run_server()
