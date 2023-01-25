def list(collection):
    odd=0
    even=0 
    for x in collection:
       if x % 2 == 0:
           odd +=1
           
           print('odd:{}'.format(odd))
       else:
           even +=1
           
           print('even:{}'.format(even))
list([5,6,7,8,9])