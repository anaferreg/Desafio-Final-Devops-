import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Criação do cliente de teste 
        cls.client = app.test_client()
    
    def test_items_response_format(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.json)
        self.assertEqual(response.json['items'], ["item1", "item2", "item3"])

    def test_protected_with_invalid_token(self):
        headers = {
            "Authorization": "Bearer token_invalido_123"
        }

        response = self.client.post('/protected', headers=headers)
        self.assertIn(response.status_code, [401, 422])
        
    def test_swagger_is_accessible(self):
        response = self.client.get('/swagger')
        self.assertIn(response.status_code, [200, 302])


if __name__ == '__main__':
    unittest.main()
