# utils.py

import csv
from collections import namedtuple
from datetime import datetime
import constants


def read_file(fname, *, delimiter=',', quotechar='"'):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        yield from reader


def parse_row(data_types, row):
    parsed_row = (data_type(item) for data_type, item in zip(data_types, row))
    return parsed_row


def create_nt(fname, class_name, data_types):
    reader = read_file(fname)
    header_fields = next(reader)
    nt = namedtuple(class_name, header_fields)
    for row in reader:
        parsed_row = parse_row(data_types, row)
        yield nt(*parsed_row)


def parse_date(value):
    return datetime.strptime(value, constants.date_format)
