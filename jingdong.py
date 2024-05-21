import csv
import requests
import json
import time
import pandas as pd


header = ["evaluation","label"]
f=open("data/pinglun2.csv",mode="w",newline="" ,encoding='utf-8')
csvwriter=csv.writer(f)
csvwriter.writerow(header)


def function_快速爬取(jdid):

    # kv用于表示爬取时表示头部，page表示页码
    kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowS".format(jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
    # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:

            list_全部评论内容.append(i['content'])


        # 将爬取到的评论内容依次保存

        for i in list_全部评论内容:
            csvwriter.writerow([i])

        # 停两秒爬取下一页
        if page == 10:
            break
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)



def function_全部爬取(jdid):

    # score=0时
    # kv用于表示爬取时表示头部，page表示页码
    kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowS".format(jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])

        for i in list_全部评论内容:
            csvwriter.writerow([i])


        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


    # score=1时
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=1&sortType=5&page={}&pageSize=10&isShadowS".format(
            jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])
        # 保存销售时间，制作销量图

        # 将爬取到的评论内容依次保存

        for i in list_全部评论内容:
            csvwriter.writerow([i])

        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


    # score=2时
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=2&sortType=5&page={}&pageSize=10&isShadowS".format(
            jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])

        # 将爬取到的评论内容依次保存

        for i in list_全部评论内容:
            csvwriter.writerow([i])

        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


    # score=3时
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=3&sortType=5&page={}&pageSize=10&isShadowS".format(
            jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])


        for i in list_全部评论内容:
            csvwriter.writerow([i])

        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


    # score=4时
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=4&sortType=5&page={}&pageSize=10&isShadowS".format(
            jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])

        # 将爬取到的评论内容依次保存

        for i in list_全部评论内容:
            csvwriter.writerow([i])

        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


    # score=5时
    page = 0
    while True:
        url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=5&sortType=5&page={}&pageSize=10&isShadowS".format(
            jdid, page)
        try:
            r = requests.get(url, headers=kv)
        except:
            print("爬取失败")
        # 处理爬取json数据，找到评论信息
        # 去除头部和尾部的无关信息
        str_评论信息 = r.text[20:-2]
        json_评论信息 = json.loads(str_评论信息)
        list_评论内容 = json_评论信息['comments']
        # 设置循环退出条件
        if len(list_评论内容) == 0:
            break
        # 把当前页的评论信息保存到列表
        list_全部评论内容 = []
        for i in list_评论内容:
            if i['content'].strip() != '此用户未填写评价内容'and i['content'].strip() != '您没有填写评价内容':
                list_全部评论内容.append(i['content'])

        # 将爬取到的评论内容依次保存

        for i in list_全部评论内容:
            csvwriter.writerow([i])
        # 停两秒爬取下一页
        time.sleep(2)
        page = page + 1
        # 以下部分测试专用
        print(page)


def spider(jdid):
    function_全部爬取(jdid)
    df = pd.read_csv('data/pinglun2.csv')
    # df.drop("此用户未填写评价内容",axis=0)
    # df.drop("您没有填写评价内容", axis=0)
    df.to_csv('data/{0}.csv'.format(jdid),index=False)

def repidspider(jdid):
    function_快速爬取(jdid)
    df = pd.read_csv('data/pinglun2.csv')
    # df.drop("此用户未填写评价内容",axis=0)
    # df.drop("您没有填写评价内容", axis=0)
    df.to_csv('data/{0}.csv'.format(jdid),index=False)


if __name__ == "__main__":
    spider(10065188093694)
