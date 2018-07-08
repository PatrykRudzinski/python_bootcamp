liczby_av = set(list(range(0, 101, 2)))
liczby_usr = []
while True:
    liczba = input('Podaj liczbę z zakresu (stop żeby skończyć): ')
    if liczba == 'stop':
        break
    liczby_usr.append(int(liczba))

wynik = [liczby_av & set(liczby_usr)]

print(f'Parzyste unikalne liczby z zakresu 0 - 100 to: {wynik}')