import os
import jieba
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (6, 6)

from collections import Counter
if os.path.isfile("data/{}.csv".format('10073101297151')):
    df=pd.read_csv("data/{}.csv".format('10073101297151'))
    comments = df['evaluation']
    label = df['label']
    list1=comments.to_list
    a=0
    for b in label:
        if b==0:
            print(df['evaluation'][a])
            a=a+1
    print(list1)

    # text_cut = [jieba.lcut(one_text) for one_text in comments]
    # with open("cn_stopwords.txt", encoding="utf-8-sig") as f:
    #     stop_words = f.read().split()
    # print(text_cut)
    # list_set = []
    # for i in text_cut:
    #     list_set.extend(i)
    # print(list_set)
    # all_words = [word for word in list_set if len(word) > 1 and word not in stop_words]
    # print(all_words)
    # words_count = Counter(all_words)
    # statics = words_count.most_common()[:10]
    #
    # px=[i[0] for i in statics]
    # py=[i[1] for i in statics]
    # plt.bar(px, py)
    # for a, b in zip(px, py):  # 柱子上的数字显示
    #     plt.text(a, b, '%.f' % b, ha='center', va='bottom', fontsize=7)
    #
    # plt.show()
    # print(statics)