from sympy import isprime, primerange
from collections import defaultdict

def twin_primes(limit):
    """
    Generates twin prime pairs up to a given limit.
    A twin prime pair is a pair of primes (p, p+2).
    """
    # Generate all primes up to the limit using primerange
    primes = list(primerange(2, limit))

    # Filter for twin prime pairs
    return [(p, p + 2) for p in primes if isprime(p + 2) and p + 2 <= limit]

def test_conjecture_quad_offsets(limit=1_000_000):
    """
    Tests a conjecture for twin primes with four offsets up to a specified limit.
    For a twin prime pair (p, p+2), the offsets tested are:
    - q1 = 2p + 1
    - q2 = 2p + 7
    - q3 = 2p - 3
    - q4 = 2p + 3

    The results are categorized by the last digits of the twin prime pairs.
    """
    # Get all twin prime pairs within the limit
    pairs = twin_primes(limit)

    # Use defaultdict to simplify the initialization of nested dictionaries
    results = defaultdict(lambda: {
        "count": 0,
        "four_prime": 0,
        "three_prime": 0,
        "two_prime": 0,
        "one_prime": 0,
        "none_prime": 0,
        "at_least_one_prime": 0,
    })
    results["total_twin_prime_pairs"] = 0

    # Iterate through each twin prime pair
    for p, p1 in pairs:
        # The only twin prime pair not ending in (1,3), (7,9) or (9,1) is (3,5).
        # We will skip this pair to focus on the requested categories.
        if p == 3:
            continue

        # Determine the category based on the last digit of p
        last_digit_p = p % 10
        category = ""
        if last_digit_p == 1:
            category = "(1,3) ending pairs"
        elif last_digit_p == 7:
            category = "(7,9) ending pairs"
        elif last_digit_p == 9:
            category = "(9,1) ending pairs"
        
        # If the category is not found, something is wrong with our assumption.
        if not category:
            continue
        
        # Increment total count for the specific category and overall
        results[category]["count"] += 1
        results["total_twin_prime_pairs"] += 1

        # Calculate the four offsets based on the new formulas
        q1 = 2 * p + 1
        q2 = 2 * p + 7
        q3 = 2 * p - 3
        q4 = 2 * p + 3

        # Check primality for all four offsets
        is_q1_prime = isprime(q1)
        is_q2_prime = isprime(q2)
        is_q3_prime = isprime(q3)
        is_q4_prime = isprime(q4)
        
        # Count how many of the four are prime
        prime_count = is_q1_prime + is_q2_prime + is_q3_prime + is_q4_prime

        # Categorize the results based on the prime count
        if prime_count == 4:
            results[category]["four_prime"] += 1
        elif prime_count == 3:
            results[category]["three_prime"] += 1
        elif prime_count == 2:
            results[category]["two_prime"] += 1
        elif prime_count == 1:
            results[category]["one_prime"] += 1
        else: # prime_count == 0
            results[category]["none_prime"] += 1
            
        if prime_count >= 1:
            results[category]["at_least_one_prime"] += 1
    
    return results

if __name__ == "__main__":
    # Run the test with the default limit of 1,000,000
    conjecture_results = test_conjecture_quad_offsets()

    # Print the results in a structured format
    print(f"Twin Prime Conjecture Test with Four Offsets (up to 1,000,000):")
    print(f"Total twin prime pairs considered: {conjecture_results['total_twin_prime_pairs']}")
    print("-" * 50)
    
    # Iterate through categories and print results
    categories = ["(1,3) ending pairs", "(7,9) ending pairs", "(9,1) ending pairs"]
    for category in categories:
        data = conjecture_results[category]
        if data["count"] > 0:
            print(f"Results for {category}: (Total pairs: {data['count']})")
            print(f"  Four primes found: {data['four_prime']} ({data['four_prime'] / data['count']:.2%})")
            print(f"  Three primes found: {data['three_prime']} ({data['three_prime'] / data['count']:.2%})")
            print(f"  Two primes found: {data['two_prime']} ({data['two_prime'] / data['count']:.2%})")
            print(f"  One prime found: {data['one_prime']} ({data['one_prime'] / data['count']:.2%})")
            print(f"  No primes found: {data['none_prime']} ({data['none_prime'] / data['count']:.2%})")
            print(f"  At least one prime found: {data['at_least_one_prime']} ({data['at_least_one_prime'] / data['count']:.2%})")
            print("-" * 50)