def pattern(row,col):
    for i in range(0,row):
        for j in range(0,i+1):
            print('*',end =" ")
        print('\r')
pattern(5,5)
