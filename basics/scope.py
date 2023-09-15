# name = "this is a global variable"
# def greet():
#     name = "sammy "
#     def hello():
#         print("hello " + name)
#     hello()
# greet()
# print(name)



i = 90
def local_():
    global i
    print(i)
    i = 'nme'
    return i
c = local_()
print(i)
print(f'the new of i is {c}')