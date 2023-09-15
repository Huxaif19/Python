def up_low(s):
    d = {'upper' : 0, 'lower' : 0}
    for char in s : 
        if char.isupper():
            d['upper'] +=1
        elif char.islower():
            d['lower'] += 1
        else:
            pass
    print(f'the no of uppercase is {d["upper"]}and lowercases {d["lower"]}')
up_low('this IS an TEst')