import random

with open("/home/stanislav/Gen_info.txt") as file:
    a = file.read()
    b = a.split("\n")
    file.close()

with open("/home/stanislav/Gen_info1.txt") as file1:
    aa = file1.read()
    bb = aa.split("\n")

listic = []

print "len b is " + str(len(b))
print "len bb is " + str(len(bb))

for thing in bb:
    listic.append(thing)

index = 0
for item in range(0,len(bb)):
    index += 1
    listic.append(b[index])


print "len listic is " + str(len(listic))


rnd = random.sample(listic,len(listic))


def split_list(lst):

    one_third = len(lst)/5
    return lst[:one_third*3], lst[one_third*3:one_third*4], lst[one_third*4:]


A, B, C = split_list(rnd)


print len(A)*100.0/len(listic),len(B)*100.0/len(listic),len(C)*100.0/len(listic)

with open("/home/stanislav/file1.txt","wb") as file:
    for item in A:
        file.write("%s\n" % item)

with open("/home/stanislav/file2.txt","wb") as file1:
    for item in B:
        file1.write("%s\n" % item)

with open("/home/stanislav/file3.txt","wb") as file2:
    for item in C:
        file2.write("%s\n" % item)



