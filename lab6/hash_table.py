from tabulate import tabulate


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def add(self, key):
        index = self.create_hash(key)
        while self.table[index] != []:
            if self.table[index] == [key]:
                print(f'Ключ "{key}" уже существует.')
                return
            if index >= self.size:
                index = 0
            else:
                index = (index + 1) % self.size

        self.table[index] = [key]
        print(f'Ключ "{key}" добавлен.')

    def read(self, key):
        index = self.create_hash(key)
        while self.table[index] != ['-']:
            if self.table[index] == [key]:
                return index, key
            if index >= self.size:
                index = 0
            else:
                index = (index + 1) % self.size
        print(f'Ключ "{key}" не найден.')
        return None

    def delete(self, key):
        index = self.create_hash(key)
        while self.table[index] != '-':
            if self.table[index] == [key]:
                self.table[index] = ['-']
                print(f'Ключ "{key}" успешно удалён.')
                return
            if index >= self.size:
                index = 0
            else:
                index = (index + 1) % self.size

        print(f'Ключ "{key}" не найден.')
        return None

    def create_hash(self, key):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        letter_number = {letter: index for index, letter in enumerate(alphabet)}
        summa_index = 0
        for letter in key.upper():
            summa_index += int(letter_number.get(letter, 0))
        while summa_index >= self.size:
            summa_index = summa_index // self.size
        return summa_index

    def display(self):

        table_data = []
        for i in range(len(self.table)):
            values = self.table[i]
            if values:
                for key in values:
                    table_data.append([i, f"{key}"])
            else:
                table_data.append([i, "-"])

        headers = ["Хэш-адрес", "Значение"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
