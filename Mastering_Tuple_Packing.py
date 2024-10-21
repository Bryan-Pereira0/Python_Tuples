#task1
def order_processor(orders):
    for order in orders:
        customer, product, amount = order
        print(f"Customer: {customer}, Product: {product}, Amount: {amount}")
    
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Jimmy", "Camera", 1),
    ("Bobby", "Printers", 4)
]

order_processor(orders)