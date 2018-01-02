# Matrix Algebra

import numpy as np

# matrix and vector assignment
A = np.array([[1, 2, 3],[2, 7, 4]])
B = np.array([[1, -1],[0, 1]])
C = np.array([[5, -1],[9, 1], [6, 0]])
D = np.array([[3, -2, -1],[1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

#Q1. Matrix Dimenstions
#1.1 A
A.shape
#--- (2, 3)

#1.2 B
B.shape
#--- (2, 2)

#1.3 C
C.shape
#--- (3, 2)

#1.4 D
D.shape
#--- (2, 3)

#1.5 u
u.shape
#--- (4,)

#1.6 w
w.shape
#--- (4, 1)


#Q2. Vector Operations
a = 6
#2.1 u+v
print(u+v)
#--- [ 9  7 -4  9]

#2.2 u-v
print(u-v)
#--- [ 3 -3 -2  1]

#2.3 au
print(a*u)
#--- [ 36  12 -18  30]

#2.4 u.v
print(u.dot(v))
#--- 51

#2.5 ||u||
print(np.sqrt(u.dot(u)))
#--- 8.60232526704


#Q3. Matrix Operations
#3.1 A+C
print(A+C)
#--- Not Defined

#3.2 A-C'
print(A-C.T)
#--- [[-4 -7 -3]
#---  [ 3  6  4]]

#3.3 C'+3D
print(C.T+3*D)
#--- [[14  3  3]
#---  [ 2  7  9]]

#3.4 BA
print(B.dot(A))
#--- [[-1 -5 -1]
#---  [ 2  7  4]]

#3.5 BA'
print(B.dot(A.T))
#--- Not Defined

#3.6 BC
print(B.dot(C))
#--- Not Defined

#3.7 CB
print(C.dot(B))
#--- [[ 5 -6]
#---  [ 9 -8]
#---  [ 6 -6]]

#3.8 B**4
print(B.dot(B.dot(B.dot(B))))
#--- [[ 1 -4]
#---  [ 0  1]]

#3.9 AA'
print(A.dot(A.T))
#--- [[14 28]
#---  [28 69]]

#3.10 D'D
print((D.T).dot(D))
#--- [[10 -4  0]
#---  [-4  8  8]
#---  [ 0  8 10]]