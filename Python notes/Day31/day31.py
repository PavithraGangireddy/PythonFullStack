#creating numpy array
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr)

#one dimensional array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])

#two dimensional array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#mean
import numpy as np
marks = np.array([60, 70, 80, 90, 100])
print("Average:", np.mean(marks))

#median
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Median:", np.median(arr))

#sorting
import numpy as np
arr = np.array([50, 20, 40, 10, 30])
print(np.sort(arr))

#student data analysis
import numpy as np
marks = np.array([65, 70, 85, 55, 90])
print("marks:" , marks)
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))

#row sum
import numpy as np
arr = np.array([
    [10, 20],
    [30, 40]
])
print(np.sum(arr, axis=1))

#coloum sum
import numpy as np
arr = np.array([
    [10, 20],
    [30, 40]
])
print(np.sum(arr, axis=0))