Filename: matmult_modifed.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     2   14.883 MiB   14.883 MiB           1   @profile
     3                                         
     4                                         def multiX(): 
     5   15.258 MiB    0.375 MiB           1    import random
     6   15.258 MiB    0.000 MiB           1    N = 50
     7                                          
     8                                          # NxN matrix
     9   15.258 MiB    0.000 MiB           1    X = []
    10   15.281 MiB    0.000 MiB          51    for i in range(N):
    11   15.281 MiB    0.023 MiB        2650        X.append([random.randint(0,100) for r in range(N)])
    12                                          
    13                                          # Nx(N+1) matrix
    14   15.281 MiB    0.000 MiB           1    Y = []
    15   15.309 MiB    0.000 MiB          51    for i in range(N):
    16   15.309 MiB    0.027 MiB        2700        Y.append([random.randint(0,100) for r in range(N+1)])
    17                                          
    18                                          # result is Nx(N+1)
    19   15.309 MiB    0.000 MiB           1    result = []
    20   15.332 MiB    0.000 MiB          51    for i in range(N):
    21   15.332 MiB    0.023 MiB          50        result.append([0] * (N+1))
    22                                          
    23                                          # iterate through rows of X
    24   15.410 MiB    0.000 MiB          51    for i in range(len(X)):
    25                                              # iterate through columns of Y
    26   15.410 MiB    0.000 MiB        2600        for j in range(len(Y[0])):
    27                                                  # iterate through rows of Y
    28   15.410 MiB    0.078 MiB      130050            for k in range(len(Y)): ----> ## this loop is memory intensive
    29   15.410 MiB    0.000 MiB      127500                result[i][j] += X[i][k] * Y[k][j]
    30   15.449 MiB    0.000 MiB          51    for r in result:
    31   15.449 MiB    0.039 MiB          50        print(r)


---------------------------------------------------------------------------------------
         727183 function calls (727140 primitive calls) in 5.935 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      4/1    0.000    0.000    5.935    5.935 {built-in method builtins.exec}---> ## one function takes most of the time but not clear which is it ... 
        1    5.552    5.552    5.935    5.935 matmult.py:2(<module>)
   125250    0.051    0.000    0.313    0.000 random.py:218(randint)
   125250    0.109    0.000    0.263    0.000 random.py:174(randrange)
      250    0.023    0.000    0.183    0.001 matmult.py:9(<listcomp>)
      250    0.022    0.000    0.175    0.001 matmult.py:14(<listcomp>)
   125250    0.103    0.000    0.153    0.000 random.py:224(_randbelow)
   158438    0.037    0.000    0.037    0.000 {method 'getrandbits' of '_random.Random' objects}
   125250    0.014    0.000    0.014    0.000 {method 'bit_length' of 'int' objects}
      9/1    0.000    0.000    0.013    0.013 <frozen importlib._bootstrap>:978(_find_and_load)
      9/1    0.000    0.000    0.013    0.013 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
      9/1    0.000    0.000    0.012    0.012 <frozen importlib._bootstrap>:663(_load_unlocked)
      3/1    0.000    0.000    0.012    0.012 <frozen importlib._bootstrap_external>:722(exec_module)
     15/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        1    0.001    0.001    0.011    0.011 random.py:38(<module>)
      250    0.006    0.000    0.008    0.000 {built-in method builtins.print}
    63010    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap>:882(_find_spec)
        1    0.000    0.000    0.004    0.004 hashlib.py:54(<module>)
--------------------------------------------------------------------------------------

n: multiX at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def multiX(): 
     5         1          7.0      7.0      0.0   import random
     6         1          3.0      3.0      0.0   N = 50
     7                                            
     8         1          2.0      2.0      0.0   X = []
     9        51         94.0      1.8      0.0   for i in range(N):
    10        50      26199.0    524.0      7.5       X.append([random.randint(0,100) for r in range(N)])
    11                                            
    12         1          1.0      1.0      0.0   Y = []
    13        51         60.0      1.2      0.0   for i in range(N):
    14        50      18383.0    367.7      5.2       Y.append([random.randint(0,100) for r in range(N+1)])
    15                                            
    16         1          1.0      1.0      0.0   result = []
    17        51         46.0      0.9      0.0   for i in range(N):
    18        50         92.0      1.8      0.0       result.append([0] * (N+1))
    19                                            
    20        51         47.0      0.9      0.0   for i in range(len(X)):
    21      2600       2481.0      1.0      0.7       for j in range(len(Y[0])):
    22    130050     124110.0      1.0     35.4 --> this loop consumes most of the time           for k in range(len(Y)):
    23    127500     177101.0      1.4     50.5               result[i][j] += X[i][k] * Y[k][j]
    24        51         61.0      1.2      0.0   for r in result:
    25        50       1728.0     34.6      0.5       print(r)

