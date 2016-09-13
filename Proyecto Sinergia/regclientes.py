# -*- encoding: utf-8 -*-
#############################
import sys, os
from shutil import *
# import qdarkstyle
from funciones import *
###############
import hashlib
################
from PyQt5.QtWidgets import *
##############################
from PyQt5.QtGui import *
############################
from PyQt5.QtCore import *
############################


class Registrar(QMainWindow):

	def __init__(self):
		super(Registrar, self).__init__()
		self.setWindowTitle('     Registar Clientes !!!!')
		self.setWindowIcon(QIcon('img/gato.jpg'))
		self.resize(800, 620)
		self.setFixedSize(800, 620)

		flags = Qt.MSWindowsFixedSizeDialogHint            
		flags2 = Qt.X11BypassWindowManagerHint
		flags3 = Qt.FramelessWindowHint
		flags4 = Qt.WindowTitleHint
		flags5 = Qt.WindowSystemMenuHint
		flags6 = Qt.WindowMinimizeButtonHint
		flags7 = Qt.WindowMaximizeButtonHint
		flags8 = Qt.WindowCloseButtonHint
		flags9 = Qt.WindowContextHelpButtonHint
		flags10 = Qt.WindowShadeButtonHint
		flags11 = Qt.WindowStaysOnTopHint
		flags12 = Qt.WindowStaysOnBottomHint
		flags13 = Qt.CustomizeWindowHint
		f = Qt.X11BypassWindowManagerHint
		a = Qt.SplashScreen
		# self.setContentsMargins(QMargins())
		self.setWindowFlags(Qt.FramelessWindowHint)
		# self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
		# self.setContentsMargins(QMargins())
########################################
		self.grilla = QWidget()
		self.grilla.setObjectName('gr')
		self.setCentralWidget(self.grilla)

#########################################
		# self.centrar()

#########################################
		self.msg = QLabel(self.grilla)
		self.msg.setObjectName('c')
		self.msg.setText('')
		self.msg.setFrameShape(QFrame.Box)
		self.msg.setFrameShadow(QFrame.Sunken)
		self.msg.setAlignment(Qt.AlignCenter)
		self.msg.setGeometry(140, 30, 611, 31)

		self.gr = QWidget(self.grilla)
		self.gr.setGeometry(QRect(40, 65, 711, 271))

		self.grid = QGridLayout(self.gr)
		self.grid.setContentsMargins(0, 0, 0, 0)
####################################
		self.a = QLabel(self.gr)
		self.a.setText('Nombre:')
		self.a.setObjectName("a")
		self.grid.addWidget(self.a, 0, 0, 1, 1)

		self.g = QLabel(self.gr)
		self.g.setText('Apellido:')
		self.g.setObjectName("a")
		self.grid.addWidget(self.g, 1, 0, 1, 1)

		self.d = QLabel(self.gr)
		self.d.setText('Correo :')
		self.d.setObjectName("a")
		self.grid.addWidget(self.d, 2, 0, 1, 1)

		self.e = QLabel(self.gr)
		self.e.setText('Funcion:')
		self.e.setObjectName("a")
		self.grid.addWidget(self.e, 3, 0, 1, 1)

		self.h = QLabel(self.gr)
		self.h.setText('Fecha reg:')
		self.h.setObjectName("a")
		self.grid.addWidget(self.h, 4, 0, 1, 1)

		self.f = QLabel(self.gr)
		self.f.setText('Tel Celular:')
		self.f.setObjectName("a")
		self.grid.addWidget(self.f, 0, 3, 1, 1)

		self.c = QLabel(self.gr)
		self.c.setText('Tel Trabajo:')
		self.c.setObjectName("a")
		self.grid.addWidget(self.c, 1, 3, 1, 1)

		self.b = QLabel(self.gr)
		self.b.setText('Tel Casa:')
		self.b.setObjectName("a")
		self.grid.addWidget(self.b, 2, 3, 1, 1)

		self.j = QLabel(self.gr)
		self.j.setText('Facebook:')
		self.j.setObjectName("a")
		self.grid.addWidget(self.j, 3, 3, 1, 1)

		self.k = QLabel(self.gr)
		self.k.setText('Twitter:')
		self.k.setObjectName("a")
		self.grid.addWidget(self.k, 4, 3, 1, 1)

		self.i = QLabel(self.gr)
		self.i.setText('WhatsApp:')
		self.i.setObjectName("a")
		self.grid.addWidget(self.i, 5, 3, 1, 1)
#################################################
		self.nom = QLineEdit(self.gr)
		self.nom.setPlaceholderText('Nom')
		self.nom.setObjectName('f')
		self.grid.addWidget(self.nom, 0, 2, 1, 1)

		self.ap = QLineEdit(self.gr)
		self.ap.setPlaceholderText('Ape')
		self.ap.setObjectName('f')
		self.grid.addWidget(self.ap, 1, 2, 1, 1)

		self.cor= QLineEdit(self.gr)
		self.cor.setPlaceholderText('Corr')
		self.cor.setObjectName('f')
		self.grid.addWidget(self.cor, 2, 2, 1, 1)

		self.fun = QLineEdit(self.gr)
		self.fun.setPlaceholderText('Fun')
		self.fun.setObjectName('f')
		self.grid.addWidget(self.fun, 3, 2, 1, 1)

		self.ch = QDateEdit(self.gr)
		self.ch.setDate(QDate.currentDate())
		# self.ch.setFrame(True)
		self.ch.setAlignment(Qt.AlignCenter)
		self.ch.setCalendarPopup(True)
		self.ch.setObjectName("dateEdit")
		self.grid.addWidget(self.ch, 4, 2, 1, 1)

		self.telm = QLineEdit(self.gr)
		self.telm.setPlaceholderText('Cel')
		self.telm.setObjectName('f')
		self.grid.addWidget(self.telm, 0, 4, 1, 1)

		self.telt = QLineEdit(self.gr)
		self.telt.setPlaceholderText('Trabj')
		self.telt.setObjectName('f')
		self.grid.addWidget(self.telt, 1, 4, 1, 1)

		self.telc = QLineEdit(self.gr)
		self.telc.setPlaceholderText('Casa')
		self.telc.setObjectName('f')
		self.grid.addWidget(self.telc, 2, 4, 1, 1)

		self.fac = QLineEdit(self.gr)
		self.fac.setPlaceholderText('Fac')
		self.fac.setObjectName('f')
		self.grid.addWidget(self.fac, 3, 4, 1, 1)

		self.tw = QLineEdit(self.gr)
		self.tw.setPlaceholderText('Twitter')
		self.tw.setObjectName('f')
		self.grid.addWidget(self.tw, 4, 4, 1, 1)

		self.cd = QCheckBox(self.gr)
		self.cd.setObjectName('f')
		self.grid.addWidget(self.cd, 5, 4, 1, 1)
###################################################
		self.gri = QWidget(self.grilla)
		self.gri.setGeometry(QRect(40, 345, 711, 194))

		self.gridd = QGridLayout(self.gri)
		self.gridd.setContentsMargins(0, 0, 0, 0)

		self.lbl = QLabel(self.gri)
		self.lbl.setText('Observ:')
		self.lbl.setObjectName("a")
		self.gridd.addWidget(self.lbl, 0, 0, 1, 1)

		self.lbla = QLabel(self.gri)
		self.lbla.setText('Foto:')
		self.lbla.setObjectName("a")
		self.gridd.addWidget(self.lbla, 0, 2, 1, 1)

		self.ed = QTextEdit(self.gri)
		self.ed.setObjectName("textEdit")
		self.gridd.addWidget(self.ed, 0, 1, 2, 1)

		self.mg = QGraphicsView(self.gri)
		self.mg.setObjectName("graphicsView")
		self.gridd.addWidget(self.mg, 0, 3, 2, 1)

##################################################
		self.btn = QPushButton(self.grilla)
		self.btn.setObjectName('c')
		self.btn.setCursor(Qt.OpenHandCursor)
		self.btn.setGeometry(QRect(204, 555, 181, 41))
		self.btn.setAutoDefault(True)
		self.btn.setText('Registrar')

		self.btn2 = QPushButton(self.grilla)
		self.btn2.setObjectName('d')
		self.btn2.setCursor(Qt.OpenHandCursor)
		self.btn2.setGeometry(QRect(400, 555, 181, 41))
		self.btn2.setAutoDefault(True)
		self.btn2.setText('Salir')

		self.btn3 = QPushButton(self.gr)
		self.btn3.setObjectName('d')
		self.btn3.setCursor(Qt.OpenHandCursor)
		self.grid.addWidget(self.btn3, 5, 0, 1, 3)
		self.btn3.setAutoDefault(True)
		self.btn3.setText('Subir foto')

		self.btn4 = QPushButton(self.grilla)
		self.btn4.setObjectName('d')
		self.btn4.setCursor(Qt.OpenHandCursor)
		self.btn4.setGeometry(QRect(750, 5, 18, 30))
		self.btn4.setText('-')

		self.btn3.clicked.connect(self.abrir)
		self.btn2.clicked.connect(self.salir)
		self.btn4.clicked.connect(self.min)
		# self.btn3.clicked['bool'].connect(lambda state)
########################################################		
	def abrir(self):
		ruta = 'fotos'
		fichero = QFileDialog.getOpenFileName(self, "Subir archivo",
                QDir.currentPath())
		destino = os.path.split(fichero[0])[-1] 
		# print(destino)
		img = QImage(fichero[0])
		folder = os.path.join(os.getcwd(), ruta)
		if not os.path.exists(folder):
			os.makedirs(folder)
		directorio = os.path.join(folder, destino)
		# print(directorio)
		response = img.save(directorio)
		if response:
			self.msg.setText("Imagen subida exitosamente")
		else:
			self.msg.setText("Solo imagenes")
################################################
	def salir(self):
		sys.exit()
######################################################
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()
####################################################
	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.dragPos = event.globalPos()
			event.accept()
#####################################################
	def min(self):
		self.setWindowState(Qt.WindowMinimized)
		# sender = self.sender()
		# self.statusBar().showMessage(msg)	
########################################################


###################################################
if __name__ == "__main__":
	app = QApplication(sys.argv)

	# with open('temas/tm.qss', 'r') as e:
	# 	estilo = e.read()
	# app.setStyleSheet(estilo)
	ap = Registrar()
	ap.show()
	sys.exit(app.exec_())
######################################################