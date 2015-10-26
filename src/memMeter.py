#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import  sys
from QtConky import  Conky
from PyQt4 import  QtGui, QtCore


"""fun to read Memory info """
try:
    import psutil
    def getMemorystate():
        mem_info = psutil.virtual_memory()
        return mem_info.percent
except ImportError:
    print "no moudle named psutil"
    
class MEMMeter(Conky):
    def __init__(self,parent=None):
        super(MEMMeter,self).__init__()
        self.logo = "Mem"
        
    def updateValue(self):
        self.value = getMemorystate()
        
def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MEMMeter()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
