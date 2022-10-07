members=[]
for i in range(51):
    names=input("enter member's name ")
    phone_no=input("enter member's phone number ")
    boat_size=int(input("enter boat size "))
    if boat_size == 50:
        pass
    elif boat_size == 55:
        pass
    elif boat_size == 128:
        pass
    else:
        boat_size=input("enter boat size, must be either 50,55 or 128 ")
member={'name': names,
    'phone number': phone_no,
    'boatsize': boat_size }
    
members.append(member)

members.sort()