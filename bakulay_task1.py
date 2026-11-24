
import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QTextEdit, QVBoxLayout, QLabel
)


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def log(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        self.messages.append(f"[{time}] {message}")

    def get_messages(self):
        return self.messages


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Баптаулар')

        QVBoxLayout(self).addWidget(
            QLabel('Баптаулар терезесі')
        )

        Logger().log('Баптаулар терезесі ашылды')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Басты терезе')

        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)

        btn = QPushButton('Баптауларды ашу')
        btn.clicked.connect(self.open_settings)

        layout = QVBoxLayout(self)
        layout.addWidget(btn)
        layout.addWidget(self.log_view)

        Logger().log('Басты терезе ашылды')
        self.refresh()

    def open_settings(self):
        self.settings = SettingsWindow()
        self.settings.show()
        self.refresh()

    def refresh(self):
        self.log_view.setPlainText(
            '\n'.join(Logger().get_messages())
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    print(Logger() is Logger())  # True болуы тиіс

    sys.exit(app.exec())
