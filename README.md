# Offsetting Twin Primes — Computational Note

**Author:** Allen Proxmire  
**Date:** August 2025  

This repository contains my computational exploration of **twin prime offsets** —  
for each twin prime pair \((p, p+2)\) with \(p \le 1,000,000\), I applied:

- q₁ = 2p + 1  
- q₂ = 2p + 7  
- q₃ = 2p − 3  
- q₄ = 2p + 3  

and checked for additional primes.

## Summary of findings
- At least one offset yields a prime in ~57% of twin prime cases.
- Twin primes ending in (1,3) and (7,9) yield primes in ~64% of cases.
- (9,1) endings yield fewer primes (~43%), and only q₁ and q₄ work here.

## Files
- **PDF:** Full write-up of results
- **Python script:** Code to generate twin primes and test offsets
- **Data (CSV):** Counts and percentages for each category

---

I welcome feedback and collaboration!  
If you want to reproduce the results, see the code file or contact me.
