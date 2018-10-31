import subprocess


def remote_shutdown_desktop():
    subprocess.call("sudo net rpc shutdown -f -t 0 -C \'SHUTTIN THIS BIATCH DOWN! (via the Raspberry Pi)\' -U ncalk%Lateralus789 -I 192.168.0.20", shell=True)
