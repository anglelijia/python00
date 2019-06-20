import urllib.request
import urllib.parse
data = bytes(urllib.parse.urlencode({'pw':'789','acc':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)


data = urllib.parse.urlencode({'wd':'柯南'},encoding='utf8')
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)