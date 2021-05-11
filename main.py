import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QFileDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = None

    def initUI(self):
        exitAct = QAction(QIcon('image/exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)


        openAct = QAction(QIcon('image/open.png'), '&open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file dialog')
        openAct.triggered.connect(self.openFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)
        editMenu = menubar.addMenu('&Edit')
        helpMenu = menubar.addMenu('&Help')

        #Gestion des calques / Layout
        layoutH = QHBoxLayout()
        layoutV = QVBoxLayout()

        layoutV.setContentsMargins(0,0,0,0)

        widgetTable = QTableWidget()
        widgetTable.setStyleSheet('background-color: red;')
        widget = QWidget()
        widget.setLayout(layoutV)

        widgetStat1 = QWidget()
        widgetStat1.setStyleSheet('background-color: blue;')
        widgetStat2 = QWidget()
        widgetStat2.setStyleSheet('background-color: green;')

        layoutV.addWidget(widgetStat1,1)
        layoutV.addWidget(widgetStat2,1)
        layoutH.addWidget(widgetTable,3)
        layoutH.addWidget(widgetStat1,1)

        widget = QWidget()
        widget.setLayout(layoutH)
        self.setCentralWidget(widget)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


    def openFile(self):
        option = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "All Files (*);;Excel Files (*.xlsx) ;;"
                                                  "CSV Files (*.csv)", options=option)

        if fileName:
            print(fileName)
            fichier = open(fileName, 'r')
            self.data = [i.split(";") for i in fichier.read().split("\n")]
            print(self.data)




def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()