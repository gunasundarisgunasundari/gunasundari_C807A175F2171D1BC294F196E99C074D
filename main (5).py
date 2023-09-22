def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage
Products=["shoes","boot","loafer","shoes","sandles","shoes"]
target="shoes"
target2='apple'
result = linear_search_product(Products,target)
print(result)