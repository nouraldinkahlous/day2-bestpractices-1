

@profile
def multiX(): 
 import random
 N = 50
 
 X = []
 for i in range(N):
     X.append([random.randint(0,100) for r in range(N)])
 
 Y = []
 for i in range(N):
     Y.append([random.randint(0,100) for r in range(N+1)])
 
 result = []
 for i in range(N):
     result.append([0] * (N+1))
 
 for i in range(len(X)):
     for j in range(len(Y[0])):
         for k in range(len(Y)):
             result[i][j] += X[i][k] * Y[k][j]
 for r in result:
     print(r)

multiX()
