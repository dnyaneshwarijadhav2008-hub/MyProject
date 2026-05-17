# Write a function to print even number from 1 to 100 using loop function
def print_even_numbers():
    for num in range(1, 101):  
        if num % 2 == 0:       
            print(num)

print_even_numbers()
