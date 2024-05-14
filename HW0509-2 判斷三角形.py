#使用者輸入3個邊，2-1 判斷是否為三角形 2-2再判斷是否為直角。
print("判斷三角形，請輸入整數")
a=int(input("請輸入第一邊:"))
b=int(input("請輸入第二邊:"))
c=int(input("請輸入第三邊:"))
print()
print("判斷為:")

if a + c > b and a + b > c and b + c > a:
    print("三角形")
    
    if a*a + b*b ==c*c or a*a + c*c ==b*b or c*c + b*b ==a*a : #直角三角形
        print("直角三角形")
        
    else:
        print("不是直角三角形") 
else:
    print("不是三角形") 
       
print("DONE")
