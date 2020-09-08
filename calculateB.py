import math
from matplotlib import pyplot as plt

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def P(n,k):
    p = 0.1
    result = nCr(n,k) * (p ** k) * ((1-p) ** (n-k))
    #print("n",n)
    #print("k",k)
    #print("result",format(result,"0.50f"))
    return result

def sum(f,n):
    sum = 0.0
    for k in range(0,min(n,11)):
        sum += f(n,k)
    return sum

if __name__ == '__main__':
    x=[]
    y=[]
    for i in range(11,40):
        x.append(i)
        value = sum(P,i)
        y.append(value)
    
        if(value<0.9996):
            print("FOUND!!")
            print("the answer is",i)
            print("the value is ",value)
            break

    print(x,y)

    plt.plot(x, y)
    plt.show()