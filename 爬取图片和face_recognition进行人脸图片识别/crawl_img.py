import requests
from bs4 import BeautifulSoup
import os
import time
import random
import face_recognition

def download_image(url, save_dir):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        file_name = url.split("/")[-1]
        file_name = file_name.split('?')[0]
        print(f"文件名:" + file_name)
        save_path = os.path.join(save_dir, file_name)
        with open(save_path, "wb") as f:
            f.write(image_data)
        print(f"已保存图片：{save_path}")
        
        known_image = face_recognition.load_image_file("dlrb.jpeg")
        unknown_image = face_recognition.load_image_file(save_path)
        dlrb_encoding = face_recognition.face_encodings(known_image)[0]
        uk_en_list = face_recognition.face_encodings(unknown_image);
        isRl = len(uk_en_list) > 0
        print(f"是否包含人脸:{isRl}")
        results = face_recognition.compare_faces([dlrb_encoding], uk_en_list[0]) if len(uk_en_list) > 0 else [False]
        if results[0] == True:
            print(f"匹配到迪丽热巴：{save_path}")
            save_path = os.path.join(save_dir + '/dlrb', file_name)
            with open(save_path, "wb") as f:
                f.write(image_data)
                print(f"已保存迪丽热巴图片：{save_path}")
        else:
             print(f"图片{save_path}不是迪丽热巴")

def crawl_images(url, save_dir):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")
        for img_tag in img_tags:
            img_url = img_tag["src"]
            if img_url.startswith("http"):
                download_image(img_url, save_dir)
                # 生成一个3到10之间的随机整数
                # random_time = random.randint(3, 10)
                # print(f"程序将暂停 {random_time} 秒")
                # time.sleep(random_time)


url = "https://www.keaitupian.cn/meinv/list_4_.html"
save_dir = "./images"
dlrb_dir = "./images/dlrb"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
if not os.path.exists(dlrb_dir):
    os.makedirs(dlrb_dir)
    

for i in range(100):
    start_time = time.time()
    url = 'https://www.keaitupian.cn/meinv/list_4_' + str(i) + '.html'
    print(f"当前页数为:{i}")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        a_tags = soup.find_all("a")
        for a_tag in a_tags:
            img_url = a_tag["href"]
            if img_url.endswith(".html"):
                crawl_images('https://www.keaitupian.cn' + img_url, save_dir)
    # 记录结束时间
    end_time = time.time()
    # 计算耗时（单位：秒）
    elapsed_time = end_time - start_time
    # 打印耗时
    print(f"当前页数为：{i} ,耗时：{elapsed_time}s")