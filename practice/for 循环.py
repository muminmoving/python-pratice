# 4-3
for i in range(1, 21):
    print(i)

# 4-4
list1 = []
count = 0
for i in range(1, 1000001):
    list1.append(i)
    count += i
    continue
    print(i)
print(count)
print(min(list1))
print(max(list1))

# 4-6
list2 = []
for j in range(1, 21, 2):
    list2.append(j)
print(list2)

# 4-7
list3 = []
for n in range(3, 31, 3):
    list3.append(n)
print(list3)

# 4-8
list4 = []
for m in range(1, 11):
    b = m ** 3
    list4.append(b)
print(list4)