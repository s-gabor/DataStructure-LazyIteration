# constants.py

from utils import parse_date


# Files
fname_personal = 'data_files/personal_info.csv'
fname_employment = 'data_files/employment.csv'
fname_update_status = 'data_files/update_status.csv'
fname_vehicles = 'data_files/vehicles.csv'
fnames = [fname_personal, fname_employment, fname_update_status, fname_vehicles]


# Parsers
date_format = '%Y-%m-%dT%H:%M:%SZ'
data_type_personal = (str, str, str, str, str)
data_type_employment = (str, str, str, str)
data_type_update_status = (str, parse_date, parse_date)
data_type_vehicles = (str, str, str, int)
data_types = (data_type_personal, data_type_employment, data_type_update_status, data_type_vehicles)


# Named tuple names
personal_class_name = 'Personal'
employment_class_name = 'Employment'
update_status_class_name = 'UpdateStatus'
vehicles_class_name = 'Vehicle'
class_names = (personal_class_name, employment_class_name, update_status_class_name, vehicles_class_name)


# Unique fields
personal_fields = (True, True, True, True, True)
employment_fields = (True, True, True, False)
update_status_fields = (False, True, True)
vehicle_fields = (False, True, True, True)
field_parsers = (personal_fields, employment_fields, update_status_fields, vehicle_fields)
# unique_fields = [value for field in fields for value in field if value]
