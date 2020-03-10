class Model:
    def modeldaten(self):
        print('Model fragt Daten ab')
        data = 'Model Daten könnten hier stehen'
        return data

class View:
    def render(self, data):
        print('Das Model wird im View gezeigt:' , data)

class Controller:
    # Initialisierung / Konstruktor
    # Instanziierung von Model und View
    def __init__(self):
        self.model = Model()
        self.view = View()


    # Controller hat eine Methode welche auf Methoden
    # der instanziierten Klassen zugreifen kann
    def present(self):
        print('Controller verwaltet Model und View')
        data = self.model.modeldaten()
        self.view.render(data)


if __name__ == "__main__":
    c = Controller()
    c.present()
