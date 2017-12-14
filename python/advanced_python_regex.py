# Pre Work Section 5b Advanced Python
# Part I - Regular Expressions
# Author: Sakina Zabuawala

import csv

with open('faculty.csv') as fid:
    reader = csv.reader(fid)
    next(reader, None) # ignoring the header
    
    # Read the file contents
    faculty_degree = []
    faculty_title = []
    faculty_email = []
    for row in reader:
       faculty_degree.append(row[1])
       faculty_title.append(row[2])
       faculty_email.append(row[3])
    
    # Q1: find the frequency of the various degrees
    degree_freq = {}
    for degrees in faculty_degree:
        for item in degrees.split():
            deg = item.replace(".","")
            if deg not in degree_freq:
                degree_freq[deg] = 1
            else:
                degree_freq[deg] += 1
    print('frequency of various degrees:')
    print(degree_freq)
    
    # Q2: Find frequency of various titles
    title_freq = {}
    title_end = -1*len(' of Biostatistics')
    for item in faculty_title:
        title = item[:title_end]#.replace(' is ', ' of ')
        if title not in title_freq:
            title_freq[title] = 1
        else:
            title_freq[title] += 1
    print('frequency of various titles:')
    print(title_freq)
            
    # Q3: Create list of email addresses
    print(faculty_email)
    
    # Q4: Find different email domains
    email_domain = []
    for email in faculty_email:
        email_domain.append(email[email.find('@')+1:])
    email_domain = set(email_domain)
    print('unique email domains:')
    print(email_domain)
    
                
