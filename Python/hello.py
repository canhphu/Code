

def f(x):
    y=abs(x)
    return y

print(f(5))
spam_amount=0
print(spam_amount)

spam_amount=spam_amount+4
if(spam_amount>0):
    print("I don't want any spam")
print("What is your name","Phu",sep='\n')

primes = [2,5,7,9]
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
print(primes[-1])

planets[:3] = ['A','B','C']
planets[4:] = ['D','E','F','G']
print(planets)

print(len(planets))
print(sorted(planets))
randomlist = [1,4,7,8,5,1,2,3,5,7,8,3,1,2,4,5,6,7,8,1,2,4,8,0,0,0]
#print(sorted(randomlist))
a = sorted(randomlist)
print(a)
b = sum(randomlist)
print(b)
c=max(randomlist)
print(c)
d = min(randomlist)
print(d)

inter = 15
print(inter.imag)
imagnum = 12 + 3j
print(imagnum.imag) #tra ve gia tri phan ao cua so phuc

print(inter.bit_length()) #tra ve do dai bit cua bien 

#list.append: them mot phan tu vao cuoi
print(planets)
planets.append('Pluto')
print(planets)

#list.pop: xoa phan tu cuoi cung o mang va tra ve phan tu bi xoa
print(planets.pop())
print(planets)

#list.index: kiem tra xem phan tu co o trong mang hay khong
m =planets.index('Mars')
print(m)
#planets.index('Earth') =>  error do khong tim duoc phan tu trong mang

#in: toan tu tra ve gia tri boolean
n = "Earth" in planets 
o ="Mars" in planets
print(n,o,sep='\n')

#Tuples
t =(1,2,3)
print(t)
x = 0.23
x1,x2 = x.as_integer_ratio() # tra ve tu va mau cua so thap phan. vd: 0.25 = 1 va 4
print(x1,x2)

alphabets = ['A', 'B', 'C', 'D']
for i in alphabets: # tu phan tu i trong alphabets (i=0,1,2,3,...)
    print(i,end=' ')

a = (2,3,4,5,6,7)
sums = 0
for i in a:
    sums = sums + i
print(sums)
print('\n')
char = 'Hi, my name is ELLy. i am 12 years Old'
for i in char:
    if(i.isupper()): #check xem phai viet hoa k
        print(i,end='')
print('\n')
for i in range(10): #range: tu dich ra tieng viet di thang luoi
    print('I love you',sep='\n')
    
i=0
sums = 0
while(i<10):
    sums = sums + i
    i+=1
print(sums)

squares = [n**2 for n in range(10)]
print(squares)

even = [n*2 for n in range(51)]
print(even)

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

odd = [i for i in range(100) if i % 2 != 0]
print(odd)

lower_printed = ['a','b','c']
upper_printed = [i.upper() + '!' for i in lower_printed]
print(upper_printed)

def count_negatives(nums):
    return sum([num< 0 for num in nums])
def lucky_numbers(nums):
    return any([num%7==0 for num in nums])
a=[-2,-1,-3,0,1,2,3,4,5,7,14,21,56,9,-10,-11]
print(count_negatives(a))
print(lucky_numbers(a))
a= []
print(len(a))

string1 = 'Pluto is a planet'
string2 = 'Pluto is a planet'
print(string1 == string2)

print('\'Pluto\' is a planet')

plant = 'Rose'
print(plant[0])

plant_loop = [char+'!' for char in plant]
print(plant_loop)

#startswith: kiem tra tu dau tien cua xau
pluto = 'Pluto'
print(string1.startswith(plant))
print(string1.startswith(pluto))

#str.split: chia xau
words = string2.split()
print(words)

today = '2023-12-16'
year,month,day = today.split('-')
print(year,month,day)

#str.join: them ki tu vao xau. Luu y: trong join chi duoc them 1 bien, vi vay de them vao giua nhieu bien, 
# ta dung lists(hay con goi la mang)
today_again =  '/'.join([year,month,day])
print(today_again)


#str.format(): them phan tu vao xau
sentence = '{} is my {}th day at Hanoi University of Science and Technology.'.format(today, 365)
print(sentence)

song='{0}, {0} little star, How {1} wonder what {2} are'.format('Hello','I','we')
print(song)

number1 = 1.999999999999999
number2 = 2.9999999999
number3 = 3.000000000000
number_sentence = '{:.2},{:.3%},{:.4},why don\'t you go hiding ?'.format(number1,number2,number3)
print(number_sentence)

#Dictionaries in Python:
counting = {'one':1, 'two':2, 'three':3}
print(counting['one'])
counting['one thousand'] =1000
print(counting)
#Cu phap cho tu dien: nghia_cua_tu : gia_tri_can_dinh_nghia
names = ['Phu','Lam','Bao','Dat',"Anh",'Bach','Tuan']
names_first_letter = {name: name[0] for name in names}
print(names_first_letter)

check1 ='Lam' in names
check2 = 'Thai' in names
print(check1,check2)

#dict.values: tra ve gia tri can dinh nghia
ten =' '.join(sorted(names_first_letter.values()))
ki_hieu = ' '.join(sorted(names))
print(ten)
print(ki_hieu)


#dict.items: goi ca dinh nghia va gia tri can dinh nghia
for ten1, kihieu in names_first_letter.items():
    print('{} begins with {}'.format(ten1.rjust(len(names)),kihieu));

#str.isdigit(): kiem tra xem phan tu trong xau co phai so hay khong
i = '1234'
print(i.isdigit())

#str.rstrip(): Xoa ki tu o ben phai xau
a = 'This is Phu speaking.'
print(a.rstrip('.'))

#strip: xoa khoang trang
vidu = '  yes   '
print(vidu.strip())

#enumerate(str): gan giong len nhung no huu ich hon
a = [10,20,30,40]
print(len(a))
print(enumerate(a))

#thu vien trong python
import math as toan # cái as này khá giống với việc đặt tên biến thôi. Ez
from math import * # thì không cần phải math.pi nữa
"""from numpy import *: Đơn giản là bên numpy cũng có hàm log, việc chúng ta gọi hết thế này khiến nó
không hiểu mình phải dùng lệnh từ thư viện nào"""
"""Cách sửa: from math import pi,log
            from numpy import asarray
    """
print('It\'s math! It has type {}'.format(type(toan))) #ban chat cua thu vien la mot module
print(dir(toan))  #in ra cac bien co the su dung
print(toan.exp(2)) #cach su dung bien trong thu vien. Co ve nhu giong struct trong c ?
print(pi,log(32,2))

import numpy as np
#module.module
#Cũng không có gì lắm ngoài 2 cái module đè lên nhau
rolls = np.random.randint(low = 1, high = 6, size = 10) #tung xuc sac 10 lan 
print(rolls)

#Mot so dung cu co ich trong viec tim hieu module
#1. type(): Day la cai gi ?
print(type(rolls))

#2. dir(): Dung kieu gi ?
#print(dir(rolls))

#3. mean(): Tra ve gia tri trung binh 
print(rolls.mean())

#4. help(): Thoi tu dich ma hieu
#help(rolls.ravel)

#5. tolist(): Sao khong thay khac voi bo .tolist di nhi ? À tạo thành cái list còn không thì giống bọn tuples
print(rolls.tolist())

#Fact: Nếu sử dụng module numpy, chúng ta có thể cộng trực tiếp các toán tử vào giá trị của mảng
#print([10,20,30] + 4) #Đây là ví dụ của việc không thể cộng được toán tử vào mảng
print(rolls + 10) #Còn cái này thì có

#string.count("kitu"): dem so lan xuat hien cua ki tu trong xau
print("The number of times e occurs in this string is ".count("e"))

#endswith: kiem tra xem chuoi co ket thuc bang mot xau con khong
print("Forest".endswith("rest"))

#check palindrome
input_string = "abc"
new_string =""
reverse_string= ""
for letter in input_string:
    if(letter != " "):
        new_string = new_string[0:] + letter
        reverse_string = letter + reverse_string[0:]
        
new_string = new_string.lower()
reverse_string = reverse_string.lower()
print(new_string)
print(reverse_string)

#rfind: tim lan cuoi xuat hien cua substring
sentence = "It's raining cats and cats"
old = "cats"
print(sentence.index(old))
print(sentence.rfind(old))

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#them mot du lieu vao cuoi list
fruits.append("Kiwi")
print(fruits)
#them mot du lieu vao vi tri bat ki tren list
fruits.insert(0,"Orange")
#loi
"""print(fruits)
fruits.insert("Peach")
"""
print(fruits)
#xoa mot thanh phan trong list
fruits.remove("Kiwi")
print(fruits)
#xoa thanh phan o vi tri index
fruits.pop(3)
print(fruits)
#thay the noi dung cua vi tri index
fruits[2] = "Strawberry"
print(fruits)

