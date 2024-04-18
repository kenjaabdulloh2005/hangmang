n = [5, 1, 23, 25, 125]
d = 0
for a in n:
    son = a
    while a % 5 == 0 and a > 0:
        a = a // 5
    if a == 1 :
        d = d + 1
        print(f"{son}True")
    else:
        print(f"{son}False")
print(d)
