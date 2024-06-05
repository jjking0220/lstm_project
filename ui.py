import tkinter as tk
import tkinter.messagebox

import jieba
import matplotlib.pyplot as plt
import jingdong
import wordcloud
import app
import os
import pandas as pd
from collections import Counter


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (10, 6)


window1 = tk.Tk()
window2 = tk.Tk()
window3 = tk.Tk()
window4 = tk.Tk()


scroll = tkinter.Scrollbar(window4,orient='vertical')
# 放到窗口的右侧, 填充Y竖直方向
scroll.pack(side=tkinter.RIGHT, fill='both')
T1 = tk.Text(window4,width=130, height=25)
T2 = tk.Text(window4,width=50, height=10)

# 两个控件关联
scroll.config(command=T1.yview)
T1.config(yscrollcommand=scroll.set)

T1.place(x=20,y=200)
# T2.place(x=500,y=300)


def _quit():
    window1.quit()
    window1.destroy()
    window2.quit()
    window2.destroy()
    window3.quit()
    window3.destroy()
    window4.quit()
    window4.destroy()





def win1():

    window2.withdraw()
    window3.withdraw()
    window4.withdraw()
    window1.deiconify()
    window1.protocol("WM_DELETE_WINDOW", _quit)
    window1.title('用户偏好分析系统')
    window1.geometry('1000x600')

    b1 = tk.Button(window1, text='单个评论情感分析', width=20, bd=10,command=win2)
    b2 = tk.Button(window1, text='根据商品id分析', width=20, bd=10,command=win3)
    b3 = tk.Button(window1, text='查看商品评论', width=20, bd=10, command=win4)
    b4 = tk.Button(window1,text='退出',width=20,bd=10,command=_quit)

    b1.place(x=400, y=100)
    b2.place(x=400, y=200)
    b3.place(x=400,y=300)
    b4.place(x=400, y=400)

    window1.mainloop()

def win2():

    window1.withdraw()
    window2.deiconify()
    window2.protocol("WM_DELETE_WINDOW", _quit)
    window2.title('单个评论情感分析')
    window2.geometry('1000x600')

    L1 = tk.Label(window2, text='输入评论：' )
    E1 = tk.Entry(window2, bd=5,width=100)
    B1=tk.Button(window2,text='分析',width=20,bd=10,command=lambda:comment(E1.get().strip('\n')))
    B2=tk.Button(window2,text='返回',width=20,bd=10,command=win1)

    L1.place(x=100, y=100)
    E1.place(x=200, y=100)
    B1.place(x=400, y=200)
    B2.place(x=400,y=300)







def win3():
    window1.withdraw()
    window3.deiconify()
    window3.protocol("WM_DELETE_WINDOW", _quit)
    window3.title('根据id统计')
    window3.geometry('1000x600')

    L1 = tk.Label(window3, text='输入商品ID：')
    E1 = tk.Entry(window3, bd=5,width=50)
    B1 = tk.Button(window3, text='分析', width=20, bd=10,command=lambda:idanalysis(E1.get().strip('\n')))
    B5 = tk.Button(window3, text='快速分析', width=20, bd=10,command=lambda:repididanalysis(E1.get().strip('\n')))
    B2 = tk.Button(window3, text='统计', width=20, bd=10, command=lambda:statistics(E1.get().strip('\n')))
    B3 = tk.Button(window3, text='词云', width=20, bd=10, command=lambda:wordc(E1.get().strip('\n')))
    B4 = tk.Button(window3, text='返回', width=20, bd=10, command=win1)




    L1.place(x=100, y=100)
    E1.place(x=200, y=100)
    B1.place(x=300, y=200)
    B5.place(x=500, y=200)
    B2.place(x=300, y=300)
    B3.place(x=300, y=400)
    B4.place(x=300, y=500)


def win4():
    window1.withdraw()

    window4.protocol("WM_DELETE_WINDOW", _quit)
    window4.title('用户偏好分析系统')
    window4.geometry('1000x600')

    L1 = tk.Label(window4, text='输入商品ID：')
    E1 = tk.Entry(window4, bd=5, width=50)
    B1 = tk.Button(window4, text='查看商品评论', width=10, bd=5, command=lambda:chack(E1.get().strip('\n')))
    B2 = tk.Button(window4, text='返回', width=10, bd=5, command=win1)
    L1.place(x=100, y=100)
    E1.place(x=200, y=100)
    B1.place(x=580,y=100)
    B2.place(x=680,y=100)
    window4.deiconify()

def chack(id):
    if len(id)==0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
        return
    if os.path.isfile("data/{}.csv".format(id)):
        T1.delete(1.0, "end")
        T2.delete(1.0, "end")
        df = pd.read_csv("data/{}.csv".format(id))
        comments = df['evaluation']
        # label = df['label']
        a = 1
        # for b in label:
        #     if b == 0:
        #         T1.insert('insert',comments[a])
        #         a = a + 1
        #     if b == 1:
        #         T2.insert('insert',comments[a])
        #         a = a + 1
        for i in comments:
            T1.insert('insert','评论'+str(a)+':'+'\n')
            T1.insert('insert',i+'\n')
            T1.insert('insert', '\n')
            a = a + 1

    else :
        tk.messagebox.showinfo(title='提醒',
                               message='未获取该商品评论')

def comment(s):
    if len(s)==0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
    else:
        list = app.singleanalysis(s)
        if list[0][1]>0.9:
            tk.messagebox.showinfo(title='分析结果',
                               message='这是一条正面评论')
        else:
            tk.messagebox.showinfo(title='分析结果',
                               message='这是一条负面评论')

def idanalysis(id):
    if len(id)==0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
    else:
        jingdong.spider(id)
        app.analysis(id)

def repididanalysis(id):
    if len(id)==0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
    else:
        jingdong.repidspider(id)
        app.analysis(id)



def statistics(id):
    if len(id)==0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
        return
    if os.path.isfile("data/{}.csv".format(id)):
        df = pd.read_csv("data/{}.csv".format(id))
        comments = df['evaluation']
        text_cut = [jieba.lcut(one_text) for one_text in comments]
        with open("baidu_stopwords.txt", encoding="utf-8-sig") as f:
            stop_words = f.read().split()
        list_set = []
        for i in text_cut:
            list_set.extend(i)
        all_words = [word for word in list_set if len(word) > 1 and word not in stop_words]
        words_count = Counter(all_words)
        statics = words_count.most_common()[:10]
        px = [i[0] for i in statics]
        py = [i[1] for i in statics]
        plt.bar(px, py)
        for a, b in zip(px, py):  # 柱子上的数字显示
            plt.text(a, b, '%.f' % b, ha='center', va='bottom', fontsize=7)
        plt.show()
        # print(statics)
    else :
        tk.messagebox.showinfo(title='提醒',
                               message='未获取该商品评论')





def wordc(id):
    if len(id) == 0:
        tk.messagebox.showinfo(title='提醒',
                               message='未输入')
        return
    if os.path.isfile("data/{}.csv".format(id)):
        df = pd.read_csv("data/{}.csv".format(id))
        comments = df['evaluation']
        text_cut = [jieba.lcut(one_text) for one_text in comments]
        with open("baidu_stopwords.txt", encoding="utf-8-sig") as f:
            stop_words = f.read().split()
        list_set = []
        for i in text_cut:
            list_set.extend(i)
        all_words = [word for word in list_set if len(word) > 1 and word not in stop_words]
        words_count = Counter(all_words)
        statics = words_count.most_common()[:20]
        newword=' '.join(word[0] for word in statics )
        wc = wordcloud.WordCloud(font_path = "STLITI.TTF",background_color='white')
        con=wc.generate(newword)
        plt.imshow(con)
        plt.show()
        # print(statics)
    else:
        tk.messagebox.showinfo(title='提醒',
                               message='未获取该商品评论')


if __name__ == '__main__':
    win1()

