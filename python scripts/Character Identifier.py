def string():
    strn=input('input a string: ')
    letters=numbers=0 
    for i in strn:
       if i.isdigit():
           numbers +=1
       elif i.alpha():
            letters +=1
    print('letters:{}'.format(letters))
    print('numbers:{}'.format(numbers))           
list()
