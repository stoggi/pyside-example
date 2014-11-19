from PySide import QtCore, QtGui
import sys

from fruit_ui import Ui_FruitBasket

class FruitBasket(QtGui.QMainWindow):
    """A custom exception dialog show the about window"""

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_FruitBasket()
        self.ui.setupUi(self)

    @QtCore.Slot()
    def on_button_add_clicked(self):
        self.ui.list_basket.addItem(self.ui.combo_fruit.currentText())

    @QtCore.Slot()
    def on_button_delete_clicked(self):
        for item in self.ui.list_basket.selectedItems():
            self.ui.list_basket.takeItem(self.ui.list_basket.row(item))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = FruitBasket()
    ui.show()
    sys.exit(app.exec_())
