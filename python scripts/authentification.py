sign_up=[]
def singup():
    for x in range(1):
        member=[]
        user_name =input('create new username: ')
        user_password =input('create new password: ')
        member.append(user_name)
        member.append(user_password)
        sign_up.append(member)
    
        authenticate()

def authenticate():        
    for y in range(1):
        user_name =input('enter username: ')
        user_password =input('enter password: ')
        for user in sign_up: 
            if user_name == user[0] and user_password == user[1]:
                print('user approved')
            else:
                print('invalid credentials')


singup()