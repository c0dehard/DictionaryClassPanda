import os
os.system('cls' if os.name == 'nt' else 'clear')

def durchschnittVon(eingabe,delimiter = " "):
    """==
    WICHTIG: Delimiter wird berücksichtigt.\n
    Sofern nichts angegeben ist ein Leerzeichen der Delimiter.\n
    Nimmt Werte und berechnet die durchschnittliche Länge. Generell gilt :                                     
    Summe aller Zahlen durch die Anzahl der Zahlen  ist  der Durchschnitt"""
    eingegeben=eingabe.split(" ")

    x=0
    # TODO  einen Weg finden der genauer aufrundet anstelle:
    # import numpy as np      np.round(x/len(eingegeben),2)
    #                         round(x/len(eingegeben)
    #
    for werte in range(len(eingegeben)):
        x=x+len(eingegeben[werte])
    return f'Die Werte sind im Durchschnitt {x/len(eingegeben)} Zeichen lang'


nurEinTest = durchschnittVon(input('Wörter mit Leerzeichen trennen.. Enter zum beenden\n>'))
print(nurEinTest)
