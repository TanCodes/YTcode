number = 6969

reverse = 0

while number > 0:
    last = number % 10  # 4
    reverse = (reverse * 10) + last  # 0 + 4 -> 4
    number = number // 10  # 1234 // 10 -> 123

print(reverse)

# simpler version
number = 123

reverse = 0

while number > 0:
    reverse = (reverse * 10) + number % 10 
    number //= 10  

print(reverse)
