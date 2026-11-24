import sys
from abc import ABC, abstractmethod

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtWidgets import QApplication, QWidget




class Renderer(ABC):

    @abstractmethod
    def render_circle(self, painter, x, y, r):
        pass

    @abstractmethod
    def render_rect(self, painter, x, y, w, h):
        pass



class FilledRenderer(Renderer):

    def render_circle(self, painter, x, y, r):
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor('steelblue'))
        painter.drawEllipse(QPoint(x, y), r, r)

    def render_rect(self, painter, x, y, w, h):
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor('steelblue'))
        painter.drawRect(x, y, w, h)

class OutlineRenderer(Renderer):

    def render_circle(self, painter, x, y, r):
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(QColor('darkred'), 3))
        painter.drawEllipse(QPoint(x, y), r, r)

    def render_rect(self, painter, x, y, w, h):
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(QColor('darkred'), 3))
        painter.drawRect(x, y, w, h)

class Figur(ABC):

    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self, painter):
        pass


class Circle(Figur):

    def __init__(self, x, y, r, renderer):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.r = r

    def draw(self, painter):
        self.renderer.render_circle(
            painter, self.x, self.y, self.r
        )



class Rectangle(Figur):

    def __init__(self, x, y, w, h, renderer):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, painter):
        self.renderer.render_rect(
            painter, self.x, self.y, self.w, self.h
        )


class Canvas(QWidget):

    def __init__(self, shapes):
        super().__init__()

        self.shapes = shapes
        self.setWindowTitle("Bridge Pattern")
        self.resize(420, 300)

    def paintEvent(self, event):
        painter = QPainter(self)

        for shape in self.shapes:
            shape.draw(painter)

        painter.end()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    filled = FilledRenderer()
    outline = OutlineRenderer()

    shapes = [
        Circle(100, 100, 40, filled),
        Circle(200, 100, 40, outline),

        Rectangle(40, 180, 100, 60, outline),
        Rectangle(220, 180, 120, 60, filled)
    ]

    window = Canvas(shapes)
    window.show()

    sys.exit(app.exec())
