import subprocess
import random
import platform


def ping_test():
    websites = ["google.com", "localhost"]
    website = random.choice(websites)
    system = platform.system()

    if system == "Windows":
        subprocess.Popen(["cmd", "/c", f"start cmd.exe /k ping {website}"])

    elif system == "Linux":
        subprocess.Popen(["gnome-terminal", "--", "ping", website])
