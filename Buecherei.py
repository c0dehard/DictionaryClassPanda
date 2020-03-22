class Buch:
  # TODO: Dieses Modul in PEP 8 Style umsetzen!
    def __init__(Buch, title, author):
        ''' Hiermit wird ein gewöhnliches Buch erstellt
        mit Buchname.__init__() kann man alles eines Buches Löschen
        TODO Ein Buch soll natürlich auch Inhalt haben später
        :param title:
        :param author:
        '''
        Buch.author = author
        Buch.title = title

    def __repr__(self):
        return self.title
    
    def informationenErhalten(Buch):
        ''' Gibt Buchtitel und Author formatiert zurück
        :return:'''
        return "{Buch.title} geschrieben von {Buch.author}"

class buechereiBuch(Buch):
    def __init__(self,title,author,verfuegbar):
        '''Bücher für eine Bücherei, können auch ihre eigenen Titel / eigenes Cover tragen
        :param title:
        :param author:
        :param verfuegbar:'''
        super().__init__(title,author);self._verfuegbar = verfuegbar

    def informationenErhalten(self):
        '''
        Zeigt an wie oft ein Buchtitel eines BüchereiBuches noch vorrätig ist (auf Lager)
        :return:'''
        super().informationenErhalten()
        print(f"von {self.title} sind noch {self.verfuegbar} auf Lager")

class buecherei(buechereiBuch):
    def __init__(self):
        '''Eine Bücherei kann nur Büchereibücher BEINhalten.. <.<'''
        self.buecher = []

    def buchAnStelle(self,index):return self.buecher[index]


    def neuesBuch(self,buechereiBuch):
        '''Ein Buch zur Bücherei hinzufügen
        TODO Bücherlisten direkt übergeben
        :param Buch:
        :return:'''
        self.buecher.append(buechereiBuch)
    
def hinweis():
    print("""Dieses Modul muss importiert werden! Nicht direkt ausführbar.
    \nAnbei ein Beispiel:

    a = buechereiBuch("Hairy Otter","Jay.Kay. Rohling",True)
    stadtBuecherei = buecherei()
    stadtBuecherei.neuesBuch(a)
    print(stadtBuecherei.buchAnStelle(0))
    
    """)

if __name__ == "__main__":
    
    hinweis()
    
    a = buechereiBuch("Hairy Otta","Jay.Kay. Rohling",True)
    stadtBuecherei = buecherei()
    stadtBuecherei.neuesBuch(a)
    
    print("Output:",stadtBuecherei.buchAnStelle(0))
