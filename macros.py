import harmony
import hue
import pc
import tplink


def turn_everything_off():
    harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    hue.turn_off_all_lights()
    pc.remote_shutdown_desktop()


def bedtime():
    turn_everything_off()
    hue.turn_on_nightlight()
