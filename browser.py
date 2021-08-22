import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://terminotech.com"))
        self.setCentralWidget(self.browser)
        self._scene = QtWidgets.QGraphicsScene(self)
        self._view = QtWidgets.QGraphicsView(self._scene)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn= QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        refresh_btn = QAction('Refresh',self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        zoom_in_btn = QAction('+',self)
        zoom_in_btn.triggered.connect(self.zoom_in)
        zoom_out_btn = QAction('-',self)
        zoom_out_btn.triggered.connect(self.zoom_out)
        navbar.addAction(zoom_out_btn)
        navbar.addAction(zoom_in_btn)
        self.browser.urlChanged.connect(self.update_url)
        self.zoom_label = QLabel('%s' % str(self.browser.zoomFactor()*100)[0:3])
        navbar.addWidget(self.zoom_label)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        

    
    def zoom_in(self):
        self.browser.setZoomFactor(self.browser.zoomFactor()+0.1)
        if self.browser.zoomFactor() >= 1.0:self.zoom_label.setText('%s' % str(self.browser.zoomFactor()*100)[0:3])
        elif 0.1 <= self.browser.zoomFactor() < 1.0: self.zoom_label.setText('%s%' % str(self.browser.zoomFactor()*100)[0:2])
    def zoom_out(self):
        self.browser.setZoomFactor(self.browser.zoomFactor()-0.1)
        if self.browser.zoomFactor() >= 1.0:self.zoom_label.setText('%s' % str(self.browser.zoomFactor()*100)[0:3])
        elif 0.1 <= self.browser.zoomFactor() < 1.0: self.zoom_label.setText('%s' % str(self.browser.zoomFactor()*100)[0:2])
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('https://') and not url.startswith('http://'):
            url = 'http://'+url
        self.browser.setUrl(QUrl(url))
        print(self.browser.zoomFactor())

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
app = QApplication(sys.argv)
QApplication.setApplicationName("Willets Browser")
window = MainWindow()
app.exec_()
