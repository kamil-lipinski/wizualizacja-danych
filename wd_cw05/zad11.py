def fibonacci():
    a=0
    b=1
    while a > -1:
        b=b+a
        a=b-a
        yield b-a

ciag=fibonacci()
for i in range(0, 100, 1):
    print('ciag('+str(i)+') =', next(ciag))