Experience Using GitHub Copilot
What code did Copilot generate?
Copilot generated a Python script to print the system uptime in the file copilot_test.py. The script works on both Linux and Windows systems, automatically detecting the OS and using the appropriate command to display the uptime.

Generated Script Example:

Python
import platform
import subprocess

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
Did you modify the script? If so, why?
Yes, I made the following modifications:

Ensured compatibility for both Windows and Linux by checking the operating system.
Added error handling to provide clear feedback if the uptime command fails.
Used subprocess.check_output() with text=True for direct string handling in Python 3.
These changes were made to improve robustness and usability across different platforms.

How did you test it?
I tested the script by running it on both Windows and Linux machines:

On Linux, it correctly displayed the uptime using the uptime -p command.
On Windows, it parsed the output of net stats srv and printed the uptime since last boot.
How to Run the Script
To run the script, make sure you have Python installed (Python 3.6 or newer recommended).

Open a terminal or command prompt.
Navigate to the repository directory.
Run the script with:
bash
python copilot_test.py
The script will automatically detect your operating system and print the system uptime.
