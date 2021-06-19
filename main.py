import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QGridLayout, QWidget

APP_NAME = "Binary Visualizer"
APP_VERSION = "0.0.1"

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(100, 60, 600, 800)
    self.setWindowTitle('{} {}'.format(APP_NAME, APP_VERSION))

    layout = QGridLayout()
    layout.addWidget(QPlainTextEdit(), 0, 0)
    layout.addWidget(QPlainTextEdit(), 1, 0)

    wid = QWidget(self)
    self.setCentralWidget(wid)
    wid.setLayout(layout)

    self.statusBar().showMessage('Ready')
    self.show()


def main():
  app = QApplication(sys.argv)

  w = MainWindow()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()