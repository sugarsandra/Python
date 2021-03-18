import random as rn

while True:
    num=rn.randint(0,36)
    print('\nΚληρώθηκε το', num)

    if num!=0:
        is_small = (num<=18)
        is_even = (num%2==0)

    if num<=10 or 19<=num<=28:
        is_red = False if is_even else True
    else:
        is_red = True if is_even else False
     
    print('Μικρός' if is_small else 'Μεγάλος', end=' ')        
    print('Ζυγός' if is_even else 'Μονός', end=' ')
    print('Κόκκινος' if is_red else 'Μαύρος')
  #################
    if input('Enter: Συνέχεια, q: Έξοδος ')=='q':
        break
