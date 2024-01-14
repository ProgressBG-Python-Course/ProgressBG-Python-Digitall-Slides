import pandas as pd

# Sample dataset
data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Applying a bulk operation - adding 10 to each element
updated_data = data + 10

print(updated_data)