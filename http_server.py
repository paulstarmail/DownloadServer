import os
import socket

port = 8000

port = str(port)
hostname = socket.gethostname()
ip_address = str(socket.gethostbyname(hostname))
url = "URL: " + ip_address + ":" + port

print(url)
os.system("python -m http.server " + port)
