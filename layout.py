# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 1024)
        Form.setMinimumSize(QtCore.QSize(1280, 1024))
        Form.setMaximumSize(QtCore.QSize(1280, 1024))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.master = QtWidgets.QVBoxLayout()
        self.master.setObjectName("master")
        self.l_Header = QtWidgets.QLabel(Form)
        self.l_Header.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.l_Header.setFont(font)
        self.l_Header.setAlignment(QtCore.Qt.AlignCenter)
        self.l_Header.setObjectName("l_Header")
        self.master.addWidget(self.l_Header)
        self.mid = QtWidgets.QHBoxLayout()
        self.mid.setObjectName("mid")
        self.image = QtWidgets.QLabel(Form)
        self.image.setMinimumSize(QtCore.QSize(950, 0))
        self.image.setObjectName("image")
        self.mid.addWidget(self.image)
        self.sidebar = QtWidgets.QVBoxLayout()
        self.sidebar.setObjectName("sidebar")
        self.instructions = QtWidgets.QTextBrowser(Form)
        self.instructions.setMaximumSize(QtCore.QSize(300, 400))
        self.instructions.setObjectName("instructions")
        self.sidebar.addWidget(self.instructions)
        self.l_btn1 = QtWidgets.QLabel(Form)
        self.l_btn1.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.l_btn1.setFont(font)
        self.l_btn1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_btn1.setObjectName("l_btn1")
        self.sidebar.addWidget(self.l_btn1)
        self.l_btn2 = QtWidgets.QLabel(Form)
        self.l_btn2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.l_btn2.setFont(font)
        self.l_btn2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_btn2.setObjectName("l_btn2")
        self.sidebar.addWidget(self.l_btn2)
        self.l_btn3 = QtWidgets.QLabel(Form)
        self.l_btn3.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.l_btn3.setFont(font)
        self.l_btn3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_btn3.setObjectName("l_btn3")
        self.sidebar.addWidget(self.l_btn3)
        self.mid.addLayout(self.sidebar)
        self.master.addLayout(self.mid)
        self.footer = QtWidgets.QHBoxLayout()
        self.footer.setObjectName("footer")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.footer.addWidget(self.label)
        self.master.addLayout(self.footer)
        self.verticalLayout.addLayout(self.master)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l_Header.setText(_translate("Form", "Fotobox"))
        self.instructions.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hallo und Willkommen in der Fotobox!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier kannst du Fotos von dir und deinen Freunden machen!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Drücke einfach auf den Knopf &quot;Neues Foto&quot; und los geht es!</p></body></html>"))
        self.l_btn1.setText(_translate("Form", "Button 1 ▶"))
        self.l_btn2.setText(_translate("Form", "Button 2 ▶"))
        self.l_btn3.setText(_translate("Form", "Button 3 ▶"))
        self.label.setText(_translate("Form", "Fotobox Version 0.0.1"))

