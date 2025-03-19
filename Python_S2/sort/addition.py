def addition(x,y):
    if x == 0:
        return y
    return addition(x-1,y+1)
print(addition(100,99))


def rec_sort(lst):
    l1 = lst[:len(lst)//2]
    l2 = lst[len(lst)//2:]
    
    
    


    