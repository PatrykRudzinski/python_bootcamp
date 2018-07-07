# # todo interakcje z userem
# name = input('Wpisz sowje imię: ')
#
# print('Witaj', name)
#
# age = int(input('Ile lat masz? '))
#
# print ('za dwa lata będziesz miał(a): ', age+2)
#
# legal_age = 18
#
# if age >= legal_age:
#     print("zapraszam na piwo")
# else:
#     print("zapraszam na colę")
# # todo interakcje z userem - cena podróży
# city_a = str(input("Miasto A: "))
# city_b = str(input("Miasto B: "))
# distance_a_b = int(input(f"Dystans {city_a}-{city_b}: "))
# gas_price = float(input("Cena paliwa: "))
# gas_100km = float(input("Spalanie na 100km: "))
#
# print(f"Koszt przejazdu {city_a}-{city_b} to {distance_a_b/100*gas_100km*gas_price:.2f}PLN")#round() zaokrąglanie
# # todo zadanie - podaj liczbę
# number = int(input("Podaj liczbę: "))
# print(f'Większa od 10: {number>10}\nMniejsza równa 15: {number<=15}\nPodzielna przez 2: {(number%2)== 0}\nCzy spełnia warunki: {number%2==0 and number%3==0 and number>10 or number==7 }')
# siła not -> and -> or
#     **      *     +-
rodzaj_bryly = str(input("Czy bryła jest prostopadłościanem?(tak/nie): "))
if rodzaj_bryly == "tak":

    a = int(input("Podaj wielkość a bryły: "))
    b = int(input("Podaj wielkość b bryły: "))
    c = int(input("Podaj wielkość c bryły: "))

    objetosc = a*b*c

    if objetosc > 1000:
            print("Bryła jest większa od 1 litra")
    else:
            print("Bryła jest mniejsza od 1 litra")
elif rodzaj_bryly == "nie":
    rodzaj_bryly = str(input("Czy bryła jest butelką?(tak/nie): "))

    promien = int(input("Podaj promień podstawy: "))
    wysokosc = int(input("Podaj wysokość butelki: "))
    pi = 3.14
    objetosc_but = pi*promien**2*wysokosc
    if objetosc_but > 1000:
          print("Bryła jest większa od 1 litra")
    else:
          print("Bryła jest mniejsza od 1 litra")
else:
    print("byrła nie jest ani prostopadłościanem ani butelką, albo podano zla wartosć ")
