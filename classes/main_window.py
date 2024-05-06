
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QTextBrowser)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("app")
        self.resize(280, 280)
        self.setMinimumSize(200, 200)
        self.setWindowIcon(QIcon('../resource/icons/app.png'))

        # Create a grid layout
        layout = QGridLayout()
        layout.setColumnStretch(0, 0)
        layout.setColumnStretch(1, 1)

        # Create the button run
        self.btn_run = QPushButton("Run", self)

        # Connect the button to the search_image function
        self.btn_run.clicked.connect(self.run)

        # Create a text browser
        self.text_browser = QTextBrowser()
        self.text_browser.setReadOnly(True)
        self.text_browser.setStyleSheet("color: yellow;")
        self.text_browser.setPlainText("waiting ...")

        layout.addWidget(self.text_browser, 0, 1)
        layout.addWidget(self.btn_run, 1, 1)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def run(self):
        self.text_browser.setStyleSheet("color: green;")
        self.text_browser.setPlainText("/started")

