# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# for i in tupla:
#     print(i)

# for nr, el in enumerate(lista, start=1):  ##todo numerowanie w liscie pętla for
#   print(nr, el)

# for i in range(len(lista)):
#     print(i, lista[i])
# for i in range(0,len(lista),2):
#     print(i)
#
# lista = [2, -3, 2, 2, 0, 1, 2, 1, -3]
# dodatnie = 0
# ujemne = 0
# zera = 0
# for i in lista:
#     if i > 0:
#         dodatnie += 1
#     elif i < 0:
#         ujemne -= 1
#     elif i == 0:
#         zera += 1
#
# print(f'Ilość dodatnich liczb: {dodatnie}\nIlość ujemnych liczb: {ujemne}\nIlość zer: {zera}')
# suma = 0
# for i in range(101):
#     if i%3 == 0 or i%5 == 0:
#         suma += 1
#         print(i)
# print(f'W zasięgu 0-100 jest {suma} takich liczb')
# print('   ', end = '')
# for s in range(10):
#     print(f'{s:>3}', end = ' ')
# print('\n')
#
# for i in range(10):
#     print(f'{i:<2} ',end = ' ')
#     for a in range(10):
#         print(f'{a*i:>2} ',end = ' ')
#     print()

li = [3,6,43,2,7,1]

nr_min = 0
nr_max = 0
wartość_min = li[0]
wartość_max = li[0]
for nr, wartość in enumerate(li):
    if wartość > wartość_max:
        nr_max = nr
    if wartość < wartość_min:
        nr_min = nr
print(nr_min, nr_max)