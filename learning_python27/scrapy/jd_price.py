# codeing=utf-8
import urllib2
import re

i = 1;
url = 'http://item.jd.com/990548.html'
jdid = re.search(r'/(\d+)\.html',url).group(1)

while i <= 3:
	#url = 'http://m.jd.com/product/'+str(int(jdid)+1) +'.html'
	url = 'http://m.jd.com/product/'+str(jdid) +'.html'
	html = urllib2.urlopen(url).read().decode('utf-8')
	aa = re.findall(r'<span id="spec_price">*.*', html)[0]
	#aa = re.findall(r'\d+\.\d+', aa)
	if re.findall(r'\d+\.\d+', aa) <> None:
		aa = re.findall(r'\d+\.\d+', aa)
	else:
		aa = 0
	print (jdid)
	print (aa[0])
	i += 1
	jdid =  int(jdid) + 1