# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 624)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.526882, y1:1, x2:0.537634, y2:0, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(151, 151, 151, 255));"
        )
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.central_widget.setStyleSheet(
            "QFrame { \n"
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
            ""
        )
        self.horizontalLayout = QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName("main_frame")
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QLabel(self.main_frame)
        self.title_label.setObjectName("title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QSize(16777215, 160))
        font = QFont()
        font.setFamilies(["Montserrat"])
        font.setPointSize(40)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("border: none;\n" "margin: none;")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.morse_buttons_frame = QFrame(self.main_frame)
        self.morse_buttons_frame.setObjectName("morse_buttons_frame")
        sizePolicy.setHeightForWidth(
            self.morse_buttons_frame.sizePolicy().hasHeightForWidth()
        )
        self.morse_buttons_frame.setSizePolicy(sizePolicy)
        self.morse_buttons_frame.setStyleSheet(
            "border: none;\n" "background: none;\n" "margin: 0px;"
        )
        self.morse_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.morse_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.morse_buttons_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.encoder_button = QPushButton(self.morse_buttons_frame)
        self.encoder_button.setObjectName("encoder_button")
        self.encoder_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encoder_button.setStyleSheet(
            "background: none;\n"
            "letter-spacing: 2px;\n"
            "color: #000;\n"
            "border: 3px solid;\n"
            "height: 35px;"
        )

        self.horizontalLayout_2.addWidget(self.encoder_button)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.decoder_button = QPushButton(self.morse_buttons_frame)
        self.decoder_button.setObjectName("decoder_button")
        self.decoder_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decoder_button.setStyleSheet(
            "background: none;\n"
            "letter-spacing: 2px;\n"
            "color: #000;\n"
            "border: 3px solid;\n"
            "height: 35px;"
        )

        self.horizontalLayout_2.addWidget(self.decoder_button)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.morse_buttons_frame)

        self.encoded_frame = QFrame(self.main_frame)
        self.encoded_frame.setObjectName("encoded_frame")
        self.encoded_frame.setStyleSheet(
            "background: none;\n" "border: none;\n" "margin: 0px;"
        )
        self.encoded_frame.setFrameShape(QFrame.StyledPanel)
        self.encoded_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.encoded_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encode_message_frame = QFrame(self.encoded_frame)
        self.encode_message_frame.setObjectName("encode_message_frame")
        self.encode_message_frame.setStyleSheet("margin: 0px;")
        self.encode_message_frame.setFrameShape(QFrame.StyledPanel)
        self.encode_message_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.encode_message_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.encoded_message = QLabel(self.encode_message_frame)
        self.encoded_message.setObjectName("encoded_message")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.encoded_message.sizePolicy().hasHeightForWidth()
        )
        self.encoded_message.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["Montserrat"])
        font1.setPointSize(28)
        font1.setBold(False)
        self.encoded_message.setFont(font1)
        self.encoded_message.setStyleSheet("margin: 0px;")
        self.encoded_message.setAlignment(Qt.AlignCenter)
        self.encoded_message.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.encoded_message)

        self.copy_encoded_message_button = QPushButton(self.encode_message_frame)
        self.copy_encoded_message_button.setObjectName("copy_encoded_message_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.copy_encoded_message_button.sizePolicy().hasHeightForWidth()
        )
        self.copy_encoded_message_button.setSizePolicy(sizePolicy2)
        self.copy_encoded_message_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            ":/src/main_window/images/copyIcon.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.copy_encoded_message_button.setIcon(icon)
        self.copy_encoded_message_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.copy_encoded_message_button)

        self.verticalLayout_2.addWidget(self.encode_message_frame)

        self.encode_input_frame = QFrame(self.encoded_frame)
        self.encode_input_frame.setObjectName("encode_input_frame")
        self.encode_input_frame.setFrameShape(QFrame.StyledPanel)
        self.encode_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.encode_input_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.encode_input_label = QLabel(self.encode_input_frame)
        self.encode_input_label.setObjectName("encode_input_label")
        sizePolicy.setHeightForWidth(
            self.encode_input_label.sizePolicy().hasHeightForWidth()
        )
        self.encode_input_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies(["Montserrat"])
        self.encode_input_label.setFont(font2)
        self.encode_input_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.encode_input_label)

        self.encode_input_line_edit = QLineEdit(self.encode_input_frame)
        self.encode_input_line_edit.setObjectName("encode_input_line_edit")
        self.encode_input_line_edit.setFont(font2)
        self.encode_input_line_edit.setStyleSheet(
            "height: 35px;\n"
            "background: rgba(0,0,0,0);\n"
            "border: 3px solid;\n"
            "letter-spacing: 2px;\n"
            "color: #000;"
        )
        self.encode_input_line_edit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.encode_input_line_edit)

        self.encode_input_button = QPushButton(self.encode_input_frame)
        self.encode_input_button.setObjectName("encode_input_button")
        self.encode_input_button.setFont(font2)
        self.encode_input_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encode_input_button.setStyleSheet(
            "letter-spacing: 2px;\n"
            "border: 3px solid;\n"
            "color: #000;\n"
            "height: 30px;"
        )

        self.verticalLayout_4.addWidget(self.encode_input_button)

        self.verticalLayout_2.addWidget(self.encode_input_frame)

        self.verticalLayout.addWidget(self.encoded_frame)

        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        self.status_bar.setFont(font2)
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Morse Code Encoder-Decoder", None)
        )
        self.title_label.setText(
            QCoreApplication.translate(
                "MainWindow", "MORSE CODE\n" "ENCODER || DECODER", None
            )
        )
        self.encoder_button.setText(
            QCoreApplication.translate("MainWindow", "ENCODE", None)
        )
        self.decoder_button.setText(
            QCoreApplication.translate("MainWindow", "DECODE", None)
        )
        self.encoded_message.setText("")
        self.copy_encoded_message_button.setText("")
        self.encode_input_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Enter Plain Text below to start encoding", None
            )
        )
        self.encode_input_line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Enter your message", None)
        )
        self.encode_input_button.setText(
            QCoreApplication.translate("MainWindow", "ENCODE MESSAGE", None)
        )

    # retranslateUi
