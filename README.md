# Offsetting Twin Primes  

## Overview  
This project explores **prime generation patterns from twin primes** by applying linear offsets to the first element \(p\) of each twin prime pair \((p, p+2)\).  

An earlier version of this analysis tested **4 offsets**. Expanding to **7 offsets** produces a significantly higher prime yield and reveals stronger distribution patterns across the offsets.  

## Offsets Analyzed  
For each twin prime pair (p, p+2), the following expressions were tested for primality:  

- q1 = 2p + 1
- q2 = 2p + 3
- q3 = 2p - 3
- q4 = 2p - 5
- q5 = 2p + 7
- q6 = 2p + 9
- q7 = 2p - 9

## Methodology  
- **Twin primes tested:** all pairs with \(p \leq 1{,}000{,}000\).  
- **Prime testing:** each \(q_i\) was checked for primality using Python.  
- **Analysis goal:** measure how often each offset produces primes and compare across offsets.  

## Key Results  
- Expanding from 4 to 7 offsets **substantially increased the number of generated primes**.  
- Certain offsets consistently outperform others in prime yield.  
- This suggests nontrivial distribution patterns worth further study.  

(A full results table is available in the repository outputs.)  

## Code and Data  
- All Python scripts used for generating and testing primes are included.  
- Data files contain counts and distributions of primes by offset.  

## Citation  
If you use this work, please cite via Zenodo:  

[![DOI]## Citation  
If you use this work, please cite via Zenodo:  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16804729.svg)](https://doi.org/10.5281/zenodo.16804729)  

## Discussion  
Open questions and possible directions:  
- Why do certain offsets consistently yield m
