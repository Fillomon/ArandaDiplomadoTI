#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
# radious of circle inscribed in a tringle
import math
#solicitamos el valor al usuario, el cual antes de almacenarse en la variable se convierte en dato tipo flotante
a=float(input("Igrese el valor del lado a: "))
b=float(input("Igrese el valor del lado b: "))
c=float(input("Igrese el valor del lado c: "))

#realizamos una suma para validar que el lado c del triangulo no sea mayor de la suma de los lados a+b
su=a+b
if (c < su):
    s=0.5*(a+b+c)
    r=math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    rad = round(r, 2)
    sum = round(s, 2)
    print("Semiperimetro=")
    print(sum)
    print("Radio=")
    print(rad)
else:
    print("Error Verifique, El lado C no puede ser mayor a la suma de los lados a y b")
    