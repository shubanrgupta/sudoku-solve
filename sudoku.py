from array import *

#making blank puzzle
m = 9
n = 9  
a = [[0 for x in range(n)] for x in range(m)]

#assigning no. to puzzle
a[0][2]=8
a[0][5]=5
a[0][6]=6
a[0][8]=2
a[1][1]=2
a[1][3]=7
a[1][6]=8
a[1][8]=5
a[2][0]=5
a[2][2]=1
a[2][4]=2
a[2][5]=8
a[2][6]=7
a[2][7]=3
a[3][5]=6
a[3][7]=2
a[3][8]=8
a[4][0]=8
a[4][2]=2
a[4][3]=1
a[4][4]=5
a[4][6]=9
a[5][3]=2
a[5][4]=8
a[5][5]=4
a[5][7]=7
a[6][1]=8
a[6][2]=4
a[6][7]=5
a[7][2]=3
a[7][3]=5
a[7][4]=4
a[7][7]=8
a[7][8]=7
a[8][0]=2
a[8][1]=5
a[8][2]=7
a[8][3]=8
a[8][6]=4
a[8][8]=9

#puzzle print function
def printing(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end = " ")
        print()

#check if specific row has repititions    
def check_row(rowno, puzzle):
    puzz2=[]
    for c in range(0,9):
        if puzzle[rowno][c]!= 0:
            puzz2.append(puzzle[rowno][c])
    if len(puzz2) == len(list(set(puzz2))):
        print("tru")
        return True 
    else:
        print("false")
        return False

#check if specific column has repititions 
def check_col(colno, puzzle):
    puzz2=[]
    for c in range(0,9):
        if puzzle[c][colno]!= 0:
            puzz2.append(puzzle[c][colno])
    if len(puzz2) == len(list(set(puzz2))):
        print("tru")
        return True 
    else:
        print("false")
        return False

#check if 3x3 matrix has repititions. Only works if row and column have no repititions
def check_box(puzzle):
    check=0
    for x in [0, 3, 6]:
        for y in [0,3, 6]:
            puzz2=[]
            for i in range(0,3):
                for j in range (0,3):
                    if puzzle[x+i][y+j]!=0:
                        puzz2.append(puzzle[x+i][y+j])
            if len(puzz2) != len(list(set(puzz2))):
                check=1
    '''for x in [2, 5, 8]:
        for y in [0,3,6]:
            puzz2=[]
            for i in range(0,3):
                if a[x-i][y+i]!=0:
                    puzz2.append(puzzle[x-i][y+i])
            if len(puzz2) != len(list(set(puzz2))):
                check=1'''
    if check==1:
        print("fal")
        return False
    else:
        print("tru")
        return True

#check if possible
def checkarow(puzzle):
    checkm=0
    for row in range(0,9):
        if not(check_row(row,puzzle)) :
            checkm=1
    for col in range(0,9):
        if not(check_col(col,puzzle)) :
            checkm=2
    if not (check_box(puzzle)):
        checkm=3
    print (checkm)
    if checkm==0:
        return True
    else:
        return False

#checks if all boxes are filled
def fulfill(puzzle):
    for row in range(0,9):
        for col in range(0,9):
            if puzzle[row][col]==0:
                return False
            else:
                return True

emptyrow=[]
emptycol=[]

#makes a list of empty row, column 
def emptylist(puzzle):
    for row in range(0,9):
        for col in range(0,9):
            if puzzle[row][col]==0:
                emptyrow.append(row)
                emptycol.append(col)

m = 9
n = 9  
arr= [[0 for x in range(n)] for x in range(m)]
for i in range(0,9):
    x=input("enter row " + str(i))
    for j in range(0,9):
        arr[i][j]=int(x[j])
printing(arr)

emptylist(arr)

def solve (puzzle):
    index=0
    while index != emptynum:
        puzzle[emptyrow[index]][emptycol[index]]+=1
        if puzzle[emptyrow[index]][emptycol[index]]==9:
            if checkarow(puzzle):
                index+=1
            else:
                puzzle[emptyrow[index]][emptycol[index]]=0
                index-=1
        elif puzzle[emptyrow[index]][emptycol[index]]>9:
            puzzle[emptyrow[index]][emptycol[index]]=0
            index-=1
        elif checkarow(puzzle):
            index+=1
        printing(puzzle)
    


#emptylist(arr)
#emptynum=len(emptycol)
emptynum=len(emptycol)
print(emptycol)
solve(arr)

