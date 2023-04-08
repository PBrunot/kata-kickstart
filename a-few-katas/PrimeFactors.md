Prime Factors
=============

**Compute the prime factors of a given natural number.**

Create a function `primeFactors` that takes in an integer number and returns a list (or array) of its prime factors.

Note: a **prime** number is a positive integer that is only divisible by itself and 1 (by the way, 1 is _not_ a prime
number).

Examples
--------

- What are the prime factors of 5?
    - 5 is a prime number, so its only prime factor is itself.
    - Thus, the prime factors of 5 are: \[ 5 \]
- What are the prime factors of 6?
    - 2 is a prime factor of 6, because 2 goes into 6 evenly.
    - 3 is also a prime factor of 6, because 3 goes into 6 evenly.
    - Thus, the prime factors of 6 are: \[ 2, 3 \]
- What are the prime factors of 60?
    - 2 is a prime factor of 60, because 60/2=30 exactly.
    - 2 is a prime factor of 30, because 30/2=15 exactly.
    - 3 is a prime factor of 15, because 15/3=5 exactly.
    - 5 is a prime factor of 5, because ... well, it's prime.
    - Thus, the prime factors of 60 are: \[ 2, 2, 3, 5 \]
- What are the prime factors of 1?
    - 1 is not a prime number, and it has no prime factors.
    - Thus, the prime factors of 1 are an empty list: \[ \]

TL;DR
-----
Return a list of the prime factors of a given natural number.

