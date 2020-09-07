#!/usr/bin/python3
#shitty tool by uhrenmacher. gpl v3
import socket
import sys

def help():
    print('Read the Readme....god damn')
if sys.argv[1].startswith("-help"):
    help()

def portscan():
    target = "uhrenmacher.onyx-7.de"
    targetIP = socket.gethostbyname(target)
    try:
        for p in range(1, 30):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("[*] Open port at  " + str(p))
            sock.close()
    except Exception:
        print("[*] Error")
        sys.exit()
    print("Scan completed in")

