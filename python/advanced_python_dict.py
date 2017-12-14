# Pre Work Section 5b Advanced Python
# Part III - Dictionary
# Author: Sakina Zabuawala

import csv

with open('faculty.csv') as fid:
    reader = csv.reader(fid)
    next(reader, None) # ignoring the header
    
    faculty_data = []
    for row in reader:
        faculty_data.append(row)
        
# Q6. Create a dictionary with last name only
faculty_dict = {}
title_end = -1*len(' of Biostatistics')
for row in faculty_data:
    faculty_lname = row[0].split()[-1]
    faculty_info = [row[1].replace('.',''), row[2][:title_end], row[3]]
    if faculty_lname not in faculty_dict:
        faculty_dict[faculty_lname] = []
    faculty_dict[faculty_lname].append(faculty_info)

print('Biostats Faculty List at University of Pennsylvania (3 of 37) :')
for k in list(faculty_dict)[:3]:
    print({k:faculty_dict[k]})
    
# Q7. Create a dictionary with first and last name
professor_dict = {}
title_end = -1*len(' of Biostatistics')
for row in faculty_data:
    faculty_name = row[0].split()
    fname = faculty_name[0] if len(faculty_name[0].replace('.',''))>1 else faculty_name[1]
    lname = faculty_name[-1]
    name_key = (fname, lname)
    faculty_info = [row[1].replace('.',''), row[2][:title_end], row[3]]
    if name_key not in professor_dict:
        professor_dict[name_key] = faculty_info
  
print('Biostats Faculty List at University of Pennsylvania (3 of 37) :')
for k in list(professor_dict)[:3]:
    print({k:professor_dict[k]})

# Q8. Sort by last name    
professor_sort = sorted(professor_dict.items(), key=lambda item:item[0][1])
for k in professor_sort[:3]:
    print(k)