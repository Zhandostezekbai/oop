import sys
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QComboBox, QPushButton, QListWidget, 
    QTableWidget, QTableWidgetItem, QLabel
)

# ==========================================
# 1. РЕАЛИЗАЦИЯ (Способы отображения)
# ==========================================

class TaskRenderer(ABC):
    @abstractmethod
    def add_task(self, task_text: str):
        pass

    @abstractmethod
    def clear(self):
        pass

class ListTaskRenderer(TaskRenderer):
    def __init__(self, list_widget: QListWidget):
        self.list_widget = list_widget

    def add_task(self, task_text: str):
        self.list_widget.addItem(task_text)

    def clear(self):
        self.list_widget.clear()

class TableTaskRenderer(TaskRenderer):
    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget
        self.table_widget.setColumnCount(1)
        self.table_widget.setHorizontalHeaderLabels(["Список задач"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)

    def add_task(self, task_text: str):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(task_text))

    def clear(self):
        self.table_widget.setRowCount(0)


# ==========================================
# 2. АБСТРАКЦИЯ (Типы задач) — МОСТ
# ==========================================

class Task(ABC):
    def __init__(self, title: str, renderer: TaskRenderer):
        self.title = title
        self.renderer = renderer  # <--- Мост

    @abstractmethod
    def display(self):
        pass

class SimpleTask(Task):
    def display(self):
        self.renderer.add_task(self.title)

class PriorityTask(Task):
    def display(self):
        formatted_text = f"[ВАЖНО] {self.title}"
        self.renderer.add_task(formatted_text)


# ==========================================
# 3. ГРАФИЧЕСКИЙ ИНТЕРФЕЙС (PyQt6)
# ==========================================

class TaskManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Система управления задачами (Паттерн Мост)")
        self.resize(500, 400)

        main_layout = QVBoxLayout()

        # Поле ввода названия задачи
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Название:"))
        self.task_input = QLineEdit()
        input_layout.addWidget(self.task_input)
        main_layout.addLayout(input_layout)

        # Выбор типа задачи
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Тип задачи:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Обычная (SimpleTask)", "Приоритетная (PriorityTask)"])
        type_layout.addWidget(self.type_combo)
        main_layout.addLayout(type_layout)

        # Выбор способа отображения
        renderer_layout = QHBoxLayout()
        renderer_layout.addWidget(QLabel("Отображение:"))
        self.renderer_combo = QComboBox()
        self.renderer_combo.addItems(["Список (QListWidget)", "Таблица (QTableWidget)"])
        self.renderer_combo.currentIndexChanged.connect(self.on_renderer_changed)
        renderer_layout.addWidget(self.renderer_combo)
        main_layout.addLayout(renderer_layout)

        # Виджеты отображения
        self.list_widget = QListWidget()
        self.table_widget = QTableWidget()
        self.table_widget.hide() # Бастапқыда тізім көрсетіледі

        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.table_widget)

        # Инициализация рендереров
        self.list_renderer = ListTaskRenderer(self.list_widget)
        self.table_renderer = TableTaskRenderer(self.table_widget)
        self.current_renderer = self.list_renderer

        # Кнопки управления
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Добавить задачу")
        self.add_btn.clicked.connect(self.add_task)
        
        self.clear_btn = QPushButton("Очистить список")
        self.clear_btn.clicked.connect(self.clear_tasks)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.clear_btn)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def on_renderer_changed(self, index):
        if index == 0:
            self.table_widget.hide()
            self.list_widget.show()
            self.current_renderer = self.list_renderer
        else:
            self.list_widget.hide()
            self.table_widget.show()
            self.current_renderer = self.table_renderer

    def add_task(self):
        title = self.task_input.text().strip()
        if not title:
            return

        task_type = self.type_combo.currentIndex()

        if task_type == 0:
            task = SimpleTask(title, self.current_renderer)
        else:
            task = PriorityTask(title, self.current_renderer)

        task.display()
        self.task_input.clear()

    def clear_tasks(self):
        self.current_renderer.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TaskManagerApp()
    ex.show()
    sys.exit(app.exec())