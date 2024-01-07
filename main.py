# import modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import sys, os

userAgent = "E-Browser/1.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3 (KHTML, like Gecko) QtWebEngine/5.15.2 Chrome/87.0.4280.88 Safari/537.3"

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # set browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # define print action
        self.printAction = QAction('Print', self)
        self.printAction.setShortcut('Ctrl+P')
        self.printAction.triggered.connect(self.printPage)
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.printAction)

        # set navigation
        backButton = QAction('Back', self)
        backButton.setShortcut('Alt+A')
        backButton.triggered.connect(self.browser.back)

        forwardButton = QAction('Forward', self)
        forwardButton.setShortcut('Alt+S')
        forwardButton.triggered.connect(self.browser.forward)

        # set search bar

        self.toolbar.addAction(backButton)
        self.toolbar.addAction(forwardButton)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateTo)
        self.toolbar.addWidget(self.urlBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def printPage(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QPrintDialog.Accepted:
            self.browser.print_(printer)

    def navigateTo(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))
        self.browser.page().profile().setHttpUserAgent = userAgent

    def updateUrl(self, q):
        self.urlBar.setText(q.toString())

Application = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(Application.exec_())
