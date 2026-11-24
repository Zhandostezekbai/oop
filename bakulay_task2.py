
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTextEdit,
    QPushButton, QVBoxLayout
)
import sys


class Storage(ABC):

    @abstractmethod
    def save(self, text: str) -> None:
        pass


class FileStorage(Storage):

    def __init__(self, path: str):
        self.path = path

    def save(self, text: str) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(text)


class NoteWindow(QWidget):

    def __init__(self, storage: Storage):
        super().__init__()

        self.storage = storage
        self.setWindowTitle("Note")

        self.editor = QTextEdit()

        btn = QPushButton('Сақтау')
        btn.clicked.connect(self.on_save)

        layout = QVBoxLayout(self)
        layout.addWidget(self.editor)
        layout.addWidget(btn)

    def on_save(self):
        self.storage.save(self.editor.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = NoteWindow(FileStorage('notes.txt'))
    window.show()

    sys.exit(app.exec())
