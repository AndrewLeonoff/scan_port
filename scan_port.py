#!/usr/bin/python3

import socket
import threading

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        print(f'Port {port} is open')
        sock.close()
    except:
        pass

if __name__ == '__main__':
    host = input('Enter hostname: ')
    try:
        ip = socket.gethostbyname(host)
    except:
        print('Input error')
    else:
        for port in range(65536):
            thread = threading.Thread(target=scan_port, args=(ip, port))
            thread.start()