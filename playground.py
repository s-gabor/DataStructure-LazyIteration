# playground.py

import csv
import constants
from itertools import islice
from collections import namedtuple


# # view the first few lines of data from the file to determine the structure
# with open(constants.fname_personal) as f:
#     for i in range(3):
#         print(next(f))
# # get dialect and sniff each file
# for fname in constants.fnames:
#     with open(constants.fname_personal) as f:
#         dialect = csv.Sniffer().sniff(f.read(2000))
#         print(f'{fname}: ', vars(dialect))
#         print(f'delimiter: {dialect.delimiter} / quotechar: {dialect.quotechar}')


# create and test csv reader
def read_file(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        yield from reader
# # for fname in constants.fnames:
# #     f = read_file(fname)
# #     print(f'\n*** {fname} ***')
# #     for line in f:
# #         print(line)
# for fname in constants.fnames:
#     f = read_file(fname)
#     print(f'\n*** {fname} ***')
#     for line in islice(f, 3):
#         print(line)


# create namedtuples for each file
def create_nt(fname):
    reader = read_file(fname)
    header_fields = next(reader)
    nt = namedtuple('Data', header_fields)
    for row in reader:
        yield nt(*row)
for fname in constants.fnames:
    print()
    data = create_nt(fname)
    for item in islice(data, 3):
        print(item)
