
# solution using third variable

x=13
y=12

temp = x

x=y
y=temp

print("The Value of x:" ,x)
print("The Value of y:" , y)

# ------------------------------------------------------------

# Solution without third variable

x=13
y=12

x,y=y,x
print("The Value of x:" ,x)
print("The Value of y:" , y)
