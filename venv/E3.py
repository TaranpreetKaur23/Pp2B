"""
Taranpreet Kaur
14/12/2023
ASIXc 1B UF1 Pp2
"""

#Programa que pinta per pantalla un taulell
#d'escacs marcat amb B les caselles blanques, i amb una N les negres.

try:
    Blanc = "B*"
    Negre = "N*"

    for i in range(8):
        for j in range(8):
            casella = Blanc
            if (i + j) % 2 != 0:
                 casella = Negre
            print(casella, end="")
        print()
except ValueError:
    print("No funciona")