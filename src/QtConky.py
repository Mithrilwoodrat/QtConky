#coding=utf-8
from Meter import Meter
from PyQt4.QtCore import Qt
from PyQt4 import  QtGui, QtCore 

class Conky(Meter):
    def __init__(self,parent=None):
        super(Conky,self).__init__()
        self.crownColor = Qt.black
        self.locked = False
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnBottomHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.createContextMenu()
        self.resize(150,150)
    
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton and not self.locked:
            self.dragPosition = QMouseEvent.globalPos() - self.frameGeometry().topLeft()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() ==QtCore.Qt.LeftButton and not self.locked:
            self.move(QMouseEvent.globalPos() - self.dragPosition)
            QMouseEvent.accept()

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        # create QMenu
        self.contextMenu = QtGui.QMenu(self)

        self.lock_menu = self.contextMenu.addAction(u'lock')
        self.close_menu = self.contextMenu.addAction(u'close')
        
        self.lock_menu.triggered.connect(self.lock_action)
        self.close_menu.triggered.connect(self.colse_action)
        
    def showContextMenu(self, pos):
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()

    def lock_action(self):
        if self.locked:
            self.locked = False
            self.lock_menu.setText('lock')
        else:
            self.locked = True
            self.lock_menu.setText('unlock')
        
    def colse_action(self):
        self.close()