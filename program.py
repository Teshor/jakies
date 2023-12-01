number = int(input('Please type in a number:'))
a = 1
b = 1

while True:
    while b >= number:
        print(f'{a} x {b} = {a * b}')
        b += 1
