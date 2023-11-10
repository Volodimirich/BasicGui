import pathlib

import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QFrame, QVBoxLayout, QLabel, QHBoxLayout, QSlider, \
    QLineEdit, QComboBox, QCheckBox, QPlainTextEdit

def image_widget(text_message, img_path, text_size=None, is_3d=True, basic_size=(256, 256)):
    label = QFrame()
    vbox = QVBoxLayout()

    text = QLabel()
    text.setText(text_message)
    vbox.addWidget(text)

    lbl = QLabel()
    lbl.setPixmap(QPixmap(img_path).scaled(*basic_size))
    lbl.setAlignment(Qt.AlignTop)
    vbox.addWidget(lbl)

    label.setLayout(vbox)
    return label, (text, lbl,)

def text_button_widget(button_text, default_text=''):
    label = QFrame()
    vbox = QVBoxLayout()
    
    text_edit = QPlainTextEdit()
    text_edit.setPlainText(default_text)
    text_edit.setReadOnly(True)
    # text_edit.resize(100, 50)
    vbox.addWidget(text_edit)

    # Add button
    button = QPushButton(button_text)
    vbox.addWidget(button)
    label.setLayout(vbox)
    return label, (text_edit, button)