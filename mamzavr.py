import random

more = [

]
list = [

]

size = int(input('Какой будет размер поля:'))

for listi in range(size):
    kletka = [0] * size
    more.append(kletka)
    list.append(listi)

counter = 0
ship_dlina =random.randint(0, size // 2)
while counter < size // 2:
    ship_list = random.randrange(0, size)
    ship_element = random.randrange(0,size)
    if more[ship_list][ship_element] == 0
        more[ship_list][ship_element] = 1
    ship_list += 1
    ship_dlina += 1







        counter += 1
    else:
        more[ship_list][ship_element] = 1
pole = size * size // 2
while True:
    for idex, row in enumerate(more):
        print(index, end='')
        for element == 0 or element == 1:
            print('🌊', end='')
        elif element == 2:
            print('🔵', end='')
        elif element == 3:
            print('❌', end='')
        print('')
    print('Здесь ' + str(counter) + ' Корабли.')
    print('У тебя осталось ' + str(pole) + ' поле.')
    if counter == 0:
        print('ЕТы победил всех противников! Победа!')
        break
    if pole == 0:
        print('Здесь еще есьб враги...')
        for index, row in enumerate(more):
            print(index, end='')
            for element in row:
                if element == 0:
                    print('🌊', end='')
                elif element == 1:
                    print('🚢 ', end='')
                elif element == 2:
                    print('🔵', end='')
                elif element == 3:
                    print('❌', end='')
            print('')
        break
    vertikal = int(input('Ертикаль:(⬇)(0-' + str(izmers - 1) + '): '))
    horizontal = int(input('Горизонталь:(➡)(0-' + str(izmers - 1) + '): '))
    if more[horizontal][vertikal] == 0:
        more[horizontal][vertikal] = 2
        pole -= 1
    elif more[horizontal][vertikal] == 1:
        more[horizontal][vertikal] = 3
        counter -= 1
        pole -= 1