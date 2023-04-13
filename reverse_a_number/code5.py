# using reverse method
number = 245
s = list(str(number))
s.reverse()

# with join
print(''.join(s))

# with for : one liner
[print(i, end="") for i in s]
