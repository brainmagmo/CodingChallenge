x = 1 
y = 1 
r = 0
while(x<4000000):
    if((x%2)==0):
        r=r+x
    z = x+y 
    x = y
    y = z
print(str(r))
#4613732
