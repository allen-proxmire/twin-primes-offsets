# Offsetting Twin Primes — Computational Note

**Author:** Allen Proxmire  
**Date:** August 2025  

---

## Overview
This project explores a simple but intriguing pattern in prime numbers.

For each twin prime pair \((p, p+2)\) with \(p \leq 1,000,000\), I applied four linear offsets to the first prime \(p\):

- **q₁ = 2p + 1**  — (Sophie Germain form)  
- **q₂ = 2p + 7**  
- **q₃ = 2p − 3**  
- **q₄ = 2p + 3**  

The resulting numbers were tested for primality, and results were categorized by the last-digit pattern of the twin prime pair.

---

## Key Findings
- At least one offset produces a prime in **~57%** of all twin prime pairs tested.
- Twin primes ending in **(1,3)** and **(7,9)** yield primes in **~64%** of cases.
- Pairs ending in **(9,1)** yield primes less often (~43%), and only q₁ and q₄ produce them in this case.
- This suggests interesting structural biases in prime distribution worth further exploration.

---

## Files in this Repository
- **OFFSETTING_TWIN_PRIMES_PUB_NOTE.pdf** — Full 3-page write-up of methods and results.
- Python script for generating twin primes, applying offsets, and testing for primality.
- CSV data file of all results for reproducibility.

---

## How to Reproduce
1. Generate all twin primes (p, p+2) with (p ≤ 1,000,000).
2. Apply the four offset formulas to \(p\).
3. Test each result for primality.
4. Tabulate prime/non-prime counts by twin prime ending digit pattern.

---

## DOI
https://doi.org/10.5281/zenodo.16804729

---

## Contact
I welcome questions, feedback, or collaborations.  
Please open an **Issue** in this repository or email me directly.
