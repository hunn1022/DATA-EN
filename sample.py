import math 
n = 12.1212

print(f'소수: {n}')
print(f'버림: {math.trunc(n)}') 
print(f'버림: {math.floor(n)}')
print(f'올림: {math.ceil(n)}')

digit = 2
print( f'소숫점 3자리에서 올림: {math.ceil(n*10**digit)/10**digit}')
print( f'소숫점 3자리에서 반올림: {round(n,2)}')