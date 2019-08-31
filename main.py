# -*- encoding: utf-8 -*-

import logging
import configparser
from components import HttpUtil, HtmlUtil
from components.Porn import Porn

logging.basicConfig(level=10,
                        format='%(asctime)s [%(module)s] %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read("./conf.ini")
    page_url = conf.get('91Porn','page_url')
    video_base_url = conf.get('91Porn','video_base_url')
    logging.debug("下载页面：%s"%page_url)
    start_page = conf.getint('91Porn','start_page')
    end_page = conf.getint('91Porn','end_page')
    download_dir = conf.get('91Porn','download_dir')
    logging.debug('目标路径：' + str(download_dir))
    logging.debug("------------预计下载第%u页到第%u页----------" %(start_page,end_page))
    porn = Porn(page_url)
    for page_num in range(start_page,end_page,1):
        logging.debug("-------------下载第%u页------------" %page_num)
        view_keys = HtmlUtil.get_viewkey(HttpUtil.get_url_response(page_url+str(page_num)))
        for video_key in view_keys:
            porn.download(video_key, page_url+str(page_num),video_base_url,download_dir)


