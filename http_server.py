#!/usr/bin/python3

# The only argument is the desired port number.

import sys
import subprocess
from subprocess import check_output

port = str(sys.argv[1])
ip = check_output(['hostname', '--all-ip-addresses'])
ip = ip.decode("utf-8").strip()
print("URL: http://" + ip + ":" + port)
try:
	subprocess.run(["python3", "-m", "http.server", port], check=True)
except subprocess.CalledProcessError:
	print("\nERROR: Please try giving another port number.")
