__author__ = 'Ajithkumarsekar'
import urllib.request as ur
import re
def call_stock():
  weblist=['aapl','fb','msft','goog','amzn']
  i=0
  while i<len(weblist):
    url='http://finance.yahoo.com/q?s='+weblist[i]
    try:
      htmlfile=ur.urlopen(url)
      #requesting the url
      regex='<span id="yfs_l84_'+str(weblist[i])+'">(.+?)</span>'
      bytes = str.encode(regex)
      type(bytes)
      #converting the string code to bytecode
      pattern=re.compile(bytes)
      #compiling the tags as according to our need using regex
      htmltext=htmlfile.read()
      #Get the source code from the object and stores it in a variable as a string
      price=re.findall(pattern,htmltext)
      #re.findall finds all the compiled tags
      print("The stock price of",weblist[i]," is ",price)
      i+=1
    except:
        print("Runtime Error occured!!")
    finally:
        print("Programm completed")

call_stock()