"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

recursion 2
"""
from random import randint, seed, choice
from time import time


# how to split a list into two list of roughly equal sizes without knowing the actual size

# in python we can give default values to functions' arguments, so that if they are not passed by you, they use the default value
# ex :

def function_with_default(a=0, b='b', c=[]):
    print('a:', a, 'b:', b, 'c:', c, sep='\t')

# a call without arguments at all
function_with_default()
print()

# if you name the parameters/arguments you can give them in any order you like
function_with_default(b='abcd')
function_with_default(c=sum)
function_with_default(c={'d':123}, b=123)
function_with_default(c=123, a=[1,5,9,7,3])
print()

# if you do not name some parameters they are taken in order as in the definition of the function
function_with_default(123)
function_with_default(123, 456)
function_with_default(123, 456, 789)
print()

# just be aware that you should not given several value to a parameter and that once you name a parameter, you should name all the ones to its right in the call
try:
    function_with_default(123, a=589) # this does not work, cause a has a first unamed value and then another value
except Exception as ex:
    print(ex)

# this will not even run
#function_with_default(a=589, 258) 


print()
print('1.')
# the splitting ways

lst = [i for i in range(50)] # our basic list to be divided

def split(l, left=[], right=[]): # if we do not give actual values to left and right, they will default to empty lists

    if len(l) == 0:
        return left, right

    elif len(l) == 1:
        return left + l, right

    else: # we know len(l) >= 2
        return split(l[2:], left+[l[0]], right+[l[1]]) # i put l[0] and l[1] into lists of their own cause + is a concatenation operator for lists, left + l[0] would not work in general


    
left, right = split(lst)
print(left)
print(right)
print(len(lst), len(left), len(right), len(left)-len(right) in [-1, 0, 1], list(sorted(lst)) == list(sorted(left+right)), sep='\t') # we check that the recombined list has the same elements and that their length are almost equal

print()
# what if we do actually give values to left and/or right
left, right = split(lst, left=[-10, -12, -15])
print(left)
print(right)
print(len(lst), len(left), len(right), len(left)-len(right) in [-1, 0, 1], list(sorted(lst)) == list(sorted(left+right)), sep='\t')


print()
print('2.')

lst = [i for i in range(50)] # our basic list to be divided

def split_rotate(l, left=[], right=[]): # if we do not give actual values to left and right, they will default to empty lists

    if len(l) == 0:
        return left, right

    else: # there is at least one element in l
        return split_rotate(l[1:], right, left + [l[0]])


    
left, right = split_rotate(lst)
print(left)
print(right)
print(len(lst), len(left), len(right), len(left)-len(right) in [-1, 0, 1], list(sorted(lst)) == list(sorted(left+right)), sep='\t') # we check that the recombined list has the same elements and that their length are almost equal



print()
print('3.')

lst = [i for i in range(50)] # our basic list to be divided

def split_parity(l, left=[], right=[], parity=0): # if we do not give actual values to left and right, they will default to empty lists

    if len(l) == 0:
        return left, right

    else: # there is at least one element in l
        if parity == 0: # let's put the element on left, next parity will be 1
            return split_parity(l[1:], left + [l[0]], right, 1)
        else: # let's put the element on right, next parity will be 0
            return split_parity(l[1:], left, right + [l[0]], 0)


    
left, right = split_parity(lst)
print(left)
print(right)
print(len(lst), len(left), len(right), len(left)-len(right) in [-1, 0, 1], list(sorted(lst)) == list(sorted(left+right)), sep='\t') # we check that the recombined list has the same elements and that their length are almost equal


print()
print('3.5.')

lst = [i for i in range(50)] # our basic list to be divided

def split_parity_alt(l, leftright=[[],[]], parity=0):
    # I put left and right into a new list so that i can index them instead of calling them by name
    
    if len(l) == 0:
        return leftright[0], leftright[1]

    else: # there is at least one element in l
        leftright[parity] += [l[0]]
        return split_parity_alt(l[1:], leftright, 1-parity) # 1-0 = 1 and 1-1 = 0, the beauty of binary arithmetic

    # this code is a bit better than the previous one, even though it does the same, because there are less comparisons
    

    
left, right = split_parity_alt(lst)
print(left)
print(right)
print(len(lst), len(left), len(right), len(left)-len(right) in [-1, 0, 1], list(sorted(lst)) == list(sorted(left+right)), sep='\t') # we check that the recombined list has the same elements and that their length are almost equal



print()
print('4.', 'timing')
# let's time all that
times = {f:[] for f in [split, split_rotate, split_parity, split_parity_alt]}
for _ in range(10000):
    for f in [split, split_rotate, split_parity, split_parity_alt]:
        t = time()
        left, right = f(lst)
        t = time() - t

        times[f].append(t)

for f in [split, split_rotate, split_parity, split_parity_alt]:
    ts = times[f]
    print(f, 'time for 10 000 runs:', sum(ts), 'min:', min(ts), 'max', max(ts), sep='\t')
# try to understand why some are faster than others and so on
        



print()
print('5.')
# by using the lists inside a list technique of split_parity_alt, implement the splitn, splitn_rotate and splitn_parity that divide a list into n lists of more or less equal size


def splitn(l):
    pass

def splitn_rotate(l):
    pass

def splitn_parity(l):
    pass


for fun in [splitn, splitn_rotate, splitn_parity]:
    subs = fun(lst)
    combined = []
    try:
        for sb in subs:
            print(len(sb), sb)
            combined += sb

        print(len(lst), len(combined), list(sorted(lst)) == list(sorted(combined)), sep='\t')
    except Exception as ex:
        print(fun, 'did not run as expected.')
        
