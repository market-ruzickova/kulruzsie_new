import geopandas as gpd

from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Load:

    def __init__(self, path):
        self.__data = gpd.read_file(path)

        self.polygony = []

    def readPol(self):
        g = [i for i in self.__data.geometry]
        max_x = -10000000
        min_x = 10000000
        max_y = -10000000
        min_y = 10000000
        for p in range(self.__data.shape[0]):
            pol0 = list(g[p].boundary.coords.xy)
            for i in range(len(pol0[0]) - 1):
                if pol0[0][i] < min_x:
                    min_x = pol0[0][i]
                if pol0[0][i] > max_x:
                    max_x = pol0[0][i]
                if pol0[1][i] < min_y:
                    min_y = pol0[1][i]
                if pol0[1][i] > max_y:
                    max_y = pol0[1][i]
        a = -(max_x + min_x) / 2
        c = -(max_y + min_y) / 2
        if abs(max_x - min_x) >= abs(max_y - min_y):
            b = d = 800 / abs(max_x - min_x)
        else:
            b = d = 550 / abs(max_y - min_y)
        for p in range(self.__data.shape[0]):
            # get x and y coordinates
            pol = list(g[p].boundary.coords.xy)

            polygon = []
            for i in range(len(pol[0]) - 1):
                polygon.append(QPointF((pol[0][i] + a) * b + 450, (-pol[1][i] - c) * d + 320))

            self.polygony.append(polygon)

    def getPol(self, p):

        return QPolygonF(self.polygony[p])

    def number(self):
        n = range(self.__data.shape[0] - 1)
        return n
