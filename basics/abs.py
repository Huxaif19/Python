print (abs (-5.60))
my = [1,2,3,3]
def lsi(mylist):
    for i in range (len(mylist) - 1):
        if mylist[i] == 3 and mylist[i+1] == 3:
            return True 
        else :
            pass 
    return False
print(lsi(my))
#this can b  also done in this way
def ht(mylist):
    for i in range (0, len(mylist) -1):
        if mylist[i:i+2] == [3,3]:
            return True
    return False
print(ht(my))
def conc(text):
    result = ''
    for char in text : 
        result += char * 3
    return result
print(conc('hello'))
mylis = [2,1,6,9,11]
def fun(mylis):
    total  = 0
    add = True
    for num in mylis:
        while add:
            if num != 6 :
                total += num
                break
            else :
                add = False
        while not add :
            if num != 9:
                break
            else :
                add = True
                break
    return total
print(fun(mylis))
my = []
def game(my) :
    code = [0,0,7,'c']
    for num in my : 
        if num  == code [0]:
            code.pop(0)
    return len(code) == 1
print(game([1,2,7,4,1,0,7,5]))