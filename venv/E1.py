"""
Taranpreet Kaur
14/12/2023
ASIXc 1B UF1 Pp2
"""
#Escriu un programa que llegeixi un nombre, enter positiu,
#i determini la quantitat de dígits que té.

try:
    numero=int(input("Escriu un nombre enter positiu: "))
    dígits=2
    print (f"El número {numero} té {dígits} dígits.")

except ValueError:
    print("Esta mal")