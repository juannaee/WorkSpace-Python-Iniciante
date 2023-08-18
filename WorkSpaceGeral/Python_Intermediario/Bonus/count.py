from itertools import count

c1 = count()
r1 = range(0, 5)


print("count")
for i in c1:
    if i == 5:
        break
    print(i)

print("--------------------------------")
print("range")
for i in r1:
    print(i)
