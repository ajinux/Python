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

