import cmath
# general formula of quardatic equation ax**2+bx+c
a=int(input("enter the coefficient of x**2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant term:"))
d=(b*b) - (4*a*c)
sqrt_value=cmath.sqrt(abs(d))
if d > 0:
      print(" real and different roots ") 
      print((-b + sqrt_value)/(2 * a)) 
      print((-b - sqrt_value)/(2 * a))
elif d==0:
    print("roots and same and real")
    print(-b / (2 * a))
else :
    print("roots are imaginary")


