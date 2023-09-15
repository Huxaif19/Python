my_list = [1,2,3,-4]
def lists(list):
    product = 1
    for i in list:
        product = product * i
    return product
print(lists([2,3,4,-1]))