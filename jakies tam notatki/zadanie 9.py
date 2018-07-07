ceny = {'ziemniaki': 2.50, 'pomidory': 4.00, 'pomarancze': 10.00, 'jablka': 8.00}
ilosc_w_mag = {'ziemniaki': 5, 'pomidory': 5, 'pomarancze': 5, 'jablka': 5}

while 1:
    operacja = input('Chcesz dokonać [d]ostawy, [z]akupu, czy dodać [n]owy towar? (end żeby skonczyć)')
    if operacja == 'end':
        break
    elif operacja == 'n':
        key = input('Jaki towar chcesz dodać? ')
        value = float(input('Jaka jest cena za tego towaru za kg? '))
        ceny[key]=value
        ilosc_w_mag[key] = 0

    elif operacja == 'z':
        koszt = 0
        while 1:
            for k, v in ceny.items():
                print(f"- {k} w cenie: {v}")

            produkt = input(f"Co chcesz kupic?('end' żeby zakończyć) \n").lower()
            if produkt == 'end':
                break
            if not produkt in ceny.keys():
                exit("Nie ma takiego produktu!")

            ilosc_zakupu = float(input("Ile kg chcesz kupić?\n"))
            if ilosc_zakupu > ilosc_w_mag[produkt]:
                exit('Nie ma tyle towaru!')
            koszt += ilosc_zakupu * ceny[produkt]
            print(f"Zapłacisz {koszt}zł")
            ilosc_w_mag[produkt] = ilosc_w_mag.get(produkt) - ilosc_zakupu

    elif operacja == 'd':
        for k in ceny.keys():
            print(k)
        rodzaj_dostawy = input('Jakiego towaru chcesz dodać? ')
        ilosc_dostawy = float(input('Ile kg towaru chcesz dodać? '))
        if not rodzaj_dostawy in ilosc_w_mag.keys():
            exit()
        ilosc_w_mag[rodzaj_dostawy] = ilosc_w_mag.get(rodzaj_dostawy) + ilosc_dostawy       ##todo:wazne!
    else:
        exit('Nie znam takiej operacji!')