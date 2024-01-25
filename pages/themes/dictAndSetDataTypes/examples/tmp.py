import time

# Creating a large set and list for demonstration
large_set = set(range(10_000_000))
large_list = list(range(10_000_000))

# Iterating through a list and a set
start_time = time.time()
for item in large_list:
    pass  # Simple iteration
list_iteration_duration = time.time() - start_time

start_time = time.time()
for item in large_set:
    pass  # Simple iteration
set_iteration_duration = time.time() - start_time

print(f"Time taken for iterating list: {list_iteration_duration:.8f} seconds")
print(f"Time taken for iterating set: {set_iteration_duration:.8f} seconds")

