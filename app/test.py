from app import app
import unittest
import xmlrunner


class test(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200) 
        
    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 
        # assert the response data
        self.assertEqual(result.data, b'Hello !')

    def test_health_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.assertEqual(self.app.get('/healthz',follow_redirects=True) ,200)

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)