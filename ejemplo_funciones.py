#!/usr/bin/python3

#guardar en la carpeta del proyecto
#x:\laragon\www\holamundo
# con el nombre de 'ejemplo_fuciones.y'

# las fuciones en python se definen con def:

def funcion_tonta(nombre) :
    separador = " "
    mensaje = separador.join(("oh", "el tonto de",nombre))
    print(mensaje)

# y llamamos a la funcion...
funcion_tonta("Gatosu")
funcion_tonta("Gatocrack")

# una funcion un poquito mas compleja: calculo de digito
# verificador de rut chileno. use solo tabs, no espacios

def digito_verificador(rut):
    digito = ""
    contador = 2
    suma = 0
    multiplo = 0
    while rut > 0:
        multiplo = ( rut % 10 ) * contador
        suma = suma + multiplo
        rut = rut // 10 # division entera!
        contador = contador + 1
        if contador == 8 :
            contador = 2
    digito = 11 - ( suma % 11 )
    if digito == 11:
        digito = 0
    if digito == 10 :
        digito = "k"
    return str(digito)

mi_rut = 5411317
print("-".join((str(mi_rut), digito_verificador(mi_rut))))


# para que los cmabios se guarden en github master...
# github add ejemplo_funcines.py
# git commit -m "Agregamos ejemplo funciones"
# git checkout master
# git pull
# git merge dm_ejemplo_funciones
# git push