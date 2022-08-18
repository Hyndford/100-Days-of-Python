# String
print("Hello"[0])

# Integer
print(123 + 456)
print(123_456_789)

# Float
print(3.14159)

# Boolean
a = True
b = False

num_char = len(input("What is your name? "))
print(type(num_char))

new_num_char = str(num_char)
print(type(new_num_char))

a = 123
print(type(a))

b = str(a)
c = float(a)
d = int(c)

print(2 ** 3)
print(6 / 3)    # Float

print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))

print(8 // 3)   # Int

result = 4 / 2
result /= 2

print("The result is " + str(result))
print(f"The result is {result}")
