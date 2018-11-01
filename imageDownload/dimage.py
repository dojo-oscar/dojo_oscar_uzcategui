import os
import urllib.request

def separate_line(file_line):
    return file_line[:-1].split(',')

def format_img(img_link):
    img_link = img_link.strip()
    return img_link

def format_title(img_title):
    if not 'jpg' in img_title:
        img_title += '.jpg'
    return img_title

def add_destination(title, destination):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    final_url = os.path.join(BASE_DIR, destination, title) 
    return final_url

def download_img(img_title, img_url, destination_dir=None):
    if destination_dir is not None:
        img_title = add_destination(img_title, destination_dir)
    urllib.request.urlretrieve(img_url, img_title)

with open('links.txt', 'r') as links_file:
    for line in links_file:
        img_title, img_url = separate_line(line)
        img_title = format_title(img_title)
        img_url = format_img(img_url)
        download_img(img_title, img_url, '../images')
        # print('Descargando', img_title)
        # urllib.request.urlretrieve(img_url, img_title)
        # print('Descargada')