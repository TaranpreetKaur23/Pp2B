"""
Taranpreet Kaur
14/12/2023
ASIXc 1B UF1 Pp2
"""

#Indica quantes vegades apareix una lletra dins d'una frase.

try:
    lletra=input("Escriu una lletra: ")
    frase=input("Escriu una frase: ")
    count = len(lletra)
    print(f"La frase {frase} té {count} lletres {lletra}")
except ValueError:
    print("Esta mal")
