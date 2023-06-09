# -*- coding: utf-8 -*-
"""700740428_ICP_ML_Assignment_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQFIcL3bCN4bYp2IwQhcFjfIZtb3je-_
"""

import numpy as np # importing numpy as np

"""Using NumPy create random vector of size 15 having only Integers in the range 1-20.

"""

data = np.random.randint(1, 13,15) # creating a numpy array with random integers from 1 to 12 and with size 15
data

"""Reshape the array to 3 by 5"""

data = data.reshape(3,5) # reshaping the numpy array with the size 3*5 
data

"""print  shape of the array"""

print(data.shape) # printing the shape of the numpy array

"""Replace the max in each row by 0"""

max_ind = np.argmax(data, axis=1) # using argmax taking the indexes of the max values in each row by giving axis = 1 
row_ind = np.arange(data.shape[0]) # getting the row index of the numpy array
multi_ind = np.array([row_ind, max_ind]) # getting an 2d array of max valued index and the row index
linear_ind = np.ravel_multi_index(multi_ind, data.shape) # Converts a tuple of index arrays into an array of flat indices
data.reshape((-1))[linear_ind] = 0 #replacing the max values in each row to 0
data # printing the numpy array

"""Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type
of the array
"""

arr = np.random.randint(1, 13,(4,3),dtype = 'int32') # creating an numpy array with integers from 1 to 12 with datatype as 4 byte int and with shape 4*3
print(arr) # printing the numpy array
print('Shape of the array is {}'.format(str(arr.shape))) # Printing the shape of the array
print('Data type of the array is {}'.format(str(arr.dtype))) # printing the datatyp of array elements

"""Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
[[ 3 -2]
[ 1 0]]
"""

eigen = np.array([[3,-2],  
              [1,0]]) # creating the given numpy array 
eigen_values, eigen_vectors = np.linalg.eig(eigen) # getting the eigen values and eigen vectors of the the given numpy array 

print("Eigen values of the given array:\n",eigen_values) # printing the eigen values

print("Right eigen vectors of the given array:\n",eigen_vectors) # printing the eigen vectors

"""Compute the sum of the diagonal element of a given array.
[[0 1 2]
[3 4 5]]

"""

diag = np.array([[0,1,2],
               [3 ,4 ,5]]) # creating the given numpy array
trace = np.trace(diag) # getting the sum of the diagnol elements
print(diag)  #printing the numpy array 
print(trace) # printing the sum of the diagnol elemnts of the numpy array

"""Write a NumPy program to create a new shape to an array without changing its data. """

resh = np.arange(1,7) # creating an 1d numpy array with values 1 to 6
resh # printing the numpy array

"""Reshape 3x2:
[[1 2]
[3 4]
[5 6]]
"""

resh = resh.reshape(3,2) # reshaping it to the size 3*2
resh # printing the numpy array

"""Reshape 2x3:
[[1 2 3]
[4 5 6]]
"""

resh = resh.reshape(2,3)  # reshaping it to the size 3*2
resh # printing the numpy array

"""Write a Python programming to create a below chart of the popularity of programming Languages. """

from matplotlib import pyplot as plt # importing the pyplot functionality from matplotlib library

languages = ['Java', 'Python', 'PHP',
        'JavaScript', 'C#', 'C++'] # creating a list of labels 
 

popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7] # creting a list of values 

explode = (0.1, 0, 0, 0,0,0) # creating a tuple to create partition in the pie chart
fig, ax = plt.subplots() # Creating the pie chart
ax.pie(popularity, explode=explode,labels=languages, autopct='%1.1f%%',shadow=True, startangle=90) # creating the pie chart and giving arguments to it for labelling, placing percentage , slicing it 

plt.show()