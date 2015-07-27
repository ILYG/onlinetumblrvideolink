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
    page = bs(rq.get(addres).text,"lxml")
    if page.find('source') == None:
        return ''
    else:
        return page.find('source').get('src')


if __name__ == '__main__':
    url = raw_input("Please Input URL : ")
    total_page = int(raw_input("Please Input Total Page : "))
    aa = find_url(url=url)
    bb = map(find_video,aa)
    url1 = []
    for i in bb:
        if i[-4:] == ('/480' or '/720'):
            url1.append(i[:-4])
        elif i[-5:] == '/1080':
            url1.append(i[:-5])
        else:
            url1.append(i)

    with open("./list.txt","w") as f:
        for j in url1:
            f.write("http://vt.tumblr.com/" + j[-24:] + ".mp4#_=_" + "\n")

    print 'Total Video Is ' + str(len(url1)) + '\n ByeBye!'