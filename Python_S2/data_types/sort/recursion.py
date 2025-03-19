# why we need recursion?
# recursion represents a kind of thiking to resolve a complex problem by diving it into sub problems
# In addition, 1 + 1 = 2, its quiet easy or intuitive. But as numbers grows, the complexity increases 
# 2 + 2 = 4, 4 + 4 = 8, 8 + 8 = 16, 16 + 16 = 32, 32 + 32 = 64, 64 + 64 = 128, 128 + 128 = 256, 256 + 256 = 512, 512 + 512 = 1024, 1024 + 1024 = 2048, 2048 + 2048 = 5096, 5096 + 5096 = 
# so our addition is already an application of recursion, so we can build it
# 10+(9+(8+(7+(5+7))))
# criteria

# where is the problem
def addition(int1=str, int2=str) -> str: # kargs is key word argument, is a dict
    if len(int1) == 1 and len(int2) == 1:
        result = int(int1) + int(int2)
        # mod = result % 10
        # carry = result // 10
        return result # int

print(addition("59", "45"))
# print(addition("323","289"))

# if a function returns more than one argument, the return object will be a tuple

def signle_addition(int1=str, int2=str):
    result = int(int1) + int(int2)
    # mod = result % 10
    # carry = result // 10
    return str(result)

print(signle_addition("6","5"))

def duo_addition(int1, int2):
    # only yi wei addition
    # if condition should return two values, one is the mod, another is the carry
    if len(int1) == 1 and len(int2) == 1:
        return int(int1) + int(int2)
    
    calculate = int(int1[0]) + int(int2[0]) + (duo_addition(int1[1:]), (int2[1:]) // 10) # from 2~19
    # add if or use the calculate directly.. have a rest

