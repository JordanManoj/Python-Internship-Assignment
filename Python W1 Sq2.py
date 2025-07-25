def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

s = int(input("Start: "))
e = int(input("End: "))

if s < 0 or e < 0:
    print("Only positive numbers allowed.")
else:
    primes = [str(i) for i in range(s, e+1) if is_prime(i)]
    for i in range(0, len(primes), 10):
        print(" ".join(primes[i:i+10]))

