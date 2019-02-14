
# Lazy Iteration

Project build with **Python** for parsing data where multiple file names are given as input, each file having a uniquely identifying key(like a CNP). The iterator combines the data from all files, returns a single namedtuple containing all the named fields with the correct data type(int, date, str).  Filter functions are also implemented where the data can be sorted and filtered in any number of ways like filtering out old records, sorting data based on gender, language, employment information and so on.
 The goal is to avoid loading all data into the memory(which wouldn’t be possible or at least not very efficient for large files) and to use lazy iteration and context managers.


### Instalation

Python 3.7.1