from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import jieba
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import torch
from torch.utils.data import DataLoader, TensorDataset
from model import SentimentNet
from torch import nn
from tqdm import tqdm
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (5, 3)


text_path = 'lstm/data/corpus.csv'
modelPath = 'lstm/models/ourNet-best.pth'
tf = pd.read_csv(text_path)
t = tf['evaluation']
device = torch.device("cuda:0")
num_words = 3000
tokenizer = Tokenizer(num_words=num_words)
# num_words = min(num_words, len(tokenizer.word_index) + 1)
model=SentimentNet(num_words, 256, 128, 8, 2)
modelpre=torch.load(modelPath)
model.load_state_dict(modelpre,strict=False)
sentence_len = 64
text_cut = [jieba.lcut(one_text) for one_text in t]
# print(tests_cut)
tokenizer.fit_on_texts(texts=text_cut)





def analysis(id):
    data_path = 'data/{0}.csv'.format(id)
    df = pd.read_csv(data_path)
    df.dropna(how='all')
    x = df['evaluation']
    tests_cut = [jieba.lcut(one_text) for one_text in x]
    tests_seq = tokenizer.texts_to_sequences(texts=tests_cut)
    tests_pad_seq = pad_sequences(tests_seq, maxlen=sentence_len, padding='post', truncating='post')
    model.to(device)
    model.eval()
    h = model.init_hidden(len(tests_pad_seq))
    output, h = model(torch.tensor(tests_pad_seq).to(device), h)
    ans = output.view(-1, 2)
    # list = ans.cpu().numpy().tolist()
    list = ans.cpu().detach().numpy().tolist()
    y = []
    # print(list)
    for i in list:
        if i[0] > 0.9:
            y.append(1)
        else:
            y.append(0)
    df['label'] = y
    df.to_csv('data/{0}.csv'.format(id), index=False)
    px=['好评','差评']
    py=[df['label'].value_counts()[0],df['label'].value_counts()[1]]
    plt.bar(px, py)
    for a, b in zip(px, py):  # 柱子上的数字显示
        plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    plt.title("好评差评统计")
    plt.show()



def singleanalysis(str):
    test_text_cut = [jieba.lcut(str)]
    test_seq = tokenizer.texts_to_sequences(texts=test_text_cut)
    test_pad_seq = pad_sequences(test_seq, maxlen=sentence_len, padding='post', truncating='post')
    model.to(device)
    model.eval()
    h = model.init_hidden(len(test_pad_seq))
    output, h = model(torch.tensor(test_pad_seq).to(device), h)
    ans = output.view(-1, 2)
    list = ans.cpu().detach().numpy().tolist()
    return list


if __name__ == '__main__':
    #analysis(10065188093694)
    list=singleanalysis('很喜欢赞嘿，总之很喜欢。新款会继续关注的物流速度也好快的呢呼，真没想到网上购物还这么有意思')
    if list[0][1]>0.9:
        print('zhengmian')

    #print(model.state_dict())
    print(model.embedding)


