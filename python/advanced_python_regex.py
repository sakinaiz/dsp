# Pre Work Section 5b Advanced Python
# Part I - Regular Expressions
# Author: Sakina Zabuawala

import csv
import re
from collections import defaultdict
import pprint

with open('faculty.csv') as fid:
    reader = csv.reader(fid)
    next(reader, None) # ignoring the header
    
    # Read the file contents
    faculty_info = []
    for row in reader:
        faculty_info.append(row)
    
    # Q1: find the frequency of the various degrees
    degree_freq = defaultdict(int)
    for row in faculty_info:
        for item in row[1].split():
            deg = re.sub(r'[\.\s]', '', item) #item.replace(".","")
            degree_freq[deg] += 1
    print('frequency of various degrees:')
    pprint.pprint(degree_freq, width=2)
    
    # Q2: Find frequency of various titles
    title_freq = defaultdict(int)
    #title_end = -1*len(' of Biostatistics')
    for row in faculty_info:
        title = re.sub(r' [ofis]+ Biostatistics', '', row[2])#[:title_end]#.replace(' is ', ' of ')
        title_freq[title] += 1
    print('frequency of various titles:')
    pprint.pprint(title_freq, width=2)
            
    # Q3: Create list of email addresses
    for row in faculty_info:
        print(row[-1].lower().strip())
    
    # Q4: Find different email domains
    email_domain = []
    for row in faculty_info:
        match = re.findall(r'[\w]+@([\w\.]+)', row[-1].lower().strip())
        if match:
            email_domain.append(match[0])#row[-1][email.find('@')+1:])
    email_domain = set(email_domain)
    print('unique email domains:')
    print(email_domain)
    
                
