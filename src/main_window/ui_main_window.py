# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(721, 799)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.526882, y1:1, x2:0.537634, y2:0, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(151, 151, 151, 255));")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"QFrame { \n"
"background: rgba(91, 92, 92, 100);\n"
"border: 3px solid black;\n"
"margin: 50px;\n"
"}\n"
"\n"
"QLabel {\n"
"color: #000;\n"
"letter-spacing: 2px;\n"
"background: none;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.main_frame)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QSize(16777215, 160))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(40)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"border: none;\n"
"margin: none;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.morse_buttons_frame = QFrame(self.main_frame)
        self.morse_buttons_frame.setObjectName(u"morse_buttons_frame")
        sizePolicy.setHeightForWidth(self.morse_buttons_frame.sizePolicy().hasHeightForWidth())
        self.morse_buttons_frame.setSizePolicy(sizePolicy)
        self.morse_buttons_frame.setStyleSheet(u"border: none;\n"
"background: none;\n"
"margin: 0px;")
        self.morse_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.morse_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.morse_buttons_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.encoder_button = QPushButton(self.morse_buttons_frame)
        self.encoder_button.setObjectName(u"encoder_button")
        self.encoder_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encoder_button.setStyleSheet(u"background: none;\n"
"letter-spacing: 2px;\n"
"color: #000;\n"
"border: 3px solid;\n"
"height: 35px;")

        self.horizontalLayout_2.addWidget(self.encoder_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.decoder_button = QPushButton(self.morse_buttons_frame)
        self.decoder_button.setObjectName(u"decoder_button")
        self.decoder_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decoder_button.setStyleSheet(u"background: none;\n"
"letter-spacing: 2px;\n"
"color: #000;\n"
"border: 3px solid;\n"
"height: 35px;")

        self.horizontalLayout_2.addWidget(self.decoder_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.morse_buttons_frame)

        self.decoded_frame = QFrame(self.main_frame)
        self.decoded_frame.setObjectName(u"decoded_frame")
        sizePolicy.setHeightForWidth(self.decoded_frame.sizePolicy().hasHeightForWidth())
        self.decoded_frame.setSizePolicy(sizePolicy)
        self.decoded_frame.setStyleSheet(u"border: none;\n"
"background: none;\n"
"margin: 0px;")
        self.decoded_frame.setFrameShape(QFrame.StyledPanel)
        self.decoded_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.decoded_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.decode_message_frame = QFrame(self.decoded_frame)
        self.decode_message_frame.setObjectName(u"decode_message_frame")
        self.decode_message_frame.setStyleSheet(u"margin: 0px;\n"
"border: 0px;\n"
"background: none;")
        self.decode_message_frame.setFrameShape(QFrame.StyledPanel)
        self.decode_message_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.decode_message_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.decoded_message = QLabel(self.decode_message_frame)
        self.decoded_message.setObjectName(u"decoded_message")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(20)
        self.decoded_message.setFont(font1)
        self.decoded_message.setStyleSheet(u"background: none;")
        self.decoded_message.setAlignment(Qt.AlignCenter)
        self.decoded_message.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.decoded_message)

        self.copy_decode_message_button = QPushButton(self.decode_message_frame)
        self.copy_decode_message_button.setObjectName(u"copy_decode_message_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.copy_decode_message_button.sizePolicy().hasHeightForWidth())
        self.copy_decode_message_button.setSizePolicy(sizePolicy1)
        self.copy_decode_message_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/src/main_window/images/copyIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_decode_message_button.setIcon(icon)
        self.copy_decode_message_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.copy_decode_message_button)


        self.verticalLayout_3.addWidget(self.decode_message_frame)

        self.decode_input_frame = QFrame(self.decoded_frame)
        self.decode_input_frame.setObjectName(u"decode_input_frame")
        self.decode_input_frame.setFrameShape(QFrame.StyledPanel)
        self.decode_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.decode_input_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.decode_input_label = QLabel(self.decode_input_frame)
        self.decode_input_label.setObjectName(u"decode_input_label")
        sizePolicy.setHeightForWidth(self.decode_input_label.sizePolicy().hasHeightForWidth())
        self.decode_input_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        self.decode_input_label.setFont(font2)
        self.decode_input_label.setStyleSheet(u"border: one;")
        self.decode_input_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.decode_input_label)

        self.decode_input_line_edit = QLineEdit(self.decode_input_frame)
        self.decode_input_line_edit.setObjectName(u"decode_input_line_edit")
        self.decode_input_line_edit.setStyleSheet(u"height: 35px;\n"
"background: rgba(0,0,0,0);\n"
"border: 3px solid;\n"
"letter-spacing: 2px;\n"
"color: #000;")
        self.decode_input_line_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.decode_input_line_edit)

        self.decode_input_button = QPushButton(self.decode_input_frame)
        self.decode_input_button.setObjectName(u"decode_input_button")
        self.decode_input_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decode_input_button.setStyleSheet(u"letter-spacing: 2px;\n"
"border: 3px solid;\n"
"color: #000;\n"
"height: 30px;")

        self.verticalLayout_5.addWidget(self.decode_input_button)


        self.verticalLayout_3.addWidget(self.decode_input_frame)


        self.verticalLayout.addWidget(self.decoded_frame)

        self.encoded_frame = QFrame(self.main_frame)
        self.encoded_frame.setObjectName(u"encoded_frame")
        sizePolicy.setHeightForWidth(self.encoded_frame.sizePolicy().hasHeightForWidth())
        self.encoded_frame.setSizePolicy(sizePolicy)
        self.encoded_frame.setStyleSheet(u"background: none;\n"
"border: none;\n"
"margin: 0px;")
        self.encoded_frame.setFrameShape(QFrame.StyledPanel)
        self.encoded_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.encoded_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.encode_message_frame = QFrame(self.encoded_frame)
        self.encode_message_frame.setObjectName(u"encode_message_frame")
        self.encode_message_frame.setStyleSheet(u"margin: 0px;")
        self.encode_message_frame.setFrameShape(QFrame.StyledPanel)
        self.encode_message_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.encode_message_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.encoded_message = QLabel(self.encode_message_frame)
        self.encoded_message.setObjectName(u"encoded_message")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.encoded_message.sizePolicy().hasHeightForWidth())
        self.encoded_message.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(28)
        font3.setBold(False)
        self.encoded_message.setFont(font3)
        self.encoded_message.setStyleSheet(u"margin: 0px;")
        self.encoded_message.setAlignment(Qt.AlignCenter)
        self.encoded_message.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.encoded_message)

        self.copy_encoded_message_button = QPushButton(self.encode_message_frame)
        self.copy_encoded_message_button.setObjectName(u"copy_encoded_message_button")
        sizePolicy1.setHeightForWidth(self.copy_encoded_message_button.sizePolicy().hasHeightForWidth())
        self.copy_encoded_message_button.setSizePolicy(sizePolicy1)
        self.copy_encoded_message_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_encoded_message_button.setIcon(icon)
        self.copy_encoded_message_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.copy_encoded_message_button)


        self.verticalLayout_2.addWidget(self.encode_message_frame)

        self.encode_input_frame = QFrame(self.encoded_frame)
        self.encode_input_frame.setObjectName(u"encode_input_frame")
        self.encode_input_frame.setFrameShape(QFrame.StyledPanel)
        self.encode_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.encode_input_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.encode_input_label = QLabel(self.encode_input_frame)
        self.encode_input_label.setObjectName(u"encode_input_label")
        sizePolicy.setHeightForWidth(self.encode_input_label.sizePolicy().hasHeightForWidth())
        self.encode_input_label.setSizePolicy(sizePolicy)
        self.encode_input_label.setFont(font2)
        self.encode_input_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.encode_input_label)

        self.encode_input_line_edit = QLineEdit(self.encode_input_frame)
        self.encode_input_line_edit.setObjectName(u"encode_input_line_edit")
        self.encode_input_line_edit.setFont(font2)
        self.encode_input_line_edit.setStyleSheet(u"height: 35px;\n"
"background: rgba(0,0,0,0);\n"
"border: 3px solid;\n"
"letter-spacing: 2px;\n"
"color: #000;")
        self.encode_input_line_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.encode_input_line_edit)

        self.encode_input_button = QPushButton(self.encode_input_frame)
        self.encode_input_button.setObjectName(u"encode_input_button")
        self.encode_input_button.setFont(font2)
        self.encode_input_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encode_input_button.setStyleSheet(u"letter-spacing: 2px;\n"
"border: 3px solid;\n"
"color: #000;\n"
"height: 30px;")

        self.verticalLayout_4.addWidget(self.encode_input_button)


        self.verticalLayout_2.addWidget(self.encode_input_frame)


        self.verticalLayout.addWidget(self.encoded_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setFont(font2)
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Morse Code Encoder-Decoder", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"MORSE CODE\n"
"ENCODER || DECODER", None))
        self.encoder_button.setText(QCoreApplication.translate("MainWindow", u"ENCODE", None))
        self.decoder_button.setText(QCoreApplication.translate("MainWindow", u"DECODE", None))
        self.decoded_message.setText(QCoreApplication.translate("MainWindow", u"wdawdad", None))
        self.copy_decode_message_button.setText("")
        self.decode_input_label.setText(QCoreApplication.translate("MainWindow", u"Enter Morse Code below to start encoding", None))
        self.decode_input_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Morse Code", None))
        self.decode_input_button.setText(QCoreApplication.translate("MainWindow", u"DECODE MESSAGE", None))
        self.encoded_message.setText("")
        self.copy_encoded_message_button.setText("")
        self.encode_input_label.setText(QCoreApplication.translate("MainWindow", u"Enter Plain Text below to start encoding", None))
        self.encode_input_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your message", None))
        self.encode_input_button.setText(QCoreApplication.translate("MainWindow", u"ENCODE MESSAGE", None))
    # retranslateUi

