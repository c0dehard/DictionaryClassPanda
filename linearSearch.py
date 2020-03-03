
def hinweis():
    print("""
    Als Skript nicht ausführbar
    muss importiert werden um Methoden nutzen zu können

    import linearSearch
    oder z.B. from linearSearch import lineareSuche

    Beispiel:
    from linearSearch import lineareSuche
    ordner1 = ["audio.ogg","bild.png","beispiel.py","index.php"]
    x = lineareSuche(ordner1,"beispiel.py")
    print(x)
    """)

def lineareSuche(woSuchen,wasGesucht):
    woSuchen,wasGesucht
    i, gefunden = 0, False
    while not gefunden and i < len(woSuchen):
        if wasGesucht == woSuchen[i]:
            gefunden = True
        i += 1
    if gefunden:
        return f"{wasGesucht} ist dabei"
    else:
        return f"{wasGesucht} ist Nicht dabei"

# Beispiele
# ordner1 = ["audio.ogg","bild.png","beispiel.py","index.php"]
# print(lineareSuche(ordner1,"beispiel.py"))

# Damit man das Modul nicht ausfersehen direkt einfach in der Konsole ausführt 
if __name__ == "__main__":
    hinweis()
