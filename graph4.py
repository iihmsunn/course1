#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import math
import numpy as np

def overseven(index):
        if (index+4)>=7:
            return index-3
        return index+4


class sevenStar:
    def calcpoints(self,center,radius,rotation=0):
        self.center = center
        self.radius = radius
        self.rotation = rotation
        self.points = []
        for i in xrange(7):
            x = self.radius*math.cos((i+1)*2*math.pi/7+rotation)+self.center[0]
            y = self.radius*math.sin((i+1)*2*math.pi/7+rotation)+self.center[1]
            self.points.append([x,y])

    def __init__(self,center,radius):
        self.calcpoints(center,radius)

    def centerpoint(self):
        ymax = 0
        xmax = 0
        for point in self.points:
            if point[0]>xmax: xmax=point[0]
            if point[1]>ymax: ymax=point[1]
        ymin = ymax
        xmin = xmax
        for point in self.points:
            if point[0]<xmin: xmin=point[0]
            if point[1]<ymin: ymin=point[1]
        return [xmax-(xmax-xmin)/2,ymax-(ymax-ymin)/2]


class mainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #QtGui.QWidget.__init__(self, None)
        leftAction = QtGui.QAction('Left', self)
        leftAction.triggered.connect(self.mleft)
        rightAction = QtGui.QAction('Right', self)
        rightAction.triggered.connect(self.mright)
        upAction = QtGui.QAction('Up', self)
        upAction.triggered.connect(self.mup)
        downAction = QtGui.QAction('Down', self)
        downAction.triggered.connect(self.mdown)
        biggerAction = QtGui.QAction('Bigger', self)
        biggerAction.triggered.connect(self.mbigger)
        smallerAction = QtGui.QAction('Smaller', self)
        smallerAction.triggered.connect(self.msmaller)
        rccwAction = QtGui.QAction('Rotate CCW', self)
        rccwAction.triggered.connect(self.mrcw)
        rcwAction = QtGui.QAction('Rotate CW', self)
        rcwAction.triggered.connect(self.mrccw)
        rccwaroundAction = QtGui.QAction('Rotate CCW around', self)
        rccwaroundAction.triggered.connect(self.mrcwaround)
        rcwaroundAction = QtGui.QAction('Rotate CW around', self)
        rcwaroundAction.triggered.connect(self.mrccwaround)
        mirrorAction = QtGui.QAction('Reflect', self)
        mirrorAction.triggered.connect(self.mirror)
        self.xr = QtGui.QLineEdit()
        self.xr.setObjectName("xr")
        self.yr = QtGui.QLineEdit()
        self.yr.setObjectName("yr")
        self.enterButton = QtGui.QPushButton()
        self.enterButton.setObjectName("enterButton")


        leftAction.setShortcut('a')
        rightAction.setShortcut('d')
        upAction.setShortcut('w')
        downAction.setShortcut('s')
        rcwAction.setShortcut('e')
        rccwAction.setShortcut('q')
        rcwaroundAction.setShortcut('z')
        rccwaroundAction.setShortcut('x')
        biggerAction.setShortcut('b')
        smallerAction.setShortcut('v')


        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(leftAction)
        self.toolbar.addAction(rightAction)
        self.toolbar.addAction(upAction)
        self.toolbar.addAction(downAction)
        self.toolbar.addAction(biggerAction)
        self.toolbar.addAction(smallerAction)
        self.toolbar.addAction(rccwAction)
        self.toolbar.addAction(rcwAction)
        self.toolbar.addAction(rccwaroundAction)
        self.toolbar.addAction(rcwaroundAction)
        self.toolbar.addAction(mirrorAction)
        self.toolbar.addWidget(self.xr)
        self.toolbar.addWidget(self.yr)
        self.toolbar.addWidget(self.enterButton)
        self.setGeometry(300, 300, 380, 370)

        self.star = sevenStar([100,100],50)

        

    def paintEvent(self, e):

        self.qp = QtGui.QPainter()
        self.qp.begin(self)
        self.drawstar()
        self.qp.end()

    def drawstar(self):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        self.qp.setPen(pen)
        for point in self.star.points[:4]:
            i = self.star.points.index(point)
            self.qp.drawLine(point[0],point[1],self.star.points[i+3][0],self.star.points[i+3][1])
            self.qp.drawLine(point[0],point[1],self.star.points[overseven(i)][0],self.star.points[overseven(i)][1])

    def mleft(self):
        for point in self.star.points:
            point[0] = point[0]-20
        self.update()
    def mright(self):
        for point in self.star.points:
            point[0] = point[0]+20
        self.update()
    def mup(self):
        for point in self.star.points:
            point[1] = point[1]-20
        self.update()
    def mdown(self):
        for point in self.star.points:
            point[1] = point[1]+20
        self.update()

    def mbigger(self):
        for point in self.star.points:
            point[0] = point[0]*1.25
            point[1] = point[1]*1.25
        self.update()
    def msmaller(self):
        for point in self.star.points:
            point[0] = point[0]/1.25
            point[1] = point[1]/1.25
        self.update()

    def mrccw(self):
        c = self.star.centerpoint()
        for point in self.star.points:
            point[0] = point[0]-c[0]
            point[1] = point[1]-c[1]
        m = np.matrix(self.star.points)
        m2 = np.matrix([[math.cos(math.pi/15),math.sin(math.pi/15)],[-math.sin(math.pi/15),math.cos(math.pi/15)]])
        m = m*m2
        self.star.points = m.tolist()
        for point in self.star.points:
            point[0] = point[0]+c[0]
            point[1] = point[1]+c[1]
        self.update()
    def mrcw(self):
        c = self.star.centerpoint()

        for point in self.star.points:
            point[0] = point[0]-c[0]
            point[1] = point[1]-c[1]
        m = np.matrix(self.star.points)
        m2 = np.matrix([[math.cos(-math.pi/15),math.sin(-math.pi/15)],[-math.sin(-math.pi/15),math.cos(-math.pi/15)]])
        m = m*m2
        self.star.points = m.tolist()
        for point in self.star.points:
            point[0] = point[0]+c[0]
            point[1] = point[1]+c[1]
        self.update()

    def mrccwaround(self):
        c = self.star.centerpoint()
        for point in self.star.points:
            point[0] = point[0]-int(self.xr.text())
            point[1] = point[1]-int(self.yr.text())
        m = np.matrix(self.star.points)
        m2 = np.matrix([[math.cos(math.pi/15),math.sin(math.pi/15)],[-math.sin(math.pi/15),math.cos(math.pi/15)]])
        m = m*m2
        self.star.points = m.tolist()
        for point in self.star.points:
            point[0] = point[0]+int(self.xr.text())
            point[1] = point[1]+int(self.yr.text())
        self.update()
    def mrcwaround(self):
        c = self.star.centerpoint()

        for point in self.star.points:
            point[0] = point[0]-int(self.xr.text())
            point[1] = point[1]-int(self.yr.text())
        m = np.matrix(self.star.points)
        m2 = np.matrix([[math.cos(-math.pi/15),math.sin(-math.pi/15)],[-math.sin(-math.pi/15),math.cos(-math.pi/15)]])
        m = m*m2
        self.star.points = m.tolist()
        for point in self.star.points:
            point[0] = point[0]+int(self.xr.text())
            point[1] = point[1]+int(self.yr.text())
        self.update()

    def mirror(self):
        c = self.star.centerpoint()

        for point in self.star.points:
            point[0] = point[0]-c[0]
            point[1] = point[1]-c[1]
        for point in self.star.points:
            point[0]*=-1
            point[1]*=-1
        for point in self.star.points:
            point[0] = point[0]+c[0]
            point[1] = point[1]+c[1]
        self.update()

def main():

    app = QtGui.QApplication(sys.argv)
    mw = mainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
