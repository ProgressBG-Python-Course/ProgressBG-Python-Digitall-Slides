products = {
    'apple': 3,
    'coffee': 2.5,
    'beer': 4.20
}

sorted_products = sorted(products.items(), key=lambda item:item[1])
print(sorted_products)