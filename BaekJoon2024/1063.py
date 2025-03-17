


King , Stone, N = input().split()

N = int(str(N))

King = list(King)
Stone = list(Stone)

def move(Key, Word):
    if 'R' in Key:
        Word[0] = chr(ord(Word[0])+1)
    if 'L' in Key:
        Word[0] = chr(ord(Word[0])-1)
    if 'B' in Key:
        Word[1] = str(int(Word[1])-1)
    if 'T' in Key:
        Word[1] = str(int(Word[1])+1)
        
def remove(Key, Word):
    if 'R' in Key:
        Word[0] = chr(ord(Word[0])-1)
    if 'L' in Key:
        Word[0] = chr(ord(Word[0])+1)
    if 'B' in Key:
        Word[1] = str(int(Word[1])+1)
    if 'T' in Key:
        Word[1] = str(int(Word[1])-1)    
    

for i in range(N):
    Key = input() 
    move(Key, King)
    if chr(ord(King[0])) < 'A' or chr(ord(King[0])) > 'H' or int(str(King[1])) < 1 or int(str(King[1])) > 8: 
        remove(Key, King)   
    
    if King == Stone:
        move(Key, Stone)
        if chr(ord(Stone[0])) < 'A' or chr(ord(Stone[0])) > 'H' or int(str(Stone[1])) < 1 or int(str(Stone[1])) > 8 :
            remove(Key, King)
            remove(Key, Stone)
    
 

    
        
     
print("".join(King))
print("".join(Stone))   
    
