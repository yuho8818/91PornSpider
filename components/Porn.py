# -*- encoding: utf-8 -*-
import os

import logging
import random
import time

from components import HttpUtil, HtmlUtil


class Porn:
    def __init__(self,page_url,video_base_url='http://91porn.com/view_video.php?viewkey='):
        self._page_url = page_url
        self._video_base_url = video_base_url
        logging.debug("Porn init!")

    def random_ip(self):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))

    def download(self,view_key,page_url,base_url,download_dir):
        headers = {'Accept-Language': 'zh-CN,zh;q=0.9',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
                   'X-Forwarded-For': self.random_ip(), 'referer': page_url,
                   'Content-Type': 'multipart/form-data; session_language=cn_CN'}
        base_req = HttpUtil.get_url_response(url=base_url + view_key, headers=headers)
        ifm = HtmlUtil.get_ifm(base_req)
        if not ifm:
            return
        bases_req = HttpUtil.get_url_response(ifm[0], headers=headers)
        video_url = HtmlUtil.get_video_url(bases_req)
        tittle = HtmlUtil.get_video_title(base_req)
        uploadtime = HtmlUtil.get_upload_time(base_req)
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
            logging.debug('创建下载路径：'+str(download_dir))
        savepath = download_dir + uploadtime + str(tittle)  # 保存路径
        if os.path.exists(savepath+'.mp4') == False:
            try:
                logging.debug('开始下载:' + str(tittle))
                HttpUtil.download_mp4(str(video_url), savepath)
                logging.debug('下载完成')
            except Exception as e:
                logging.debug(e)
        else:
            logging.debug('已存在文件夹,跳过')
            time.sleep(2)


