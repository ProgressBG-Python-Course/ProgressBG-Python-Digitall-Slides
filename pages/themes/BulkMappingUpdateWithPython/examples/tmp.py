# Sample data: List of transactions with product codes
transactions = [
    {'transaction_id': 1, 'product_code': 'A1', 'quantity': 3},
    {'transaction_id': 2, 'product_code': 'B2', 'quantity': 2},
    {'transaction_id': 3, 'product_code': 'C3', 'quantity': 1},
    {'transaction_id': 4, 'product_code': 'A1', 'quantity': 5},
]

# Dictionary for mapping product codes to product names
product_mapping = {
    'A1': 'Product A',
    'B2': 'Product B',
    'C3': 'Product C',
}

# Perform bulk mapping using list comprehension and dictionary get method
mapped_transactions = [
    {
        **transaction,
        'product_name': product_mapping.get(transaction['product_code'], 'Unknown'),
    }
    for transaction in transactions
]

# Optionally, if you want to remove the product_code key:
for transaction in mapped_transactions:
    del transaction['product_code']

# Display the result
for transaction in mapped_transactions:
    print(transaction)
