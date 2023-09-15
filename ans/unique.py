def unique_list(lst):
    return list(set(lst))   ## set(lst) prints the unique elements in a list
print(unique_list([1,2,1,2,4,5]))
def unique2(lst):
    c = []
    for number in lst :
        if number not in c:
            c.append(number)
    return c
print(unique2([1,2,3,1,2]))