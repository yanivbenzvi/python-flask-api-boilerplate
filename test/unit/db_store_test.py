import unittest
from src.utility.db_store import MemoryDbStore


class MemoryDbStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.db = MemoryDbStore()

    def test_get_set_get(self):
        self.db.set('test1', 'test2')
        self.assertEqual(self.db.get('test1'), 'test2')

    def test_get_with_no_exist_value(self):
        self.assertEqual(self.db.get('test1'), None)

    def test_get_set_get_with_default_and_override(self):
        self.db.set('test', 'test')
        self.assertEqual(self.db.get('test'), 'test')

if __name__ == '__main__':
    unittest.main()
