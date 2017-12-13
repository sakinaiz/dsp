# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> >  
>> * show current working directory path  
>>  `pwd`  
>> * creating a directory  
>>  `mkdir <dirname>`  
>> * deleting a directory    
>>  `rm -r <dirname>`  
>> * creating a file using `touch` command  
>>  `touch <filename>`  
>> * deleting a file  
>>  `rm <filename>`  
>> * renaming a file  
>>  `mv <oldname> <newname>`  
>> * listing hidden files  
>>  `ls -a`  
>> * copying a file from one directory to another  
>>  `cp <src> <dest>`  
>> * display content of text file  
>>  `cat <filename>`  
>> * display the user manual   
>>  `man <keyword>`  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
>> * `ls`  
>> lists the files and directories inside current working directory  
>> * `ls -a`   
>> lists all contents of current directory including hidden files and directories  
>> * `ls -l`   
>> lists all contents of current directory in long format  
>> * `ls -lh`  
>> lists all contents of current directory in long format with readable file size  
>> * `ls -lah`   
>> lists all contents of current directory including hidden files and directories in long format with readable file size  
>> * `ls -t`   
>> lists all contents of current directory ordered by the time they were last modified   
>> * `ls -Glp`  
>> lists all contents of current directory in long format and enables colorized output. Also, writes a slash (`/`) after each filename if that file is a directory  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
>> * `ls -lc`
>> lists all contents of current directory in long format using time when file status was last changed
>> * `ls -m`
>> lists the names as a comma separated list
>> * `ls -lr`
>> lists the names in reverse order
>> * `ls -1`
>> lists each entry on a line
>> * `ls -lL`
>> lists the file or directory referenced by a symbolic link

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` reads input from standard input and executes the command supplied to it as argument one or more times based on the input read  
>> Example: `find . -type f -name '*.py' | xargs grep -l "Sakina"`




 

