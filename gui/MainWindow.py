import datetime
import json
import pathlib
import sys
import time

from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QImageReader, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QFrame, QVBoxLayout, QSlider, \
    QLineEdit, QMessageBox, QPushButton, QFileDialog, QCheckBox, QProgressBar, QComboBox, QStyle
import numpy as np

from NeuralNet import NeuralNet
from GuiBuildBlocs import image_widget, text_button_widget


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Image app")
        self.target_img_path = '../files/cat.jpg'
        self.net = NeuralNet()

        self.init_main()
        self.create_menus()


    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()


    def openFileNameDialog(self, call_type):
        supportedFormats = QImageReader.supportedImageFormats()
        text_filter = "Images ({})".format(" ".join(["*.{}".format(fo.data().decode()) for fo in supportedFormats]))

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  filter = text_filter, options=options)
        if fileName:
            print(fileName)
            self.target_img_path = fileName
            self.image.setPixmap(QPixmap(fileName).scaled(256, 256))
            self.text_edit.setPlainText(f"Please, press predict button")
            

    def call_model(self):
        prediction = self.net.predict(self.target_img_path)
        self.text_edit.setPlainText(f"It's {prediction} on the picture!")
        
    def init_main(self):
        mainWigh = QFrame(self)
        hboxMain = QHBoxLayout()
        
        label_im, (_, self.image) = image_widget('Image', self.target_img_path)
        
        hboxMain.addWidget(label_im)
      
        label_txt, (self.text_edit, self.button) = text_button_widget('Predict', 'Hello')
        self.button.clicked.connect(lambda: self.call_model())
        hboxMain.addWidget(label_txt)
      
      
        mainWigh.setLayout(hboxMain)
        self.setCentralWidget(mainWigh)
        self.setMinimumSize(400, 200)

    def create_menus(self):
        '''Create the application menus.'''
        menubar = self.menuBar()

        # -- File Menu --
        fileMenu = menubar.addMenu('&File')
        # reaction = lambda: (self.target_img := self.openFileNameDialog(), self.img=self.target_img, self.slider_changed())
        open_target_files_action = fileMenu.addAction('&Image open',
                                                      lambda: self.openFileNameDialog(call_type='target'))
        open_target_files_action.setShortcut('Ctrl+I')


        exitAction = fileMenu.addAction('&Quit', self.close)
        exitAction.setShortcut('Ctrl+Q')

        # -- Edit Menu --
        # editMenu = menubar.addMenu('&Settings')
        # self.synchro_mode = editMenu.addAction('Synchronised slider',
                                            #    lambda: pass)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())