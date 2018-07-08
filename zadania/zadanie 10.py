text = input('Podaj napis: ').lower()
ilosci = {}
for l in text:
    ilosci[l] = ilosci.get(l, 0) + 1
for k, v in ilosci.items():
    print(f'Znak {k} wystąpił {v} razy.')