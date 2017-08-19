import sys
import os
import subprocess
from datetime import datetime, date, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from layout import Ui_Form
from shutil import copyfile, move
from stat import S_ISREG, ST_MTIME, ST_MODE
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

class Ui_Form_mod(Ui_Form):

    ########### INIT

    def initTimer(self, Form):
        #Camera
        self.camera = PiCamera()
        self.isLive = False

        #Countdown Updater
        self.timerCnt = QTimer(Form)
        self.timerCnt.timeout.connect(self.updateCountdown)
        self.timerCnt.setSingleShot(True)

        #Blank dummy image
        self.blankImage = QPixmap(1,1)

        self.lastPhoto = ""
        self.screen = ""
        self.temp = "/tmp/fotobox/"
        self.saved = "/media/usb0/"

        if not os.path.exists(self.temp):
            os.makedirs(self.temp)
        if not os.path.exists(self.saved):
            os.makedirs(self.saved)

    def patchDesign(self, Form):
        Form.setWindowTitle("Fotobox")
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.l_btn1.setFont(font)
        self.l_btn2.setFont(font)
        self.l_btn3.setFont(font)

        self.footerTpl = "Fotobox Version 0.0.2 · sponsored by: BitBastelei · Reichelt Elektronik"

        Form.showFullScreen()

    ########### MAIN
    def screenMain(self):
        self.screen = 1
        #Show instructions
        self.instructions.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hallo und willkommen in der Fotobox!</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier kannst du Fotos von dir und deinen Freunden machen!</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Drücke einfach auf den Knopf &quot;Neues Foto&quot; und los geht es!</p>"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du kannst du Fotos hier oder per Handy anschauen/runterladen: http://fotobox.ffmyk</p></body></html>")

        #Change buttons
        self.l_btn1.setText("Neues Foto ▶")
        self.l_btn2.setText("Fotobuch ▶")
        self.l_btn3.setText(" ")

        #start image update process
        if not self.isLive:
                self.image.setPixmap(self.blankImage)
                self.camera.start_preview(fullscreen=False, window = (0, 115, 960, 720))
                self.isLive = True

        #Reset footer
        self.label.setText(self.footerTpl)

    ########### CAPTURE

    def screenCapture(self):
        self.screen = 2
        #Change buttons
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.l_btn1.setFont(font)
        self.l_btn1.setText(" ")
        self.l_btn2.setText(" ")
        self.l_btn3.setText(" ")

        footer = self.footerTpl
        self.label.setText(footer)

        #start image update process
        if not self.isLive:
                self.image.setPixmap(self.blankImage)
                self.camera.start_preview(fullscreen=False, window = (0, 115, 960, 720))
                self.isLive = True

        #start countdown
        self.countdownTime = 4 #start at 3 seconds
        self.updateCountdown()

    #Countdown update
    def updateCountdown(self):
        self.countdownTime-=1 #I want my -- back :(

        instr = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:17pt; font-weight:400; font-style:normal; text-align: center;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Los geht's!</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:220pt; \">")
        instr += str(self.countdownTime)
        instr += "</p></body></html>"

        self.instructions.setHtml(instr)
        if(self.countdownTime > 0):
            self.timerCnt.start(1000)
        else:
            self.photoTake()

    #Take photo
    def photoTake(self):
        if(self.isLive):
                self.camera.stop_preview()
                self.isLive=False

        self.lastPhoto = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
        #@TODO Capture
        #copyfile(self.live, self.temp+self.lastPhoto)
        self.camera.capture(self.temp+self.lastPhoto)
        self.screenOK()

    def screenOK(self):
        self.screen = 3
        self.instructions.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alles OK?</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wenn ja drücke unten auf den passenden Knopf - dein Foto wird dann gespeichert und kann hier über das Fotobuch oder dein Handy angesehen werden.</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grimasse doch zu schlimm? Drück auf &quot;Neues Foto&quot; und versuchs gleich nochmal</p></body></html>")


        #Change buttons
        self.l_btn1.setText("Speichern ▶")
        self.l_btn2.setText("Neues Foto ▶")
        self.l_btn3.setText("Abbruch ▶")

        #last image
        pixmap = QPixmap(self.temp+self.lastPhoto)
        pixmapS = pixmap.scaledToWidth(950)
        self.image.setPixmap(pixmapS)

        footer = self.footerTpl
        footer += " · Foto: "
        footer += self.lastPhoto
        self.label.setText(footer)

    def tempDel(self):
        if self.lastPhoto != "" and os.path.isfile(self.temp+self.lastPhoto):
            os.remove(self.temp+self.lastPhoto)
            self.lastPhoto = ""

    def noConfirm(self):
        self.tempDel()
        self.screenMain()

    def doConfirm(self):
        move(self.temp+self.lastPhoto, self.saved+self.lastPhoto)
        self.screenMain()

    def retry(self):
        self.tempDel()
        self.screenCapture()

    ########### VIEWER
    def startViewer(self):
        self.screen = 4
        if(self.isLive):
                self.camera.stop_preview()
                self.isLive = False

        #@TODO find last photo
        self.entries = None
        self.entries = (os.path.join(self.saved, fn) for fn in os.listdir(self.saved))
        self.entries = ((os.stat(path), path) for path in self.entries)
        self.entries = ((stat[ST_MTIME], path)
                   for stat, path in self.entries if S_ISREG(stat[ST_MODE]))
        self.entries = list(self.entries)

        if(len(self.entries) > 0):
            self.viewerIndex = len(self.entries)-1
            self.screenViewer()
        else:
            self.screenMain()

    def screenViewer(self):

        self.instructions.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier sind die letzten Fotos der Veranstaltung</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mit den Knöpfen unten kannst du dir andere Bilder anschauen oder zurück zur Aufnahme gehen.</p>\n"
"<hr>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du kannst du Fotos hier oder per Handy anschauen/runterladen:<br>http://fotobox.ffmyk</p></body></html>")


        #Change buttons
        if(self.viewerIndex < (len(self.entries)-1)):
            self.l_btn1.setText("Nächstes ▶")
        else:
            self.l_btn1.setText(" ")
        if(self.viewerIndex > 0):
            self.l_btn2.setText("Letztes ▶")
        else:
            self.l_btn2.setText(" ")
        self.l_btn3.setText("Zurück ▶")

        #last image
        pixmap = QPixmap(str(self.entries[self.viewerIndex][1]))
        pixmapS = pixmap.scaledToWidth(950)
        self.image.setPixmap(pixmapS)

        footer = self.footerTpl
        footer += " · Foto: "
        footer += str(self.viewerIndex+1)
        footer += " von "
        footer += str(len(self.entries))
        footer += " · "
        footer += str(self.entries[self.viewerIndex][1])
        self.label.setText(footer)
    def viewPrev(self):
        print(self.viewerIndex)
        if(self.viewerIndex > 0):
            self.viewerIndex -= 1
        self.screenViewer()

    def viewNext(self):
        print(str((len(self.entries)-1)))
        print(self.viewerIndex)
        if(self.viewerIndex < (len(self.entries)-1)):
            self.viewerIndex += 1
        self.screenViewer()

class QDialog_mod(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = Ui_Form_mod()
        self.ui.setupUi(self)
        self.ui.initTimer(self)
        self.ui.patchDesign(self)
        self.ui.screenMain()

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(25, GPIO.OUT)

        self.btnC1 = GPIO.HIGH
        self.btnC2 = GPIO.HIGH
        self.btnC3 = GPIO.HIGH
        self.btnB  = 1

        #Key Poller
        self.timerKey = QTimer(self)
        self.timerKey.timeout.connect(self.buttonCheck)
        self.timerKey.start(25)

        self.show()

    def buttonCheck(self):
        if self.btnB == 0:
            if GPIO.input(17) != self.btnC1:
                self.btnB =3
                if GPIO.input(17) == GPIO.LOW:
                    self.buttonPress(1)
                self.btnC1 = GPIO.input(17)
            if GPIO.input(21) != self.btnC2:
                self.btnB = 3
                if GPIO.input(21) == GPIO.LOW:
                    self.buttonPress(2)
                self.btnC2 = GPIO.input(21)
            if GPIO.input(22) != self.btnC3:
                self.btnB = 3
                if GPIO.input(22) == GPIO.LOW:
                    self.buttonPress(3)
                self.btnC3 = GPIO.input(22)
        else:
            self.btnB -= 1

    #keyHandling
    def buttonPress(self, btn):
        if(self.ui.screen == 1):
            if(btn == 1):
                self.ui.screenCapture()
            elif(btn == 2):
                self.ui.startViewer()
        elif(self.ui.screen == 3):
            if(btn == 1):
                self.ui.doConfirm()
            elif(btn == 2):
                self.ui.retry()
            elif(btn == 3):
                self.ui.noConfirm()
        elif(self.ui.screen == 4):
            if(btn == 1):
                self.ui.viewNext()
            elif(btn == 2):
                self.ui.viewPrev()
            elif(btn == 3):
                self.ui.screenMain()

    #Emulation
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif e.key() == QtCore.Qt.Key_Q: #gimme switch/case -.-
            self.ui.screenMain()
        elif e.key() == QtCore.Qt.Key_W: #gimme switch/case -.-
            self.ui.screenCapture()
        elif e.key() == QtCore.Qt.Key_E: #@TODO viewer
            self.ui.startViewer()
        elif e.key() == QtCore.Qt.Key_Y: #@TODO save
            self.ui.doConfirm()
        elif e.key() == QtCore.Qt.Key_N: #@TODO abort
            self.ui.noConfirm()
        elif e.key() == QtCore.Qt.Key_R: #@TODO retry
            self.ui.retry()
        elif e.key() == QtCore.Qt.Key_K: #Left/Right is not passed
            self.ui.viewPrev()
        elif e.key() == QtCore.Qt.Key_L:
            self.ui.viewNext()
        elif e.key() == QtCore.Qt.Key_1:
            self.buttonPress(1)
        elif e.key() == QtCore.Qt.Key_2:
            self.buttonPress(2)
        elif e.key() == QtCore.Qt.Key_3:
            self.buttonPress(3)


app = QApplication(sys.argv)
window = QDialog_mod()

sys.exit(app.exec_())
