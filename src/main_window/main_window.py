from PySide6.QtWidgets import QMainWindow
from src import Encoder

from src import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encoded_frame.hide()

        self.encoder_button.clicked.connect(self.open_encode_frame)
        self.encode_input_button.clicked.connect(self.encode_message)

    def open_encode_frame(self):
        self.morse_buttons_frame.hide()
        self.encoded_frame.show()

    def encode_message(self):
        encoder = Encoder()
        message = self.encode_input_line_edit.text()
        self.encoded_message.setText(encoder.play_morse_code(message))
