import os
z= "registro.txt"

class usuario ():
		def crear (self):
			self.nombre = input ('Nombre: ')
			self.apellido = input ('Apellido:')
			self.correo = input ('Correo: ')
			self.contraseña = input ('Contraseña: ')

def write (f,b):
		f1=open('registro.txt', 'a')
		f1.write (b)
		f1.close ()
	
def Calculadora():
    print ("""Calculadora
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir
    """)
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese el primer numero:\n"))
        y = int(input("Ingrese el segundo numero:\n"))
        if (opc==1):
            print ("La Suma es:", x+y)
            opc = int(input("Selecione ujna opcion\n"))
        elif(opc==2):
            print ("La Resta es:",x-y)
            opc = int(input("Selecione una opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("Selecione una opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:", x/y)
              opc = int(input("Selecione una opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Selecione una pcion\n"))
			
ses=usuario()
archivo= "registro.txt"
list = []

while True:
	print ('1.Iniciar Sesion')
	print ('2. Registrarse')
	print ('3.Salir')
	opci= int(input ('Ingrese la opcion deseada: '))
	os.system ('cls')
	
	if opci==1:
		cor = input ('Correo: ')
		con = input ('Contraseña: ')
		f= open('registro.txt', 'r')
		while True: 
			l = f.readline()
			if not l: 
				print ('')
				s= input ('Presione ENTER para continuar')
				os.system ('cls')
				break
			elif l.split("/")[2]==cor and l.split("/")[3]==con:
				os.system('cls')
				Calculadora()
				break 
			elif cor=="administrador" and con== l.split ("/")[3]: #El usuario que desee tener los derechos de admi deberá registrarse
				f= open('registro.txt', 'r')					  #con su correo administrador y su clave admi
				while True:
					l= f.readline()
					print(l)
					print ('')
					if not l: 
						break
		os.system ('cls')
		f.close()

	if opci==2:
		ses.crear()
		d= ses.nombre+ "/" + ses.apellido + "/" + ses.correo + "/" +ses.contraseña + "/" + "\n"
		write (archivo, d)
		os.system ('cls')
		
	if opci==3:
		break
