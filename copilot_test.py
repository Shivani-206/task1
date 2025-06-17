import os
import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse output for uptime
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime (since):", line.split("Statistics since")[-1].strip())
                    return
            print("Unable to determine uptime on Windows.")
        elif system == "Linux" or system == "Darwin":
            # Unix-like systems: use 'uptime -p'
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            print("System Uptime:", output.strip())
        else:
            print(f"Unsupported OS: {system}")
    except Exception as e:
        print(f"Error retrieving uptime: {e}")

if __name__ == "__main__":
    print_system_uptime()
