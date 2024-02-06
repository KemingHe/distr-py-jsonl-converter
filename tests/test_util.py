import os
import unittest
from src.csv4vertex.util import *

class TestUtil(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_fpath_not_none(self):
        reinit_file(None)

    def test_create_if_not_exist(self):
        fpath = 'tests/test_data/didnt_exist.txt'
        self.assertFalse(os.path.exists(fpath))

        reinit_file(fpath)
        self.assertTrue(os.path.exists(fpath))

        os.remove(fpath)

    def test_outfile_empty_after_reinit(self):
        fpath = 'tests/test_data/pre_populated.txt'
        tmp_txt = 'hello world'
        tmp_len = len(tmp_txt)

        with open(fpath, 'w') as tmpf:
            tmpf.write(tmp_txt)

        self.assertEqual(os.stat(fpath).st_size,
                          tmp_len)

        reinit_file(fpath)
        self.assertEqual(os.stat(fpath).st_size, 0)

