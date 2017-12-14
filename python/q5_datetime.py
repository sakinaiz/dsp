# Hint:  use Google to find python function
# Pre-work: Question 5
# Use Python to compute days between start and stop date
# Author: Sakina Zabuawala

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_format = '%m-%d-%Y'
d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
delta = d2-d1
print("Answer a:", delta.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  
date_format = '%m%d%Y'
d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
delta = d2-d1
print("Answer b:", delta.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_format = '%d-%b-%Y'
d1 = datetime.strptime(date_start, date_format)
d2 = datetime.strptime(date_stop, date_format)
delta = d2-d1
print("Answer c:", delta.days)
