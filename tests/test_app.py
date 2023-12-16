import unittest
import json
from app import app

class TestAppEndpoints(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_all_listings_success(self):
        response = self.app.get('/listings')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your specific response content

    def test_get_all_listings_bad_request(self):
        response = self.app.get('/listings?invalid_param=value')
        self.assertEqual(response.status_code, 400)

    # Repeat similar tests for other endpoints...

    def test_create_listing_success(self):
        data = {
            'name': 'New Listing',
            'price': 100,
            'neighborhood': 'Downtown'
            # Add other required fields
        }
        response = self.app.post('/listings', json=data)
        self.assertEqual(response.status_code, 200)

    def test_create_listing_bad_request(self):
        data = {
            'invalid_field': 'Invalid Value'
            # Missing required fields
        }
        response = self.app.post('/listings', json=data)
        self.assertEqual(response.status_code, 400)

    # Repeat similar tests for other endpoints...

    def tearDown(self):
        # Clean up any test-specific resources or data if needed
        pass

if __name__ == '__main__':
    unittest.main()
