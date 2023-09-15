# def myfunc (a,b):
#     return sum((a,b)) * 0.05
# print(myfunc(40,60))
# def my(*args):
#     for item in args :
#         print (item)
#     print(args) # it prints a tuple 
# my(90,90,30)
# def dict(**kwargs):
#     if 'fruits' in kwargs:
#         print('my favourite fruit is {}'.format(kwargs['fruits']))
#     else :
#         print('no fruits in the dict')
#     print(kwargs) # it prints a dictionary
# dict(fruits = 'apple', veggie = 'lettuce')
# def this(*args , **kwargs):
#     print('i would like {} {}'.format(args[0],kwargs['food']))
# this(10,203,40, fruits= 'mango', animal = 'cat', food = 'liver')
def myfunc(word):
    string = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            string += letter.upper()
        else:
            string += letter.lower()
        index +=1
    return string
print(myfunc('anthropology'))