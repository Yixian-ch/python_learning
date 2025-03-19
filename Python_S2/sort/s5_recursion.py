"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

The Art Of Recursion
"""
from random import randint, seed, choice
from math import log2

# at the heart of recursive functions lies the distinction between simple cases that are easy to solve and more complex cases that are easier to break down
# one should then thing in terms of simple cases and complex cases and find a way to build the solution for complex cases from solutions of simple ones

# let's start with the problems discussed during the lesson

# as usual, feel free to modify the code to understand what's going on
seed(0) # initialise the random generator for replicability

# 1. length of list
lst = [randint(-100, 100) for _ in range(randint(5, 15))] # create a random list with length between 5 and 15

def length(l):
    # simple case first
    if l == []:
        # l is the empty, so length is 0
        return 0

    # more complex case
    else:
        # l is not empty so it has at least one element
        return 1 + length(l[1:])

print('1.', lst, len(lst), length(lst), sep='\t')
print()

# 2. BE CAREFUL !!! if the recursion is not going toward simpler cases, the function will never stop !!!
# in fact, python keeps track of the number of recursions and will prevent you from going too far, but still

print('2.')
def badly_defined(x):
    if x == 0: # simple case
        print('!!! 0 !!!')
        return 0

    else:
        print(x)
        res = 1 + badly_defined(x+1) # x increases instead of going to 0
        return res

badly_defined(0) # works
badly_defined(-10) # works
#badly_defined(1) # breaks, comment this line to continue

try:
    badly_defined(1) # breaks
except:
    print('we caught the exception!!')

print()


#3. parity of number, multiple possibility
def parity_1(n):
    # simple cases : 0 and 1 
    if n == 0:
        return 'even / pair'
    if n == 1:
        return 'odd / impair'

    # complex case, n != 0 and n != 1 so n >= 2
    return parity_1(n-2)

def parity_2(n):
    # simple case : 0
    if n == 0:
        return 'even / pair'

    # complex case, n != 0, the parity of n is the opposite of the one of n-1
    if parity_2(n-1) == 'even / pair':
        return 'odd / impair'
    else:
        return 'even / pair'

print('3.')
for _ in range(10):
    r = randint(0, 1000)
    print(r, parity_1(r), parity_2(r), sep='\t')

print()    
    


# 4. modulo
print('4.')

def mod_1(x, b):
    # simple case : x < b
    if x < b:
        return x

    # complex case : x >= b
    return mod_1(x-b, b)


def mod_2(x, b): # more fun !
    # simple case : 0
    if x == 0:
        return 0

    # more complex cases : x != 0
    m = 1 + mod_2(x-1, b) # divid x into b, for example x=5, b=2, once m=2=b, it will be reset to 0

    # new simplest case : m == b, cause b mod b is 0
    if m == b: # how many b x can divided
        return 0
    else:
        return m


for _ in range(10):
    r = randint(0, 1000)
    b = randint(1, 50)
    print(r, b, r%b, mod_1(r, b), mod_2(r, b), sep='\t')

print()


# now your turn


# 5. representation in base b
def representation_1(n, b):
    # simple case : n < b
    if n < b:
        return 'abc'

    # complex case
    res = 'some recursive computation'
    return res


# for testing purpose another way of doing it
# with the computation of columns first
def representation_2(n, b, col=1):
    #print(n, b, col)
    # this version is bit more tricky
    # there are nested computations, cause we need to compute the column values to use them

    # more complex case : n >= col * b
    if n >= b * col:
        rep, rem = representation_2(n, b, b * col) # by design rem will be smaller than b*col
    else:
        rep = ''
        rem = n
        
    digit = rem // col # how many times col goes into rem
    rep += str(digit)
    rem = rem - digit * col

    if col != 1:
        # col != 1 so we still have more digits to append
        return rep + ':', rem
    return rep

print('5.')

for _ in range(10):
    r = randint(0, 1000)
    b = randint(2, 50)
    print(r, b, representation_1(r, b), representation_2(r, b), sep='\t')

print()


#6. comparison of number, you can only test if a number is equal to zero

print('6.')

def compare(x, y):
    # simple case : x = 0 or y = 0 or x = y = 0
    NotImplemented

    # more complex : x and y != 0
    # how do you set yourself in a simpler case
    NotImplemented

for _ in range(10):
    x = randint(0, 1000)
    y = randint(0, 1000)
    print(x, y, x < y, compare(x, y), sep='\t')

print()

    

# 7. addition, multiplication
print('7.')

def add(x, y):
    # simple case : adding 0 to anything is easy
    NotImplemented

    # more complex : x and y != 0
    NotImplemented


for _ in range(10):
    x = randint(0, 1000)
    y = randint(0, 1000)
    print(x, y, x + y, add(x, y), sep='\t')

print()


#8. sort
# remember how we did sort a list by finding its smallest element and then repeating on the list with the min removed ?


print('8.')

def minimum(l):
    # simple case : l has only one element
    NotImplemented

    # more complex : l has more than one element, you need to find a way to simplify this
    NotImplemented


def sorting(l):
    # simple case : if l has 0 or 1 element, it is already sorted
    NotImplemented

    # more complex : l has more than 1 element, find the smallest, remove it and sort the rest
    NotImplemented


for _ in range(10):
    lst = [randint(-100, 100) for _ in range(randint(5, 500))]
    slst = list(sorted(lst))
    print(sorting(lst) == slst, sep='\t')

print()
