
from datetime import datetime
from typing import BinaryIO
import numpy as np


_M = 2**31 - 1
_A = 7**5
_B = 0

def LCG(n):
    seed = datetime.now().microsecond
    x1 = _A*seed % _M

    seq = [x1]
    
    for _ in range(n):
        x1 = (_A*x1 + _B)% _M
        seq.append(x1)
    return [seq[i]/_M for i in range(0,n)]



def Bernoulli(m, p):
    result = LCG(m)
    return [1 if result[i]<=p else 0 for i in range(m)]
    



def Geometric(m, p):
    sample = []
    seed = datetime.now().microsecond

    for _ in range(m):
        seed = (_A*seed)%_M
        toss = 1
        while seed>p*_M:
            seed = (_A*seed)%_M
            toss += 1
        sample.append(toss)

    return sample
    



def Binomial(m, n, p):
    result = []
    L = Bernoulli(n*m, p)

    for i in range(m):
        success = sum([ L[j] for j in range(n*i, n*(i+1)) ])
        result.append(success)
    return result


def Multinom(m: int, x: list, p: list):
    U = LCG(m)
    K = len(x)
    result = []
    
    p_cum = [p[0]]
    for i in range(1, K):
        p_cum.append(p[i]+p_cum[-1])

    for i in range(m):
        j = 0
        while U[i]>p_cum[j]:
            j += 1
        result.append(x[j])
    return result
    

x = list(range(1,7))
p = [0.1, 0.3, 0.2, 0.1, 0.1, 0.2]

print(Multinom(5, x, p))
