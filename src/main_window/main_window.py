import sys
import threading

from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import QApplication, QMainWindow

from src import Decoder, Encoder, Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encoded_frame.hide()
        self.decoded_frame.hide()

        self.encoder_button.clicked.connect(self.open_encode_frame)
        self.encode_input_button.clicked.connect(self.encode_message)
        self.copy_encoded_message_button.clicked.connect(self.copy_encoded_message)

        self.decoder_button.clicked.connect(self.open_decode_frame)
        self.decode_input_button.clicked.connect(self.decode_message)
        self.copy_decode_message_button.clicked.connect(self.copy_decoded_message)

    def open_encode_frame(self):
        self.encode_message_frame.hide()
        self.encoded_frame.show()

        self.decoded_frame.hide()

    def open_decode_frame(self):
        self.decode_message_frame.hide()
        self.decoded_frame.show()

        self.encoded_frame.hide()

        # "- .... . / .-.. --- ...- . / -.-. .... .- .-. ... / -- --- .-. -. .. -. --. / .- -. -.. / --- ..-. / - .... . / .-.. --- ...- ."

    def encode_message(self):
        encoder = Encoder()
        self.encode_message_frame.show()
        message = self.encode_input_line_edit.text()
        self.encoded_message.setText(encoder.play_morse_code(message))

    def copy_encoded_message(self):
        clipboard = QClipboard()
        clipboard.setText(self.encoded_message.text())
        self.status_bar.showMessage("Encoded Message copied to clipboard", 5000)

    def decode_message(self):
        decoder = Decoder()
        self.decode_message_frame.show()
        message = self.decode_input_line_edit.text()
        decoded_text = self.decoded_message.setText(decoder.morse_to_chars(message))

    def copy_decoded_message(self):
        clipboard = QClipboard
        clipboard.setText(self.decoded_message.text())
        self.status_bar.showMessage("Decoded Message copied to clipboard", 5000)
