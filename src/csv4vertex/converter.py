import os
import psutil
import numpy as np
import pandas as pd

from src.csv4vertex.util import *

class Converter:

    def __init__(self, csv_fpath, jsonl_fpath):
        assert os.path.exists(csv_fpath)
        assert jsonl_fpath is not None

        self.csv_fpath = csv_fpath
        self.jsonl_fpath = jsonl_fpath

        reinit_file(jsonl_fpath)

