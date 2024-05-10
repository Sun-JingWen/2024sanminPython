#亂數產生5-100之間可以被5整除的數，列出5個且不重複，請用五個變數去儲存。
import random

a = random.randint(5, 101)
while a % 5 != 0:
    a = random.randint(5, 101)

b = random.randint(5, 101)
while b == a or b % 5 != 0:
    b = random.randint(5, 101)

c = random.randint(5, 101)
while c == a or c == b or c % 5 != 0:
    c = random.randint(5, 101)

d = random.randint(5, 101)
while d == a or d == b or d == c or d % 5 != 0:
    d = random.randint(5, 101)

e = random.randint(5, 101)
while e == a or e == b or e == c or e == d or e % 5 != 0:
    e = random.randint(5, 101)
    
print(a, b, c, d, e)
