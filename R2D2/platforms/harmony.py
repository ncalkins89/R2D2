import subprocess

# dependent on pyharmony program being installed, so only works on linux at the moment:

# /home/pi/miniconda3/bin/harmony
# /home/pi/miniconda3/bin/harmony --harmony_ip "192.168.0.4" power_off


def turn_off_current_activity():
    subprocess.call(['bash', r'/home/pi/HomeAutomation/harmonyhub/harmony_power_off.sh'])


def home_theater_on():
    subprocess.call(['bash', r'/home/pi/HomeAutomation/harmonyhub/harmony_home_theater_on.sh'])
