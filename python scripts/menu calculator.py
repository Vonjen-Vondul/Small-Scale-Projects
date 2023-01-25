customer=[]
number=[]

main_menu={'Rice and stew':1500,
'Eba and egusi':2000,
'Pounded_yam and vegetable_soup':2500,
'Stir_fried spag':3500,'Meat_balls':1000,
'Cowmeat':500,
'Goatmeat':700,
'Fullchicken':3000,
'Chickenlap':600 ,
'Halfchicken':1500
}

def online_order():
    order=input('from menu select your food: '.strip())
    order_number=int(input('select of item: '.strip()))
    p= int(main_menu.get(order)*order_number)
    print(p)


online_order()
