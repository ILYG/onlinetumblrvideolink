__author__ = 'Arpat'

import requests as rq
import re
from bs4 import BeautifulSoup as bs

pp = {
    'socks5':'localhost:1080'
}


def find_url(url):
    temp = []
    for i in range(1,50):
        addrs = url + 'page/' + str(i)
        p = rq.get(addrs,proxies=pp).text
        l1 = re.findall('tumblr_video_container_\d*',p)
        for i in range(len(l1)):
            l1[i] = l1[i].split('_')[-1]
        for i in l1:
            print i
            temp.append(str(i))
    temp = list(set(temp))
    return temp

def find_video(addr):
    addres = 'http://www.tumblr.com/video/' + re.findall('/\/\w*\.',url)[0][2:-1] + '/' + addr + '/1366/'
    page = bs(rq.get(addres,proxies=pp).text)
    if page.find('source') == None:
        return ''
    else:
        return page.find('source').get('src')

if __name__ == '__main__':
    url = raw_input("Please Input URL : ")
    aa = find_url(url=url)
    bb = map(find_video,aa)
    with open('list.txt','w') as f:
        for i in bb:
            if i[-3:] == '480' or i[-3:] == '720':
                i = i[:-3]+'1080'
                f.write(i+'\n')
            else:
                i = i + r'/1080'
                f.write(i+'\n')
    print 'Total Video Is ' + str(len(bb)) + '\n ByeBye!'