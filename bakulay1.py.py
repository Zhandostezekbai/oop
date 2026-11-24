import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout
)

class WindowsButton(QPushButton):
    def _init_(self):
        super()._init_('OK (Windows)')
        self.setStyleSheet(
            'background-color: #0078d7; color: white;'
        )

class LinuxButton(QPushButton):
    def _init_(self):
        super()._init_('OK (Linux)')
        self.setStyleSheet(
            'background-color: #e95420; color: white;'
        )

class Dialog(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle('Диалог')

        layout = QVBoxLayout(self)
        button = self.create_button()
        button.clicked.connect(self.close)
        layout.addWidget(button)

    def create_button(self) -> QPushButton:
        if os_name == 'windows':
            return WindowsButton()
        elif os_name == 'linux':
            return LinuxButton()
        else:
            raise ValueError('Белгісіз операциялық жүйе')

if _name_ == '_main_':
    app = QApplication(sys.argv)

    os_name = 'linux'  # windows немесе linux

    dialog = Dialog()
    dialog.show()

    sys.exit(app.exec())