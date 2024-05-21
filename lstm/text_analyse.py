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


if __name__ == '__main__':

    data_path = 'data/corpus.csv'
    df = pd.read_csv(data_path)

    x = df['evaluation']
    y = df['label']

    texts = [jieba.lcut(one_text) for one_text in x]




    stop_words = []
    with open('cn_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stop_words.insert(0,line.strip())



    texts_cut = [word for word in texts if word not in stop_words]

    label_set = set()
    for label in y:
        label_set.add(label)
    label_set = np.array(list(label_set))
    labels_one_hot = []
    for label in y:
        label_zero = np.zeros(len(label_set))
        label_zero[np.in1d(label_set, label)] = 1
        labels_one_hot.append(label_zero)
    labels = np.array(labels_one_hot)

    num_words = 3000
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(texts=texts_cut)
    num_words = min(num_words, len(tokenizer.word_index) + 1)

    sentence_len = 64
    texts_seq = tokenizer.texts_to_sequences(texts=texts_cut)
    texts_pad_seq = pad_sequences(texts_seq, maxlen=sentence_len, padding='post', truncating='post')



    # 拆分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(texts_pad_seq, labels, test_size=0.2, random_state=1)
    train_dataset = TensorDataset(torch.from_numpy(x_train), torch.from_numpy(y_train))
    test_dataset = TensorDataset(torch.from_numpy(x_test), torch.from_numpy(y_test))
    batch_size = 32
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

    model = SentimentNet(num_words, 256, 128, 8, 2)

    lr = 0.0001
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()
    device = model.device

    epochs = 64
    step = 0
    epoch_loss_list = []
    lossBest = 100000


    model.to(device)
    model.train()  # 开启训练模式

    for epoch in range(epochs):
        epoch_loss = 0
        for index, (x_train, y_train) in enumerate(train_loader):
            cur_batch = len(x_train)
            h = model.init_hidden(cur_batch)  # 初始化第一个Hidden_state

            x_train, y_train = x_train.to(device), y_train.to(device)
            step += 1  # 训练次数+1

            x_input = x_train.to(device)
            model.zero_grad()

            output, h = model(x_input, h)

            # 计算损失
            loss = criterion(output, y_train.float().view(-1))
            loss.backward()
            #梯度裁剪
            nn.utils.clip_grad_norm_(model.parameters(), max_norm=5)
            #更新模型权重
            optimizer.step()
            epoch_loss += loss.item()

        print("Epoch: {}/{}...".format(epoch + 1, epochs),
              "Step: {}...".format(step),
              "Loss: {:.6f}...".format(epoch_loss))

        if loss / (epoch + 1) < lossBest:
            lossBest = loss / (epoch + 1)
            torch.save(model.state_dict(), './models/ourNet-best2.pth')  # 保存最佳模型

        torch.save(model.state_dict(), './models/ourNet-last2.pth')  # 保存模型

        epoch_loss_list.append(epoch_loss)


    # 评估模式
    model.eval()
    loss = 0
    for data in tqdm(test_loader):
        x_val, y_val = data
        x_val, y_val = x_val.to(device), y_val.to(device)

        h = model.init_hidden(len(x_val))  # 初始化第一个Hidden_state

        x_input = x_val.long()
        x_input = x_input.to(device)
        output, h = model(x_input, h)

        loss += criterion(output, y_val.float().view(-1))

    print("test Loss: {:.6f}...".format(loss))

    test_text_cut = [jieba.lcut("商品质量相当不错，点赞"),
                     jieba.lcut("什么破东西，简直没法使用")]

    test_seq = tokenizer.texts_to_sequences(texts=test_text_cut)
    test_pad_seq = pad_sequences(test_seq, maxlen=sentence_len, padding='post', truncating='post')
    h = model.init_hidden(len(test_pad_seq))

    output, h = model(torch.tensor(test_pad_seq).to(device), h)

    print(output.view(-1, 2))

    x = [epoch + 1 for epoch in range(epochs)]


    torch.save(model.state_dict(), './models/ourNet-last2.pth')


    plt.plot(x, epoch_loss_list)
    plt.xlim(0, 64)
    plt.ylim(0, 100)
    plt.show()











