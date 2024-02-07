# --------------------------------- Example 1 -------------------------------- #
# filename = 'example.txt'

# Pipeline Construction - Variant 1
# # Step 1: Read Lines
# lines = (line for line in open(filename))

# # Step 2: Normalize Text
# normalized_lines = (line.lower().strip() for line in lines)

# # Step 3: Filter Out Comments
# non_comment_lines = (line for line in normalized_lines if not line.startswith('#'))

# Pipeline Construction - Variant 1
# non_comment_lines = (
#     line for line in (                       # Step 3
#         line.lower().strip() for line in (   # Step 2
#             line for line in open(filename)  # Step 1
#         )
#     ) if not line.startswith('#')
# )
# # Execute the pipeline
# for line in non_comment_lines:
#     print(line)

# --------------------------------- Example 2 -------------------------------- #
# SAMPLE DATA: List of sales records
# TASK:
# 1. Filter records to include only sales from a specific region (e.g., "Europe").
# 2. Convert each record into just the sales amount (mapping).
# 3. Calculate the total sales amount for the filtered records.
sales_data = [
    {'amount': 1000, 'region': 'Europe'},
    {'amount': 1500, 'region': 'North America'},
    {'amount': 800, 'region': 'Europe'},
    {'amount': 1200, 'region': 'Asia'},
    {'amount': 3000, 'region': 'Europe'},
    {'amount': 700, 'region': 'North America'},
]
# Variant 1: with generators
europe_sales_amounts = (
    # map
    sale['amount'] for sale in (
        # filter:
        sale for sale in sales_data if sale['region']=='Europe'
    )
)
total_sales_amount = sum(europe_sales_amounts)

print(total_sales_amount)

# # Variant 2: with reduce/map/filter
# from functools import reduce
# europe_sales = filter(lambda sale:sale['region']=="Europe", sales_data)
# europe_sales_amounts = map(lambda sale:sale['amount'], europe_sales)
# total_sales_amount = sum(
#     map(lambda sale:sale['amount'],
#         filter(lambda sale:sale['region']=="Europe", sales_data)
#     )
# )

# print(total_sales_amount)

