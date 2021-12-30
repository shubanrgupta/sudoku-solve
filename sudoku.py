from array import *

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
        print("falserow", rowno)
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
        print("falsecol", colno)
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

#check if current iteration is valid, prints 0, 1, 2 or 3 based on type of mistake
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



#inputs the puzzle: use 0 for empty boxes
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
    if checkarow(puzzle):
        while index != emptynum:
            print("index", index)
            puzzle[emptyrow[index]][emptycol[index]]+=1
            print(puzzle[emptyrow[index]][emptycol[index]], "indval")
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
    else:
        print("invalid puzzle")
		
#calling final functions		
emptynum=len(emptycol)
print(emptycol)
checkarow(arr)
solve(arr)

