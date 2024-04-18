def qoshish(x, y):
    return x + y

def ayrish(x, y):
    return x - y

def kopaytirish(x, y):
    return x * y

def bolish(x, y):
    if y == 0:
        return "Nolga bo'lish mumkin emas"
    else:
        return x / y
print("1. Qo'shish")
print("2. Ayrish")
print("3. Ko'paytirish")
print("4. Bo'lish")
amal = input("Amalni tanlang (1/2/3/4): ")
num1 = int(input("1-sonni kiriting: "))
num2 = int(input("2- sonni kiriting: "))
if amal == '1':
    print("Natija:", qoshish(num1, num2))
elif amal == '2':
    print("Natija:", ayrish(num1, num2))
elif amal == '3':
    print("Natija:", kopaytirish(num1, num2))
elif amal == '4':
    print("Natija:", bolish(num1, num2))
else:
    print("Noto'g'ri amal tanlandi")
