a = [s.upper() for s in "SAlam khobi halet chetore"]

print(a)


b = [w.strip(",") for w in ["one," , "world,,,,", "appel", "google, youtube,,,,,"]]
print(b)

line = "SAlam khobi halet chetore"

c = [word for word in line.split()]
print(c)


line = "SAlam khobi halet chetore"
d = ["/".join(sorted(word)) for word in line.split()]
print(d)


list2 = [x if x in "apple, orange" else "*" for x in "apple, orange, fuck"]
print(list2)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
ae = [x.sort() for x in [[1,2],[5,8],[0,6],[2,10]]]
print(ae)
be = [sorted(x) for x in [[1,2],[3,1],[0,6],[5,1],[2,10]]]
print(be)