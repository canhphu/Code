import numpy
import random
def san_sinh_mang(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100,10)
        mang.append(so_ngau_nhien)
    return mang
array = [19,19,29,94,29]
array.append(99)
print(array)
pp = array.pop()
print(pp)

arr  = san_sinh_mang(20)
arr = list(arr)
print(arr)
m = arr.pop()
while(arr!=[]):
    b = arr.pop()
    if(b>m):
        m=b
print("Largest num in the array is:",m)