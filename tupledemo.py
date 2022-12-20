d=(10,20,30,40)
print(d)

print(d[0:2])
print(d[2:0])
print(d[0:-2])
print(d[-2:0])
print(d[1:2])
print(d[2:3])

st=list(d)
st.append(50)
d=tuple(st)
print(d)

st=list(d)
st.remove(50)
d=tuple(st)
print(d)





