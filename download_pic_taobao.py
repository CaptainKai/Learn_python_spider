# -*- coding: utf-8 -*-
# 使用urllib2访问页面，open创建文件，下载图片
import urllib2
import re


class download():
    def __init__(self, _loadpath):
        self.loadpath = _loadpath

    def get_data(self, root_url):
        # 访问目标页面（伪装）
        Head = {
            "authority":"s.taobao.com",
            "method":"GET",
            "accept - encoding":"gzip,deflate,br",
            "scheme":"https",
            "accept - language":"zh-CN,zh;q=0.9",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        req = urllib2.Request(root_url, headers=Head)
        responce = urllib2.urlopen(req)

        if responce.getcode() != 200:
            print "%s visit error!" % (root_url)
            return None
        self.data = responce.read()

        # 下面的代码用于测试：是否进入到真正的淘宝界面
        # f = open('taobao.html', 'w')
        # f.write(self.data)
        # f.close()
        # print self.data

    def handler_pic(self):
        # 因为返回为script，直接使用正则获取需要的网址
        links = re.findall(r'//g-search.{70,119}jpg', self.data)
        count = 1
        for link in links:
            # 写一个url.txt文件存储下载照片的来源
            u_f = open(self.loadpath+r'\url.txt', 'a+')
            u_f.write(link)
            u_f.write('\n')
            u_f.close()
            print "%d.%s" % (count, link)
            filename = self.loadpath + "/taobao_" + str(count) + ".jpg"
            f = open(filename, 'wb')
            responce = urllib2.urlopen("http:"+link)
            if responce.getcode() != 200:
                print "%s visit error!" % (root_url)
                return None
            data = responce.read()
            f.write(data)
            f.close()
            count = count + 1


def download_pic(root_url):
    loadpath = r"E:/Code/Python/taobao_pic"
    run = download(loadpath)
    run.get_data(root_url)
    run.handler_pic()
if __name__ == '__main__':
    root_url = "https://s.taobao.com/search?q=%E6%89%8B%E8%A1%A8"
    download_pic(root_url)