#basket={"Mango","grapes","banana","orange"}
#print(basket)

#basket={"Mango","grapes","banana","orange","Mango","banana"}

a=set("Mango")
b=set("orange")
print(a)            #print uniqe 
print(a-b)          #print in a but not in b
print(a|b)          #print in a or b or both
print(a & b)        #print in a and b
print(a or b)       #print in a or b but not in both

a={x for x in 'abcabcrdabc' if x not in 'abc'}
print(a)