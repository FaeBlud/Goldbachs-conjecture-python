upper = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
filename = "primenumbers.txt"

with open(filename, "w") as f:
    for num in range(2, upper):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            f.write(str(num) + "\n")
