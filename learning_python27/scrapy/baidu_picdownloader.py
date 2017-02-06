#-*- coding:utf-8 -*-
import re
import requests


def downloadPic(html,keyword,quantity):

    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    quantity = int(quantity) - 1
    print 'Found pic(s) contain key word: '+keyword+' start downloading the first '+ str(quantity + 1) + ' pic(s)...'
    for each in pic_url:
        if i <= quantity:
            print 'Downloading '+str(i+1)+'# pic(s), URL: '+str(each)
            try:
                pic = requests.get(each, timeout=10)
            except requests.exceptions.ConnectionError:
                print '[Error] current pic cannot be downloaded!'
                continue
            string = 'pictures\\'+keyword+'_'+str(i) + '.jpg'
            #resolve the problem of encode, make sure that chinese name could be store
            fp = open(string.decode('utf-8').encode('cp936'),'wb')
            fp.write(pic.content)
            fp.close()
            i += 1  
        else:
            print '\nDownloading completed!!!'
            break
        
class downloader:
    def download(self):
        print 'I am download method'

if __name__ == '__main__':
    word = raw_input("Input key word: ")
    quantity = raw_input("Input pic(s) quantity you want to download: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    downloadPic(result.text,word,quantity)
    downloader1=downloader