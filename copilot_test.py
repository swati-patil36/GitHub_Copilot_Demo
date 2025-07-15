import platform
import subprocess
import sys

def get_uptime():
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime:", line.strip())
                    return
            print("Uptime info not found.")
        except Exception as e:
            print("Error getting uptime on Windows:", e)
    elif platform.system() == "Linux":
        try:
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            print("System Uptime:", output.strip())
        except Exception as e:
            print("Error getting uptime on Linux:", e)
    else:
        print("Unsupported OS:", platform.system())

if __name__ == "__main__":
    get_uptime()
