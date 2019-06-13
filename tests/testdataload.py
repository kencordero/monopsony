import json
import unittest

class TestDataLoad(unittest.TestCase):
    def test_properties(self):
        filename = 'data/properties.json'
        with open(filename) as f:
            data = json.load(f)
        props = data['properties']
        self.assertEqual(props[14]['name'], 'Kentucky Ave.')

if __name__ == '__main__':
    unittest.main()