'''
d=[1,2,3,4,5,6]
for i in d:
    if i%2==1:
        print (i)

#Using function

def odd(d):
    for i in d:
        if i%2==1:
            print(i)
odd([1,2,3,4,5,6])

def odd_word(s):
    for i in s:
        if len(i)%2==1:
            print(i)
        
odd_word(["Back","Welcome","Hi","Prana","Jadhao","Raj"])'''
