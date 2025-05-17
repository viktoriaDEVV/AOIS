import unittest
from unittest.mock import patch
from io import StringIO
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.size = 10
        self.ht = HashTable(self.size)

    def test_initialization(self):
        size = 10
        ht = HashTable(size)
        self.assertEqual(ht.size, size)
        self.assertEqual(ht.table, [[] for _ in range(size)])

    def test_hash(self):
        hash_value = self.ht.create_hash('Ковальчук')
        self.assertEqual(hash_value, 1)

    def test_add(self):
        self.ht.add("Ковальчук")
        self.assertIn("Ковальчук", self.ht.table[1])
        self.ht.add("Петрова")
        self.ht.add("Петрова")
        index = self.ht.create_hash("Петрова")
        self.assertEqual(self.ht.table[index].count("Петрова"), 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_existing_key(self, mock_stdout):
        self.ht.add("Ковальчук")
        self.ht.add("Ковальчук")  # Попытка добавить существующий ключ

        # Проверяем, что вывод содержит сообщение о существующем ключе
        output = mock_stdout.getvalue()
        self.assertIn('Ключ "Ковальчук" уже существует.', output)

    def test_read(self):
        self.ht.add("Ковальчук")
        self.ht.add("Ковалёва")
        self.ht.add("Ковалёв")
        found_result1 = self.ht.read("Ковальчук")
        self.assertEqual(found_result1, (1, 'Ковальчук'))
        self.assertEqual(self.ht.read('Ковалёва'), (4, 'Ковалёва'))
        self.assertEqual(self.ht.read('Ковалёв'), (5, 'Ковалёв'))

    def test_delete(self):
        self.ht.add("Ковальчук")
        self.ht.add("Ковалёва")
        self.ht.add("Ковалёв")
        self.ht.delete("Ковальчук")
        self.ht.delete("Ковалёва")
        self.ht.delete("Ковалёв")
        self.assertNotIn("Ковальчук", self.ht.table)
        self.assertNotIn("Ковалёва", self.ht.table)
        self.assertNotIn("Ковалёв", self.ht.table)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        self.ht.add("Ковальчук")
        self.ht.add("Петрова")
        self.ht.display()
        output = mock_stdout.getvalue()

        # Проверяем, что вывод содержит ключи и соответствующие хэш-адреса
        self.assertIn("Ковальчук", output)
        self.assertIn("Петрова", output)
        self.assertIn("Хэш-адрес", output)
        self.assertIn("Значение", output)




if __name__ == "__main__":
    unittest.main()


