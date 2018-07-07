# # todo pętla while

# przygotowanie danych
# jak długo ma się wykonywać
# co ma się dziać

# a = 1           # przygotowanie
# while a < 10:   # warunek
#     print(a)    # ciało pętli
#     a = a + 1   # zmiana zmiennej sterującej
#
# print('po petli')

# a = 1
#
# while a <= 100:
#     print(a**2)
#     a += 1
# # todo petla zadanko
# a = 1
# temp: int = 0       # zmienna: typ <- oznaczenia - flaga nie ma wplywu na kod
#
# okres = int(input('Z jakiego okresu chcesz średnią? '))
#
# while a <= okres:       #ilośc dni pomiaru
#     temp += int(input(f"Podaj temperature {a} dnia w ℃:  "))
#     a += 1
#
#
# srednia = round(temp/(okres-1), 2)
#
# if srednia > 30:
#     print(f'Uff gorąco - {srednia} ℃')
# elif srednia < 5:
#     print(f'Brr zimno - {srednia} ℃')
# else:
#     print(srednia, "℃")

# # todo kolejne zadanko petla

# liczba = input('Podaj liczbę ["koniec" żeby zakończyć]: ')
# if liczba != 'koniec':
#     min_liczba = int(liczba)
#     max_liczba = int(liczba)
#     liczba = int(liczba)
#
#     while liczba != 'koniec':
#         liczba = int(liczba)
#         if liczba > max_liczba:
#             max_liczba = liczba
#         if liczba < min_liczba:
#             min_liczba = liczba
#         liczba = input('Podaj liczbę ["koniec" żeby zakończyć]: ')
#     print(f'Największa liczba to {max_liczba}, a najmnieszą liczbą jest {min_liczba}')
# # todo while true
# najpierw przypadki szczególne
# komunikat = 'Podaj liczbę ["koniec" żeby zakończyć]: '
# res = input(komunikat)
#
# if res == 'koniec':
#     exit('nie podales liczby')
# liczba = int(res)
# min = liczba
# max = liczba
# while True:
#     res = input(komunikat)
#     if res == 'koniec':
#         break
#     liczba = int(res)
#     if liczba > max:
#         max = liczba
#     if liczba < min:
#         min = liczba
# print(f'Największa liczba to {max}, a najmnieszą liczbą jest {min}')

import random ## todo pierwsza gierka

chest_pos_y = random.randrange(1,11)
chest_pos_x = random.randrange(1,11)
player_pos_x = random.randrange(1,11)
player_pos_y = random.randrange(1,11)

#print(f'Skarb Pozycja {chest_pos_x}x, {chest_pos_y}y')
print(f'Gracz Pozycja {player_pos_x}x, {player_pos_y}y')
dis_x = 0
dis_y = 0
dis_x_after = 0
dis_y_after = 0
move = ''
steps = 0

while True:
    move = input(' Podaj w którą strone chcesz iść[w,s,a,d]:')
    dis = abs(chest_pos_x - player_pos_x) + abs(chest_pos_y - player_pos_y)
    if move == 'w':
        player_pos_y -= 1
    elif move == 's':                                                                       #
        player_pos_y += 1
    elif move == 'a':                                                                       #
        player_pos_x -= 1                                                                   #
    elif move == 'd':                                                                       #
        player_pos_x += 1                                                                   #
    steps += 1
    dis_after = abs(chest_pos_x - player_pos_x) + abs(chest_pos_y - player_pos_y)           #dystans po kroku
    tip_chance = random.randrange(1,6)                                                      #
    if player_pos_x == chest_pos_x and player_pos_y == chest_pos_y:                         #Warunki końca gry
        print('Brawo znalazłeś skarb!')                                                     #
        break                                                                               #
    if  player_pos_x > 10 or player_pos_x < 1 or player_pos_y < 1 or player_pos_y > 10:     #
        print('Spadasz z planszy!')                                                         #
        break

    if dis_after < dis and tip_chance != 1:
        print('Jesteś bliżej')                                                              #
    elif tip_chance != 1:                                                                   #
        print('Jesteś dalej')                                                               #
    elif tip_chance == 1:                                                                   #
        print('Nie ma wskazówki dla Ciebie')

    if steps == 10 and (player_pos_x != chest_pos_x or player_pos_y != chest_pos_y):        #ponowne losowanie skarbu
        print('Za dużo kroków, skarb ucieka!')
        chest_pos_y = random.randrange(1, 11)
        chest_pos_x = random.randrange(1, 11)
        steps = 0

  #  print(f'Skarb Pozycja {chest_pos_x}x, {chest_pos_y}y')
    print(f'Gracz Pozycja {player_pos_x}x, {player_pos_y}y')

    # # ruch konia