# NumPy: A Fundamental Python Library for Scientific Computing

# Main Purpose

NumPy (Numerical Python) is a vital Python library designed for scientific computing. It offers support for large, multi-dimensional arrays and matrices, along with a comprehensive collection of mathematical functions. NumPy's main purpose is to enable efficient numerical computations in Python, particularly when dealing with large datasets or complex mathematical operations.

# When to Use NumPy

Consider using NumPy in the following scenarios,

- **Numerical Computations**: When performing mathematical operations on large arrays of data, NumPy provides optimized routines that significantly improve performance over standard Python lists.
- **Data Analysis**: NumPy is widely used for handling and manipulating large datasets, performing statistical operations, and numerical computations required for data preprocessing.
- **Scientific Simulations**: NumPy's array operations and mathematical functions are valuable for representing and manipulating data involved in scientific simulations or modeling.
- **Machine Learning**: NumPy is a fundamental library in machine learning, providing support for handling training data, performing matrix computations, implementing algorithms, and optimizing code execution.

## Problems NumPy Fixes

NumPy addresses several limitations and performance issues associated with standard Python lists. It fixes the following problems,

- **Speed**: NumPy's pre-compiled C code makes it significantly faster than standard Python lists for array operations.
- **Memory Efficiency**: NumPy arrays are more memory-efficient due to their homogeneous data types and fixed sizes.
- **Vectorized Operations**: NumPy allows performing operations on entire arrays, eliminating the need for explicit loops and resulting in cleaner and more concise code.
- **Mathematical Functions**: NumPy provides a wide range of efficient mathematical functions such as trigonometry, logarithms, exponentials, and more.

# Essential Understanding of NumPy

## ndarray Object

The ndarray is the core object of NumPy, representing a multi-dimensional array. It has the following essential attributes,

- **ndarray.shape**: Returns the dimensions of the array.
- **ndarray.dtype**: Specifies the data type of the elements in the array.
- **ndarray.ndim**: Gives the number of array dimensions.

Here is a following example,

```Python
import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d.shape)  # Output: (5,)
print(arr_1d.dtype)  # Output: int64 or int32 depending on the system architecture
print(arr_1d.ndim)   # Output: 1

# Creating a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d.shape)  # Output: (2, 3)
print(arr_2d.dtype)  # Output: int64 or int32 depending on the system architecture
print(arr_2d.ndim)   # Output: 2

```

## Array creation

NumPy provides various functions to create arrays efficiently. Some commonly used functions include:

- **numpy.array()**: Creates an array from a Python list or tuple.
- **numpy.zeros()**: Creates an array filled with zeros.
- **numpy.ones()**: Creates an array filled with ones.
- **numpy.random.random()**: Creates an array of random values between 0 and 1.
- **numpy.arange()**: Creates an array with evenly spaced values.

Here is a following example,


#### np.array()

```
arr = np.array([1, 2, 3, 4, 5])              # 1D array
print(arr)

arr_2 = np.array([[1, 2, 3],  # 2D array
                  [4, 5, 6]])
print(arr_2)
```

```
[1 2 3 4 5]
```

```
[[1 2 3]
 [4 5 6]]
```

#### np.zeros()


```Python
zeros_arr = np.zeros((3, 4))                 # 2D array filled with zeros
```

```
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```

#### np.ones()

```Python
ones_arr = np.ones((2, 2, 2))                # 3D array filled with ones
```

```
[[[1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]]]
```

#### np.random.random()

```Python
random_arr = np.random.random((2, 3))        # 2D array of random values
```

```
[[0.22241877 0.10325394 0.16304831]
 [0.40448334 0.4438561  0.80418444]]
```

#### np.arange()

```Python
range_arr = np.arange(0, 10, 2)              # 1D array with values from 0 to 10 (exclusive), step size 2
```

```
[0 2 4 6 8]
```

Although `arange()` does not directly support the immediate creation of a 2D array, it can be changed by reshaping it.

```Python
import numpy as np

# Create a 1D array with a range of values
arr_1d = np.arange(6)  # Output: [0, 1, 2, 3, 4, 5]

# Reshape the 1D array into a 2D array
arr_2d = arr_1d.reshape((2, 3))
print(arr_2d)
```

```
[[0 1 2]
 [3 4 5]]
```

## Broadcasting

Broadcasting is a feature in NumPy that enables performing operations between arrays of different shapes, automatically aligning their dimensions. It simplifies calculations and avoids unnecessary array copying.

```Python
import numpy as np

arr = np.array([1, 2, 3])
scalar = 5
print(arr * scalar)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(arr_2d + row)
```

```
[ 5 10 15]

[[11 22 33]
 [14 25 36]]
```

## Array Reshaping

Reshaping arrays allows you to change their dimensions and reorganize the data. The `reshape()` function is used to modify the shape of an array while preserving the data.

```Python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)

flattened_arr = reshaped_arr.reshape((6,))
print(flattened_arr)
```

```
[[1 2 3]
 [4 5 6]]

[1 2 3 4 5 6]
```

## Array Manipulation

 NumPy provides functions for manipulating arrays, including concatenation (`numpy.concatenate()`), splitting (`numpy.split()`), stacking (`numpy.stack()`), and more. These functions allow you to rearrange, combine, or divide arrays as needed.

 ```Python
 import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)

arr_1_2D = np.array([[1, 2, 3],
                     [4, 5, 6]])
arr_2_2D = np.array([[10, 11, 12],
                     [13, 14, 15]])
concatenated_arr_2D = np.concatenate((arr_1_2D, arr_2_2D))
print(concatenated_arr_2D)

split_arrs = np.split(concatenated_arr, 2)
print(split_arrs)

stacked_arr = np.stack((arr1, arr2))
print(stacked_arr)
 ```

 ```
 [1 2 3 4 5 6]

[[ 1  2  3]
 [ 4  5  6]
 [10 11 12]
 [13 14 15]]

[array([1, 2, 3]), array([4, 5, 6])]

[[1 2 3]
 [4 5 6]]
 ```

 ## Array Iteration

Iterating over arrays using loops or using NumPy's own iteration functions, such as `numpy.nditer()`, helps access and process array elements efficiently.
  
```Python
import numpy as np

arr = np.array([1, 2, 3])

for element in arr:
    print(element)

arr_2d = np.array([[1, 2], [3, 4]])

for row in arr_2d:
    for element in row:
        print(element)
```

```
1
2
3
1
2
3
4
```

## Vectorized Operations

Taking advantage of vectorized operations in NumPy, which operate on entire arrays rather than individual elements, greatly improves the performance and efficiency of numerical computations.

```Python
import numpy as np

arr = np.array([1, 2, 3])
another_arr = np.array([4, 5, 6])

result = arr + another_arr
print(result)
```

```
[5 7 9]
```

## Indexing, Slicing and Pandas

NumPy supports are same slicing techniques as a Pandas DataFrame, that is, such as the comma seperated slicing techniques such as

```Python
import numpy as np

a = np.array([[1, 2, 3], 
              [4, 5, 6]])
print(a[:, 1])
```

```
[2 5]
```

For a more detailed reiteration of the slicing techniques, they're detailed into my notes for the [Pandas library](https://github.com/Michael-Cowie/Notes/blob/main/Python/Notes/pandas.md). The page almost describes the key differences because Pandas and NumPy