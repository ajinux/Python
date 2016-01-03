#String slicing
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sliced_string=string[::]
print(sliced_string)

sliced_string=string[0:len(string):2]
print(sliced_string)

sliced_string=string[20::-1]
print(sliced_string)

sliced_string=string[::-1]
print(sliced_string,end='\n\n')

#string count()
string=''' This course is not about how to build a pretty web page, it's about how to build
and deploy the full stack of protocols and technologies associated with a complete web app.
That said, it is not possible for you to become an expert in this area in a few weeks. My
goal, rather, is to put you on the right path by providing a solid foundation and framework
for understanding web applications, allowing you to dig deeper and learn more on your own. The
next bullet points describe how we're going to do this.'''
ref="the"
count1=string.count(ref)
print(count1,end='\n\n')

#string find()
string="This course is not about how to build a pretty web page"
index_find=string.find("how")
print(index_find,end='\n\n')

#string index()
string="This course is not about how to build a pretty web page"
try:
    index_position=string.index("the")
    print("INDEX:",index_position,end='\n\n')
except:
    print("The substring not found!",end='\n\n')

#string upper()
print(string.upper())
print(string.lower(),end='\n\n')

#string endswith()
string="www.python.org"
if string.endswith(".org"):
    print("The string ends with '.org'")
else:
    print("The string dosen't ends with '.org'")

