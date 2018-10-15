import harmony
import hue
import pc


def bedtime():
    harmony.turn_off_current_activity()
    hue.turn_off_all_lights()
    hue.turn_on_master_bedroom_night_scene()
    pc.remote_shutdown_desktop()


def turn_everything_off():
    harmony.turn_off_current_activity()
    hue.turn_off_all_lights()
    pc.remote_shutdown_desktop()
