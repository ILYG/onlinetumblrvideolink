__author__ = 'Arpat'

import requests as rq
import re
from bs4 import BeautifulSoup as bs


def find_url(url):
    temp = []
    for i in range(1,total_page):
        addrs = url + 'page/' + str(i)
        p = rq.get(addrs).text
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
    page = bs(rq.get(addres).text)
    if page.find('source') == None:
        return ''
    else:
        return page.find('source').get('src')

def find_304(first_url):
    if first_url is not (None or ''):
        r = rq.get(first_url)
        return r.url
    else:
        return ''

if __name__ == '__main__':
    url = raw_input("Please Input URL : ")
    total_page = int(raw_input("Please Input Total Page : "))
    aa = find_url(url=url)
    bb = map(find_video,aa)
    url1 = []
    for i in bb:
        if i[-3:] == '480' or i[-3:] == '720':
            i = i[:-4]
            url1.append(i)
        elif i[-4:] == '1080':
            i = i[:-5]
            url1.append(i)
    for i in url1:
        print i
    #with open("./list.txt","w") as f:
    #    for j in url2:
    #        f.write(j+'\n')

    print 'Total Video Is ' + str(len(bb)) + '\n ByeBye!'