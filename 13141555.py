# %%
a = int(input("정수: "))
b = int(input("정수: "))
if a＞b:  
    print("큰 수:", a)
else:  
    print("큰 수:", b)

# %%
a = int(input("정수: "))
if a＜0:    
print(a, ": 음수")
elif a＞0:     
print(a, ": 양수")
else:     
print(a, ": 0")

# %%
a = int(input("정수: "))
b = int(input("정수: "))
c = int(input("정수: "))
if a＞b:     
 if a＞c:        
  print("가장 큰 수 :", a)            
 else:
 print("가장 큰 수 :", c)
else: 
 if b＞c:
 print("가장 큰 수 :", b)
 else:
 print("가장 큰 수 :", c)

# %%
m = int(input("정수: "))
a = int(input("정수: "))
if a＞m:     
    m = a
a = int(input("정수: "))
if a＞m:    
  m = a
print("가장 큰 수:", m)

# %%
a = int(input("정수: "))
if a%2 == 0:    
 print(a, ": 짝수")
else:     
 print(a, ": 홀수")

# %%
a = int(input("정수: "))
if a%3 == 0:     
 print(a, ": 3의 배수")
else:     
 print(a, ": 3의 배수 아님")

# %%
charge = 5000
age = int(input("나이: "))
if age＜8:     
 print("입장료: 0")
elif age＜60:     
 print("입장료:", charge)
else:     
 print("입장료:", charge*0.5)

# %%
a = int(input("정수: "))
if a%3==0 and a%5==0:     
 print(a, ": 3과 5의 배수")
else:     
 print(a, ": 3과 5의 배수 아님")

# %%
age = int(input("나이: "))
if age＜8 or age＞=60:     
 print("입장료: 무료")
else:     
 print("입장료: 5000원")

# %%



