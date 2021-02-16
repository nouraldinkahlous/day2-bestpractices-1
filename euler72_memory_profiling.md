30397485.0
Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4   14.777 MiB   14.777 MiB           1   @profile
     5                                         def gen_primes(n):
     6   14.777 MiB    0.000 MiB           1       l = range(2,n)
     7   14.777 MiB    0.000 MiB           1       primes = []
     8   14.777 MiB    0.000 MiB         999       for j in range(0,len(l)):
     9   14.777 MiB    0.000 MiB         998           p = True
    10   14.777 MiB    0.000 MiB        2968           for d in primes:
    11   14.777 MiB    0.000 MiB        2967               if(d > sqrt(l[j])):
    12   14.777 MiB    0.000 MiB         167                   break
    13   14.777 MiB    0.000 MiB        2800               if(l[j] % d == 0):
    14   14.777 MiB    0.000 MiB         830                   p = False
    15   14.777 MiB    0.000 MiB         830                   break;
    16   14.777 MiB    0.000 MiB         998           if(p):
    17   14.777 MiB    0.000 MiB         168               primes.append(l[j])
    18                                         
    19   14.777 MiB    0.000 MiB           1       return primes


Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21   14.941 MiB 149347.605 MiB        9999   @profile
    22                                         def factorize(n,primes):
    23   14.941 MiB    0.000 MiB        9999       factors = []
    24   14.941 MiB    0.000 MiB        9999       init_n = n
    25   14.941 MiB    0.000 MiB       96347       for p in primes:
    26   14.941 MiB    0.000 MiB      118736           while(n%p == 0):
    27   14.941 MiB    0.000 MiB       22389               n = n/p
    28   14.941 MiB    0.000 MiB       22389               factors.append(p)
    29   14.941 MiB    0.164 MiB       96347           if(p > sqrt(n)):
    30   14.941 MiB    0.000 MiB        9999               break
    31   14.941 MiB    0.000 MiB        9999       if(n > 1):
    32   14.941 MiB    0.000 MiB        9596           factors.append(n)
    33   14.941 MiB    0.000 MiB        9999       return factors


Filename: euler72.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    50   14.941 MiB   14.777 MiB        9999   @profile
    51                                         def fast_phi(n,primes):
    52   14.941 MiB 149347.770 MiB      9999   --->  ## this line consumes tons of memory    factors = factorize(n,primes)
    53   14.941 MiB    0.000 MiB        9999       phi = factors[0]-1
    54   14.941 MiB    0.000 MiB       31985       for i in range(1,len(factors)):
    55   14.941 MiB    0.000 MiB       21986           if(factors[i] == factors[i-1]):
    56   14.941 MiB    0.000 MiB        7685               phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                 else:
    58   14.941 MiB    0.000 MiB       14301               phi *= (factors[i]-1)
    59   14.941 MiB    0.000 MiB        9999       return phi


