def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) # remove odd numbers
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]
    
    # In case you noob, use primes = list(primes_upto(n)) to get the list
