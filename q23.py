import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_sums = np.sum(data, axis=1)
column_sums = np.sum(data, axis=0)

print(f'Sum of rows: {row_sums}')
print(f'Sum of columns: {column_sums}')
