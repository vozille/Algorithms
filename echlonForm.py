import sys
sys.stdin = open('input.txt','r')

num = input()
matrix = []
for i in range(num):
    matrix.append(map(float,raw_input().split()))

def EchlonForm(matrix):
    depth = len(matrix)
    pivot = 0
    base = 0
    while pivot < len(matrix[0])-1 and base < depth:
        allZero = True
        swp = base
        for j in range(base,depth):
            if matrix[j][pivot] == 0:
                swp += 1
            else:
                allZero = False
                break
        if allZero == True:
            base += 1
            continue
        matrix[base],matrix[swp] = matrix[swp],matrix[base]
        for j in range(base+1,depth):
            x = -matrix[j][pivot]/matrix[base][pivot]
            for i in range(len(matrix[0])):
                matrix[j][i] = matrix[j][i] + x*matrix[base][i]
        pivot += 1
        base += 1
    return matrix

res = EchlonForm(matrix)
# x,y,z = 0.0,0.0,0.0
# z = res[2][3]/res[2][2]
# y = (res[1][3] - (res[1][2]*z))/res[1][1]
# x = (res[0][3] - (res[0][2]*z) - (res[0][1])*y)/res[0][0]

# print x,y,z

val = [res[-1][-1]/res[-1][-2]]

def getValues(matrix):
    n = len(matrix)
    for i in range(n-2,-1,-1):
        ctr = 0
        for j in matrix[i]:
            if j != 0:
                break
            ctr += 1
        subtract = 0
        coff = -1
        for j in range(ctr+1,len(matrix[i])-1):
            subtract += matrix[i][j]*val[coff]
            coff -= 1
        val.append((matrix[i][-1]-subtract)/matrix[i][ctr])

    print val[::-1]

getValues(res)
