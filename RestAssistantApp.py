#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2019/2/28 14:02
@Author  : Negen
@Site    :
@File    : RestAssistantApp.py
@Software: PyCharm
'''
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QColor, QPalette
class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.WindowMinimizeButtonHint)
        font = QFont()
        font.setPointSize(16)
        self.timeLabel = QLabel(self)
        self.timeLabel.setFont(font)
        self.timeLabel.resize(300, 30)
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

        self.label = QLabel("输入休息间隔时长（M）", self)
        self.label.setFont(font)
        self.label.move(50, 50)
        self.label.resize(250, 30)
        self.edit = QLineEdit(self)
        self.edit.setFont(font)
        self.edit.move(125, 95)
        self.edit.resize(50, 30)
        self.btn = QPushButton("确认", self)
        self.btn.resize(150, 30)
        self.btn.move(75, 150)
        self.resize(300, 200)
        self.setWindowTitle('护眼助手')
        self.show()

    """
    实时显示时间
    """
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        timeText = datetime.toString()
        self.timeLabel.setText(" " + timeText)

    def clickHandel(self):
        try:
            minutes = int(self.edit.text())
            self.close()
            self.littleFrame = LittleFrame(minutes)
            self.littleFrame.show()
        except Exception as e:
            QMessageBox.information(self, "提示", "请输入整数")


class LittleFrame(QMainWindow):
    def __init__(self,minutes):
        super().__init__()
        self.initUI()
        self.minutes = minutes
        self.second = minutes * 60

    def initUI(self):
        self.desktop = QApplication.desktop()
        # 获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry(self.width*0.85, self.height*0.8, 250, 80)
        # self.setFixedSize(self.width*0.9, self.height*0.9)
        #禁用最大化按钮  #置顶
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('护眼助手运行中...')
        font = QFont()
        font.setPointSize(16)
        self.timeLabel = QLabel(self)
        self.timeLabel.setFont(font)
        self.timeLabel.move(40,15)
        self.timeLabel.resize(250,50)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showtime)
        self.timer.start()

    """
    实时显示时间
    """
    def showtime(self):
        if self.second == 0:
            self.close()
            self.restFrame = RestFrame()
            self.restFrame.setStyleSheet("#MainWindow{background-color: yellow}")
            self.restFrame.show()

        self.timeLabel.setText(str(self.second).zfill(2) + "秒后休息哦")
        self.second -= 1


class RestFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.desktop = QApplication.desktop()
        # 获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry(self.width*0.05, self.height*0.05, self.width*0.9, self.height*0.9)
        # self.setFixedSize(self.width*0.9, self.height*0.9)
        #禁用最大化按钮  #置顶
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("#MainWindow{background-color: yellow}")
        font = QFont()
        font.setPointSize(80)
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("休息中哦...")
        self.titleLabel.resize(self.width,self.height/2)
        self.titleLabel.move(self.width*0.3, self.height*0.3)
        self.titleLabel.setFont(font)
        self.setWindowTitle('休息中...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = MainFrame()
    a.show()
    a.btn.clicked.connect(a.clickHandel)
    sys.exit(app.exec_())
