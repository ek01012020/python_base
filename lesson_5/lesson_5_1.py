'''Создать  программно  файл  в  текстовом  формате,  записать  в  него  построчно  данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''

print('Введите построчно необходимую информацию, для завешения записи в файл введите пустую строку')
my_list = []
with open('task_1.txt', 'w', encoding='utf-8') as f:
    while True:
        my_str = input()
        if my_str == '':
            break
        else:
            my_list.append(my_str + '\n')
    f.writelines(my_list)