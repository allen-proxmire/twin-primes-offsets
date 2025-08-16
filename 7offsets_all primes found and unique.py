import math
import csv

def is_prime(n):
    """
    Checks if a number is prime using an efficient trial division method.
    It returns True if n is prime, otherwise False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(limit):
    """
    Finds all twin prime pairs (p, p+2) where p is less than the specified limit.
    Returns a list of the first term, p, for each twin prime pair.
    """
    twin_primes_p_terms = []
    # Twin primes must be of the form (6k-1, 6k+1) or (3, 5), so we can skip most numbers.
    # The first twin prime pair is (3, 5).
    if limit > 5:
        twin_primes_p_terms.append(3)
    
    num = 5
    while num < limit:
        if is_prime(num) and is_prime(num + 2):
            twin_primes_p_terms.append(num)
        num += 2
    return twin_primes_p_terms

def analyze_offsets(p_values, offsets):
    """
    Applies a list of offsets to a list of p-values, checks for primality,
    and returns two lists: one with all primes (including duplicates) and one with only unique primes.
    """
    all_primes_list = []
    
    for p in p_values:
        for offset in offsets:
            q = 2 * p + offset
            if is_prime(q):
                all_primes_list.append(q)
    
    # Create a list of unique primes from the full list
    unique_primes_list = sorted(list(set(all_primes_list)))
    
    return all_primes_list, unique_primes_list

# --- Main script execution ---

# 1. Define the upper limit for twin prime search.
TWIN_PRIME_LIMIT = 1_000_000

# 2. Define the offsets to test.
OFFSETS = [1, 3, -3, -5, 7, 9, -9]

print(f"Finding twin primes with p < {TWIN_PRIME_LIMIT}...")
first_terms_of_twin_primes = find_twin_primes(TWIN_PRIME_LIMIT)
print(f"Found {len(first_terms_of_twin_primes)} twin primes.")
print("-" * 50)

# 3. Test the offsets against the twin primes.
print("Analyzing offsets and collecting primes...")
all_primes, unique_primes = analyze_offsets(first_terms_of_twin_primes, OFFSETS)

print("Analysis complete.")
print(f"Total primes produced (with duplicates): {len(all_primes)}")
print(f"Total unique primes produced: {len(unique_primes)}")
print("-" * 50)

# 4. Save results to a CSV file.
file_name = "twin_prime_analysis.csv"
print(f"Writing results to '{file_name}'...")

# Write all_primes and unique_primes side-by-side in a single CSV
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["All Primes Produced (including repeats)", "Unique Primes Produced"])

    # Determine the number of rows to write
    max_len = max(len(all_primes), len(unique_primes))
    
    for i in range(max_len):
        all_prime = all_primes[i] if i < len(all_primes) else ""
        unique_prime = unique_primes[i] if i < len(unique_primes) else ""
        writer.writerow([all_prime, unique_prime])

print("CSV file has been created successfully.")

