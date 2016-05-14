  
from html.parser import HTMLParser  
from urllib.parse import urlparse  
#from urllib.parse import urllib2  
  
#import HTMLParser  
#import urlparse  
#import urllib2  
#import cookielib  
  
import urllib  
import urllib.request  
import http.cookiejar  
import string  
import re  

def Login():  
    #登录的主页面  
    hosturl = 'http://114.215.88.35:5678/' #自己填写  
    #post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
    posturl = 'http://114.215.88.35:5678/rest/user/login' #从数据包中分析出，处理post请求的url  
    
    #设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
    cj = http.cookiejar.LWPCookieJar()  
    cookie_support = urllib.request.HTTPCookieProcessor(cj)  
    opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)  
    urllib.request.install_opener(opener)  
    
    #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
    h = urllib.request.urlopen(hosturl)  
    
    #构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
            'Referer' : 'http://114.215.88.35:5678/'}  
    #构造Post数据，他也是从抓大的包里分析得出的。  
    postData = {'data' : "{\"email\":\"0002\",\"password\":\"0028\",\"remember\":true,\"next\":\"\"}"}  
    
    #需要给Post数据编码
    postData = urllib.parse.urlencode(postData).encode('utf-8')  
    
    #通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
    request = urllib.request.Request(posturl, postData, headers)  
    print(request)  
    response = urllib.request.urlopen(request)  
    text = response.read()  
    print(text)  
    
    save_path="D:\\snatch2.txt"   
    # save_path 's file unnecessary to be exist  
    f_obj = open(save_path,'wb')  
    f_obj.write(text)  
    print("snatch successfully.")  

def Get(startP):
    try:
        for i in range(startP, end):
            #每一定次数就重登陆一次
            if i%4000==0:
                Login()        
            file = urllib.request.urlopen("http://114.215.88.35:5678/rest/file/download/CV"+str(i))  
            htmlFile = file.read()  
            htmlPath="D:\\my\\python\\PythonTools\\DownloadFiles\\files\\CV"+str(i)+".html"

            f_obj = open(htmlPath,'wb')  
            f_obj.write(htmlFile)
            p=i
            print("snatch successfully.")  
    except Exception as what: 
        print(what)
        return get(p)


start = 800001
end = 900000

p = start


Login()
Get(p)