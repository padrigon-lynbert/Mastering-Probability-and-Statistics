# from icecream import ic # arepl: collision, not recognized

A = {1,2,3,8}
B = {4, 5}

# check membership
# print(1 in A)

# flag = 4 in A; print(type(flag)); print(flag)

# print(B.issubset(A))

def f_issubset(set1, set2):
    for element in set1:
        if element in set2: return True
        else: return False

print(f_issubset(B, A))
print(f_issubset({2,3,4}, {1,2,3,4,5,6}))

# chal_1: write a function that takes a set and show all its subsets

def out(set1, set2):
    ret = (set1, set2)
    return ret

print(out({1,2,3,4}, {5,6,7,3,2}))

# chal_2: write a function that takes a set and return a power set

def out2(set1, set2):
    ret = (set1 | set2) #UNION OPERATOR shortcut for "result=set1.union(set2)"
    return ret

print(out2({1,2,3,4}, {5,6,7,3,2}))

