def inside(elm,lst):
    if lst ==[]:
        return False
    else:
        if elm == lst[0]:
            return True
        else:
            return inside(elm,lst[1:])

def shared(l1,l2):
    if l1 == [] or l2 == []:
        return []
    value = inside(l1[0],l2)
    if value:
        inter = [l1[0]]
    else:
        inter = []

    inter += shared(l1[1:],l2)

    return inter 


def shared_improved(l1,l2): # list ordered
    if l1 == [] or l2 == []:
        return []
    if l1[0] == l2[0]:
        inter = l1[0]
        l1 = l1[1:]
        l2 = l2[1:]
        return inter + shared_improved(l1,l2)
        
    if l1[0] < l2[0]:
        return shared_improved(l1[1:],l2)
    else:
        return shared_improved(l1,l2[1:])
    


