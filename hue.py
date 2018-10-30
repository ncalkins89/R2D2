import requests
import json

# TODO: refactor first two functions below to use these configurations
ip = '192.168.0.2'
username = 'UCZMnJgAGzu5iDVeItDw03m3wU-YPspQtJvgyz0R'
api_root = 'http://{}/api/{}'.format(ip, username)

payloads = {
    'turn_on': json.dumps({'on': True}),
    'turn_off': json.dumps({'on': False})
}


def _endpoint(suffixes):
    return '/'.join([api_root] + suffixes)


def turn_off_all_lights():
    all_light_group = api_root + '/groups/0/action'
    requests.put(all_light_group, payloads['turn_off'])


def turn_on_scene(scene_id):
    # useful: https://stackoverflow.com/questions/16356810/string-format-a-json-string-gives-keyerror
    resp = requests.put(url='/'.join([api_root, 'groups', '0', 'action']), data=json.dumps(dict(scene=scene_id)))
    print(resp.content)


def turn_on_master_bedroom_night_scene():
    turn_on_scene(scene_id='i04J1E5ZO2ryl59')


def toggle_living_room():
    # if any living room lights are on, then turn them all off (living room is group 3)
    if requests.get(_endpoint(['groups', '3'])).json()['state']['any_on']:
        requests.put(_endpoint(['groups', '3', 'action']), payloads['turn_off'])
    else:
        requests.put(_endpoint(['groups', '3', 'action']), payloads['turn_on'])


# def turn_on_nightlight():
#     ip = '192.168.0.2'
#     username = 'UCZMnJgAGzu5iDVeItDw03m3wU-YPspQtJvgyz0R'
#     root = 'http://{}/api/{}/'.format(ip, username)
#     obj = 'lights'
#     url = root + obj
#     # light is number 8.  body contains desired settings
#     act = url + '/8/state'
#     body = \
#     '{' \
#     '"bri": 81,'\
#     '"hue": 63669,'\
#     '"on": true,'\
#     '"sat": 178,'\
#     '"xy": [0.6024, 0.3198]'\
#     '}'
#     resp = requests.put(act, body)
#     print(resp.content)
