# import urllib.request
# ur1='http://www.baidu.com'
# proxy_handle={
#    'http':'183.51.190.51',
#    'http':'59.52.187.38'
# }
# proxy=urllib.request.ProxyHandler(proxy_handle)
# opener=urllib.request.build_opener(proxy)
# request=urllib.request.Request(ur1=ur1)
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf8'))
# while 1:
#     print(response.status)
#     if (response.status==200):
#         print('爬取失败')
#         break




import os,re
import mechanize
browser = mechanize.Browser()
browser.addheaders = [('User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')]
res  = browser.open('http://www.17k.com/chapter/2933095/36699279.html')
data = res.read()
data = data.replace('\t','')
regx = '<a href="(.*)" target="_blank" style="color:#08619D">\r\n(.*)\r\n</a>'
domainlist =  re.findall(regx,data)
print len(domainlist)
for domain in domainlist:
    print domain[1].decode('utf-8'), domain[0] 

with open(u'金融.txt','wb') as fp:
    str1 = ''
    for domain in domainlist:
            str1 += domain[1]+ '----' + domain[0] + '----'+ '\r\n'
    fp.write(str1)