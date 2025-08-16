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
OFFSET_LABELS = {1: "2p+1", 3: "2p+3", -3: "2p-3", -5: "2p-5", 7: "2p+7", 9: "2p+9", -9: "2p-9"}

print(f"Finding twin primes with p < {TWIN_PRIME_LIMIT}...")
first_terms_of_twin_primes = find_twin_primes(TWIN_PRIME_LIMIT)
total_twin_primes = len(first_terms_of_twin_primes)
print(f"Total twin prime pairs considered: {total_twin_primes}")
print("-" * 50)

# 3. Initialize data structures to hold results by p's last digit.
# The keys will be the last digit (1, 7, or 9).
results_by_digit = {
    1: {'count': 0, 'offsets': defaultdict(int), 'total_primes': 0, 'label': "(1,3) ending pairs"},
    7: {'count': 0, 'offsets': defaultdict(int), 'total_primes': 0, 'label': "(7,9) ending pairs"},
    9: {'count': 0, 'offsets': defaultdict(int), 'total_primes': 0, 'label': "(9,1) ending pairs"}
}

# 4. Analyze each p and count the successful offsets.
print("Analyzing offsets and grouping by the last digit of p...")

for p in first_terms_of_twin_primes:
    p_last_digit = p % 10
    
    if p_last_digit in results_by_digit:
        results_by_digit[p_last_digit]['count'] += 1
        
        for offset in OFFSETS:
            q = 2 * p + offset
            if is_prime(q):
                results_by_digit[p_last_digit]['offsets'][offset] += 1
                results_by_digit[p_last_digit]['total_primes'] += 1

# 5. Write the final report to a CSV file.
file_name = "offset_success_by_digit.csv"
print(f"Writing results to '{file_name}'...")

with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Offset Success by Last Digit Categories"])
    writer.writerow(["", "", ""]) # Blank row for separation

    # Write results for each category.
    for digit in sorted(results_by_digit.keys()):
        category_data = results_by_digit[digit]
        total_pairs_in_category = category_data['count']
        total_primes_produced = category_data['total_primes']
        
        writer.writerow([f"Results: Offset Success for {category_data['label']}: (Total pairs: {total_pairs_in_category})", "", ""])
        
        # Sort offsets for consistent output order.
        for offset in sorted(OFFSETS):
            success_count = category_data['offsets'][offset]
            # The percentage is now calculated based on the total primes produced in the category.
            percentage = (success_count / total_primes_produced) * 100 if total_primes_produced > 0 else 0
            writer.writerow([f"Offset {OFFSET_LABELS[offset]}:", f"{success_count} successes", f"({percentage:.2f}%)"])
        
        writer.writerow(["Primes produced:", category_data['total_primes'], ""])
        writer.writerow(["", "", ""]) # Blank row for separation
        
print("CSV file has been created successfully.")
