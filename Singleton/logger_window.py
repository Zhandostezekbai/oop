from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPlainTextEdit,
    QPushButton
)
from app_logger import Logger

class LoggerWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Журнал оқиғалары")
        self.setGeometry(650, 200, 400, 300)

        self.logger = Logger()

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)

        self.refresh_button = QPushButton("Журналды жаңарту")
        self.refresh_button.clicked.connect(self.load_logs)

        self.clear_button = QPushButton("Журналды тазалау")
        self.clear_button.clicked.connect(self.clear_logs)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.clear_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_logs()

    def load_logs(self):
        logs = self.logger.get_logs()
        self.text_edit.setPlainText("\n".join(logs))

    def clear_logs(self):
        self.logger.clear_logs()
        self.load_logs()
        if self.parent() and hasattr(self.parent(), 'update_counter'):
            self.parent().update_counter()