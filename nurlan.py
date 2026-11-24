import sys
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QApplication, QWidget, QFormLayout,
    QLineEdit, QPushButton
)


class Form(QWidget):
    def _init_(self):
        super()._init_()
        self.form_layout = QFormLayout(self)

    def add_row(self, label: str, widget: QWidget):
        self.form_layout.addRow(label, widget)

    def add_widget(self, widget: QWidget):
        self.form_layout.addRow(widget)


class FormBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_text_field(self, label: str):
        pass

    @abstractmethod
    def add_password_field(self, label: str):
        pass

    @abstractmethod
    def add_submit_button(self, text: str):
        pass

    @abstractmethod
    def get_result(self) -> Form:
        pass


class QtFormBuilder(FormBuilder):

    def reset(self):
        self.form = Form()

    def add_text_field(self, label: str):
        field = QLineEdit()
        self.form.add_row(label, field)

    def add_password_field(self, label: str):
        field = QLineEdit()
        field.setEchoMode(QLineEdit.EchoMode.Password)
        self.form.add_row(label, field)

    def add_submit_button(self, text: str):
        button = QPushButton(text)
        self.form.add_widget(button)

    def get_result(self) -> Form:
        return self.form


class FormDirector:

    def _init_(self, builder):
        self.builder = builder

    def build_login_form(self):
        self.builder.reset()
        self.builder.add_text_field("Логин:")
        self.builder.add_password_field("Құпиясөз:")
        self.builder.add_submit_button("Кіру")
        return self.builder.get_result()

    def build_register_form(self):
        self.builder.reset()
        self.builder.add_text_field("Аты-жөні:")
        self.builder.add_text_field("Email:")
        self.builder.add_password_field("Құпиясөз:")
        self.builder.add_password_field("Құпиясөзді қайталаңыз:")
        self.builder.add_submit_button("Тіркелу")
        return self.builder.get_result()


if _name_ == "_main_":
    app = QApplication(sys.argv)

    builder = QtFormBuilder()
    director = FormDirector(builder)

    login = director.build_login_form()
    login.setWindowTitle("Login Form")
    login.resize(350, 150)
    login.show()

    register = director.build_register_form()
    register.setWindowTitle("Register Form")
    register.resize(350, 200)
    register.show()

    sys.exit(app.exec())