
from PyQt6.QtWidgets import (QApplication)
from classes.main_window import MainWindow

if not __name__ == "__main__":
    exit()
lauch
app = QApplication([])
ww = MainWindow()
ww.show()
app.exec()

