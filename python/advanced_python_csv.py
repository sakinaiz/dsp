# Pre Work Section 5b Advanced Python
# Part II - CSV
# Author: Sakina Zabuawala

import csv

with open('faculty.csv') as fid:
    reader = csv.reader(fid)
    next(reader, None) # ignoring the header
    
    faculty_email = []
    for row in reader:
        faculty_email.append(row[-1])

# Q5. Write emails to csv file        
with open('emails.csv', 'w') as fid:
    for email in faculty_email:
        fid.write(email+'\n')
    