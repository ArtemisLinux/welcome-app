## Artemis OS Welcome
## Maintained by: Frazer Grant
## Version: 0.1



## Modules to import ##
import sys
import subprocess
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPlainTextEdit, QCheckBox
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtGui import *
import os
import sys





## Main Window ##
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("welcome.ui", self)
        width = 640
        height = 480
        self.setFixedSize(width, height)
        self.p = QProcess() 

## Buttons ##
        self.output = QPlainTextEdit(self.output1)
        self.output.setReadOnly(True)
        self.close.clicked.connect(QCoreApplication.instance().quit)
        self.website.clicked.connect(self.openwebsite)
        self.github.clicked.connect(self.githubopen)
        self.update.clicked.connect(self.updatesys)
        self.pacfix.clicked.connect(self.gpgfix)
        self.clearbox.clicked.connect(self.clearmsgbox)
        self.autostart.stateChanged.connect(self.clickBox)





## Definitions ## 
    def openwebsite(self):
        subprocess.run(["xdg-open", "https://artemislinux.github.io/"])
    
    def githubopen(self):
        subprocess.run(["xdg-open", "https://github.com/ArtemisLinux"])

    def message(self, s):
        self.output.appendPlainText(s)

    def updatesys(self):
        self.p.start("kitty", ["update"])
        self.message("Updating system, Please wait...")
        self.p.finished.connect(self.process_finished)  # Clean up once complete.


    def gpgfix(self):
        self.p.start("kitty", ["gpgfix"])
        self.p.finished.connect(self.process_finished)  # Clean up once complete.
        self.message("Updating GPG")



    def process_finished(self):
        self.message("Process finished.")
        #self.p = None

    def clearmsgbox(self):
        self.output.clear() 


    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
         self.p.start("bash", ['./autostart_enable'])
        else:
         self.p.start("bash", ['./autostart_disable'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setDesktopFileName("artemisos-welcome-app")    #
    ui = MainUI()
    ui.show()
    app.exec_()




