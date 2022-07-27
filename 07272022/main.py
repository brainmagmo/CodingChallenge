from animals import animals

a = int(input('Enter chickens: '))
b = int(input('Enter cows: '))
c = int(input('Enter pigs: '))

print(f'Total legs for {a} chickens, {c} pigs, and {b} cows is {animals(a, b, c)}')
