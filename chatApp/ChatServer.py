#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2019/1/26 13:39
@Author  : Negen
@Site    : 
@File    : ChatServer.py
@Software: PyCharm
'''
import socket
from socket import AF_INET
from socket import SOCK_STREAM
server = socket.socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 6666))
server.listen(5)
print("server started")
allClient = set()
while True:
    conn, addr = server.accept()
    print("connect establish ：", conn, addr)
    if conn not in allClient:
        allClient.add(conn)
    data = conn.recv(1024).decode()
    print(allClient)
    if data is not None:
        print("from", addr, "recve msg：", data)
        for client in allClient:
            if conn != client:
                client.send(bytes(addr[0] + ":" + str(addr[1]) + " say：" + data, 'utf-8'))
