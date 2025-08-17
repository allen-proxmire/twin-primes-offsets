# Offsetting Twin Primes — Computational Note

**Author:** Allen Proxmire  
**Date:** August 2025  

---

## Overview
This project explores a simple but intriguing pattern in prime numbers.

For each twin prime pair \((p, p+2)\) with \(p \leq≤\ 1,000,000\), I applied seven linear offsets to the first prime \(p\):

- **q1 = 2p + 1**  (Sophie Germain form)
- **q2 = 2p + 3**  
- **q3 = 2p − 3**
- **q4 = 2p − 5**  
- **q5 = 2p + 7**  
- **q6 = 2p + 9**
- **q7 = 2p − 9**  

The resulting numbers were tested for primality, and results were categorized by the last-digit pattern of the twin prime pair.

---

## Key Findings
- At least one offset produces a prime in **~82%** of all twin prime pairs tested.
- Twin primes ending in (1,3), (7,9), (9,1) yield primes from the offsets in amounts ~5% of each other.
- Applying the seven offsets to the twin primes generates 7.65% of all prime numbers tested.
- This suggests interesting structural biases in prime distribution worth further exploration.

---

## Files in this Repository
- **OFFSETTING TWIN PRIMES_v3.1_7OFFSETS_15AUG25.pdf** — Full 5-page write-up of methods and results.
- Python script for generating twin primes, applying offsets, and testing for primality.
- CSV data file of all results for reproducibility.

---

## How to Reproduce
1. Generate all twin primes (p, p+2) with (p ≤ 1,000,000).
2. Apply the seven offset formulas to \(p\).
3. Test each result for primality.
4. Tabulate exact and cumulative totals.
5. Tabulate prime/non-prime counts by twin prime ending digit pattern.

---

## DOI
https://doi.org/10.5281/zenodo.16804729

---

## Contact
I welcome questions, feedback, or collaborations.  
Please open an **Issue** in this repository or email me directly.
