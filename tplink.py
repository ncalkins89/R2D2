from pyHS100 import Discover
from pyHS100 import SmartPlug


# discover plugs
# for dev in Discover.discover().values():
#     print(dev)


# check if a plug is on or off
# subwoofer.state

subwoofer = SmartPlug('192.168.0.23')


def toggle_plug_state(plug):
    if plug.state == 'ON':
        plug.turn_off()
    elif plug.state == 'OFF':
        plug.turn_on()


def toggle_subwoofer():
    toggle_plug_state(subwoofer)