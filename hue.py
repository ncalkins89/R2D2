import requests


def turn_off_all_lights():
    turn_off = '{"on":false}'
    all_light_group = "http://192.168.0.2/api/UCZMnJgAGzu5iDVeItDw03m3wU-YPspQtJvgyz0R/groups/0/action"
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
