"""Common TCP Ports
23 - Telnet - login
25 - SMTP - email
80 - HTTP - web
110 - POP3 - email
143 - IMAP - email
443 - HTTPS - secure web
465 - SMTPS - secure email
993 - IMAPS - secure email
995 - POP3S - secure email
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysock.close()

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

