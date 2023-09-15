# functions in python >>>>>>>>
from random import shuffle
# def fun(name ='huzaif'):
#     print("hello world" + name)
# fun()
# def add_fun(num1, num2):
#     print (num1+ 2)
#     return num1+num2
# result = add_fun(1,2)
# print(result)
# def my(num1= 2, num2 = 2):
#     print(num1 + num2)
# result = my()
# def is_even():
    
#      x = int(input("enter the number"))
#      if not x%2:
#         print("even")
#      else :
#         print("odd")
# is_even()
# mylist = [1,2,5]
# def list_in(mylist):
#     for i in mylist:
#         if i % 2 ==0:
#             return True
#         else :
#             pass
#     return False
# print(list_in(mylist))
# >>>>>return list form a fun<<<<<<<
# list = [1,2,5]
# def list_in(list):
#     even_numbers= []
#     for i in list:
#         if i % 2 ==0:
#             even_numbers.append(i)
#         else :
#             pass
#     return even_numbers
# print(list_in(list))



# >>>> return tuple <<<<<
# t = [('apple', 400), ('samsung',90)]
# for i in t:
#     print(i)
# for i , l in t:
#     print(i)
work_hrs = [('hei',79), ('billy', 90), ('jose', 89),('him', 98)]
# def check_hrs(work):
#     curr =0 
#     emp = ''
#     for t,i in work :
#         if i > curr:
#             curr = i
#             emp = t
#         else : 
#             pass
#     return (emp, curr)
# print(check_hrs(work_hrs))
# shuffle(work_hrs)
# print(work_hrs)
my_list = ['', 'o','']
shuffle(my_list)
def player_guess ():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input ("pick a number: 0,1,2")
        return int(guess)
def check_guess(mylist, guess):
    if my_list[guess] == 'o':
        print ("correct!")
    else :
        print("wrong answer")
        print(my_list)
guess = player_guess()
check_guess(my_list, guess)