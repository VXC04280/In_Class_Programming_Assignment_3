Assignment - 3
Machine Learning (CS 5710) CRN: 22002
Vinay Kumar Camarushi
700740428
GitHub Link: https://github.com/VXC04280/In_Class_Programming_Assignment_3
Question – a)
Using NumPy create random vector of size 15 having only Integers in the range 1-20.
Solution :
• creating a numpy array with random integers from 1 to 12 and with size 15

Question – a1)
Reshape the array to 3 by 5
Sol: reshaping the numpy array with the size 3*5

Question – a2)
print shape of the array
• printing the shape of the numpy array using shape function.

Question – a3)
Replace the max in each row by 0
• using argmax taking the indexes of the max values in each row by giving axis = 1 in line 1 
• getting the row index of the numpy array in line 2 
• getting an 2d array of max valued index and the row index in line 3
• ravel_multi_index Converts a tuple of index arrays into an array of flat indices in line 4
• replacing the max values in each row to 0 in line 5 using the assignment operator

Question – 2)
Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the 
shape, type and data type of the array.
• creating an numpy array with integers from 1 to 12 with datatype as 4 byte int and with 
shape 4*3
• And printing the shape of the array along with its datatype

Question – 2a)
Write a program to compute the eigenvalues and right eigenvectors of a given square array given 
below: [[ 3 -2] [ 1 0]]
• creating the given numpy array
• getting the eigen values and eigen vectors of the the given numpy array using the linear 
algebra method.
• Printing the eigen values and eigen vectors of the given numpy array.


Question – 2b)
• Compute the sum of the diagonal element of a given array. [[0 1 2] [3 4 5]]
• creating the given numpy array
• getting the sum of the diagnol elements using the trace method.
• Printing the trace of the given numpy array


Question – 2c)
Write a NumPy program to create a new shape to an array without changing its data.
• creating the numpy array using np.arange method
• Printing the array after reshaping it to 3*2 and 2*3 arrays without changing its data with the 
help of reshape method.

Question – 2c)
Write a Python programming to create a below chart of the popularity of programming Languages. 
Sample data: Programming languages: Java, Python, PHP, JavaScript, C#, C++ 
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


Solution : 
• creating a list of labels
• creating a list of values
• creating a tuple to create partition in the pie chart
• Creating the pie chart using subplot methods and giving arguments to it for labelling, placing 
percentage, slicing it and giving the shadow


