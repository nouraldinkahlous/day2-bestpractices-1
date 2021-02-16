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

Wrote profile results to matmult.py.lprof
Timer unit: 1e-06 s

Total time: 33.1757 s
File: matmult.py
Function: MultiX at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def MultiX():
     5         1          2.0      2.0      0.0   N = 250
     6
     7                                            # NxN matrix
     8         1          1.0      1.0      0.0   X = []
     9       251        250.0      1.0      0.0   for i in range(N):
    10       250     377978.0   1511.9      1.1       X.append([random.randint(0,100) for r in range(N)])
    11
    12                                            # Nx(N+1) matrix
    13         1          1.0      1.0      0.0   Y = []
    14       251        238.0      0.9      0.0   for i in range(N):
    15       250     380057.0   1520.2      1.1       Y.append([random.randint(0,100) for r in range(N+1)])
    16
    17                                            # result is Nx(N+1)
    18         1          1.0      1.0      0.0   result = []
    19       251        204.0      0.8      0.0   for i in range(N):
    20       250       1644.0      6.6      0.0       result.append([0] * (N+1))
    21
    22                                            # iterate through rows of X
    23       251        220.0      0.9      0.0   for i in range(len(X)):
    24                                                # iterate through columns of Y
    25     63000      49284.0      0.8      0.1       for j in range(len(Y[0])):
    26                                                    # iterate through rows of Y
    27  15750250   13441752.0      0.9     40.5  =====> ##this loop takes most of time         for k in range(len(Y)):
    28  15687500   18865657.0      1.2     56.9  =====> ##also this line            result[i][j] += X[i][k] * Y[k][j]
    29       251        247.0      1.0      0.0   for r in result:
    30       250      58191.0    232.8      0.2  =====> ##here not much     print(r)


====>--------------------------------- After Optimization ---------------------------------------------<====

Total time: 18.8465 s
File: matmult_modifed.py
Function: do_multi at line 2

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     2                                           @profile
     3                                           def do_multi(result,X,Y,j,k,i): ### New function 
     4  15687500   12671871.0      0.8     67.2   result[i][j] += X[i][k] * Y[k][j]
     5  15687500    6174592.0      0.4     32.8   return result

Total time: 63.5463 s
File: matmult_modifed.py
Function: run_multiX at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def run_multiX():
     8         1          2.0      2.0      0.0   N = 250
     9                                           
    10         1          2.0      2.0      0.0   X = []
    11       251        288.0      1.1      0.0   for i in range(N):
    12       250     379769.0   1519.1      0.6       X.append([random.randint(0,100) for r in range(N)])
    13                                           
    14         1          1.0      1.0      0.0   Y = []
    15       251        293.0      1.2      0.0   for i in range(N):
    16       250     381155.0   1524.6      0.6       Y.append([random.randint(0,100) for r in range(N+1)])
    17                                           
    18         1          2.0      2.0      0.0   result = []
    19       251        262.0      1.0      0.0   for i in range(N):
    20       250       1606.0      6.4      0.0       result.append([0] * (N+1))
    21                                           
    22                                           ### ====> this is a faster nasted list comprehension version of the old loops <====
    23         1          3.0      3.0      0.0   [do_multi(result,X,Y,j,k,i)
    24         1   62774844.0 62774844.0     98.8          for i in range(len(X))
    25                                                       for j in range(len(Y[0]))
    26                                                           for k in range(len(Y))]
    27                                           
    28         1       8031.0   8031.0      0.0   [print(r) for r in result] ### ===> this is also faster than the old one

