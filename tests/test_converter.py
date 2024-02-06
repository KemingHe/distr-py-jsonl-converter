import os
import unittest
from src.csv4vertex.converter import Converter


class TestCSV4Vertex(unittest.TestCase):

    @unittest.expectedFailure
    def test_converter_is_instantiable(self):
        tmp_c = Converter(None, None)
        self.assertIsInstance(tmp_c, Converter)

    def test_converter_checks_path(self):
        tmp_c = Converter('tests/test_data/test1.csv', 
                          'tests/test_data/out1.jsonl')
        self.assertIsInstance(tmp_c, Converter)

    @unittest.expectedFailure
    def test_csv_fpath_valid(self):
        tmp_c = Converter('', '')

    def test_jsonl_init(self):
        csv_p = 'tests/test_data/test1.csv'
        jsonl_p = 'tests/test_data/out1.jsonl'
        tmp_c = Converter(csv_p, jsonl_p)

        self.assertTrue(os.path.exists(jsonl_p))
        self.assertEqual(os.stat(jsonl_p).st_size, 0)

if __name__ == 'main':
    unittest.main()

