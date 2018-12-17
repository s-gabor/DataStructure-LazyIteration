# utils.py

import csv
from collections import namedtuple
from datetime import datetime


def read_file(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        yield from reader


def parse_row(data_types, row):
    parsed_row = [datetime.strptime(item, '%Y-%m-%dT%H:%M:%SZ') if data_type == 'date' else data_type(item)
                  for data_type, item in zip(data_types, row)]
    return parsed_row


def create_nt(fname, data_types):
    reader = read_file(fname)
    header_fields = next(reader)
    nt = namedtuple('Data', header_fields)
    for row in reader:
        parsed_row = parse_row(data_types, row)
        yield nt(*parsed_row)
