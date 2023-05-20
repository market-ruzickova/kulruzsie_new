# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from algorithms import *
from load import Load as LoadSHP


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Load = QtWidgets.QFileDialog(MainWindow)
        self.Canvas = Draw(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuElement = QtWidgets.QMenu(self.menubar)
        self.menuElement.setObjectName("menuElement")
        self.menuSimplify = QtWidgets.QMenu(self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionElement = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/element.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionElement.setIcon(icon1)
        self.actionElement.setObjectName("actionElement")
        self.actionBarrier = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/barrier.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBarrier.setIcon(icon2)
        self.actionBarrier.setObjectName("actionBarrier")
        self.actionDisplace_1_element = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/displace.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDisplace_1_element.setIcon(icon3)
        self.actionDisplace_1_element.setObjectName("actionDisplace_1_element")
        self.actionClear = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon4)
        self.actionClear.setObjectName("actionClear")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionOpen)
        self.menuElement.addAction(self.actionElement)
        self.menuElement.addAction(self.actionBarrier)
        self.menuSimplify.addAction(self.actionDisplace_1_element)
        self.menuSimplify.addSeparator()
        self.menuSimplify.addAction(self.actionClear)
        self.menuOptions.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuElement.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionElement)
        self.toolBar.addAction(self.actionBarrier)
        self.toolBar.addAction(self.actionDisplace_1_element)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)

        #User-defined actions
        self.actionDisplace_1_element.triggered.connect(self.displaceClick)
        self.actionElement.triggered.connect(self.drawLineClick)
        self.actionBarrier.triggered.connect(self.drawBarrierClick)
        self.actionClear.triggered.connect(self.clearClick)
        self.actionOpen.triggered.connect(self.load)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuElement.setTitle(_translate("MainWindow", "Input"))
        self.menuSimplify.setTitle(_translate("MainWindow", "Simplify"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Load barrier, then element"))
        self.actionElement.setText(_translate("MainWindow", "Element"))
        self.actionBarrier.setText(_translate("MainWindow", "Barrier"))
        self.actionDisplace_1_element.setText(_translate("MainWindow", "Displace 1 element"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

    def displaceClick(self):
        #Get polyline and barrier
        L = self.Canvas.getL()
        B = self.Canvas.getB()

        # Set parameters
        dmin = 100
        alpha = 0.3
        beta = 1000
        gamma = 1000
        lam = 20
        iters = 500

        #Run displacement
        a = Algorithms()
        d, xq, yq = a.getPointLineDistance(100, 100, 0, 100, 100, 90)
        LD = a.minEnergySpline(L, B, alpha, beta, gamma, lam, dmin, iters)

        #Set results
        self.Canvas.setLD(LD)

        #Repaint
        self.Canvas.repaint()

    def drawLineClick(self):
        self.Canvas.setSource(True)

    def drawBarrierClick(self):
        self.Canvas.setSource(False)

    def clearClick(self):
        self.Canvas.clearAll()
        self.Canvas.repaint()

    def load(self):
        data = LoadSHP(self.Load.getOpenFileName()[0])
        data.readPolyline()
        for p in data.number():
            self.Canvas.setL(data.getPol(p))

        data = LoadSHP(self.Load.getOpenFileName()[0])
        data.readPolyline()
        for p in data.number():
            self.Canvas.setB(data.getPol(p))

        self.Canvas.repaint()


from draw import Draw


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
