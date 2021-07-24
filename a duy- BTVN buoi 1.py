#Bai 1:Tính và in ra tích của 10 số tự nhiên đầu tiên . [0 →10].
tong=(10+0)*11/2
print(tong)

#Bai 2:Nhập vào số nguyên dương  n từ bàn phím. Tính và in ra n! (giai thừa). 
n = int(input("Nhập số cần tính giai thừa: "))
 
def giaithua(n):
    a=1
    if n==0 or n==1:
        return a
    else:
        for i in range (2, n+1):
            a=a*i
        return a
giaithua(n)
print(giaithua(n))

#Bài 3: Nhập vào số nguyên dương n từ bàn phím. Kiểm tra xem số n có phải là số nguyên tố hay không. Nếu là số nguyên tố thì in ra dòng text : “Đây là số nguyên tố”. Nếu không thì in ra: “Không phải là số nguyên tố”. 
import math
a=int(input("Nhập một số:"))
def songuyento(a):
    for i in range (2, int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
print(songuyento(a))
n=int(input("Hãy nhập một số tự nhiên bất kì:"))

#Bài 4:Nhập vào từ bàn phím số nguyên n. In ra tổng của các số thỏa mã hai điều kiện: - nhỏ hơn n và là số chẵn.
def ans(n):
    b=0
    for i in range (0,n,+2):
        b=b+i
    return b
print(ans(n))
    
#Bài 5: nhập vào số nguyên từ bàn phím. In ra tích của 2 nhân với các giá trị nhỏ n. 
n=int(input("Hãy nhập một số nguyên n:"))    
i=1
for i in range(1, n+1):        
    print("2*",i,"=",2*i)
     
#Bài 6: In ra các số trong khoảng từ 10 → 50 thỏa mã điều kiện chia hết cho 2 , vừa chia hết cho 3. 
for n in range ( 10, 51):
    if n%6==0:
        print(n)
        
#Bài 7: Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình
a=str(input("Nhập 1 chuỗi bất kì:"))
print(a.upper())

#Bài 8: Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp rồi in chúng.
a=input("Nhập một chuỗi")
b=getattr(a, 'split')()
def cau_moi(b):
    chuỗi=''
    for từ in b:
        if từ not in chuỗi:   
           chuỗi = chuỗi + " "+  từ
    return chuỗi
print(cau_moi(b))
        
#Bài 9:  Đề bài: Yêu cầu người dùng cung cấp một chuỗi và cho biết đó có phải một palindrome không .Chú ý: palindrome là một chuỗi có thể được viết xuôi hay viết ngược vẫn chỉ cho ra chính nó).

a=str(input("Nhập một cụm từ:" ))
if a[:len(a)//2] == a[:-len(a)//2]:
    print("Đây là một palindrome")
else:
    print("Đây không là một palindrome")

#Bài 10: Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.
import re
a=input()
result=re.findall("\d+",a)
print(result)

#Bài 11:
def Roman(a):
    gia_tri={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":500}
    ans=0
    for i in range (len(a)):
        if i==0:
            ans=ans+value[a[i]]
        else:
            if value[a[i]] > value[a[i-1]]:
                ans=ans+value[a[i]]-2*[a[i-1]]
            else:
                ans=ans+value[a[i]]
    return ans

#Bài 13:
def restoreString(s: str, indices: list) -> str:
    output = [''] * len(s) 
    index = 0
    for n in indices:
        output[n]=s[index]
        index+=1
    output = ''.join(output)
    return output
