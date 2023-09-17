import sympy 
import numpy

#* Se crea la funcion que permite obtener la derivada parcial de cualquier funcion matematica
#*Obtiene como parameto las variables simbolicas y la funcion en cuestion
def getDerivada(variables, funcion):

    #*Se calcula la derivada parcial de ambas variables y se devuelve en
    #* forma de tupla
    #! La libreria sympy permite calcular estas derivadas y obtenerlas de forma simbolica,
    #! es decir, como seria la representacion matematica
    respectoX1 = sympy.diff(funcion, variables[0])
    respectoX2 = sympy.diff(funcion, variables[1])

    return respectoX1, respectoX2

#*Se crean los valores simbolicos, es decir, que variables usa la funcion
#* En este caso seran x1 y x2 porque la actividad lo requiere
x1, x2 = sympy.symbols('x1 x2')

#*Se crea una variable que contiene la funcion
#! El metodo exp se usa para representar el numero de euler
func = 10 - sympy.exp(-(x1**2 + 3*x2**2))

print(f"Las derivadas parciales son: {getDerivada((x1,x2),func)}")