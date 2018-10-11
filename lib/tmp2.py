import requests
import json
import subprocess

# TODO: store functions, especially subprocess functions, as text files


def do_something():

    # turn on bedroom nightlight
    turn_on_nightlight()
    # shut down pc
    remote_shutdown_desktop()
    # power off harmony activity
    subprocess.call(['bash', r'/home/pi/HomeAutomation/harmonyhub/harmony_power_off.sh'])
