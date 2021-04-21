from tkinter import *

ventana = Tk()
ventana.title("calculadora")

#entrada
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row=0, column =0, columnspan=4, padx=5,pady=5)

i=0
total=0
#funciones
def click_boton(valor):
	global i
	e_texto.insert(i, valor)
	i += 1

def borra():
	e_texto.delete(0,END)
	i=0

def opera():
	ecu = e_texto.get()
	resultado = eval(ecu)
	e_texto.delete(0,END)
	e_texto.insert(0,resultado)
	i=0

#botones
boton1 = Button(ventana, text="1", width = 5,height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text="2", width = 5,height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text="3", width = 5,height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text="4", width = 5,height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text="5", width = 5,height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text="6", width = 5,height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text="7", width = 5,height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text="8", width = 5,height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text="9", width = 5,height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text="0", width = 5,height = 2, command = lambda: click_boton(0))

boton_borra = Button(ventana, text="AC", width = 5,height = 2, command = lambda: borra())
boton_par1 = Button(ventana, text="(", width = 5,height = 2, command = lambda: click_boton("("))
boton_par2 = Button(ventana, text=")", width = 5,height = 2, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width = 5,height = 2, command = lambda: click_boton("."))

boton_div = Button(ventana, text="/", width = 5,height = 2, command = lambda: click_boton("/"))
boton_mul = Button(ventana, text="x", width = 5,height = 2, command = lambda: click_boton("*"))
boton_sum = Button(ventana, text="+", width = 5,height = 2, command = lambda: click_boton("+"))
boton_res = Button(ventana, text="-", width = 5,height = 2, command = lambda: click_boton("-"))
boton_igu = Button(ventana, text="=", width = 5,height = 2, command = lambda: opera())

#botones en pantalla
boton7.grid(row=1 ,column = 0,padx = 5,pady = 5)
boton8.grid(row=1 ,column = 1,padx = 5,pady = 5)
boton9.grid(row=1 ,column = 2,padx = 5,pady = 5)
boton_div.grid(row=1 ,column = 3,padx = 5,pady = 5)

boton4.grid(row=2 ,column = 0,padx = 5,pady = 5)
boton5.grid(row=2 ,column = 1,padx = 5,pady = 5)
boton6.grid(row=2 ,column = 2,padx = 5,pady = 5)
boton_mul.grid(row=2 ,column = 3,padx = 5,pady = 5)

boton1.grid(row=3 ,column = 0,padx = 5,pady = 5)
boton2.grid(row=3 ,column = 1,padx = 5,pady = 5)
boton3.grid(row=3 ,column = 2,padx = 5,pady = 5)
boton_res.grid(row=3 ,column = 3,padx = 5,pady = 5)

boton_borra.grid(row=4 ,column = 0,padx = 5,pady = 5)
boton0.grid(row=4 ,column = 1,padx = 5,pady = 5)
boton_igu.grid(row=4 ,column = 2,padx = 5,pady = 5)
boton_sum.grid(row=4 ,column = 3,padx = 5,pady = 5)


ventana.mainloop()