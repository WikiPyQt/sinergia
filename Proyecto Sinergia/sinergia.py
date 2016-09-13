# -*- coding: utf-8 -*-
#############################
import sys, os
import hashlib
#############################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
#.....................................................
from  master import *
from fire import * 

class Principal(QMainWindow):
	"""docstring for Principal"""
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('ui/inicio.ui', self)

		self.setWindowFlags(Qt.SplashScreen)
		self.centrar()
#.............................................................................................
		self.msg4.setGeometry(QRect(440, 25, 21, 21))
		self.msg4.setCursor(Qt.PointingHandCursor)
		self.msg4.setScaledContents(True)
		self.msg4.setPixmap(QPixmap("img/min.ico"))

		self.msg5.setGeometry(QRect(480, 25, 21, 21))
		self.msg5.setCursor(Qt.PointingHandCursor)
		self.msg5.setScaledContents(True)
		self.msg5.setPixmap(QPixmap("img/cierre.ico"))

		self.msg4.mouseReleaseEvent = self.mini
		self.msg5.mouseReleaseEvent = self.salir


		self.btn2.clicked.connect(self.entrar)
		self.btn3.clicked.connect(sys.exit)
#.............................................................................................
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
#.............................................................................................

	def centrar(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

	def salir(self, event):
		sys.exit()

	def mini(self, event):
		self.setWindowState(Qt.WindowMinimized)
# ----------------------------------------------------------------------
	def entrar(self):
			ent = self.ent.text()
			# con = self.txb.text()
			if ent == '':
				self.msg.setText('Campo A Vacio ?')
			else:
				#sql =("SELECT * FROM personal ")
				sql =("SELECT * FROM personal WHERE nombre = '%s' OR correo = '%s' " % (ent, ent) )
				self.datos = conectar(sql) 
				if not self.datos:
					self.msg.setText('Dato no disponible ??')
				else:
					self.contra()

	def contra(self):
		ent2 = self.ent2.text()
		if ent2 == '':
			self.msg.setText('Campo B Vacio ?')
		else:
			cifrado = hashlib.sha1(ent2.encode('utf-8'))
			if cifrado.hexdigest() == self.datos[0][7]:
				# print(self.datos[0][7])
				self.permiso()
			else:
				self.msg.setText('Dato no disponible ??')

	def permiso(self):
		# print('aa')
		nombre = self.datos[0][1].capitalize()
		correo = self.datos[0][2]
		permiso = self.datos[0][8]
		if permiso == 1:
			permiso = 'Admin'
		else:
			permiso = 'Empleado'
		Principal.close(self)

		self.pr = Mast()
		self.pr.show()
		self.pr.msg.setText('Bienvenido(@):' + ' ' + nombre + '\n' + 'Correo:' + ' ' + correo + ' ' + ' Nivel:' + ' ' + str(permiso))
		# self.pr.msg.setText('Correo:' + ' ' + correo + ' ' + ' Nivel:' + ' ' + str(permiso))



# ...........................................................................................................
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ap = Principal()
	ap.show()
	ap.centrar()
	sys.exit(app.exec_())