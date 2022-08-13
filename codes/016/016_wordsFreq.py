# coding:utf-8
from collections import Counter

import jieba

with open("./news.txt", 'r', encoding="utf8") as txt_file:
    txt = txt_file.read()

txt = txt.replace("\n", '').replace('\u3000', '')
print(txt)

words = jieba.cut(txt)

spam_words = ['，', '。', '的', '了']

words_list = []
for word in words:
    if word and word not in spam_words:
        words_list.append(word)


count = Counter(words_list)
print(count)

res = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(res)

top_5_word = res[:5]
for item in top_5_word:
    word_freq = item[1] / len(words_list)
    print(f'{item[0]} 出现了 {item[1]} 次, 词频是 {word_freq}')