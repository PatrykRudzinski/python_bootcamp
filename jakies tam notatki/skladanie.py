lista = [x for x in range(11)] ##todo: wazne

kwadraty = [i**2 for i in lista]
kwadraty = [(i, i**2, i**3) for i in range(-10, 11)]
zbior_wyr = {'aa', '1233', '111111'}
slownik = {i : len(i)for i in zbior_wyr}

print(kwadraty, slownik, sep='\n')