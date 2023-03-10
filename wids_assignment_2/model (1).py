# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z5oqvFi30Q0QsH6IlUBfMf-lf1pE_948
"""

import torch
from torch import nn

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.linear1 = nn.Linear(28*28, 400) 
        self.linear2 = nn.Linear(400, 128) 
        self.linear3 = nn.Linear(128, 84)
        self.linear4 = nn.Linear(84, 10)
        self.relu = nn.ReLU()

    def forward(self, img): 
        x = img.view(-1, 28*28)
        x = self.relu(self.linear1(x))
        x = self.relu(self.linear2(x))
        x = self.relu(self.linear3(x))
        x = self.relu(self.linear4(x))
        return x