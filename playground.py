# playground.py

import csv
import constants
import utils
from itertools import islice
from collections import namedtuple
from datetime import datetime


# # extract the first few lines of data from the file to determine the structure
# with open(constants.fname_personal) as f:
#     for i in range(3):
#         print(next(f))
# # get dialect and sniff each file
# for fname in constants.fnames:
#     with open(constants.fname_personal) as f:
#         dialect = csv.Sniffer().sniff(f.read(2000))
#         print(f'{fname}: ', vars(dialect))
#         print(f'delimiter: {dialect.delimiter} / quotechar: {dialect.quotechar}')


# # create and test csv reader
# def read_file(fname):
#     with open(fname, 'r') as f:
#         reader = csv.reader(f, delimiter=',', quotechar='"')
#         yield from reader
# # test the first 3 rows of data from each file
# for fname in constants.fnames:
#     f = read_file(fname)
#     print(f'\n*** {fname} ***')
#     for line in islice(f, 3):
#         print(line)
# # test the first all data from each file !!! NOT recommended if the file is very large!!!
# for fname in constants.fnames:
#     f = read_file(fname)
#     print(f'\n*** {fname} ***')
#     for line in f:
#         print(line)


# # create and test namedtuples for each file
# def create_nt(fname):
#     reader = utils.read_file(fname)
#     header_fields = next(reader)
#     nt = namedtuple('Data', header_fields)
#     for row in reader:
#         yield nt(*row)
# for fname in constants.fnames:
#     print()
#     data = create_nt(fname)
#     for item in islice(data, 3):
#         print(item)


# # create a data parser
# def parse_row(data_types, row):
#     parsed_row = [datetime.strptime(item, '%Y-%m-%dT%H:%M:%SZ') if data_type == 'date' else data_type(item)
#                   for data_type, item in zip(data_types, row)]
#     return parsed_row
# # skip the header and test parse_row
# reader = utils.read_file(constants.fname_vehicles)
# next(reader)
# for row in islice(reader, 3):
#     print(parse_row(constants.data_type_vehicles, row))
# reader = utils.read_file(constants.fname_update_status)
# next(reader)
# for row in islice(reader, 3):
#     print(parse_row(constants.data_type_update_status, row))


# # create and test namedtuples for each file using parsed data
# def create_nt(fname, data_types):
#     reader = read_file(fname)
#     header_fields = next(reader)
#     nt = namedtuple('Data', header_fields)
#     for row in reader:
#         parsed_row = parse_row(data_types, row)
#         yield nt(*parsed_row)
# for fname, data_types in zip(constants.fnames, constants.data_types):
#     print()
#     data = utils.create_nt(fname, data_types)
#     for nt in islice(data, 3):
#         print(nt)


# create date parser
def parse_date(value):
    return datetime.strptime(value, constants.date_format)