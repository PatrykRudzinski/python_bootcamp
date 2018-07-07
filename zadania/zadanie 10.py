text = input('Podaj napis: ')
ilosci = {}
for l in text:
    ilosci[l] = ilosci.get(l, 0) + 1
print(ilosci)