def counter():
    camelCase = input('Enter camelCase: ')
    count=0
    for i in camelCase:
        if i.isupper():
            count+=1
    print(count)

counter()

