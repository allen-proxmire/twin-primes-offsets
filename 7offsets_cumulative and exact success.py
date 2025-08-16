import math
import csv
from collections import defaultdict

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
    # The first twin prime pair is (3, 5).
    if limit > 5:
        twin_primes_p_terms.append(3)
    
    num = 5
    while num < limit:
        if is_prime(num) and is_prime(num + 2):
            twin_primes_p_terms.append(num)
        num += 2
    return twin_primes_p_terms

# --- Main script execution ---

# 1. Define the upper limit for twin prime search.
TWIN_PRIME_LIMIT = 1_000_000

# 2. Define the offsets to test.
OFFSETS = [1, 3, -3, -5, 7, 9, -9]

print(f"Finding twin primes with p < {TWIN_PRIME_LIMIT}...")
first_terms_of_twin_primes = find_twin_primes(TWIN_PRIME_LIMIT)
total_twin_primes = len(first_terms_of_twin_primes)
print(f"Total twin prime pairs considered: {total_twin_primes}")
print("-" * 50)

# 3. Analyze each p and count the successful offsets.
# `success_counts` will store the count of how many times each number of successful offsets occurred.
success_counts = defaultdict(int)
# `all_primes_produced` will store all primes, including duplicates, to find the number of unique primes.
all_primes_produced = set()

for p in first_terms_of_twin_primes:
    successful_offsets_for_p = 0
    for offset in OFFSETS:
        q = 2 * p + offset
        if is_prime(q):
            successful_offsets_for_p += 1
            all_primes_produced.add(q)
    success_counts[successful_offsets_for_p] += 1

# 4. Process the data for reporting.
total_unique_primes = len(all_primes_produced)

# Calculate cumulative distribution
cumulative_counts = {}
current_sum = 0
for i in range(len(OFFSETS), -1, -1):
    current_sum += success_counts[i]
    cumulative_counts[i] = current_sum

# 5. Write the final report to a CSV file.
file_name = "offset_distribution.csv"
print(f"Writing results to '{file_name}'...")

with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write a summary section at the top.
    writer.writerow(["Summary", "Value", "Percentage"])
    writer.writerow(["Total twin prime pairs considered", total_twin_primes, ""])
    writer.writerow(["Unique prime numbers produced", total_unique_primes, ""])
    writer.writerow([]) # Blank row for separation

    # Write the exact success count distribution.
    writer.writerow(["Exact success count distribution", "", ""])
    writer.writerow(["Offsets Succeeded", "Count", "Percentage"])
    for i in range(len(OFFSETS) + 1):
        count = success_counts.get(i, 0)
        percentage = (count / total_twin_primes) * 100 if total_twin_primes > 0 else 0
        writer.writerow([i, count, f"{percentage:.2f}%"])

    writer.writerow([]) # Blank row for separation

    # Write the cumulative success count distribution.
    writer.writerow(["Cumulative success count distribution", "", ""])
    writer.writerow(["Offsets Succeeded", "Count", "Percentage"])
    for i in range(len(OFFSETS), 0, -1):
        count = cumulative_counts.get(i, 0)
        percentage = (count / total_twin_primes) * 100 if total_twin_primes > 0 else 0
        writer.writerow([f"at least {i}", count, f"{percentage:.2f}%"])

print("CSV file has been created successfully.")
