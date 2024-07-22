import random

def san_sinh_mang(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100,10)
        mang.append(so_ngau_nhien)
    
    return mang

def tim_tuyen_tinh(mang,x):
    n = len(mang)
    for i in range(n):
        if(mang[i]==x):
            return i
        
    return -1

def main():
    mang = san_sinh_mang(20)
    print(mang)
    vitri = -1
    while(vitri == -1):
        x = int(input("Nhap vao gia tri x can tim: "))
        vitri = tim_tuyen_tinh(mang,x)
        if vitri != -1:
            print("Gia tri {} duoc tim thay tai vi tri {}".format(x,vitri+1))
        else: print("Khong tim thay gia tri {} can tim".format(x))
    
if __name__ == "__main__":
    main()
