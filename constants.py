# constants.py

from datetime import datetime

fname_personal = 'data_files/personal_info.csv'
fname_employment = 'data_files/employment.csv'
fname_update_status = 'data_files/update_status.csv'
fname_vehicles = 'data_files/vehicles.csv'
fnames = [fname_personal, fname_employment, fname_update_status, fname_vehicles]

date_format = '%Y-%m-%dT%H:%M:%SZ'
data_type_personal = (str, str, str, str, str)
data_type_employment = (str, str, str, str)
data_type_update_status = (str, 'date', 'date')
data_type_vehicles = (str, str, str, int)
data_types = (data_type_personal, data_type_employment, data_type_update_status, data_type_vehicles)
