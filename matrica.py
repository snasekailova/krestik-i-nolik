import random

def vivod_pole(pole):
    for rows in pole:
        print(rows)

def hot_user(twod_list , dictionary):
    krusts = int(input('Куда будет твой ход:'))
    x = dictionary.get(krusts)

    while x == None:
        print(krusts)
        print('ДАВАЙ ЕЩЁ РАЗ!')
        krusts = int(input('Куда будет твой ход:'))
        x = dictionary.get(krusts)
    dictionary.pop(krusts)
    x1 = x[0]
    x2 = x[1]
    twod_list[x1][x2] = 'X'


def hot_abuser(twod_list , free_hoti):
    print('Ходит абьюзер')
    random_number = random.randint(0 , len(free_hoti))
    spisok_values = free_hoti.values()
    free_index = list(spisok_values)[random_number]
    x1 = free_index[0]
    x2 = free_index[1]
    twod_list[x1][x2] = 'O'


def proverka(index, free_index):
    if index == free_index:
        while index != free_index:
            hot_o = hot_abuser(twod_list , free_hoti)
            hot_x = hot_user(twod_list , dictionary)

def igra():
    while proverka != None:
        hot_abuser()
        hot_user()



colums = int(input('colums count: '))
twod_list = []
jnumbers = 1
dictionary = {

}


for i in range(colums):
    colums_list = [1] * colums
    twod_list.append(colums_list)
    for j in  range(len(twod_list[i])):
        twod_list[i][j] = jnumbers
        dictionary.update({jnumbers : [i , j]})
        jnumbers += 1

vivod_pole(twod_list)
hot_abuser(twod_list , dictionary)
vivod_pole(twod_list)
hot_user(twod_list , dictionary)
vivod_pole(twod_list)
proverka(index, free_index)
vivod_pole(twod_list)
igra()
vivod_pole(twod_list)










