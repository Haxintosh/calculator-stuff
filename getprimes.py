import math

def find_primes(limit):
    sieved_array = [False]*(limit+1)
    primes = [];
    for i in range(2, limit+1):
        if not sieved_array[i] :
            primes.append(i)
        for j in range(1, (math.floor((limit)/i))+1):
            sieved_array[j*i] = True
    return primes

limit = input("To: ")
print(find_primes(int(limit)))
