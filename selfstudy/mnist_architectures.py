import torch 
import torch.nn as nn
import torch.nn.functional as F


class MNIST_tf(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding='same')
        self.conv2 = nn.Conv2d(32, 64, 3, padding='same')
        self.conv3 = nn.Conv2d(64, 64, 3, padding='same')
        self.fc = nn.Linear(64 * 7 * 7, 10)
        self.out = None

    def forward(self, xb):
        # xb = xb.view(-1, 1, 28, 28) # already done in train loader now
        xb = F.max_pool2d(F.relu(self.conv1(xb)),2)
        xb = F.max_pool2d(F.relu(self.conv2(xb)),2)
        xb = F.relu(self.conv3(xb))
        xb = xb.view(-1, 64 * 7 * 7)
        xb = self.fc(xb)
        self.out = xb
        return xb
