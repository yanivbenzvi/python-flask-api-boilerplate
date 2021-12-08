from src.app import app
from src.utility.db_store import MemoryDbStore
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self) -> None:
        self.app = None
        MemoryDbStore().clear()

    def test_get_user_without_insertion_empty_result(self):
        response = self.app.get('/user')
        data = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual([], data)

    def test_get_user_with_insertion_result(self):
        self.app.post('/user', json={'username': 'test'})

        response = self.app.get('/user')
        data = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(data))
        self.assertEqual('test', data[0]['username'])

    def test_get_user_by_id_without_insertion_empty_result(self):
        response = self.app.get('/user/1')
        data = response.get_json()
        self.assertEqual(404, response.status_code)

    def test_get_user_by_id_with_insertion_result(self):
        response = self.app.post('/user', json={'username': 'test'})
        user_id = response.get_json().get('id')

        response = self.app.get(f'/user/{user_id}')
        data = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual('test', data['username'])

    def test_get_user_by_id_with_insertion_result_not_found(self):
        response = self.app.post('/user', json={'username': 'test'})
        user_id = response.get_json().get('id')

        response = self.app.get(f'/user/{user_id + "1"}')
        data = response.get_json()
        self.assertEqual(404, response.status_code)

    def test_delete_user_by_id_without_insertion_empty_result(self):
        response = self.app.delete('/user/1')
        self.assertEqual(204, response.status_code)

    def test_delete_user_by_id_with_insertion_result(self):
        response = self.app.post('/user', json={'username': 'test'})

        user_id = response.get_json().get('id')
        response = self.app.delete(f'/user/{user_id}')
        data = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(user_id, data['id'])

    def test_delete_user_by_id_with_insertion_result_not_found(self):
        response = self.app.post('/user', json={'username': 'test'})
        user_id = response.get_json().get('id')

        response = self.app.delete(f'/user/{user_id + "1"}')
        self.assertEqual(204, response.status_code)

    def test_delete_a_deleted_user_by_id_without_insertion_empty_result(self):
        response = self.app.post('/user', json={'username': 'test'})
        user_id = response.get_json().get('id')

        response = self.app.delete(f'/user/{user_id}')
        data = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(user_id, data['id'])

        response = self.app.delete(f'/user/{user_id}')
        self.assertEqual(204, response.status_code)

    def test_update_user_by_id_without_insertion_empty_result(self):
        response = self.app.put('/user/1', json={'username': 'test'})
        self.assertEqual(204, response.status_code)


if __name__ == '__main__':
    unittest.main()
