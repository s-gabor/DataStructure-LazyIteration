# utils.py

import csv
import constants
from collections import namedtuple
from datetime import datetime
from itertools import chain


def read_file(fname, *, delimiter=',', quotechar='"', include_header=False):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        if not include_header:
            next(reader)
        yield from reader


def parse_row(data_types, row):
    parsed_row = (data_type(item) for data_type, item in zip(data_types, row))
    return parsed_row


def extract_field_names(fname):
    return next(read_file(fname, include_header=True))


def create_namedtuple(fname, class_name):
    header_fields = extract_field_names(fname)
    return namedtuple(class_name, header_fields)


def iter_file(fname, class_name, data_types):
    reader = read_file(fname)
    nt = create_namedtuple(fname, class_name)
    for row in reader:
        parsed_row = parse_row(data_types, row)
        yield nt(*parsed_row)


def parse_date(value, *, date_format='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, date_format)


def create_extended_namedtuple(fnames, parsers):
    all_header_fields = []
    for fname in fnames:
        reader = read_file(fname, include_header=True)
        all_header_fields.extend(next(reader))
    unique_header_fields = (header for header, parser in zip(all_header_fields, parsers) if parser is True)
    return namedtuple('CombinedData', unique_header_fields)


def iter_combined_files(fnames, data_types, field_parsers):
    all_parsers = list(chain(*field_parsers))
    all_data_types = list(chain(*data_types))
    nt = create_extended_namedtuple(constants.fnames, all_parsers)
    readers = (read_file(fname) for fname in fnames)
    for fields in zip(*readers):
        fields_iterator = chain(*fields)
        unique_fields = (data_type(field) for data_type, field, parser in
                         zip(all_data_types, fields_iterator, all_parsers)
                         if parser is True)
        yield nt(*unique_fields)





