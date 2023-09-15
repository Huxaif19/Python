# my_iterable = [1,2,3]
# for i in my_iterable:
#     print(i)
# print('\n \n')
# my_list = [1,2,3,4,5,6,7,8,9,10]
# for i in my_list: 
#     if (i%2 == 0):
#         print(i)
#     else : 
#        print(f'odd number: {i}')
# sum = 0
# for _ in my_list : 
#     sum += _
# print(sum)
# for _ in "hello":
#     print(_)


# theie = [(1,2),(3,4)]
# for item in theie:
#     print(item)
# for (a,b) in theie: 
#     print(a)
#     print(b)
# d =  {'kk' : 1, 'kkk' : 2, 'kkkk' : 3}
# for  value in d.values(): 
#     print(value)



# while loops in python
# i = 0
# while(i <10): 
#     print(f'the value of i is: {i}')
#     i+=1



# use case
# x = [1,2,3]
# for _ in  x : 
#     #comment
#     pass
# print('end of this loop')
# my_string = "hello world"
# for _ in my_string: 
#     if (_ == 'l'):
#       continue
#     print(_)
# for _ in range (20):
#     if _ == 5:
#         continue
#     print(_)
# for _ in range(10):
#     if _ == 5:
#         break
#     print(_)
# x = 0
# while(x <5):
#     if x ==2:
#         break
#     print(x)
#     x +=1

# #   useful operators 
# my_list = [1,2,3,4,5,6,7,8]
# for _ in range(my_list):
#     print(_)
# count = 0
# for letter in 'abcde':
#     print('at index {} the letter is {}'.format (count, letter))
#     count+=1
# word = 'abcde'
# for index,letter in enumerate(word):
#     print(letter)
#     print(index)
my_list = [1,2,3,9,0]
my_list2 = ['a', 'b','c', 'd']
my3 = [1,'t',100]
for item in zip (my_list, my_list2,my3):
    print(item)
print('x ' in [1,2,3,9,0])
print(min(my_list))
my_list.sort()
print(my_list)