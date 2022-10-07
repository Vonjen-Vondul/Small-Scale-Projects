def compareTriplets(integer_array_a,integer_array_b):
    alice=0
    bob=0
    new_list=[]
    for i in range(len(integer_array_a)):
        if integer_array_a[i] > integer_array_b[i]:
            alice += 1
        elif integer_array_a[i] < integer_array_b[i]:
            bob += 1
        elif integer_array_a[i] == integer_array_b[i]:
            bob += 0
            alice += 0
    new_list.append(alice)
    new_list.append(bob)
    print(new_list)
    
compareTriplets([1,2,3],[3,2,1])
