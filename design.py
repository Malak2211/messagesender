# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designnn.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtMultimedia,QtCore, QtGui, QtWidgets 
from PyQt5.QtMultimedia import QMediaRecorder,QMediaPlayer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(66, 20, 61, 21))
        self.namelabel.setObjectName("namelabel")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(510, 360, 101, 20))
        self.radioButton.setObjectName("radioButton")
        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(140, 20, 381, 20))
        self.namebox.setObjectName("namebox")
        self.messagebox = QtWidgets.QLineEdit(self.centralwidget)
        self.messagebox.setGeometry(QtCore.QRect(20, 360, 401, 20))
        self.messagebox.setObjectName("messagebox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 49, 591, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.namelabel.setText(_translate("MainWindow", "Enter name"))
        self.radioButton.setText(_translate("MainWindow", "click to record"))
        self.messagebox.setPlaceholderText(_translate("MainWindow", "Message"))
        self.pushButton.setText(_translate("MainWindow", "Send"))

import PyQt5.QtWidgets as qtw
from design import Ui_MainWindow

class Main_window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_message)
        self.recording=False #initialize recording state
        self.media_player = QtMultimedia.QMediaPlayer(self)#creating a media player
        self.recorder=QtMultimedia.QMediaRecorder(self.media_player) #place audio recorder setup with media
        self.radioButton.toggled.connect(self.checkrecording) #connect radiobutton to checkrecording function to see if it will start or stop recorder button 

    def send_message(self):
        name=self.namebox.text()
        msg=self.messagebox.text()
        text=f'{name}:{msg}'
        message=qtw.QLabel()
        message.setText(text)
        self.verticalLayout.addWidget(message)
    def checkrecording(self,clicked):
        if clicked:
            self.startrecording()
        else:
            self.stoprecording
    def stoprecording(self):
        self.recorder.stop()
        self.recording = False
        self.radioButton.setText("Start Recording") 
    def startrecording(self):
        self.recorder.record()
        self.recording = True  
        self.radioButton.setText("Stop Recording") 
    
app=qtw.QApplication([])
application_window=Main_window()
application_window.show()
app.exec_()

