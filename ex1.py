
    
def print_numbers():
    """Print the first 10 numbers using a while loop"""
    
    numbers = range(1,10)
    while True:
        for num in numbers:
            print(num)
        if num > 10:
            break
            

print_numbers()