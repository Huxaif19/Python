my = [2,3,6,8]
# def square(num):
#      return num ** 2
# for item in  map(square, my):
#     print (item)
# print(list (map(square, my)))
def splicer (string):
    if len(string)% 2 == 0 :
        return "even"
    else:
        return string[0]
names = ['huzaif', 'safiya','ourson','heena', 'saqlain','hff']
print(list(map(splicer,names)))
# def check_even(num):
    # return num % 2 == 0
# mylist = [1,2,3,4,5,6,7,8,9,10]
# for n in filter(check_even,mylist):
#     print(n)
# lambda function is also known as anonymous function
# square = lambda num : num ** 2
# print(square (3))
# for i in map (lambda num : num** 2, my):
#     print (i)
my_list = [2,3,4,5,6,7,8,9]
print(list(filter(lambda num: num % 2 ==0, my_list)))
