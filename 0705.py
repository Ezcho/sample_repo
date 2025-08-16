
n = 10

for i in range(n): #i는 index i의 범위(scope)는, 0~9까지.. 증분
    print(i)

for j in range(1,11): #j의 scope 1~ 10까지.
    print(j)

for k in range(1,10,2): #k는 1부터 9까지 2씩 증분
    print(k)

s = "HelloWorld"
for i in range(len(s)): #len은, ~의 길이. 10  length(길이)
    print(s[i])

for v in s: #v는 index가 아니고, s의 개별 문자.
    print(v)

lst = [1,6,3,45,52,3,4,6,7]
for i in range(len(lst)): 
    print(lst[i])

for v in lst:
    print(v)

print(range(1,10))