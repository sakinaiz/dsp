# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> #### Similarities:
>>
>>  Both store a ordered sequence of values and the values can be of any type and are indexed by integers
>> 
>> #### Differences:
>> 
>> * Tuples are immutable, whereas lists are mutable
>> * Tuples are hashable, while lists are not hashable
>> * Tuples are heterogeneous data structures while lists are homogeneous sequences
>>
>> Tuples will work as keys in dictionaries, since they are immutable

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> #### Similarities:
>>
>> Both store a sequence of values and the values can be of any type
>>
>> #### Differences:
>>
>> * Sets are unordered collection with no duplicate elements, while lists are ordered collection of elements
>> * Sets are immutable whereas lists are mutable
>> * Set items can not be accessed by index
>>
>> #### Examples:
>>
>> **Lists**:  
>> ```
>> >>> a = [1, 2, 3, 3]
>> >>> b = [3, 4, 5, 5]
>> >>> a.extend(b)
>> >>> print(a)
>> [1, 2, 3, 3, 3, 4, 5, 5, 3, 4, 5, 5]
>>```
>> **Sets**: 
>> ```
>> >>> a = set([1, 2, 3, 3])
>> >>> b = set([3, 4, 5, 5])
>> >>> a.union(b)
>> set([1, 2, 3, 4, 5])
>> ```
>> ##### Performance Comparison
>>
>> Sets are significantly faster than unsorted lists for finding an element in a sequence, since they are hashable

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is used to create small anonymous functions (i.e., functions that do not have a name) in Python. It can have any number of arguments but only one expression.  
>> It is used whenever function objects are required.  
>> Example:
>>
>> ```
>> >>> double = lambda x: 2*x  
>> >>> print(double(5))  
>> 10
>> 
>> >>> students = [("Alice", 30), ("Bob", 25), ("Joe", 22)]  
>> >>> sorted(students, key=lambda pair:pair[1])  
>> [('Joe', 22), ('Bob', 25), ('Alice', 30)]
>> ```
>>

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> #### List Comprehension
>> List comprehension is an elegant way to define and create a list in Python
>> ```
>> >>> map(lambda x:x**2, range(10)) # using map 
>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>> >>> [x**2 for x in range(10)] # using list comprehension
>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>
>> >>> filter(lambda x: x%2, range(10)) # using filter
>> [1, 3, 5, 7, 9]
>> >>> [x for x in range(10) if x%2!=0] # using list comprehension
>> [1, 3, 5, 7, 9]
>> ```
>> 
>> #### Set Comprehension
>> ```
>> >>> x2 = {x**2 for x in range(10) if x%2==0} # squares of even numbers betwen 0 and 9
>> >>> print x2
>> set([0, 16, 4, 64, 36])
>> ```
>> #### Dictionary Comprehension
>> ```
>> >>> c = {1:"one", 2:"two"}
>> >>> d = {3:"three", 4:"four"}
>> >>> merged = {k:v for a in (c,d) for k,v in a.items()}
>> >>> print merged
>> {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>> ```
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





