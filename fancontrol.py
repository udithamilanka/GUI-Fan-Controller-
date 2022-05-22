from PyQt5 import QtCore, QtGui, QtWidgets
import os
import os.path
from pathlib import Path
import time

configpath = str(Path.home()) + '/.fanctrl'
fanctrl1 = str(Path.home()) + '/.fanctrl1'
fanctrl2 = str(Path.home()) + '/.fanctrl2'

if os.path.isfile(configpath)==True:
    f = open(configpath, "r")
    command = f.read()
    f.close() 
else:
    f = open(configpath, "w")
    f.write("mono /opt/nbfc/nbfc.exe set")
    f.close()
    f = open(configpath2, "w")
    f.write(0,0)
    f.close()
    command = "mono /opt/nbfc/nbfc.exe set"

f = open(fanctrl1, "w")
f.write("0")
f.close()
f = open(fanctrl2, "w")
f.write("0")
f.close()


class Ui_Fan(object):
    def setupUi(self, Fan):
        Fan.setObjectName("Fan")
        Fan.resize(503, 440)
        self.centralwidget = QtWidgets.QWidget(Fan)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Z003")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Z003")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(200, 70, 261, 21))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(200, 140, 261, 21))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 40, 58, 18))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 40, 58, 18))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(40, 10, 171, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(20)
        font.setItalic(True)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 240, 261, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(20)
        font.setItalic(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 290, 351, 24))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(20)
        font.setItalic(True)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 300, 16, 18))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(1)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        Fan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 23))
        self.menubar.setObjectName("menubar")
        Fan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fan)
        self.statusbar.setObjectName("statusbar")
        Fan.setStatusBar(self.statusbar)

        self.retranslateUi(Fan)
        QtCore.QMetaObject.connectSlotsByName(Fan)

        # Set Button States
        self.radioButton1.toggled.connect(lambda:self.btnstate(self.radioButton1))
        self.radioButton_2.toggled.connect(lambda:self.btnstate(self.radioButton_2))
        self.radioButton_3.toggled.connect(lambda:self.btnstate(self.radioButton_3))
        self.horizontalSlider.valueChanged[int].connect(self.changeValue1)
        self.horizontalSlider_2.valueChanged[int].connect(self.changeValue2)
        self.pushButton.clicked.connect(self.button_clicked)
        


    def retranslateUi(self, Fan):
        _translate = QtCore.QCoreApplication.translate
        Fan.setWindowTitle(_translate("Fan", "MainWindow"))
        self.label.setText(_translate("Fan", "CPU"))
        self.label_2.setText(_translate("Fan", "GPU"))
        self.label_3.setText(_translate("Fan", "0 %"))
        self.label_4.setText(_translate("Fan", "100 %"))
        self.radioButton1.setText(_translate("Fan", "Set Manually"))
        self.radioButton_2.setText(_translate("Fan", "Set Automatically"))
        self.radioButton_2.setStatusTip(_translate("Fan", "Will take some time to change fan speed"))
        self.radioButton_3.setText(_translate("Fan", "Fans Go Brrrrrrrrrrrrrrrr"))
        self.pushButton.setStatusTip(_translate("Fan", "Open config file using nano.(Or change .fanctrl @Home directory manually)"))
        self.pushButton.setText(_translate("Fan", "Config"))
        self.label_5.setText(_translate("Fan", "CrazzyUMP"))


    def changeValue1(self, value):
        newcommand = command + ' -a'
        os.system(newcommand)
        self.radioButton1.setChecked(True)
        fan1 = str(int(value)+1)
        newcommand = command + ' -f 0 -s ' + fan1
        os.system(newcommand)
        f = open(fanctrl1, "w")
        f.write(fan1)
        f.close()
    

    def changeValue2(self, value):
        newcommand = command + ' -a'
        os.system(newcommand)
        self.radioButton1.setChecked(True)
        fan2 = str(int(value)+1)
        newcommand = command + ' -f 1 -s ' + fan2
        os.system(newcommand)
        f = open(fanctrl2, "w")
        f.write(fan2)
        f.close()


    def btnstate(self, b):
        if b.isChecked():
            if b.text() == "Fans Go Brrrrrrrrrrrrrrrr":
                newcommand = command + ' -s 100'
                os.system(newcommand)

            elif b.text() == "Set Automatically":
                newcommand = command + ' -f 0 -s 0'
                os.system(newcommand)
                newcommand = command + ' -f 1 -s 0'
                os.system(newcommand)
                newcommand = command + ' -a'
                os.system(newcommand)
            else:
                newcommand = command + ' -a'
                os.system(newcommand)
                f = open(fanctrl1, "r")
                newcommand = command + ' -f 1 -s ' + f.read()
                f.close()
                os.system(newcommand)
                f = open(fanctrl2, "r")
                newcommand = command + ' -f 1 -s ' + f.read()
                f.close()
                os.system(newcommand)

    def button_clicked(self):
        newcommand  = 'nano '+ configpath
        os.system(newcommand)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fan = QtWidgets.QMainWindow()
    ui = Ui_Fan()
    ui.setupUi(Fan)
    Fan.show()
    sys.exit(app.exec_())
