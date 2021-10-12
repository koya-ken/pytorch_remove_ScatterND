import torch
import torch.nn as nn

class ScatterNdModel(nn.Module):
  def __init__(self):
    super(ScatterNdModel,self).__init__()

  def forward(self,x):
    # (batch,3,1)
    x[:,0,:] = x[:,0,:] * 2
    x[:,1,:] = x[:,1,:] * 3
    x[:,2,:] = x[:,2,:] * 4
    return x