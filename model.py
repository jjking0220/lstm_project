import torch.nn as nn
import torch


class SentimentNet(nn.Module):
    device = torch.device("cuda:0")

    def __init__(self, vocab_size, input_dim, hid_dim, layers, output_dim):
        super(SentimentNet, self).__init__()
        self.n_layers = layers
        self.hidden_dim = hid_dim
        self.embeding_dim = input_dim
        self.output_dim = output_dim
        drop_prob = 0.5

        self.lstm = nn.LSTM(self.embeding_dim, self.hidden_dim, self.n_layers,
                            dropout=drop_prob, batch_first=True)

        self.fc = nn.Linear(in_features=self.hidden_dim, out_features=self.output_dim)
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(drop_prob)

        self.embedding = nn.Embedding(vocab_size, self.embeding_dim)

    def forward(self, x, hidden):
        x = x.long()
        embeds = self.embedding(x)

        lstm_out, hidden = self.lstm(embeds, hidden)
        out = self.dropout(lstm_out)
        out = self.fc(out)
        out = self.sigmoid(out)
        out = out[:, -1, :]
        out = out.squeeze()
        out = out.contiguous().view(-1)
        return out, hidden

    def init_hidden(self, batch_size):
        hidden = (torch.zeros(self.n_layers, batch_size, self.hidden_dim).to(self.device),
                  torch.zeros(self.n_layers, batch_size, self.hidden_dim).to(self.device))
        return hidden