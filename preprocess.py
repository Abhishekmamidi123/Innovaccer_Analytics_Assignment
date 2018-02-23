# -*- coding: utf-8 -*-
import csv
import Levenshtein
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def read_data(): 
	open_file = open('Sample_Dataset.csv', 'rU')
	reader = csv.reader(open_file)
	global data
	data = []
	for x in reader:
		data.append((x[3], x[0]))

def tokenize_name(name):
    clean_name = ''.join(c if c.isalnum() else ' ' for c in name)
    return clean_name.lower().split()

def is_first_names_matched(fn_name_1, fn_name_2):
    length_1 = len(fn_name_1)
    length_2 = len(fn_name_2)
    if length_1 == 1 and length_2 == 1:
        ratio = Levenshtein.ratio(fn_name_1[0], fn_name_2[0])
        if ratio == 1:
            print "First names are matching"
            return True
        elif (1-ratio)*len(fn_name_1) == 1:
            print "There is an spelling mistake in the first names"
            return True
        else:
            print "Two names are different"
            return False

def is_last_names_matched(ln_name_1, ln_name_2):
    print ln_name_1
    print ln_name_2

def is_name_matched(name_1, name_2):
    fn_name_1 = name_1[0].split(" ")
    fn_name_2 = name_2[0].split(" ")
    print fn_name_1
    print fn_name_2
    is_fn_matched = is_first_names_matched(fn_name_1, fn_name_2)
    print is_fn_matched
    if is_fn_matched == True:
        ln_name_1 = name_1[1].split(" ")
        ln_name_2 = name_2[1].split(" ")
        is_ln_matched = is_last_names_matched(ln_name_1, ln_name_2)

# -- Main function -- #
# suffixes = {'junior', 'jr', 'senior', 'sr', 'ii', 'iii', 'iv'}
read_data()
length = len(data)

for i in range(1):
    for j in range(1):
        print data[1], data[2]
        is_name_matched(data[1], data[2])
        print "Abhishek"

# is_name_matched('ROY CARLSON JR'.lower(), 'ROY CARLSON JR'.lower())
print "\n"
# is_name_matched('CARLSON JR ROY', 'CARLSON JR RON')
print "\n"
# is_name_matched('CARLSON JR ROY', 'CARLSON JR RONA')
print "\n"

print tokenize_name('Abhsihek-mamidi-123/456')
