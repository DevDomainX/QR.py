#!/usr/bin env python3
import qrcode


print("""     
Creador  :         Hans Saldias

Crear codigo qr con cualquier texto o links

Lenguaje :         python

\n""")


def code():
    while True:
        texto = input("Ingresa el texto o link:  ")
        imagen = qrcode.make(texto)
        imagen.save("codigoqr.png")
       
print(imagen)