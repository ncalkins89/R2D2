import harmony
import hue
import pc


def bedtime():
    harmony.turn_off_current_activity()
    hue.turn_off_all_lights()
    hue.turn_on_nightlight()
    pc.remote_shutdown_desktop()
