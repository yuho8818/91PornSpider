# -*- encoding: utf-8 -*-


import logging
import requests
import os, re, time, random

def get_viewkey(raw_html):
    return re.findall('http://91porn.com/view_video.php\?viewkey=(.*?)&page=.*?&viewtype=basic&category=.*?" title=',raw_html.text)


def get_upload_time(raw_html):
    uploadtime = re.findall(r'<span class="info">添加时间: </span>.*<span class="title">(\d\d\d\d-\d\d-\d\d)</span>',str(raw_html.content, 'utf-8', errors='ignore'))  # 视频上传时间
    uploadtime_str = "".join(uploadtime)  # 视频上传时间
    return uploadtime_str

def get_ifm(raw_html):
    return re.findall('<iframe width="560" height="315" src="(.*?)" frameborder="0" allowfullscreen></iframe>',
                         raw_html.text)

def get_video_url(raw_html):
    return re.findall(r'<source src="(.*?)" type=\'video/mp4\'>',
                               str(raw_html.content, 'utf-8', errors='ignore'))[0]

def get_video_title(raw_html):
    tittle = re.findall(r'<div id="viewvideo-title">(.*?)</div>', str(raw_html.content, 'utf-8', errors='ignore'),
               re.S)
    try:
        t = tittle[0]
        tittle[0] = t.replace('\n', '')
        t = tittle[0].replace(' ', '')
        return t
    except Exception as e:
        print(e)

def get_upload_time(raw_html):
    return "".join(re.findall(
        r'<span class="info">添加时间: </span>.*<span class="title">(\d\d\d\d-\d\d-\d\d)</span>',
        str(raw_html.content, 'utf-8', errors='ignore')))  # 视频上传时间

