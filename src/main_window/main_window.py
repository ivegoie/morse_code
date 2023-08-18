from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QClipboard, QGuiApplication
from src import Encoder

from src import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encoded_frame.hide()

        self.encoder_button.clicked.connect(self.open_encode_frame)
        self.encode_input_button.clicked.connect(self.encode_message)
        self.copy_encoded_message_button.clicked.connect(self.copy_encoded_message)

    def open_encode_frame(self):
        self.morse_buttons_frame.hide()
        self.encoded_frame.show()
        self.encode_message_frame.hide()

    def encode_message(self):
        encoder = Encoder()
        self.encode_message_frame.show()
        message = self.encode_input_line_edit.text()
        self.encoded_message.setText(encoder.play_morse_code(message))

    def copy_encoded_message(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.encoded_message.text())
        self.status_bar.showMessage("Copied to clipboard", 5000)
