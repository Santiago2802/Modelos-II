from functools import reduce


lista=[(8,2),(3,2),(7,4),(6,3),(15,5),(10,4),(21,6)]


o=list(filter(lambda x: x[0]==((x[1]*(x[1]+1))/2),lista))
print(o)

k=list(map(lambda x: x[0],o)) 
print(k)

r=reduce(lambda x,y: x+y,k)

print(r)
