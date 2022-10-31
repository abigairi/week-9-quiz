#question one:What is the result of the following code?

from statistics import median
import statistics
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

#question two:Create a numpy array of 10 zeros. and reshape it to (2, 5)

array=np.zeros(10)
array=array.reshape(2,5)
print(array)

#question three:Find Mean, Mode, Median, Standard Deviation of the following data
#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data = np.array(data)
#mean
mean = data.mean()
print(mean)

#median
median = np.median(data)
print(median)

#mode
mode =statistics.mode(data)
print(mode)


#question four:create a 6x6 numpy array with random values and find the min and max values

array = np.random.random((6,6))
print("6x6 numpy array is")
print(array) 
array_min, array_max = array.min(), array.max()
print("Minimum and Maximum Values is")
print(array_min, array_max)


#question five:create a 3D numpy array and reshape it to 2D

