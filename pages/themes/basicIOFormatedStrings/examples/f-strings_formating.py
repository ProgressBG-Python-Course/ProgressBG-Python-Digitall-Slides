# # ------------------- Precision for Floating Point Numbers ------------------- #
# pi = 3.14159265

# # rounded to 2 decimal places
# print(f"{pi:.2f}")
# # 3.14

# # ---------------------- Format a number as a percentage --------------------- #
# accuracy = 0.95678
# print(f"Accuracy: {accuracy:.2%}")


# # ----------------------------- Aligning Strings ----------------------------- #
# x = 123

# # Right-align a string and pad it with spaces on the left:
# print(f"--->{x:>10}<---")
# # --->       123<---

# # Center-align a string by adding spaces on both sides:
# print(f"--->{x:^10}<---")
# # --->   123    <---

# # Pad a string with different symbol ('*'):
# print(f'--->{x:*^10}<---')
# # --->***123****<---

# day = 5

# # Pad an integer with zeros.
# print(f"Day of the month: {day:02d}")
# # Day of the month: 05


# # ---------------------------- Dynamic Formatting ---------------------------- #
# value = 12.34567
# precision = 3

# # Use variables to determine the format.
# print(f"Value: {value:.{precision}f}")
# # Value: 12.346


# ----------------------------------- TASK: ---------------------------------- #
# |==========|==========|
# |         1|1         |
# |        23|23        |
# |       456|456       |
# |==========|==========|

print(f"|{'='*10}|{'='*10}|")
print(f"|{1:>10}|{1:<10}|")
print(f"|{23:>10}|{23:<10}|")
print(f"|{456:>10}|{456:<10}|")
print(f"|{'='*10}|{'='*10}|")