# | Feature                   | NumPy Array                               | Python List                               |
# |---------------------------|-------------------------------------------|-------------------------------------------|
# | Type                      | ndarray (multi-dimensional array)         | List (dynamic array)                      |
# | Storage                   | Contiguous memory blocks                  | Non-contiguous memory blocks              |
# | Performance               | Faster due to optimized C code            | Slower due to Python overhead             |
# | Data Type Consistency     | Requires consistent data types            | Allows mixed data types                   |
# | Element-wise Operations   | Supports element-wise operations          | No native element-wise operations         |
# | Memory Efficiency         | More memory efficient                     | Less memory efficient                     |
# | Ease of Use               | Requires learning NumPy-specific syntax   | Simpler to use with basic Python syntax   |
# | Functions and Methods     | Rich set of mathematical functions        | Limited functions compared to NumPy       |
# | Scalability               | Better for large-scale data               | Not optimized for large data sets         |
# | Broadcasting              | Supports broadcasting for operations      | No support for broadcasting               |

import numpy as np

# # a=np.array([1,2,3,4,5])
# # print(a)

# b=np.array([[1,2,3,4],[1,2,3,5]])
# # print(b)
# # print(b.ndim )
# # print(b.shape)
# # print(b.dtype)
# # print(b.nbytes)
# # print(b.size)
# # print(b.itemsize)
# # print(b[1,2]) # 3
# # print(b[0])
# # print(b[:,3])
# a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])#[start:end:step]

# print(a[0,1:-1:1])

no