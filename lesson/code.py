


import random

def genOddList(n: int):

    oddList = random.sample(range(1,99), k=n+1)
    for i in range(0,n): oddList.append(oddList[i])
    random.shuffle(oddList)

    return oddList


def findSingle(L, start=0):
    if start==len(L): return start

    for i in range(0,len(L)):
        if (start!=i) and (L[start]==L[i]): return findSingle(L, start+1)

    return start


                
    



L = [46, 25, 46, 25, 17, 87, 87, 17, 31]

print(findSingle(L))

