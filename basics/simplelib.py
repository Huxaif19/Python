# # from random import shuffle
# # from random import randint
# # mylist = [1,2,4,5,6,7,8,9,19]
# # shuffle(mylist)
# # print(mylist)
# # print(randint(0,20000))
# # i = int (input ('enter the number'))
# # print (i)
# # print (type (i))
# # # list comprehension
# # mystring = 'hello' 
# # my8= []
# # # for letter in mystring: 
# # #     my8.append(letter)
# # # print(my8)
# # # this can be done in another way in python
# # my8=[letter for letter in mystring]
# # print(my8)
# mylist = [num ** 2 for num in range(0,10)]
# print(mylist)
# mylist = [x for x in range(0,11) if x%2 ==0]
# print(mylist)
# celcius = [0,14,-40,40,58]
# farhenheit = [((9/5)*temp+32) for temp in celcius]
# print(farhenheit)
# results = [s if s % 2 == 0 else 'odd' for s in range(0,10)]
# print(results)
# mylist = [x*y for x in [2,5,6] for y in [100,200,300]]
# # for x in [2,5,6]:
# #     for y in [100,200,300]:
# #         mylist.append(x*y)
# print (mylist)
list = ['c++', 'java', 'python']
if 'java' in list:
    print(True)
else : 
    print(False)