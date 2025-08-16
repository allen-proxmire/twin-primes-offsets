from sympy import isprime, primerange
from collections import defaultdict

def twin_primes(limit):
    """
    Generates twin prime pairs up to a given limit.
    A twin prime pair is a pair of primes (p, p+2).
    
    Args:
        limit (int): The upper limit for the twin prime pairs.
    
    Returns:
        list: A list of twin prime pairs found.
    """
    # Generate all primes up to the limit using primerange, which is very efficient.
    primes = list(primerange(2, limit))

    # Filter for twin prime pairs from the generated list of primes.
    # The condition `p + 2 <= limit` ensures we don't exceed the boundary.
    return [(p, p + 2) for p in primes if isprime(p + 2) and p + 2 <= limit]

def test_unique_primes_from_offsets(limit=1_000_000):
    """
    Tests a conjecture for twin primes with four offsets and counts the number
    of unique prime numbers produced by these offsets.

    For a twin prime pair (p, p+2), the offsets tested are:
    - q1 = 2p + 1
    - q2 = 2p + 7
    - q3 = 2p - 3
    - q4 = 2p + 3
    
    Args:
        limit (int): The upper limit for the twin prime pairs to be checked.

    Returns:
        tuple: A tuple containing:
            - The number of unique primes found.
            - The total number of twin prime pairs considered.
    """
    # Get all twin prime pairs within the specified limit
    pairs = twin_primes(limit)
    
    # Initialize a set to store all unique prime numbers found.
    # A set is used because it automatically handles duplicates.
    unique_primes_found = set()
    
    # Iterate through each twin prime pair
    for p, p1 in pairs:
        # The only twin prime pair not ending in (1,3), (7,9) or (9,1) is (3,5).
        # We will skip this pair to focus on the requested categories, but we still 
        # need to check the (3,5) pair to be comprehensive in the unique prime count.
        # This modification is made to ensure all twin primes are considered.
        
        # Calculate the four offsets
        q1 = 2 * p + 1
        q2 = 2 * p + 7
        q3 = 2 * p - 3
        q4 = 2 * p + 3

        # Check each offset for primality and add to the set if it's a prime.
        # The set handles the uniqueness automatically.
        if isprime(q1):
            unique_primes_found.add(q1)
        if isprime(q2):
            unique_primes_found.add(q2)
        if isprime(q3):
            unique_primes_found.add(q3)
        if isprime(q4):
            unique_primes_found.add(q4)
            
    return len(unique_primes_found), len(pairs)

if __name__ == "__main__":
    # Run the test with the default limit of 1,000,000
    number_of_unique_primes, total_pairs = test_unique_primes_from_offsets()

    # Print the results
    print(f"Twin Prime Conjecture Test with Four Offsets (up to 1,000,000):")
    print(f"Total twin prime pairs considered: {total_pairs}")
    print(f"Number of unique prime numbers produced by the four offsets: {number_of_unique_primes}")
    print("-" * 50)
    print(f"The offsets are: 2p+1, 2p+7, 2p-3, and 2p+3.")