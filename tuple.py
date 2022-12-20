a=(10,20,30,40)
print(a)

print(a[1:3])
print(a[2:4])
print(a[2:0])
print(a[0:-2])

st=list(a)
st.append(60)
a=tuple(st)
print(st)

st=list(a)
st.remove(60)
a=tuple(st)
print(st)




