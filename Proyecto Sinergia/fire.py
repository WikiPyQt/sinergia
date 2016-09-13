# -*- coding: utf-8 -*-
import os, sys
import fdb as sg

#metodo de conexion
def conectar(x):
	# print(x)
	ruta = 'bd/sga.fdb'
	con = sg.connect(
			dsn = ruta,
			user = 'sysdba',
			password = 'sabroso',
			charset ='utf8'		
	)

	cx = con.cursor()
	cx.execute(x)
	if x.startswith("SELECT"):
		datos = cx.fetchall()
	else:
		con.commit()
		datos = None
	cx.close()
	con.close()
	return datos









# a = 'angy'
# b = 'angy@mail.com'
# sql5 = ("SELECT * FROM personal WHERE nombre = '%s' and correo = '%s' " % (a,b ))
# datos = conectar(sql5) 

# # fila = cx.fetchall()
# print(datos[0][7])

# con.commit()
# con.close()
# print('Consulta exitosa !!!!')
# input('')

