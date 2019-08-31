# -*- encoding: utf-8 -*-

import socket
import urllib
import logging
import chardet
import sys
import os, re, time, random
import requests

def get_random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))


def download_mp4(url,dir):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
        'Referer': 'http://91porn.com'}
    req = requests.get(url=url)
    filename = str(dir) + '.mp4'
    with open(filename, 'wb') as f:
        f.write(req.content)

def download_img(url, dir):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name',
        'Referer': 'http://91porn.com'}
    req = requests.get(url=url)
    with open(str(dir) + '/thumb.png', 'wb') as f:
        f.write(req.content)

def get_url_response(url,headers=None):
    if not headers:
        return requests.get(url)
    return requests.get(url=url, headers=headers)
