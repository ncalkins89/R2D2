import requests
import json

# TODO: refactor first two functions below to use these configurations
ip = '192.168.0.2'
username = 'UCZMnJgAGzu5iDVeItDw03m3wU-YPspQtJvgyz0R'
api_root = 'http://{}/api/{}'.format(ip, username)


def turn_off_all_lights():
    turn_off = '{"on":false}'
    all_light_group = api_root + '/groups/0/action'
    requests.put(all_light_group, turn_off)


def turn_on_nightlight():
    ip = '192.168.0.2'
    username = 'UCZMnJgAGzu5iDVeItDw03m3wU-YPspQtJvgyz0R'
    root = 'http://{}/api/{}/'.format(ip, username)
    obj = 'lights'
    url = root + obj
    # light is number 8.  body contains desired settings
    act = url + '/8/state'
    body = \
    '{' \
    '"bri": 81,'\
    '"hue": 63669,'\
    '"on": true,'\
    '"sat": 178,'\
    '"xy": [0.6024, 0.3198]'\
    '}'
    resp = requests.put(act, body)
    print(resp.content)


def turn_on_scene(scene_id):
    # useful: https://stackoverflow.com/questions/16356810/string-format-a-json-string-gives-keyerror
    resp = requests.put(url='/'.join([api_root, 'groups', '0', 'action']), data=json.dumps(dict(scene=scene_id)))
    print(resp.content)


def turn_on_master_bedroom_night_scene():
    turn_on_scene(scene_id='i04J1E5ZO2ryl59')
