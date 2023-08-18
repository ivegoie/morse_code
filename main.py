import sys
from PySide6.QtWidgets import QApplication
from src import MainWindow

app = QApplication(sys.argv)

widget = MainWindow()
widget.show()

app.exec()
