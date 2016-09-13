# -*- coding: utf-8 -*-
#############################
import sys
#############################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from sinergia import *

class Mast(QMainWindow):
	"""docstring for Raiz"""
	def __init__(self):
		super(Mast, self).__init__()
		QMainWindow.__init__(self)

		loadUi('ui/principal.ui', self)
		self.setWindowFlags(Qt.SplashScreen)

		self.minx.setCursor(Qt.PointingHandCursor)
		self.minx.setScaledContents(True)
		self.minx.setPixmap(QPixmap("img/min.ico"))

		self.maxb.setCursor(Qt.PointingHandCursor)
		self.maxb.setScaledContents(True)
		self.maxb.setPixmap(QPixmap("img/min.ico"))

		self.clos.setCursor(Qt.PointingHandCursor)
		self.clos.setScaledContents(True)
		self.clos.setPixmap(QPixmap("img/cierre.ico"))


		self.minx.mouseReleaseEvent = self.mini
		self.maxb.mouseReleaseEvent = self.maxx
		self.clos.mouseReleaseEvent = self.salir
#.........................................................................................
	def salir(self, event):
		sys.exit()

	def mini(self, event):
		self.setWindowState(Qt.WindowMinimized)

	def maxx(self, event):
		self.setWindowState(Qt.WindowMaximized)


# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	ap = Mast()
# 	ap.show()
# 	sys.exit(app.exec_())