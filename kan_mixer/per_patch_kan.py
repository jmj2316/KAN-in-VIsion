import torch.nn as nn
from .kan_linear import KANLinear

class PerPatchKAN(nn.Module):
    def __init__(self, n_pixels, n_channel):
        super().__init__()
        self.kan = KANLinear(n_pixels, n_channel)

    def forward(self, x):
        output = self.kan(x)
        return output
