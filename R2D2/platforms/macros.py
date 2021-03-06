from R2D2.platforms import hue, tplink, harmony, pc


def turn_everything_off():
    harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    tplink.backyard.turn_off()
    hue.turn_off_all_lights()
    pc.remote_shutdown_desktop()

def bedtime():
    # need to fix harmony api with firmware update 
    # harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    tplink.backyard.turn_off()
    # liv room off, kitchen off, front porch on 
    # later: turn off pc, when fixed
    hue.turn_on_master_bedroom_nightlight()


def home_theater_on():
    harmony.home_theater_on()
    tplink.subwoofer.turn_on()
    # TODO: add WOL after adding ethernet cable, or figuring out wireless


def home_theater_off():
    harmony.turn_off_current_activity()
    tplink.subwoofer.turn_off()
    pc.remote_shutdown_desktop()
