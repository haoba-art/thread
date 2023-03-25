# -*- coding=utf-8 -*-
# @Time: 2023/3/25 10:04
# @AUTHOR: HUI
# @File: thread_test.py
# @software: PyCharm
import threading
import urllib.request

class DownloadThread(threading.Thread):
    def __init__(self, url, name):
        threading.Thread.__init__(self)
        self.url = url
        self.name = name

    def run(self):
        print("Starting " + self.name)
        urllib.request.urlretrieve(self.url, self.name)
        print("Finished " + self.name)

threads = []
urls = ['https://m701.music.126.net/20230325103805/a45e8fc63abfe632728fc5b5c4e2e9f4/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096436041/b811/9137/4055/7f761d9d6e630bcab156a1496f648ffd.mp3',
        'https://sv-sycdn.kuwo.cn/2e678062975ed58c8b91578c73808611/641e58e7/resource/n2/66/23/2672962327.mp3',
        'https://gf-sycdn.kuwo.cn/d07fd403f5b240b071d27f88bfd268b1/641e5921/resource/n2/89/44/2573320478.mp3']

for i in range(len(urls)):
    t = DownloadThread(urls[i], "Thread " + str(i+1)+".mp3")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads finished.")
