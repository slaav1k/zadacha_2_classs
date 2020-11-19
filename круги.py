import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.flag = True
        self.repaint()
        # Имя элемента совпадает с objectName в QTDesigner

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            self.circle(painter)
            painter.end()

    def circle(self, painter):
        r = random.randint(1, 100)
        painter.setPen(Qt.yellow)
        painter.drawEllipse(50, 70 - r, 2 * r, 2 * r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
