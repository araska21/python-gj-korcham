a = int(input("정수: "))
b = int(input("정수: "))
print("덧셈:", a+b, "곱셈:", a*b)

a = int(input("정수: "))
b = int(input("정수: "))
print("몫:", a//b, "나머지:", a%b)

a = int(input("성적1: "))
b = int(input("성적2: "))
c = int(input("성적3: "))
sum = a+b+c
print("총점:", sum, "평균:", sum/3)

s = int(input("초 단위의 시간: "))
h = s//3600
s = s%3600
m = s//60
s = s%60
print(h, "시간", m, "분", s, "초")