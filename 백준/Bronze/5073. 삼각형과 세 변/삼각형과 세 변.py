while True:
    A, B, C = map(int,input().split())
    
    if A+B+C == 0:
        break;
    
    if A == B == C:
        print('Equilateral')
    
    elif A+B <= C or B+C <= A or A+C <= B:
        print('Invalid')
        
    elif A != B and A!= C and B != C:
        print('Scalene')
        
    else:
        print('Isosceles')