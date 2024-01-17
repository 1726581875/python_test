import os
import glob
import face_recognition
import shutil

# 指定目录路径
directory = "D:\\mytest\\python\\face\\crawlTest\\images\\dlrb\\"
save_dir = "./images"
# 目标人脸图片
target_face_img = "dlrb.jpeg"

# 定义图片文件的扩展名
image_extensions = ["jpg", "jpeg", "png", "gif"]

# 使用 glob 模块匹配图片文件
image_files = []
for extension in image_extensions:
    pattern = os.path.join(directory, f"*.{extension}")
    image_files.extend(glob.glob(pattern))

# 打印图片文件路径
for file in image_files:
    print(file)
    # 已知图片
    dlrb_img = face_recognition.load_image_file(target_face_img)
    dlrb_img_encoding = face_recognition.face_encodings(dlrb_img)[0]
    # 未知图片
    unknown_img = face_recognition.load_image_file(file)
    unknown_img_en_arr = face_recognition.face_encodings(unknown_img)
    if len(unknown_img_en_arr) > 0:
        known_encodings = [
            dlrb_img_encoding
        ]         
        face_distances = face_recognition.face_distance(known_encodings, unknown_img_en_arr[0])
        print(f"face_distances={face_distances}") 
        if face_distances[0] < 0.5: 
            file_name = file.split("\\")[-1]
            print(f"热巴图片：{file_name}")
            save_path = os.path.join(save_dir + '/dlrb2', file_name)
            shutil.copy2(file, save_path)
    else:
        print("不是人像图") 