# coding=utf-8
with open("./news.txt", 'r', encoding="utf8") as txt_file:
    txt = txt_file.read()

txt = txt.replace("\n", '').replace('\u3000', '')
print(txt)


import jieba

words = jieba.cut(txt)
print(type(words))