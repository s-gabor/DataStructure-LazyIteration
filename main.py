# main.py

import constants
import utils
from itertools import islice

#
# for fname, class_name, data_types in zip(constants.fnames, constants.class_names, constants.data_types):
#     print()
#     data = utils.iter_file(fname, class_name, data_types)
#     for nt in islice(data, 3):
#         print(nt)

ext_nt = utils.iter_combined_files(constants.fnames, constants.data_types, constants.field_parsers)
for rows in islice(ext_nt, 7):
    print(list(rows))
