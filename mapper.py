# -*- coding: utf-8 -*-  
import sys  
count =0
# input comes from STDIN (standard input)  
for line in sys.stdin: 
    #print line.decode('UTF-8')
    # remove leading and trailing whitespace  
    count += 1
    if count == 1:
        continue
    # remove leading and trailing whitespace
    line = line.strip()
    #print 'count:%s----------------------------------->>' % count
    #print 'line:----->>', line
    # split the line into words
    words = line.split(',')
    #print 'words:%s--------->>len:%s' % (words, len(words))
    if not len(words) > 1:
        continue
    # increase counters
    '''
    num = 0
    for word in words:
        word = word.decode('UTF-8')
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if num == 1 and word:
	    # num 1 is user_id
            print '%s\t%s' % (word, 1)
	    continue
        num +=1
    '''
    words = line.split(',') 
    user_id = words[1]
    if user_id:
        print '%s\t%s' % (user_id, 1)  

    