class Buch:
    """
    Buch braucht Title und Author
    """

    def __init__(self,title,author):
        self._title=title
        self._author=author
    def __repr__(self):
        return f"Buch: {self._title} Author: {self._author}"
        
    @property
    def author(self):
        return f"Author: {self._author}"
    @author.setter
    def author(self,newname):
        self._author = newname
    @author.deleter
    def author(self):
        """
        Kann mittels del gelöscht werden
        del instanz.variable
        """
        self._author = None

def message():
    print("Dieses Modul muss importiert werden! Nicht direkt ausführbar.")
if __name__ == '__main__':
    message()
