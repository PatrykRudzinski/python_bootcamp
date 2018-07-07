##todo zadanie if 1
# import datetime
#
# data = datetime.date.today()
# current_year =int(data.year)
# birth_year = int(input("Podaj rok urodzenia: "))
# if 18 < current_year - birth_year:
#     print("Jesteś pełnoletni!")
# elif 18 == current_year - birth_year:
#     print("Brawo w tym roku kończysz 18 lat")
# elif 18 > current_year - birth_year:
#     print("Nie jesteś pełnoletni!")
# else:
#     print("Podano złą wartość!")
##todo zadanie if 2

# liczba_a = float(input("Podaj pierwszą liczbę: "))
# liczba_b = float(input("Podaj drugą liczbę: "))
# operacja = str(input("Podaj rodzaj operacji(+,-,*,/,^): "))
#
# if operacja == "+":
#     print(f'Wynik: {liczba_a+liczba_b}')
# elif operacja == "-":
#     print(f'Wynik: {liczba_a-liczba_b}')
# elif operacja == "*":
#     print(f'Wynik: {liczba_a*liczba_b}')
# elif operacja == "/":
#     if liczba_b == 0:
#         exit('nie wolno dzielic przez 0')
#     print(f'Wynik: {liczba_a/liczba_b}')
# elif operacja == "^":
#     print(f'Wynik: {liczba_a**liczba_b}')
# else:
#     exit("Nie znam takiej operacji")

# # todo zadanie if 3 - plansza xy
# coordinate_x = int(input("Podaj pozycje gracza X: "))
# coordinate_y = int(input("Poadj pozycje gracza Y: "))

# if 100 >= coordinate_x > 90:
#     if 100 >= coordinate_y >= 90:
#         print("Gracz znajduję się w prawym dolnym rogu")
#     elif 10 < coordinate_y < 90:
#         print("Gracz znajduję się w prawej krawędzi")
#     elif coordinate_y <= 10:
#         print("Gracz znajduję się w prawym górnym rogu")
# elif 90 > coordinate_x > 10:
#     if coordinate_y >= 90:
#         print("Gracz znajduję się w dolnej krawędzi")
#     elif 10 < coordinate_y < 90:
#         print("Gracz znajduję się w centrum")
#     elif coordinate_y <= 10:
#         print("Gracz znajduję się w górnej krawędzi")
# elif 0 < coordinate_x < 90:
#     if coordinate_y >= 90:
#         print("Gracz znajduję się w lewym dolnym rogu")
#     elif 10 < coordinate_y < 90:
#         print("Gracz znajduję się w lewej krawędzi")
#     elif coordinate_y <= 10:
#         print("Gracz znajduję się w lewym górnym rogu")
# else:
#     print("Gracz znajduje się poza planszą")

# x = int(input("Podaj pozycje gracza X: "))
# y = int(input("Poadj pozycje gracza Y: "))
#
# if x < 10:
#     pos_x = 'left'
# elif x > 90:
#     pos_x = 'right'
# else:
#     pos_x = ''
#
# if y < 10:
#     pos_y = 'top'
# elif y > 90:
#     pos_y = 'bottom'
# else:
#     pos_y = ''
#
# if pos_x and pos_y:
#     print(pos_y, pos_x, 'corner')
# elif pos_x or pos_y:
#     print(pos_y, pos_x, 'edge')
# else:
#     print('center')