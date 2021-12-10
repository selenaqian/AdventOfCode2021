count = 0
f = open("input.txt", "r")
a = int(f.readline())
b = int(f.readline())
c = int(f.readline())
for x in f:
    d = int(x)
    if b+c+d > a+b+c:
        count+=1
    a = b
    b = c
    c = d
    
print(count)
