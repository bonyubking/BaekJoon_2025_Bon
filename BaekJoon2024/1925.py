X_1, Y_1 = map(int,input().split())
X_2, Y_2 = map(int,input().split())
X_3, Y_3 = map(int,input().split())

## 한 점을 0,0 으로 Convert해서 계산해보자

x_0 , y_0 = 0, 0
x_1 , y_1 = (X_2- X_1), (Y_2-Y_1)
x_2 , y_2 = (X_3- X_1), (Y_3-Y_1)

Line1 = (x_1)**2 + (y_1)**2
Line2 = (x_2)**2 + (y_2)**2
Line3 = (x_1-x_2)**2 + (y_1-y_2)**2
triangleList = [Line1, Line2, Line3]
triangleList.sort()
sortLine1, sortLine2, sortLine3 = triangleList[0:3]


if  (x_1 * y_2) == (y_1 * x_2):
    print('X')
    
elif Line1 == Line2 == Line3:
    print("JungTriangle")
    
elif sortLine1 == sortLine2:
    if sortLine3 > (sortLine1)*2:
        print("Dunkak2Triangle")
    elif sortLine3 == (sortLine1)*2:           
        print("Jikkak2Triangle")
    else:
        print("Yeahkak2Triangle")

elif sortLine2 == sortLine3:
    print("Yeahkak2Triangle")

elif sortLine1 != sortLine2 != sortLine3:
    if sortLine1 + sortLine2 == sortLine3:
        print('JikkakTriangle')
    elif sortLine1 + sortLine2 > sortLine3:
        print('YeahkakTriangle')
    else:
        print('DunkakTriangle')