# main.py

import constants
import utils
from itertools import islice
from datetime import datetime


# for fname, class_name, data_types in zip(constants.fnames, constants.class_names, constants.data_types):
#     print()
#     data = utils.iter_file(fname, class_name, data_types)
#     for nt in islice(data, 3):
#         print(nt)

# ext_nt = utils.iter_combined_files(constants.fnames, constants.data_types, constants.field_parsers)
# for rows in islice(ext_nt, 7):
#     print(list(rows))


def filter_stale_records():
    # a record is considered stale if the last_updated date < 3/1/2017
    records = utils.iter_combined_files(constants.fnames, constants.data_types, constants.field_parsers)
    is_stale = False
    for record in records:
        if record.last_updated < datetime.strptime('3/1/2017', '%m/%d/%Y'):
            is_stale = True
        if not is_stale:
            yield record


it = filter_stale_records()
j = 0
for i in islice(it, 50):
    pass
