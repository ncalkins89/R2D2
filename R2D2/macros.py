import hue
import tplink

from R2D2.platforms import harmony, pc


def turn_everything_off():
    harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    hue.turn_off_all_lights()
    pc.remote_shutdown_desktop()


def bedtime():
    turn_everything_off()
    hue.turn_on_master_bedroom_night_scene()


def home_theater_on():
    harmony.home_theater_on()
    tplink.subwoofer.turn_on()
    # TODO: add WOL after adding ethernet cable, or figuring out wireless


def home_theater_off():
    harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    pc.remote_shutdown_desktop()