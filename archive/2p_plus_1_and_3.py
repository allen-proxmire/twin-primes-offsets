from sympy import isprime, primerange

def twin_primes(limit):
    """
    Generates twin prime pairs up to a given limit.
    A twin prime pair is a pair of primes (p, p+2).
    """
    # Generate all primes up to the limit
    # The primerange function from sympy is a very efficient way to get primes
    primes = list(primerange(2, limit))

    # Filter for twin prime pairs
    # A pair (p, p+2) is a twin prime pair if both p and p+2 are prime
    # and p+2 does not exceed the limit.
    return [(p, p + 2) for p in primes if isprime(p + 2) and p + 2 <= limit]

def test_conjecture_v2(limit=1_000_000):
    """
    Tests a modified conjecture for twin primes up to a specified limit.
    The conjecture states that for a twin prime pair (p, p+2),
    q1 = 2p + 1 and/or q2 = 2p + 3 are prime with high frequency.
    
    The results are categorized by the last digits of the twin prime pairs.
    """
    # Get all twin prime pairs within the limit
    pairs = twin_primes(limit)

    # Initialize a nested dictionary to store the results, categorized by the last digits
    results = {
        "total_twin_prime_pairs": 0,
        "(1,3) ending pairs": {
            "count": 0,
            "both_prime": 0,
            "only_q1_prime": 0,
            "only_q2_prime": 0,
            "neither_prime": 0,
            "at_least_one_prime": 0,
        },
        "(7,9) ending pairs": {
            "count": 0,
            "both_prime": 0,
            "only_q1_prime": 0,
            "only_q2_prime": 0,
            "neither_prime": 0,
            "at_least_one_prime": 0,
        },
        "(9,1) ending pairs": {
            "count": 0,
            "both_prime": 0,
            "only_q1_prime": 0,
            "only_q2_prime": 0,
            "neither_prime": 0,
            "at_least_one_prime": 0,
        }
    }

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
        
        # Increment total count for the specific category
        results[category]["count"] += 1
        results["total_twin_prime_pairs"] += 1

        # Calculate q1 and q2 based on the new formulas
        q1 = 2 * p + 1
        q2 = 2 * p + 3

        # Check if q1 and q2 are prime
        is_q1_prime = isprime(q1)
        is_q2_prime = isprime(q2)

        # Categorize the results based on primality of q1 and q2
        if is_q1_prime and is_q2_prime:
            results[category]["both_prime"] += 1
            results[category]["at_least_one_prime"] += 1
        elif is_q1_prime:
            results[category]["only_q1_prime"] += 1
            results[category]["at_least_one_prime"] += 1
        elif is_q2_prime:
            results[category]["only_q2_prime"] += 1
            results[category]["at_least_one_prime"] += 1
        else:
            results[category]["neither_prime"] += 1
    
    return results

if __name__ == "__main__":
    # Run the test with the default limit of 1,000,000
    conjecture_results = test_conjecture_v2()

    # Print the results in a structured format
    print(f"Modified Conjecture Test Results (up to 1,000,000):")
    print(f"Total twin prime pairs considered: {conjecture_results['total_twin_prime_pairs']}")
    print("-" * 50)
    
    for category, data in conjecture_results.items():
        if category != "total_twin_prime_pairs":
            print(f"Results for {category}: (Total pairs: {data['count']})")
            print(f"  Both q1 and q2 prime: {data['both_prime']} ({data['both_prime'] / data['count']:.2%})")
            print(f"  Only q1 prime: {data['only_q1_prime']} ({data['only_q1_prime'] / data['count']:.2%})")
            print(f"  Only q2 prime: {data['only_q2_prime']} ({data['only_q2_prime'] / data['count']:.2%})")
            print(f"  Neither prime: {data['neither_prime']} ({data['neither_prime'] / data['count']:.2%})")
            print(f"  At least one prime: {data['at_least_one_prime']} ({data['at_least_one_prime'] / data['count']:.2%})")
            print("-" * 50)
