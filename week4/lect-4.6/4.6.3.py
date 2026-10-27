# write a piece of code to  find the dot product.

x=[1,7,3,4]
y=[8,6,3,2]

import numpy as np

x = np.array([1, 7, 3, 4])
y = np.array([8, 6, 3, 2])

# Dot product using @ operator
dot_product = x @ y
print(dot_product)

# Alternative: np.dot()
dot_product_np = np.dot(x, y)
print(dot_product_np)

# Alternative: np.sum() with element-wise multiplication
dot_product_sum = np.sum(x * y)
print(dot_product_sum)

