def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def twin_primes(limit):
    twins = []
    for p in range(3, limit, 2):
        if is_prime(p) and is_prime(p + 2):
            twins.append((p, p + 2))
    return twins

# Example: twin primes under 1000
twin_list = twin_primes(1000)
for pair in twin_list:
    print(pair)

print(f"Total twin primes under 1000: {len(twin_list)}")
