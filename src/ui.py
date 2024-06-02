#******************************************************************
# content = UI for user to select Maya object and texture files
# author = Edwina Asumang
#******************************************************************

import sys
from PySide6 import QtCore, QtWidgets


class HelloWorldWidget(QtWidgets.QWidget):
    """Trying out Pyside"""
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)


#may not need to have this as a function separate from main function in the end
def create_widget():
    """Display widget"""
    app = QtWidgets.QApplication([])

    widget = HelloWorldWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    create_widget()
