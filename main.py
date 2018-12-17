# main.py

import constants
import utils
from itertools import islice


for fname, data_types in zip(constants.fnames, constants.data_types):
    print()
    data = utils.create_nt(fname, data_types)
    for nt in islice(data, 3):
        print(nt)

