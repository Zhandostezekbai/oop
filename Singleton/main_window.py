from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from logger import Logger
from logger_window import LoggerWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Басты терезе - Singleton Logger")
        self.setGeometry(200, 200, 400, 250)

        self.logger = Logger()

        self.title_label = QLabel("Қосымшаның тақырыбы: Оқиғаларды басқару")
        
        self.counter_label = QLabel()
        self.update_counter()

        self.action_button = QPushButton("Әрекетті орындау")
        self.action_button.clicked.connect(self.perform_action)

        self.open_log_button = QPushButton("Журналды ашу")
        self.open_log_button.clicked.connect(self.open_logger_window)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.counter_label)
        layout.addWidget(self.action_button)
        layout.addWidget(self.open_log_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.logger_window = None

    def update_counter(self):
        """Тіркелген оқиғалар санын жаңарту."""
        count = len(self.logger.get_logs())
        self.counter_label.setText(f"Тіркелген оқиғалар саны: {count}")

    def perform_action(self):
        """Әрекетті орындап, журналға жазу."""
        self.logger.log("Пайдаланушы әрекетті орындады")
        self.update_counter()

    def open_logger_window(self):
        """Журнал терезесін ашу."""
        if self.logger_window is None or not self.logger_window.isVisible():
            self.logger_window = LoggerWindow(self)
            self.logger_window.show()
        else:
            self.logger_window.load_logs()
            self.logger_window.raise_()