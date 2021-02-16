import random
@profile
def do_multi(result,X,Y,j,k,i): ### New function 
 result[i][j] += X[i][k] * Y[k][j]
 return result
@profile
def run_multiX():
 N = 250

 X = []
 for i in range(N):
     X.append([random.randint(0,100) for r in range(N)])

 Y = []
 for i in range(N):
     Y.append([random.randint(0,100) for r in range(N+1)])

 result = []
 for i in range(N):
     result.append([0] * (N+1))

### ====> this is a faster nasted list comprehension version of the old loops <====
 [do_multi(result,X,Y,j,k,i)
        for i in range(len(X))
            for j in range(len(Y[0]))
                for k in range(len(Y))]

 [print(r) for r in result] ### ===> this is also faster than the old one

run_multiX()
###----------------------------------------------------old_Version-------------------------------------------------###

###
###import random
###
###def multi(i,j,k,X):
### result[i][j] += X[i][k] * Y[k][j]
### return result
###
###def multiX(): 
### N = 50
### 
### X = []
### for i in range(N):
###     X.append([random.randint(0,100) for r in range(N)])
### 
### Y = []
### for i in range(N):
###     Y.append([random.randint(0,100) for r in range(N+1)])
### 
### result = []
### for i in range(N):
###     result.append([0] * (N+1))
### 
### for i in range(len(X)):
###     for j in range(len(Y[0])):
###         for k in range(len(Y)):
###             result[i][j] += X[i][k] * Y[k][j]
### 
### [r for r in result]
###
###multiX()
###
