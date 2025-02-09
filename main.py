def main():
    print("Hello World")

#Lab1 - Python Exercise Ex 1
# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
def find_factor():
    # print("========== Start ==========")

    x = 52633
    factors = []
    for i in range(x+1):
        if i == 0:
            continue

        if x % i == 0:
            factors.append(i)

    # print(factors)

    # print("========== End ==========")

#Lab1 - Python Exercise Ex 2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    print("========== Start ==========")

    factors = []
    for i in range(x+1):
        if i == 0:
            continue

        if x % i == 0:
            factors.append(i)

    print(factors)

    print("========== End ==========")

if __name__ == '__main__':
    print_factor(52633)