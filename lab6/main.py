from hash_table import *


def main():
    ht = HashTable(20)
    ht.display()
    while True:
        print(f"1. Добавить элемент\n"
              f'2. Удалить элемент\n'
              f'3. Поиск элемента\n'
              f'4. Отобразить хэш-таблицу\n')

        choice = int(input('Введите номер операции: '))
        if choice == 1:
            key = input("Введите ключевое значение: ")
            ht.add(key)
        elif choice == 2:
            key = input("Введите ключевое значение: ")
            ht.delete(key)
        elif choice == 3:
            key = input("Введите ключевое значение: ")
            print(ht.read(key))

        elif choice == 4:
            ht.display()


if __name__ == '__main__':
    main()
