# main.py

import constants
import csv
from collections import namedtuple


def read_file(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        yield from reader


def create_nt(fname):
    reader = read_file(fname)
    header_fields = next(reader)
    nt = namedtuple('Data', header_fields)
    for row in reader:
        yield nt(*row)


