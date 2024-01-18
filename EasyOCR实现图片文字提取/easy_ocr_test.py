import easyocr

img_path = "orc_example_img.png"
# 'ch_sim'表示中文简体字符，'en'表示英文字符
reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext(img_path)

print(result)
for item in result:
    print("提取到文字:" + item[1])

print("=========== simple result ===============")
simple_result = reader.readtext(img_path, detail = 0)
print(simple_result)
for str in simple_result:
    print("提取到文字:" + str