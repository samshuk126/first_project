import random
print("welcome to password generaton")
Chars ='92kwjshsjekkdndkdkdkeldk'
Number = input("amount of password to generate")
Number = int(Number)
Length = input("input your password length: ")
Length = int(Length)

print("\nhere are your password: ")

for x in range(Number):
    password=''
    for y in range(Length):
        password+=random.choice(Chars)
    print(password)


