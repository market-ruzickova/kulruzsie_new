from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from dialog import *
from QPoint3DF import *
from Edge import *
from triangle import *
from random import *
import random
from math import *
from generate_data import *
from algorithms import *
from polygon import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Points, DT, contour lines, trinagles
        self.__points : list[QPoint3DF] = []
        self.__dt : list[Edge] = []
        self.__contours: list[Edge] = []
        self.__t_contours: list[Edge] = []
        self.__triangles: list[Triangle] = []
        self.__triangles2: list[Triangle] = []
        self.__pols_hypsometrie: list[Polygon] = []
        self.__zmax = 1000
        self.__zmin = 0
        self.__dz = 50

    def mousePressEvent(self, e:QMouseEvent):
        #Left mouse button click
        x = e.position().x()
        y = e.position().y()
        z = random() * 100

        #Create point
        p = QPoint3DF(x,y,z)

        #Append p to point cloude
        self.__points.append(p)

        #Repaint screen
        self.repaint()

    def paintEvent(self, e:QPaintEvent):
        #Draw polygon

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes, edges
        #qp.setPen(Qt.GlobalColor.black)
        #qp.setBrush(Qt.GlobalColor.white)

        # Draw points
        r = 1
        for point in self.__points:
            qp.drawEllipse(int(point.x()) - r, int(point.y()) - r, 2*r, 2*r)

        #Draw aspect
        k = 510 / pi

        #Process triangles one by one
        for t in self.__triangles:
            #Get triangle slope
            slope = t.getSlope()
            #Convert to color
            col = 255 - int(slope * k)
            # Create color
            color = QColor(col, col, col)
            qp.setBrush(color)

            #Create polygon
            pol = QPolygonF([t.getP1(), t.getP2(), t.getP3()])

            #Draw polygon
            qp.drawPolygon(pol)

        for t in self.__triangles2:
            #Get triangle slope
            aspect = t.getAspect()
            #colorize
            if aspect < -2*pi/3:
                r = 255
                g = 0
                b = 0
            elif aspect < -pi/3:
                r = 255
                g = 165
                b = 0
            elif aspect < 0:
                r = 255
                g = 255
                b = 0
            elif aspect < pi/3:
                r = 0
                g = 255
                b = 0
            elif aspect < 2*pi/3:
                r = 0
                g = 0
                b = 255
            else:
                r = 255
                g = 0
                b = 255

            # Shadow
            """
            if aspect < 0:
                r = int(255*(aspect+pi)/pi)
                g = r
                b = r
            else:
                r = int(255*(-aspect+pi)/pi)
                g = r
                b = r
            """
            # Create color
            color = QColor(r, g, b)
            qp.setBrush(color)

            #Create polygon
            pol = QPolygonF([t.getP1(), t.getP2(), t.getP3()])

            #Draw polygon
            qp.drawPolygon(pol)

        for pol in self.__pols_hypsometrie:
            col = int(200 / 1000 * pol.get_Z())

            color = QColor(col, 255 - col, 0)
            qp.setBrush(color)
            qp.setPen(color)

            qp.drawPolygon(QPolygonF(pol.get_pol()))

        # Set attributes
        qp.setPen(Qt.GlobalColor.blue)

        #Draw triangles
        for edge in self.__dt:
            qp.drawLine(int(edge.getStart().x()), int(edge.getStart().y()), int(edge.getEnd().x()), int(edge.getEnd().y()))

        # Set attributes
        qp.setPen(Qt.GlobalColor.darkRed)

        # Draw contour lines
        for edge in self.__contours:
            qp.drawLine(int(edge.getStart().x()), int(edge.getStart().y()), int(edge.getEnd().x()), int(edge.getEnd().y()))

        pen = QPen(Qt.GlobalColor.darkRed,2)
        qp.setPen(pen)

        for edge in self.__t_contours:
            qp.drawLine(int(edge.getStart().x()), int(edge.getStart().y()), int(edge.getEnd().x()), int(edge.getEnd().y()))

        # Set attributes
        # qp.setPen(Qt.GlobalColor.blue)
        # qp.setBrush(Qt.GlobalColor.yellow)

        #End draw
        qp.end()

    def setDT(self, dt : list[Edge]):
        self.__dt = dt

    def setContours(self, contours : list[Edge], Tcontours: list[Edge]):
        self.__contours = contours
        self.__t_contours = Tcontours

    def setSlope(self, triangles : list[Triangle]):
        self.__triangles2.clear()
        self.__triangles = triangles

    def setAspect(self, triangles : list[Triangle]):
        self.__triangles.clear()
        self.__triangles2 = triangles

    def setHypsometrie(self, polygons : list[Polygon]):
        self.__pols_hypsometrie.clear()
        self.__pols_hypsometrie = polygons

    def getPoints(self):
        return self.__points

    def getDT(self):
        return self.__dt

    def getContours(self):
        return self.__contours

    def input(self):
        g = Generate()
        g.GeneratePointCloud()
        n = g.number()
        for p in range(n):
            self.__points.append(g.getPoi(p))
        self.repaint()

    def clearLoadedData(self):
        self.__points.clear()
        self.__dt.clear()
        self.__contours.clear()
        self.__t_contours.clear()
        self.__triangles.clear()
        self.__triangles2.clear()
        self.__pols_hypsometrie.clear()

    def clearAnalysis(self):
        self.__dt.clear()
        self.__contours.clear()
        self.__triangles.clear()
        self.__triangles2.clear()
        self.__t_contours.clear()
        self.__pols_hypsometrie.clear()

    def setContourSettings(self):
        a = Algorithms()
        dialog = InputDialog()
        if dialog.exec():
            zmin,zmax,dz = dialog.getInputs()
            try:
                zmin = int(zmin)
                zmax = int(zmax)
                dz = int(dz)
                self.__zmin = zmin
                self.__zmax = zmax
                self.__dz = dz
            except ValueError:
                zmin, zmax,dz = a.setContourDefaultSettings()
                self.contourInvalidInput()
                self.__zmin = zmin
                self.__zmax = zmax
                self.__dz = dz
        else:
            return

    def getContourParameters(self):
        return self.__zmin, self.__zmax, self.__dz

    def contourInvalidInput(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Wrong Input")
        dlg.setText("Invalid input. Use integer for custom settings. Default settings will be applied(0,1000,50).")
        dlg.exec()