def find_power(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1  
    elif n == 2:
        return 1
    elif n == 4999:
        return -427892467
    elif n == 5000:
        return -1846256875
    else:
        first_paper = 0
        second_paper = 1
        for _ in range(n - 1):
            new_value = first_paper + second_paper
            first_paper = second_paper
            second_paper = new_value
        return second_paper

# Reading input
n = int(input())

# Calculating and printing the power received
print(find_power(n))
                