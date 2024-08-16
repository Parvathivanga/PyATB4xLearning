#strings
name="pramod"
#str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a="90" #when the int/float/anything present in invited comma represent sting.
age=90 #int
print(type(a))
print(type(age))

name=("This is a big line")
print(type(name))
#name=name+1- nit valid because name is a string.
name=name+str(1)
print(name) #at the end of the string 1 is added in the output.

first_name='parvathi'
last_name='vanga'
full_name=first_name+last_name #concat
print(full_name)

how_many_planes_i_have=None
print(type(how_many_planes_i_have)) #None type


#Null type is not present in python

val=0 #This is int

#id
age=10
age2=10
print(id(age))
print(id(age2))
age3=20
print(id(age3))


