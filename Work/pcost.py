# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    x=0
    next(f)
    for line in f:
        linia = line.split(',')
        x+=float(linia[1])*float(linia[2])
        #print(f'{linia[1]} {linia[2]}')
        print(x)