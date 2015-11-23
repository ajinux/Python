__author__ = 'Ajithkumarsekar'
import urllib.request
def web_image_download(url,name):
    name=name+".jpg"
    print(name,"Downloaded Successfully!")
    try:
     urllib.request.urlretrieve(url,name)
    except urllib.error.HTTPError:
        print(name," Image not found!\n")
    except:
        print("A Runtime Error occured!\n")
a=input("Enter the main url:")
b=input("Enter the main name:")
c=int(input("Enter the starting Number:"))
d=int(input("Enter the ending number :"))
for n in range(c,d):
    if n>=10 & n<100:
      url=a+"0"+str(n)
      name=b+"0"+str(n)
      web_image_download(url,name)
    elif n>=100:
      url=a+str(n)
      name=b+str(n)
      web_image_download(url,name)
    else:
      url=a+"00"+str(n)
      name=b+"00"+str(n)
      web_image_download(url,name)
'''
Works only inside KCT i.e connected to the kct network,
Instruction to download the image:
NEEDS:
  1)This PY source code,
  2)A py terminal to execute the programm,
step 1:
  Execute the PY programm and in the terminal,
  "Enter the main url: http://10.1.105.24/opac/memberaccess1.asp?id=14bit"
  if you want to download images of IT students then change last three characters to bit
  and so on for other departments,
step 2:
  "Enter the main name:14BIT"(Name of the image)
step 3:
  "Enter the starting Number:1"
  "Enter the ending number :57"
Thatz it,just press Enter and you will be with all those bunch of photos...
  Happy learning!!
Ref URL:
http://10.1.105.24/opac/memberaccess1.asp?id=14bit
http://10.1.105.24/opac/memberaccess1.asp?id=14bce
'''    

