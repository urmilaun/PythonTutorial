def simpleinterest(p,t,r):
    print('The principal is', p)
    print('The time is', t)
    print('The rate is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     

simpleinterest(8, 6, 8)