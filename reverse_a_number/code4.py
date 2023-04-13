# using reversed function
number = 123

digits = list(str(number))
rev = reversed(digits)
# with join
print(''.join(rev))

# with for : one liner
[print(i, end="") for i in rev]
