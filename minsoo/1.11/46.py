f = open('C:/Users/wwnis/Desktop/46.txt', 'r')
A = []
B = []
while 1:
    line = f.readline()
    if not line: break
    line_col = line.split()
    for x in line_col:
        A.append(x)
A.sort()
A.append('')
i = 0
while i in range(len(A)):
    j = 1
    try:
        while A[i] == A[i+1]:
            j += 1
            A.pop(i+1)
    except: break                               # i == len(A) - 1 일때만 except에 걸린다. 주의, A[i] != A[i+1]과 A[i] == A[i+1]이 '오류'인 경우는 다르다. (즉, 마지막에만 except가 걸리기 때문에, ''를 마지막에 추가해줌.)
    B.append([j, A[i]])
    i += 1
def getKey(item):
    return[item[0]]
C = sorted(B, key = getKey)
C.reverse()
for i in range(len(C)):
    print(f'{C[i][1]+":":<15} {"*"*C[i][0]:<10}')