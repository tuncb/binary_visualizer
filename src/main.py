from BinaryDataType import BinaryDataType
import sys
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QPlainTextEdit, QGridLayout, QPushButton, QVBoxLayout, QWidget

from DecimalConvertor import convertToDecimal

APP_NAME = "Binary Visualizer"
APP_VERSION = "0.0.1"

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def handlePasteBtnPressed(self):
    self.topTextEdit.setPlainText(QApplication.clipboard().text())

  def handleCopyBtnPressed(self):
    QApplication.clipboard().setText(self.bottomTextEdit.toPlainText())

  def updateData(self):
    input = self.topTextEdit.toPlainText()
    dataType = BinaryDataType[self.dataTypeComboBox.currentText()]
    self.bottomTextEdit.setPlainText(convertToDecimal(input, dataType))

  def initUI(self):
    self.setGeometry(100, 60, 1000, 800)
    self.setWindowTitle("{} {}".format(APP_NAME, APP_VERSION))

    self.topTextEdit = QPlainTextEdit()
    self.topTextEdit.textChanged.connect(self.updateData)
    self.topPasteBtn = QPushButton("Paste")
    self.topPasteBtn.clicked.connect(self.handlePasteBtnPressed)
    topSideLayout = QVBoxLayout()
    topSideLayout.addWidget(self.topPasteBtn)

    self.bottomTextEdit = QPlainTextEdit()
    self.bottomTextEdit.setReadOnly(True)

    self.dataTypeComboBox = QComboBox()
    self.dataTypeComboBox.addItems([e.name for e in BinaryDataType])
    self.dataTypeComboBox.currentIndexChanged.connect(self.updateData)
    self.bottomCopyBtn = QPushButton("Copy")
    self.bottomCopyBtn.clicked.connect(self.handleCopyBtnPressed)

    bottomSideLayout = QVBoxLayout()
    bottomSideLayout.addWidget(self.dataTypeComboBox)
    bottomSideLayout.addWidget(self.bottomCopyBtn)

    layout = QGridLayout()
    layout.addWidget(self.topTextEdit, 0, 0)
    layout.addWidget(self.bottomTextEdit, 1, 0)
    layout.addLayout(topSideLayout, 0, 1)
    layout.addLayout(bottomSideLayout, 1, 1)

    wid = QWidget(self)
    wid.setLayout(layout)
    self.setCentralWidget(wid)

    self.statusBar().showMessage("Ready")
    self.show()


def main():
  app = QApplication(sys.argv)

  w = MainWindow()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()