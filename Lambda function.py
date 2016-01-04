__author__ = 'Ajithkumarsekar'
product=lambda var1,var2: var1*var2
print("Product :",product(3,5))

#def square(x):return x*x
square=lambda x:x*x
print(square(9))

#removing duplicates
remove_dup=lambda lists:set(lists)

print(remove_dup([1,1,3,2,5,2,4,6,5]))

print(remove_dup("Hello"))

#convert list of str to int
convert_int=lambda lists:list(map(int,lists))
string="12 34 67 34 86 23 12"
string=string.split(" ")
print(convert_int(string))
