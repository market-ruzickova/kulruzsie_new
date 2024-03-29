from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
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
        self.actionExit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_DT = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/triangles2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_DT.setIcon(icon2)
        self.actionCreate_DT.setObjectName("actionCreate_DT")
        self.actionCreate_contour_lines = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/contours2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_contour_lines.setIcon(icon3)
        self.actionCreate_contour_lines.setObjectName("actionCreate_contour_lines")
        self.actionAnalyze_slope = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/slope2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyze_slope.setIcon(icon4)
        self.actionAnalyze_slope.setObjectName("actionAnalyze_slope")
        self.actionAnalyze_aspect = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/orientation2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyze_aspect.setIcon(icon5)
        self.actionAnalyze_aspect.setObjectName("actionAnalyze_aspect")
        self.actionParameters = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionParameters.setIcon(icon6)
        self.actionParameters.setObjectName("actionParameters")
        self.actionClear_results = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon7)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(MainWindow)
        self.actionClear_all.setIcon(icon7)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionHypsometry = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/contours3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHypsometry.setIcon(icon8)
        self.actionHypsometry.setObjectName("actionHypsometry")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAnalysis.addAction(self.actionCreate_DT)
        self.menuAnalysis.addAction(self.actionCreate_contour_lines)
        self.menuAnalysis.addAction(self.actionAnalyze_slope)
        self.menuAnalysis.addAction(self.actionAnalyze_aspect)
        self.menuAnalysis.addAction(self.actionHypsometry)
        self.menuSettings.addAction(self.actionParameters)
        self.menuView.addAction(self.actionClear_results)
        self.menuView.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_DT)
        self.toolBar.addAction(self.actionCreate_contour_lines)
        self.toolBar.addAction(self.actionAnalyze_slope)
        self.toolBar.addAction(self.actionAnalyze_aspect)
        self.toolBar.addAction(self.actionHypsometry)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionParameters)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)

        #Connect signals and slots
        self.actionCreate_DT.triggered.connect(self.runDT)
        self.actionCreate_contour_lines.triggered.connect(self.runContourLines)
        self.actionAnalyze_slope.triggered.connect(self.runSlope)
        self.actionAnalyze_aspect.triggered.connect(self.runAspect)
        self.actionOpen.triggered.connect(self.Open)
        self.actionExit.triggered.connect(self.exit)
        self.actionClear_all.triggered.connect(self.Clear_data)
        self.actionClear_results.triggered.connect(self.Clear_analysis)
        self.actionParameters.triggered.connect(self.settings)
        self.actionHypsometry.triggered.connect(self.runHypsometrie)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DTM analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Generate point cloud"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Generate data"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionCreate_DT.setText(_translate("MainWindow", "Create DT"))
        self.actionCreate_DT.setToolTip(_translate("MainWindow", "Create Delaunay triangulation"))
        self.actionCreate_contour_lines.setText(_translate("MainWindow", "Create contour lines"))
        self.actionAnalyze_slope.setText(_translate("MainWindow", "Analyze slope"))
        self.actionAnalyze_slope.setToolTip(_translate("MainWindow", "Analyze slope of DTM triangles"))
        self.actionAnalyze_aspect.setText(_translate("MainWindow", "Analyze aspect"))
        self.actionAnalyze_aspect.setToolTip(_translate("MainWindow", "Analyze aspect of DTM"))
        self.actionParameters.setText(_translate("MainWindow", "Parameters"))
        self.actionParameters.setToolTip(_translate("MainWindow", "Parameters"))
        self.actionHypsometry.setText(_translate("MainWindow", "Color hypsometry"))
        self.actionHypsometry.setToolTip(_translate("MainWindow", "Color hypsometry"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))

    def runDT(self):
        #Get points
        points = self.Canvas.getPoints()

        #Run triangulation
        a = Algorithms()
        dt = a.createDT(points)

        #Set results to draw
        self.Canvas.setDT(dt)
        self.Canvas.repaint()

    def runContourLines(self):
        # Set parameters of contour lines
        zmin, zmax, dz = self.Canvas.getContourParameters()
        DZ = dz*5

        # Get DT
        dt = self.Canvas.getDT()

        #Create contour lines
        a = Algorithms()
        contours = a.createContourLines(dt, zmin, zmax, dz)
        Tcontours = a.createContourLines(dt, zmin, zmax, DZ)
        #Set resulzs to draw
        self.Canvas.setContours(contours,Tcontours)
        self.Canvas.repaint()

    def runSlope(self):
        # Set parameters of contour lines
        # Get DT
        dt = self.Canvas.getDT()

        #Create contour lines
        a = Algorithms()
        dtm = a.analyzeDTMSlope(dt)

        #Set resulzs to draw
        self.Canvas.setSlope(dtm)
        self.Canvas.repaint()

    def runAspect(self):
        # Get DT
        dt = self.Canvas.getDT()

        # Create contour lines
        a = Algorithms()
        dtm = a.analyzeAspect(dt)

        # Set resulzs to draw
        self.Canvas.setAspect(dtm)
        self.Canvas.repaint()

    def runHypsometrie(self):
        a = Algorithms()

        self.Canvas.setHypsometrie(a.hypsometrie(self.Canvas.getDT(), self.Canvas.getContours()))
        self.Canvas.repaint()

    def Open(self):
        ui.Canvas.clearLoadedData()
        self.Canvas.input()
        self.Canvas.repaint()

    def exit(self):
        quit()

    def Clear_data(self):
        ui.Canvas.clearLoadedData()
        self.Canvas.repaint()

    def Clear_analysis(self):
        ui.Canvas.clearAnalysis()
        self.Canvas.repaint()

    def settings(self):
        self.Canvas.setContourSettings()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
