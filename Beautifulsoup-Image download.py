__author__ = 'Ajithkumarsekar'
import urllib.request
import random
def web_image_download(url,name):
    #name=random.randrange(1,10000)
    try:
      imagename=str(name)+".jpg"
      urllib.request.urlretrieve(url,imagename)
    except urllib.error.HTTPError:
        print("Invalid url!!")
    except:
        print("Runtime Error!!")
    # urllib.request.urlretrieve(url, full_name)
a=input("Enter the image url to be downloaded:")
b=input("Enter the name of the image to be stored:")
web_image_download(a,b)

