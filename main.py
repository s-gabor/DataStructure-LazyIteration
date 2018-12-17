# main.py

import constants
import utils
from itertools import islice


for fname, class_name, data_types in zip(constants.fnames, constants.class_names, constants.data_types):
    print()
    data = utils.create_nt(fname, class_name, data_types)
    for nt in islice(data, 3):
        print(nt)

