import argparse
from collections import OrderedDict

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

from R2D2.platforms import tplink, hue, pc
from R2D2.platforms.macros import bedtime, turn_everything_off, home_theater_on, home_theater_off


# configure buttons.  id to name and action
button_config = OrderedDict([
    ('bedtime_button', {
        'name': 'Bedtime',
        'className': 'macro_button',
        'action': bedtime
    }),
    ('everything_off_button', {
        'name': 'House: Off',
        'className': 'off_button',
        'action': turn_everything_off
    }),
    ('toggle_subwoofer_button', {
        'name': 'Subwoofer: On/Off',
        'className': 'toggle_button',
        'action': tplink.toggle_subwoofer
    }),
    ('home_theater_on_button', {
        'name': 'Home Theater: On',
        'className': 'on_button',
        'action': home_theater_on
    }),
    ('home_theater_off_button', {
        'name': 'Home Theater: Off',
        'className': 'off_button',
        'action': home_theater_off
    })
    ,
    ('pc_off_button', {
        'name': 'PC: Off',
        'className': 'off_button',
        'action': pc.remote_shutdown_desktop
    })
    ,
    ('house_nightlight_button', {
        'name': 'House Nightlight: On',
        'className': 'on_button',
        'action': hue.turn_on_house_nightlight
    })
])

# add placeholders for output components
for (i, (k, v)) in enumerate(button_config.items()):
    v['output_component_id'] = 'placeholder' + str(i)

# use optional command line arg to toggle between local and remote server.  default to local
parser = argparse.ArgumentParser()
parser.add_argument('--remote', help='Run server remotely.  Otherwise, runs locally.', action='store_true')
args = parser.parse_args()

app = dash.Dash(__name__)

# layout part 1: the buttons, each in its own paragraph
button_layout = [html.P(html.Button(v['name'], id=k, className=v['className'])) for (k, v) in button_config.items()]
# layout part 2: placeholders...apparently need one for each callback even if output not needed
placeholder_layout = [html.P(id=v['output_component_id']) for k, v in button_config.items()]
# combine
app.layout = html.Div(button_layout + placeholder_layout)

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


# to create dynamic callbacks.
# see: https://stackoverflow.com/questions/13184281/python-dynamic-function-creation-with-custom-names
def create_callback(button_id, attributes):
    @app.callback(
        Output(component_id=attributes['output_component_id'], component_property='children'),
        [Input(button_id, 'n_clicks')]
    )
    def new_callback(n_clicks, action=attributes['action']):
        click_button(n_clicks, action)
        # callback forces an output, so returning None to placeholder paragraph
        return None
    new_callback.__name__ = button_id + '_click'

    return new_callback


for (k, v) in button_config.items():
    callback = create_callback(button_id=k, attributes=v)


if __name__ == '__main__':
    if args.remote:
        app.run_server(host='0.0.0.0')
    else:
        app.run_server()
