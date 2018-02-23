import Levenshtein

name_1 = 'Michael John Pfeng'
name_2 = 'M. John Penn'
name_1 = 'RON CARLSON JR'
name_2 = 'R CARLSON JR'
name_1 = 'Barack Obama'
name_2 = 'B. Bbama G'
name_1 = 'JOHN MICHAELSON'
name_2 = 'JOHN LIND JR'
name_1 = 'Vladimir Frometa G'
name_2 = 'Vladimir A Frometa'
print name_1
print name_2

name_1_tokens = name_1.split(' ')
name_1_tokens = [w.strip('.') for w in  name_1_tokens]
name_2_tokens = name_2.split(' ')
name_2_tokens = [w.strip('.') for w in  name_2_tokens]

pointer = 0
count_1 = 0
count_2 = 0
for i in range(len(name_1_tokens)):
    print i, pointer
    try:
        index = name_2_tokens[pointer:].index(name_1_tokens[i])
        pointer = index + pointer + 1
        count_1+=1
    except:
        index = -1
    if index == -1:
        print "Entered"
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
        	        		print 'False'
print "\n"
print count_1, count_2
if count_1 == 0 or min(len(name_1_tokens), len(name_2_tokens)) > count_1 + count_2:
	print 'False'
else:
	print 'True'
