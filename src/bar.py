a = [11, 22, 33, 44]

print(a)
print(a[2])
print(a[1:3]) # slice
print(a[1:]) # slice
print(a[:2]) # slice
print(a[:]) # make a copy

print()

for elem in a:
    print(elem) # loop

print()

for i, elem in enumerate(a):
    print(i, elem)
    print(f"Index {i} holds the value {elem}")

for i in range(len(a)):
    elem = a[i]
    print(f"indeeeeex {i} holds the value {elem}")