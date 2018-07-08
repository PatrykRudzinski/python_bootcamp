liczby_av = set(range(0, 101, 2))
liczby_usr = set()
while True:
    liczba = input('Podaj liczbę z zakresu (stop żeby skończyć): ')
    if liczba == 'stop':
        break
    liczby_usr.add(int(liczba))

wynik = liczby_av & liczby_usr

print(f'Jest {len(wynik)} parzystych unikalnych liczb w zakresie 0 - 100')
for i in wynik:
    print(i, end=", ")