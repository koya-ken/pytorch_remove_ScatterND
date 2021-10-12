import torch
import torch.nn as nn

class CatModel(nn.Module):
  def __init__(self):
    super(CatModel,self).__init__()

  def forward(self,x):
    # (batch,3,1)
    x1 = x[:,[0],:] * 2
    x2 = x[:,[1],:] * 3
    x3 = x[:,[2],:] * 4
    return torch.cat([x1,x2,x3],axis=1)