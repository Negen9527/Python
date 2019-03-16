#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2019/1/26 13:45
@Author  : Negen
@Site    : 
@File    : ChatClient.py
@Software: PyCharm
'''
import socket

import sys
from PyQt5 import QtCore
from socket import AF_INET
from socket import SOCK_STREAM

from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit

from threading import Thread

class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = socket.socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 6666))
        self.initUI()

    def initUI(self):
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)
        font = QFont()
        font.setPointSize(12)
        self.b = QPlainTextEdit(self)
        # self.b.setEnabled(False)
        self.b.setFont(font)
        self.b.move(0,20)
        self.b.resize(500, 200)

        self.edit = QLineEdit(self)
        self.edit.setFont(font)
        self.edit.move(50, 300)
        self.edit.resize(400, 50)
        self.btn = QPushButton("发送", self)
        self.btn.resize(150, 50)
        self.btn.move(175, 400)
        self.resize(500, 500)
        self.setWindowTitle('聊天窗')
        self.show()

    def clickHandel(self):
        inputs = self.edit.text()
        self.b.insertPlainText("your say：" + inputs + '\n')
        self.client.send(bytes(inputs, 'utf-8'))
        self.edit.setText("")
        self.b.moveCursor(QTextCursor.End)



    def showMsg(self):
        #显示收到得消息
        while True:
            receivedMsg = self.client.recv(1024).decode()
            if receivedMsg != "":
                self.b.insertPlainText(receivedMsg + '\n')



# client.send(bytes("你好啊", encoding="utf-8"))
# while True:
#     data = client.recv(1024).decode()
#     if data != "":
#         print(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainFrame()
    a.btn.clicked.connect(a.clickHandel)
    a.show()
    showMsgThread = Thread(target=a.showMsg, args=())
    showMsgThread.start()
    sys.exit(app.exec_())