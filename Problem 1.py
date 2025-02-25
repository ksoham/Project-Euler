#Multiples of 3 or 5
#approach 1

def sum_3_5(n: int) -> int:
    total = 0
    for i in range(3, n):  # Loop through numbers from 3 to n-1
        if i % 3 == 0 or i % 5 == 0:
            total += i  # Add to total
    return total  # Return the final sum after the loop completes

print(sum_3_5(10))



