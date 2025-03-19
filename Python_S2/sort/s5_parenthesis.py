"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

The Art Of Recursion
"""
from random import seed, randint

# in this one we will create a well parenthesised expression, recursively and then we'll test it

# inductive definition of a well parenthesised expression :
# '' is well parenthesised, so is ()
# if e1 and e2 are well parenthesised, e1e2 is too, and (e1) is too

seed(0)

def generate(depth, width):
    # depth is the maximum depth we will allow
    # width is the maximum number of leaves

    if depth == 0:
        return '()'*width

    else:
        children = []
        while sum(children) < width:
            children.append(randint(1, width-sum(children)))

        rep = ''
        for w in children:
            rep += generate(randint(0, depth-1), w)

        return '('+rep+')'


for i in range(5, 10):
    for j in range(5, 10):
        print(i, j, generate(i, j), sep='\t')


print()

# a well parenthesised expression as said in the quiz has the same number of ( and ) in total, and at any time the number of ( must be larger or equal the number of )

def test(expression): # this is not recursive
    
    counter = 0
    for p in expression:
        if p == '(':
            counter += 1

        elif p == ')':
            counter -= 1

    if counter < 0: # too many closing
        return False

    if counter > 0: # not enough closing
        return False

    return True


def test_rec(expression):
    #simple case: '' or '()'
    if expression == '' or expression == '()':
        return True

    # more compelex case: we can remove the easy matching pairs ()
    if '()' in expression: 
        return test_rec(expression.replace('()', ''))
    return False


for i in range(5, 10):
    for j in range(5, 10):
        exp = generate(i, j)
        print(i, j, exp, test(exp), test_rec(exp), sep='\t')


print()
for i in range(5, 10):
    for j in range(5, 10):
        exp = generate(i, j)
        # remove 4 parenthesis at random
        for _ in range(4):
            r = randint(0, len(exp)-1)
            exp = exp[0:r-1] + exp[r+1:]
        print(i, j, exp, test(exp), test_rec(exp), sep='\t')
