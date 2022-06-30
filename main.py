import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('640x470') 
ventana.title('Conversor de Unidades.exe')
ventana.configure(bg = 'cyan2')
ventana.resizable(False, False)

fuente1 = font.Font(family = 'Arial', size = '30' )
fuente2 = font.Font(family = 'Arial', size = '20' )
fuente3 = font.Font(family = 'Arial', size = '10' )



number_from = StringVar()


def fromfunc(event):
    global result_from
    result_from = event.widget.get()


def tofunc(event):
    global result_to
    result_to = event.widget.get()


def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error','Dato Inválido')
    
    #Volumen
    if result_from == 'Metros Cúbicos' and result_to == 'Metros Cúbicos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Metros Cúbicos' and result_to == 'Litros':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Metros Cúbicos' and result_to == 'Galones':
        calculate = number1*264.172
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metros Cúbicos' and result_to == 'Centimetros cúbicos':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Litros' and result_to == 'Litros':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Litros' and result_to == 'Metros Cúbicos':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Litros' and result_to == 'Galones':
        calculate = number1*0.26417
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Litros' and result_to == 'Centimetros cúbicos':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Galones' and result_to == 'Metros Cúbicos':
        calculate = number1*0.003785
        result.cget('text')
        result.configure(text = (calculate,result_to))


    elif result_from == 'Galones' and result_to == 'Litros':
        calculate = number1*3.7854
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Galones' and result_to == 'Galones':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Galones' and result_to == 'Centimetros cúbicos':
        calculate = number1*3786.41
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimetros cúbicos' and result_to == 'Metros Cúbicos':
        calculate = number1*9.99999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    
    elif result_from == 'Centimetros cúbicos' and result_to == 'Litros':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimetros cúbicos' and result_to == 'Metros Cúbicos':
        calculate = number1*9.9999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimetros cúbicos' and result_to == 'Litros':
        calculate = number1*0.00099999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimetros cúbicos' and result_to == 'Galones':
        calculate = round(number1*0.00026417,2)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimetros cúbicos' and result_to == 'Centimetros cúbicos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    #Longitud
    elif result_from == 'Centimetros' and result_to == 'Centimetros':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centimetros' and result_to == 'Metros':
        calculate = number1/(10**2)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centimetros' and result_to == 'Kilometros':
        calculate = number1/(10**5)
        result.cget('text')
        result.configure(text = (calculate,result_to))


    elif result_from == 'Metros' and result_to == 'Metros':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Metros' and result_to == 'Centimetros':
        calculate = number1*(10**2)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Metros' and result_to == 'Kilometros':
        calculate = number1/(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))


    elif result_from == 'Kilometros' and result_to == 'Kilometros':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilometros' and result_to == 'Centimetros':
        calculate = number1*(10**5)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilometros' and result_to == 'Metros':
        calculate = number1*(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    

    #Masa
    elif result_from == 'Kilogramos' and result_to == 'Kilogramos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilogramos' and result_to == 'Gramos':
        calculate = number1*(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilogramos' and result_to == 'Miligramos':
        calculate = number1*(10**6)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilogramos' and result_to == 'Toneladas':
        calculate = number1/(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))



    elif result_from == 'Gramos' and result_to == 'Gramos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Gramos' and result_to == 'Kilogramos':
        calculate = number1/(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Gramos' and result_to == 'Miligramos':
        calculate = number1*(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Gramos' and result_to == 'Toneladas':
        calculate = number1/(10**6)
        result.cget('text')
        result.configure(text = (calculate,result_to))



    elif result_from == 'Miligramos' and result_to == 'Miligramos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Miligramos' and result_to == 'Kilogramos':
        calculate = number1/(10**6)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Miligramos' and result_to == 'Gramos':
        calculate = number1/(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Miligramos' and result_to == 'Toneladas':
        calculate = number1/(10**9)
        result.cget('text')
        result.configure(text = (calculate,result_to))



    elif result_from == 'Toneladas' and result_to == 'Toneladas':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Toneladas' and result_to == 'Kilogramos':
        calculate = number1*(10**3)
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Toneladas' and result_to == 'Gramos':
        calculate = number1*(10**6)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Toneladas' and result_to == 'Miligramos':
        calculate = number1*(10**9)
        result.cget('text')
        result.configure(text = (calculate,result_to))


    #Velocidad
    elif result_from == 'm/s' and result_to == 'm/s':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'm/s' and result_to == 'Km/h':
        calculate = round((number1*(1/3.6)),2)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Km/h' and result_to == 'Km/h':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Km/h' and result_to == 'm/s':
        calculate = round((number1*3.6),2)
        result.cget('text')
        result.configure(text = (calculate,result_to))   
    
    
    #Tiempo
    elif result_from == 'Segundos' and result_to == 'Segundos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Segundos' and result_to == 'Minutos':
        calculate = (number1/60)
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Segundos' and result_to == 'Horas':
        calculate = number1/3600
        result.cget('text')
        result.configure(text = (calculate,result_to))



    elif result_from == 'Minutos' and result_to == 'Minutos':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Minutos' and result_to == 'Segundos':
        calculate = number1*60
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Minutos' and result_to == 'Horas':
        calculate = number1/60
        result.cget('text')
        result.configure(text = (calculate,result_to))



    elif result_from == 'Horas' and result_to == 'Horas':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Horas' and result_to == 'Segundos':
        calculate = number1*3600
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Horas' and result_to == 'Minutos':
        calculate = number1*60
        result.cget('text')
        result.configure(text = (calculate,result_to))

# Menús
def selected(event):
    unit = event.widget.get()
    if unit == 'Volumen':
        fromdd['values'] = ('Metros Cúbicos',
                            'Litros',
                            'Galones',
                            'Centimetros cúbicos')

        todd['values'] = ('Metros Cúbicos',
                            'Litros',
                            'Galones',
                            'Centimetros cúbicos')

    elif unit == 'Longitud':
        fromdd['values'] = ('Centimetros','Metros',
                            'Kilometros')

        todd['values'] = ('Centimetros','Metros',
                            'Kilometros')

    elif unit == 'Masa':
        fromdd['values'] = ('Kilogramos',
                            'Gramos',
                            'Miligramos',
                            'Toneladas')

        todd['values'] = ('Kilogramos',
                            'Gramos',
                            'Miligramos',
                            'Toneladas')
    
    elif unit == 'Velocidad':    
        fromdd['values'] = ('m/s',
                            'Km/h')

        todd['values'] = ('m/s',
                            'Km/h')
    elif unit == 'Tiempo':
        fromdd['values'] = ('Segundos',
                            'Millisegundos',
                            'Microsegundos',
                            'Nanosegundos',
                            'Horas')

        todd['values'] = ('Segundos','Minutos',
                            'Horas')

        
    



main = tk.Label(ventana,text = 'Proyecto: Conversor de Unidades', bg = 'cyan2')
main['font']  = fuente1 
main.place(relx = '0.48', rely = '0.1', anchor = 'center')


unit = tk.Label(ventana,text = 'Magnitud:',bg = 'cyan2')
unit['font'] = fuente3
unit.place(relx = '0.288',rely = '0.28')


n = StringVar()
unitdd = ttk.Combobox(ventana,width = '35',textvariable = n)


unitdd['values'] = ('Volumen',
                    'Longitud',
                    'Masa',
                    "Velocidad",
                    "Tiempo")

unitdd.place(relx = '0.57',rely = '0.3',anchor = 'center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)


label_from = tk.Label(ventana,text = 'Unidad original:',bg = 'cyan2')
label_from['font'] = fuente3
label_from.place(relx = '0.238',rely = '0.37')


f = StringVar()
fromdd = ttk.Combobox(ventana,width = '35',textvariable = f)

fromdd.place(relx = '0.57',rely = '0.39',anchor = 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

# entrada de datos
label_fro = tk.Label(ventana,text = 'ingrese la cantidad:',bg = 'cyan2')
label_fro['font'] = fuente3
label_fro.place(relx = '0.2',rely = '0.53')
num_from = tk.Entry(ventana,width = 38,textvariable = number_from)
num_from.place(relx = '0.390',rely = '0.53')

answer = partial(answer,num_from)


to = tk.Label(ventana,text = 'Unidad final:',bg = 'cyan2')
to['font'] = fuente3
to.place(relx = '0.265',rely = '0.45')


t = StringVar()
todd = ttk.Combobox(ventana,width = 35,textvariable = t)

todd.place(relx = '0.57',rely = '0.47',anchor = 'center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)


result = tk.Label(ventana,text = 'Resultado',bg= 'white',width = 25)
result['font'] = fuente2
result.place(relx = '0.21',rely = '0.6')


get_answer = tk.Button(ventana,text = 'Convertir',bg = 'red',command = answer)
get_answer['font'] = fuente3
get_answer.place(relx = '0.46',rely = '0.7')



ventana.mainloop()

