def lineareSuche(woSuchen,wasGesucht):
    i, gefunden = 0, False
    while not gefunden and i < len(woSuchen):
        if wasGesucht == woSuchen[i]:
            gefunden = True
        i += 1
    if gefunden:
        return f"{wasGesucht} ist dabei!"
    else:
        return f"{wasGesucht} ist Nicht dabei!"

# Test
personen = ["alf","bert","claus","horst"]
print(lineareSuche(personen,"bert"))
