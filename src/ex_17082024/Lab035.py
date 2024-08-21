# write  program to clculte the
# area of a circle given its radius using the formula.
# area = pi*r**2 (Take pi as .14)
import math

# Logic buildig the formula
# step1 figure out the inputs and outputs
# input->r->datatype->float
# pi-3.14
#power-?pow fumtion or **->any
#O/P-> float, area, print(area)
# step2
#rough logc=area=3.14*pow(r,2)

#step3 -write the logic

radius=float(input("Enter the 'r' of the ciccle\n"))
print(radius)
print(math.pi)
area=math.pi=math.pow(radius,2)
print("Area of the circle is->", area)
print(f"Area of the circle is-> {area:2f}")

#print(3.14*(float(input("Enter the radius\n")**2)
#*-Mul
#**-power