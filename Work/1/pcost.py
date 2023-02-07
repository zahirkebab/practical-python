# pcost.py
#
# Exercise 1.27

def cost(filename):
 with open(filename, 'rt') as f:
    x=0
    for line in f:
        try:
          linia = line.split(',')
          x+=float(linia[1])*float(linia[2])
          #print(f'{linia[1]} {linia[2]}')
        except ValueError:
          print('Couldnt parse')
    print(x)


cost('../Data/portfolio.csv')