import unittest
from view.util import get_data_with_id

class TestGLS(unittest.TestCase):
    """
    Our basic test class
    """

    def test_get_data_with_id(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        expected_output = {
            "id": "1",
            "content": "tip on first div",
            "selector": "#id_1",
            "next": "2"
        }

        res = get_data_with_id(1)
        self.assertEqual(res, expected_output)
        
        res = get_data_with_id(2)
        self.assertNotEqual(res, expected_output)


if __name__ == '__main__':
    unittest.main()