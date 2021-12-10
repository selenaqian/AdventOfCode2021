count = 0
f = open("input.txt", "r")
a = f.readline()
for x in f:
    b = x
    if int(b) > int(a):
        count+=1
    print("%d, %d, %d" % (int(a), int(b), count))
    a = b
    
print(count)
