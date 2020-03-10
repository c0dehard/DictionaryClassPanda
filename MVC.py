class Model:
    def modeldaten(self):
        """
        Mittels dieser Methode lassen sich die Daten erzeugen und zurückgeben
        Dient jedoch nur zur Veranschaulichung
        """
        print('Model fragt Daten ab.. ')
        data = 'Model Daten könnten hier stehen'
        return data

class View:
    def render(self, data):
        """
        Zeigt in der Konsole die eingegebenen Daten an
        """
        print('Daten von Model werden im View gezeigt.. ' , data)

class Controller:

    def __init__(self):
        """
        Initialisierung / Konstruktor
        Instanziierung von Model und View
        """
        self.model = Model()
        self.view = View()

    # Controller hat eine Methode welche auf Methoden
    # der instanziierten Klassen zugreifen kann
    def present(self):
        """
        Diese Methode hat natürlich Zugriff auf Methoden
        der instanziierten Klassen
        Daten werden generiert und letzendlich dem Benutzer präsentiert
        """
        print('Controller verwaltet also Model und View.. ')
        # Beispieldaten erzeugt mit der demo Methode, dient nur zur Veranschaulichung
        data = self.model.modeldaten()
        self.view.render(data)


if __name__ == "__main__":
    c = Controller()
    c.present()
