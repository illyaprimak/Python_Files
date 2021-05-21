import os
import shutil

def make_folder(dir, parent_dir='C:'):
    path = parent_dir + "\\" + dir
    os.mkdir(path)
    return path


def make_file(dir, parent_dir='C:\\'):
    path = parent_dir + "\\" + dir
    text_file = open(path, "w")


def main_cycle():
    parent_dir = input("Введіть директорію де створити кореневу папку: ")
    parent_path = make_folder(parent_dir)
    make_file_cycle(parent_dir, parent_path)
    make_folder_cycle(parent_dir, parent_path)
    return parent_path


def make_folder_cycle(parent_dir, parent_path):
    number = input("Хочете створити піддерикторію в папці " + parent_dir + "?. Введіть 1 , якщо хочете, введіть 2 "
                                                                           "якщо ні: ")
    while int(number) != 2:
        name = input("Введіть назву підпапки: ")
        new_parent = make_folder(name, parent_path)
        make_file_cycle(name, new_parent)
        number = input("Хочете створити піддерикторію в папці " + parent_dir + "?. Введіть 1 , якщо хочете, введіть 2 "
                                                                               "якщо ні: ")


def make_file_cycle(parent_dir, parent_path):
    number = input("Хочете створити файл в папці " + parent_dir + " ?. Введіть 1 , якщо хочете, введіть 2 якщо ні: ")
    while int(number) != 2:
        name = input("Введіть назву файлу: ")
        make_file(name, parent_path)
        number = input(
            "Хочете створити файл в папці " + parent_dir + " ?. Введіть 1 , якщо хочете, введіть 2 якщо ні: ")


def struct_listdir(parent_dir):
    print("Склад кореневої папки за допомогою os.listdir(): ")
    list = os.listdir(parent_dir)
    for item in list:
        print(item)


def struct_scandir(parent_dir):
    print("Склад кореневої папки за допомогою os.scandir(): ")
    with os.scandir(parent_dir) as entries:
        for entry in entries:
            print(entry.name)


def struct_listdir_files(parent_dir):
    print("Склад кореневої папки за допомогою os.listdir()(тільки файли): ")
    list = os.listdir(parent_dir)
    for item in list:
        if os.path.isfile(parent_dir + "//" + item):
            print(item)


def struct_scandir_files(parent_dir):
    print("Склад кореневої папки за допомогою os.scandir()(тільки файли): ")
    with os.scandir(parent_dir) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)


def txt_files(parent_dir):
    print("Файли з кореневої папки , що мають розширення .txt: ")
    with os.scandir(parent_dir) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.name.endswith(".txt"):
                    print(entry.name)


def find_all_files(parent_dir):
    print("Всі файли і папки з кореневої директорії")
    for dirpath, dirnames, filenames in os.walk(parent_dir):
        for dirname in dirnames:
            print("Каталог:", dirname)
        for filename in filenames:
            print("Файл:", filename)


def py_to_csv(parent_dir):
    print("Змінити розширення всіх файлів .py на .csv")
    for dirpath, dirnames, filenames in os.walk(parent_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                base = os.path.splitext(filename)[0]
                print(base)
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, base + ".csv"))
                print("Файл", base + ".csv")



def remove_dir(parent_dir):
    shutil.rmtree(parent_dir)

parent_path = main_cycle()
struct_listdir(parent_path)
struct_scandir(parent_path)
struct_listdir_files(parent_path)
struct_scandir_files(parent_path)
txt_files(parent_path)
find_all_files(parent_path)
py_to_csv(parent_path)
remove_dir(parent_path)