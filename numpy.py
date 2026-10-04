#Q1
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", numbers)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)
print("Number of Dimensions:", numbers.ndim)

#Q2
import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 8, 10])

print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)
print("Modulus:", array1 % array2)

#Q3
import numpy as np

values = np.array([12, 25, 8, 45, 32, 19, 50, 27, 14, 36])

print("Array:", values)
print("Maximum:", np.max(values))
print("Minimum:", np.min(values))
print("Sum:", np.sum(values))
print("Average:", np.mean(values))

#Q4
import numpy as np

numbers = np.arange(1, 21)

even_numbers = numbers[numbers % 2 == 0]
odd_numbers = numbers[numbers % 2 != 0]

print("Array:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

#Q5
import numpy as np

numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)

print("\n2 x 6 Matrix:")
print(numbers.reshape(2, 6))

print("\n3 x 4 Matrix:")
print(numbers.reshape(3, 4))

print("\n4 x 3 Matrix:")
print(numbers.reshape(4, 3))

#Q6
import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Matrix Addition:")
print(result)

#Q8
import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:")
print(matrix)

print("Transpose:")
print(matrix.T)

#Q12
import numpy as np

numbers = np.array([20, 65, 35, 80, 45, 90, 10, 55, 30, 75])

print("Original Array:", numbers)

numbers[numbers > 50] = 0

print("Updated Array:", numbers)

#Q13
import numpy as np

numbers = np.array([45, 12, 89, 23, 67, 5, 34])

ascending = np.sort(numbers)
descending = np.sort(numbers)[::-1]

print("Original Array:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

#Q14
import numpy as np

numbers = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40, 10])

unique_values = np.unique(numbers)

print("Original Array:", numbers)
print("Unique Elements:", unique_values)

#Q15
import numpy as np

marks = np.array([78, 85, 67, 92, 74, 88, 95, 69, 81, 76])

print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

