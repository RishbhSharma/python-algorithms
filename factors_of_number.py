def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, long(n**0.5) + 1) if n % i == 0))))