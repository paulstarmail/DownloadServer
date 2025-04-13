#!/usr/bin/python3

import sys
import requests
import subprocess
from subprocess import check_output

FIREWALL_PORT = "30004"

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json()["ip"].strip()
        return ip
    except requests.RequestException as e:
        print("Error fetching IP:", e)
        return None

try:
    port = str(sys.argv[1])
except:
    port = "6004"
ip = check_output(['hostname', '--all-ip-addresses'])
ip = ip.decode("utf-8").strip()
print("Public URL: http://" + str(get_public_ip()) + ":" + FIREWALL_PORT)
print("Local URL: http://" + ip + ":" + port)
try:
    subprocess.run(["python3", "-m", "http.server", port], check=True)
except subprocess.CalledProcessError:
    print("\nERROR: The port " + port + " is in use by some other program.")
