"""Notepad using PyQt5"""
from PyQt5 import QtWidgets, QtGui
import sys


class notepad(QtWidgets.QWidget):
    """
    Notepad Window
    """

    def __init__(self):
        """
        Initialize window
        """
        super().__init__()

        self.setWindowTitle("Notepad")
        self.icon = QtGui.QIcon('icon.png')
        self.setWindowIcon(self.icon)
        self.editing = QtWidgets.QPlainTextEdit()
        self.savebutt = QtWidgets.QPushButton("Save")
        self.loadbutt = QtWidgets.QPushButton("Load from file")
        self.fontplusbutt = QtWidgets.QPushButton("+")
        self.fontminusbutt = QtWidgets.QPushButton("-")
        self.layout = QtWidgets.QVBoxLayout()
        self.buttonslay = QtWidgets.QHBoxLayout()
        self.buttonslay.addWidget(QtWidgets.QLabel())
        self.buttonslay.addWidget(self.fontminusbutt)
        self.buttonslay.addWidget(self.fontplusbutt)
        self.buttonslay.addWidget(self.savebutt)
        self.buttonslay.addWidget(self.loadbutt)
        self.layout.addWidget(self.editing)
        self.layout.addLayout(self.buttonslay)
        self.setLayout(self.layout)
        self.font = QtGui.QFont("Comic Sans", 10)
        self.editing.setFont(self.font)

        self.savebutt.clicked.connect(self.txtsave)
        self.loadbutt.clicked.connect(self.txtload)
        self.fontplusbutt.clicked.connect(self.font_size_increase)
        self.fontminusbutt.clicked.connect(self.font_size_decrease)

    def font_size_increase(self):
        """
        Increase font
        :return: None
        """
        size = self.font.pointSize()
        self.font.setPointSize(size + 5)
        self.editing.setFont(self.font)

    def font_size_decrease(self):
        """
        Decrease font
        :return: None
        """
        size = self.font.pointSize()
        self.font.setPointSize(size - 5)
        self.editing.setFont(self.font)

    def txtsave(self):
        """
        Save text
        :return: None
        """
        try:
            name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', "file.txt", "Any file (*.*)")
            if '.' in name[0]:
                f = open(name[0], "w")
                tekst = self.editing.toPlainText().split("\n")
                for i in tekst:
                    f.write(i)
                    if '\n' not in i:
                        f.write('\n')
                f.close()
        finally:
            pass

    def txtload(self):
        """
        Load text
        :return: None
        """
        name = QtWidgets.QFileDialog.getOpenFileName()
        if '.' in name[0]:
            self.editing.clear()
            f = open(name[0])
            lines = f.readlines()
            for i in lines:
                self.editing.appendPlainText(i)
            f.close()


def main():
    """
    Main function
    """
    if __name__ == "__main__":
        app = QtWidgets.QApplication([])

        widget = notepad()
        widget.resize(800, 600)
        widget.show()

        sys.exit(app.exec_())


main()
