import os
import time
from pprint import pprint

# TODO: Должен получится следующий словарь


'''
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


# TODO: На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова

# def get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2):
#     pass


# TODO: Нужно написать функцию, которая на вход принимает список блюд из
#  cook_book и количество персон для кого мы будем готовить

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


# TODO Необходимо объединить их в один по следующим правилам:
'''
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них 
(то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt
# 
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
# 
# Строка номер 1 файла номер 2
# Итоговый файл:
# 
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
'''


def rewrite_files(directory=None):
    if directory is None:
        directory = 'sorted'

    files_info = {}
    output_file = "rewrite_file.txt"

    # Формируем путь до директории
    dir_path = os.path.abspath(directory)

    # Получаем список всех файлов в директории
    file_paths = [os.path.join(dir_path, filename) for filename in os.listdir(dir_path)]

    # Читаем содержимое каждого файла и сохраняем информацию в словарь
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                files_info[file_path] = {
                    'filename': os.path.basename(file_path),
                    'line_count': len(content),
                    'content': content
                }
        except IOError as e:
            print(f"Не удалось прочитать файл {file_path}: {e}")

    # Сортируем файлы по количеству строк
    sorted_files = sorted(files_info.items(), key=lambda x: x[1]['line_count'])

    # Записываем результаты в выходной файл
    with open(output_file, 'w', encoding='utf-8') as f_total:
        for file_path, info in sorted_files:
            f_total.write(info['filename'] + '\n')
            f_total.write(str(info['line_count']) + '\n')
            f_total.writelines(info['content'])
            f_total.write('\n')

    return


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    print('Задание 1------------------------------------------------------------')
    time.sleep(1)
    print(cook_book)
    print('Задание 2------------------------------------------------------------')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))

    time.sleep(2)
    print('Задание 3------------------------------------------------------------')
    rewrite_files()