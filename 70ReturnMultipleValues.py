# This is calculator

def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u
result = calc(10,5)
for i in result: print(i)

#Alternatively, the result can be nested inside the print funcation, as shown in the last script.