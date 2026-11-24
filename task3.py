import sys

from PyQt6.QtWidgets import QApplication,QWidget,QTextEdit,QPushButton,QVBoxLayout,QMessageBox




class TextStorage:
    def save(self, text: str):
        with open('notes.txt', 'w', encoding='utf-8') as f:
            f.write(text)

    def load(self):
        with open('notes.txt', encoding='utf-8') as f:
            return f.read()



class ReadOnlyStorage(TextStorage):
    def save(self, text: str):
        raise PermissionError('Бұл қойма тек оқуға арналған')



class Editor(QWidget):
    def __init__(self, storage: TextStorage):
        super().__init__()

        self.storage = storage

        self.setWindowTitle("Text Editor")
        self.resize(400, 300)

        self.edit = QTextEdit()

        btn = QPushButton('Сақтау')
        btn.clicked.connect(self.save_text)

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(btn)

    def save_text(self):
        try:
            self.storage.save(self.edit.toPlainText())
            QMessageBox.information(self, "Дұрыс", "Текст сақталды!")

        except PermissionError as e:
            QMessageBox.warning(self, "Қате", str(e))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    editor = Editor(ReadOnlyStorage())
    editor.show()

    sys.exit(app.exec())
