import csv
import numpy as np
import Levenshtein
from random import shuffle

name_1 = 'Michael John Pfeng'
name_2 = 'M. John Penn'
name_1 = 'Barack Obama'
name_2 = 'B. Bbama G'
name_1 = 'JOHN MICHAELSON'
name_2 = 'JOHN LIND JR'
name_1 = 'Vladimir Frometa G'
name_2 = 'Vladimir A Frometa'
name_2 = 'RON CARLSON JR'
name_1 = 'ROY CARLSON JR'
# print name_1
# print name_2


def read_data(filename): 
	open_file = open(filename, 'rU')
	reader = csv.reader(open_file)
	global data
	data = []
	for x in reader:
		data.append(x[3] + " " + x[0])
	data = data[1:]
	shuffle(data)

def is_name_matched(name_1, name_2):
	name_1_tokens = name_1.split(' ')
	name_1_tokens = [w.strip('.') for w in  name_1_tokens]
	name_2_tokens = name_2.split(' ')
	name_2_tokens = [w.strip('.') for w in  name_2_tokens]
	
	index = -1
	pointer = 0
	count_1 = 0
	count_2 = 0
	for i in range(len(name_1_tokens)):
	    # print i, pointer
	    try:
	        index = name_2_tokens[pointer:].index(name_1_tokens[i])
	        pointer = index + pointer + 1
	        count_1+=1
	    except:
	        index = -1
	    if index == -1:
	        if len(name_2_tokens[pointer:])!=0:
	        	char = name_1_tokens[i][0]
	        	for j in range(pointer, len(name_2_tokens)):
	        	    if char == name_2_tokens[j][0]:
	        	    	if len(name_2_tokens[j])==1:
	        	        	pointer = j
	        	        	count_2+=1
	        	        elif len(name_1_tokens[i])!=1 and len(name_2_tokens[j])!=1:
	        	        	ratio = Levenshtein.ratio(name_1_tokens[i], name_2_tokens[j])
	        	        	if (1-ratio)*len(name_2_tokens[j]) == 1:
	        	        		pointer = j
	        	        		count_2+=1
	        	        	else:
	        	        		return 'False'
	if count_1 == 0 or min(len(name_1_tokens), len(name_2_tokens)) > count_1 + count_2:
		return 'False'
	else:
		return 'True'
		
def cluster_names():
	count = 0
	length = len(data)
	# length = 20
	info = np.zeros(length)
	for i in range(0, length):
		if info[i] == 0:
			print data[i]
			for j in range(i+1, length):
				if info[j] == 0:
					check_1 = is_name_matched(data[i], data[j])
					check_2 = is_name_matched(data[j], data[i])
					check = check_1 or check_2
					# print check
					if check_1 == 'True' or check_2 == 'True':
						print data[j]
						info[j] = 1
			count+=1
			info[i] = 1
#			print info
			print '\n'
	print count

filename = 'Sample_Dataset.csv'
read_data(filename)
cluster_names()

name_2 = 'ADDISON J HANNA'
name_1 = 'ADDISON JOHN HANNA'
print is_name_matched(name_1, name_2)
